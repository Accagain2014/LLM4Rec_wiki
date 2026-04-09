---
title: "Unified Transformer Backbone — Single Architecture for Feature Interaction and Sequence Modeling"
category: "concepts"
tags: [unified transformer, feature interaction, sequence modeling, OneTrans, unified architecture, tokenization]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../sources/2510_paper_25102610_OneTrans_Unified_Feature_Interaction_and_Sequence_Modeling.md"]
related:
  - "../models/OneTrans.md"
  - "../models/RankMixer.md"
  - "../models/LONGER.md"
  - "../concepts/feature_interaction.md"
confidence: "high"
status: "stable"
---

# 统一 Transformer 主干 — 特征交互与序列建模的单一架构

## 概述

统一 Transformer 主干是推荐系统中的一种设计范式，其中**单一 Transformer 架构**同时处理**特征交互**（建模用户、物品和上下文特征之间的关系）和**序列建模**（捕捉用户行为历史中的时间模式）。传统上，这两个任务由单独的模块处理（如 Wukong/RankMixer 用于特征交互，LONGER 用于序列建模），这阻碍了双向信息交换并阻止了统一优化。统一方法以 OneTrans 为代表，采用共享 Transformer 和统一 tokenization，将所有属性（序列和非序列）转换为单一 token 序列，并采用参数共享策略以尊重序列 token 与静态 token 的不同性质。

## 要点

- **统一架构**：单一 Transformer 取代单独的特征交互和序列模块
- **统一 tokenization**：所有特征（序列和非序列）转换为通用 token 格式
- **参数共享**：相似序列 token 共享参数，非序列 token 使用特定参数
- **跨请求 KV 缓存**：支持预计算和缓存以提高效率
- **OneTrans**：工业推荐中首个实现该范式的模型
- **每用户 GMV +5.68%**：在线 A/B 测试中得到验证

## 详情

### 碎片化问题

传统推荐架构将建模分为两个独立的轨道：

```
┌─────────────────────┐    ┌─────────────────────┐
│ Feature Interaction  │    │ Sequence Modeling    │
│ (Wukong, RankMixer) │    │ (LONGER, HSTU)       │
│                      │    │                      │
│ User × Item features │    │ Behavior history     │
│ Context features     │    │ Temporal patterns    │
└─────────┬───────────┘    └─────────┬───────────┘
          │                          │
          └──────────┬───────────────┘
                     ↓
              Separate combination
```

这种分离导致：
1. **无双向交换**：特征交互无法从序列模式中受益，反之亦然
2. **无统一优化**：每个模块独立优化，错过全局最优
3. **冗余计算**：相似模式在每个模块中分别学习

### 统一 Transformer 设计

统一方法将两个任务合并为单一架构：

```
Unified Tokenizer
    ↓
[User features] [Item features] [Context features] [History token 1] [History token 2] ... [History token N]
    ↓
Stacked Transformer Blocks (shared with parameter differentiation)
    ↓
Unified representation for prediction
```

#### 统一 Tokenization
- 将**所有**属性转换为通用 token 格式
- 序列属性（行为历史）→ 带时间排序的 token
- 非序列属性（用户画像、物品元数据、上下文）→ 无时间排序的 token
- 单一词汇表支持跨域注意力

#### 参数共享策略
- **序列 token**：在相似位置共享参数（如所有历史 token 使用相似变换）
- **非序列 token**：特定 token 参数以捕捉独特的特征特征
- 这平衡了效率（共享）与表达能力（专业化）

#### 因果注意力 + 跨请求 KV 缓存
- **因果注意力**：防止来自未来 token 的信息泄漏
- **跨请求 KV 缓存**：预计算和缓存重复特征的中间表示
  - 用户画像特征变化不频繁 → 缓存其 KV 状态
  - 物品特征在多个用户间共享 → 全局缓存
  - 减少跨请求的冗余计算

### 统一架构的益处

| 益处 | 描述 |
|------|------|
| **双向交换** | 特征模式告知序列建模，反之亦然 |
| **统一优化** | 单一目标联合优化所有组件 |
| **减少冗余** | 重叠模式的共享计算 |
| **KV 缓存** | 预计算减少每请求延迟 |
| **可扩展性** | 单一架构比多个模块扩展更高效 |
| **简化部署** | 一个模型而非多个模块需要维护 |

### OneTrans：工业验证

OneTrans（被 WWW 2026 接收）验证了这一范式：

- **统一 tokenization**：将序列和非序列属性转换为单一 token 序列
- **堆叠 OneTrans 块**：序列 token 参数共享，非序列 token 特定参数
- **因果注意力**：确保正确的信息流
- **跨请求 KV 缓存**：减少训练和推理中的计算成本
- **每用户 GMV +5.68%**：A/B 测试中显著的业务影响

### 与分离架构对比

| 方面 | 分离模块 | 统一 Transformer |
|------|---------|-----------------|
| 架构 | 多个专业模块 | 单一共享 Transformer |
| 信息流 | 单向或无 | 通过共享注意力双向 |
| 优化 | 逐模块 | 端到端 |
| KV 缓存 | 有限 | 支持跨请求缓存 |
| 维护 | 多个代码库 | 单一架构 |
| 扩展 | 每个模块独立扩展 | 统一扩展 |

### 与先前工作的关系

- **RankMixer**：统一了特征交互但不包括序列建模
- **LONGER**：优化了序列建模但不包括特征交互
- **OneTrans**：在单一架构中统一两者

## 关联

- [OneTrans](../models/OneTrans.md) — 实现该范式的模型
- [RankMixer](../models/RankMixer.md) — 特征交互专家
- [LONGER](../models/LONGER.md) — 序列建模专家
- [特征交互](./feature_interaction.md) — 统一范式的一半

## 开放问题

1. 统一 tokenization 如何处理差异很大的特征类型（类别型、连续型、文本、图像）？
2. 序列和非序列 token 之间的最优参数共享比率是什么？
3. 跨请求 KV 缓存如何影响推荐的新鲜度？
4. 统一方法能否有效处理多模态特征？
5. 与分离模块相比，统一架构的训练稳定性如何？

## 参考文献

- Zhang, Z., Pei, H., Guo, J., Wang, T., Feng, Y., Sun, H., Liu, S., & Sun, A. (2026). OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender. WWW 2026. arXiv:2510.26104.
- arXiv: https://arxiv.org/abs/2510.26104


## 更新于 2026-04-09

**来源**: 2311_paper_23110588_Hiformer_Heterogeneous_Feature_Interactions_Learning_with_T.md
：添加 Hiformer 作为统一 Transformer 骨干架构的早期工业案例，补充异构特征交互处理的技术细节
