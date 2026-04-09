---
title: "HiGR — Hierarchical Planning for Generative Slate Recommendation"
category: "models"
tags: [HiGR, slate recommendation, hierarchical planning, semantic ID, multi-objective, Tencent, generative retrieval]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/paper_8edbf8_HiGR_Efficient_Generative_Slate_Recommendation_via_Hierarch.md"]
related:
  - "../concepts/slate_recommendation.md"
  - "../concepts/hierarchical_planning_rec.md"
  - "../concepts/generative_retrieval.md"
  - "../models/PLUM.md"
  - "../methods/multi_objective_alignment.md"
confidence: "high"
status: "stable"
---

# HiGR — 基于层次化规划的高效生成式列表推荐

## 概述

HiGR（Hierarchical planning + multi-objective preference alignment for Generative Recommendation）是一个部署在腾讯的**生成式列表推荐**高效框架。它解决了现有生成式推荐方法的三个关键局限：物品 tokenization 纠缠、低效的序列解码，以及缺乏全局 slate 级规划。HiGR 相比先前的生成式基线实现了 **10%+ 的离线提升**和 **5 倍推理加速**。

## 要点

- **层次化两阶段生成**：列表级规划 → 物品级解码
- **残差量化 + 对比自编码器**用于 Semantic ID tokenization
- **多目标列表级偏好对齐**，利用隐式反馈
- **生产级部署**于腾讯（数亿用户）
- **在线 A/B 测试**：平均观看时长 +1.22%，平均播放次数 +1.73%

## 详情

### 问题：Slate 推荐

Slate 推荐在单次展示中向用户呈现一个**排序物品列表**。传统方法逐物品优化，忽略了物品间的依赖关系和全局 slate 质量。使用自回归 Semantic ID 生成的生成式模型面临以下问题：

1. **Tokenization 纠缠**：物品 ID 缺乏语义结构
2. **低效解码**：序列自回归生成速度慢
3. **无 slate 级规划**：每个 token 生成时缺乏全局意图

### 架构

HiGR 将生成分解为两个阶段：

#### 第一阶段：列表级规划
- 从用户上下文中捕捉**全局 slate 意图**
- 生成 slate 级表示以约束搜索空间
- 支持跨多目标的可控生成

#### 第二阶段：物品级解码
- 在 slate 规划的条件下生成单个物品的 Semantic ID
- 使用残差量化码实现结构化的层次 ID
- 搜索空间显著缩减 → 5 倍加速

### Semantic ID Tokenization

HiGR 设计了一个**带残差量化和对比约束的自编码器**：
- 物品被映射到**多层码字元组**（粗粒度 → 细粒度）
- 对比损失确保语义相似的物品共享前缀码
- 支持**可控生成**：前缀码控制类目/类型，后缀码控制具体细节

### 多目标偏好对齐

- **列表级优化**：整体优化 slate 质量，而非逐物品
- **多目标对齐**：平衡用户偏好与业务需求
- 利用**用户隐式反馈**（观看时长、播放次数、跳过）进行训练

### 性能

| 指标 | 结果 |
|------|------|
| 离线提升 | 相比 SOTA 生成式基线 >10% |
| 推理加速 | 比自回归基线快 5 倍 |
| 在线观看时长 | +1.22%（腾讯 A/B 测试） |
| 在线视频播放 | +1.73%（腾讯 A/B 测试） |

### 部署

- 部署于**腾讯商业平台**（数亿用户）
- 在生产延迟约束下处理实时 slate 生成
- 与腾讯推荐基础设施集成

## 关联

- [Slate 推荐](../concepts/slate_recommendation.md) — HiGR 解决的问题场景
- [层次化规划](../concepts/hierarchical_planning_rec.md) — 核心生成范式
- [PLUM](./PLUM.md) — 另一个工业级生成式推荐框架（YouTube）
- [生成式检索](../concepts/generative_retrieval.md) — HiGR 构建的更广泛范式
- [多目标对齐](../methods/multi_objective_alignment.md) — HiGR 的对齐机制

## 开放问题

1. HiGR 如何泛化到非视频推荐领域（电商、新闻）？
2. 层次化规划机制能否扩展到动态/交互式 slate 更新？
3. 对于不同物品目录，最优的层次数量是多少？

## 参考文献

- Pang, Y., Liu, Z., Li, Y., Zhu, S., Luo, Z., Yu, C., Wu, S., Shen, S., Xu, C., Wang, B., Jiang, K., Yu, H., Zhuo, C., & Li, Z. (2025). HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning and Multi-Objective Preference Alignment. arXiv:2512.24787.
- arXiv: https://arxiv.org/abs/2512.24787
