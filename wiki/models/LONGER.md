---
title: "LONGER — Long-Sequence Optimized Transformer for Industrial Recommenders"
category: "models"
tags: [LONGER, long sequence, transformer, ByteDance, sparse attention, token merge, industrial deployment, scaling law]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md"]
related:
  - "../concepts/scaling_laws_recsys.md"
  - "../methods/sparse_attention_seq_rec.md"
  - "../methods/long_context_efficiency.md"
  - "../entities/bytedance.md"
confidence: "high"
status: "stable"
---

# LONGER — 面向 GPU 高效推荐器的长序列优化 Transformer

## 概述

LONGER（Long-sequence Optimized traNsformer for GPU-Efficient Recommenders）是字节跳动开发的工业级规模序列建模系统，解决了在生产推荐系统中建模**超长用户行为序列**的挑战。先前的解决方案依赖于两阶段检索或间接建模范式，遭受上下游不一致和计算效率低下的问题。LONGER 引入了完全同步的端到端 Transformer，具有三项关键创新：（1）**全局 token 机制**用于稳定长上下文上的注意力，（2）**token 合并模块**结合轻量级 InnerTransformers 和混合注意力以降低二次复杂度，（3）**GPU 优化工程**包括混合精度训练、KV 缓存服务和统一训练/服务框架。LONGER 已部署于字节跳动 10+ 场景，服务数十亿用户。

## 要点

- **端到端长序列建模**：消除两阶段检索的不一致性
- **全局 token 机制**：稳定超长上下文上的注意力模式
- **Token 合并 + InnerTransformer**：降低二次注意力复杂度
- **全 GPU 优化**：混合精度、激活重计算、KV 缓存
- **工业级部署**：字节跳动 10+ 场景，数十亿用户
- **验证工业级扩展定律**：广告和电商中离线和在线的一致增益**

## 详情

### 问题：超长序列建模

在工业推荐系统中，捕捉**长期和短期用户偏好**需要对非常长的行为序列建模。现有方法面临两个根本性局限：

1. **两阶段检索**：先检索候选，再排序——引入阶段间不一致
2. **间接建模**：通过摘要或池化近似长序列——丢失细粒度信息

两种方法都无法充分利用长用户历史中的信息。

### 核心创新

#### 1. 全局 Token 机制

- 引入特殊的**全局 token**，与序列中所有位置相互关注
- 作为稳定信号，防止在极长序列上的注意力退化
- 与 BERT 中的 [CLS] token 类似，但在训练期间动态学习
- 防止"中间丢失"问题，即中间序列物品获得的注意力不足

#### 2. 带 InnerTransformers 的 Token 合并模块

为了解决长序列上自注意力的**二次复杂度**：

- **Token 合并**：将相似 token 分组以减少有效序列长度
- **InnerTransformers**：轻量级 transformer 模块，处理合并后的 token 组
- **混合注意力策略**：在关键 token 上使用完整自注意力，在合并组上使用近似注意力
- 实现近线性扩展，同时保持表示能力

该方法可理解为：
```
Full sequence → Token merge → Grouped tokens → InnerTransformer → Hybrid attention → Output
```

#### 3. 工程优化

LONGER 包含全面的系统级优化：

| 优化 | 目的 |
|------|------|
| 混合精度训练 | 以最小精度损失实现更快训练 |
| 激活重计算 | 减少更长序列的内存占用 |
| KV 缓存服务 | 通过缓存注意力状态加速推理 |
| 完全同步训练/服务 | 统一的 GPU 稠密和稀疏参数更新 |

这确保模型不仅在理论上合理，而且**已准备好投入生产**。

### 部署与结果

LONGER 已在字节跳动的**广告和电商服务**中部署：

- **10+ 重要场景**，涵盖 diverse 推荐任务
- 每日服务**数十亿用户**
- 在离线指标和在线 A/B 测试中**持续超越强基线**
- **验证工业级扩展定律**：更长序列和更大模型产生可预测、单调的 CTR、CVR 和停留时间提升

### 与扩展定律的关联

LONGER 为推荐系统中的扩展定律提供了经验证据：
- 增加序列长度 → 更好的偏好捕捉 → 提升指标
- 增加模型容量 → 更好的模式学习 → 提升指标
- 这种关系是**可预测且单调的**，类似于 LLM 扩展定律

这验证了在工业推荐中投入更大、更长序列模型的投资。

## 关联

- [推荐中的扩展定律](../concepts/scaling_laws_recsys.md) — LONGER 提供经验验证
- [稀疏注意力](../methods/sparse_attention_seq_rec.md) — 相关效率技术
- [长上下文效率](../methods/long_context_efficiency.md) — LONGER 的优化方法
- [字节跳动](../entities/bytedance.md) — 部署组织

## 开放问题

1. 在收益递减之前的最大有效序列长度是多少？
2. Token 合并质量在不同推荐领域（视频、电商、新闻）之间如何变化？
3. LONGER 在生产规模下的确切延迟概况是什么？
4. 全局 token 机制能否扩展到跨用户协同建模？

## 参考文献

- Chai, Z., Ren, Q., Xiao, X., Yang, H., Han, B., Zhang, S., Chen, D., Lu, H., Zhao, W., Yu, L., Xie, X., Ren, S., Sun, X., Tan, Y., Xu, P., Zheng, Y., & Wu, D. (2025). LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders. RecSys 2025. arXiv:2505.04421.
- arXiv: https://arxiv.org/abs/2505.04421
