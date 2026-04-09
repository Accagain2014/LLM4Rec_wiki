---
title: "Model FLOPs Utilization (MFU) — Measuring Hardware Efficiency in Recommendation Models"
category: "concepts"
tags: [MFU, hardware efficiency, GPU utilization, compute efficiency, scaling, RankMixer]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../sources/2507_paper_25071555_RankMixer_Scaling_Up_Ranking_Models_in_Industrial_Recommend.md"]
related:
  - "../models/RankMixer.md"
  - "../models/ULTRA_HSTU.md"
  - "../concepts/scaling_laws_recsys.md"
  - "../concepts/hardware_aware_design.md"
confidence: "high"
status: "stable"
---

# 模型 FLOPs 利用率（MFU）— 推荐模型中的硬件效率

## 概述

模型 FLOPs 利用率（MFU）衡量**实际计算吞吐量与硬件加速器（通常是 GPU）理论最大值的比率**。在推荐系统中，MFU 已成为关键指标，因为许多传统排序模型由于不规则的内存访问模式和 CPU 时代的设计选择，在现代 GPU 上实现极低的利用率（低至 4.5%）。低 MFU 意味着单纯增加更多计算不会转化为成比例的性能提升——硬件未被充分利用。因此，提高 MFU 对于扩展推荐模型至关重要：RankMixer 证明，用硬件感知设计取代手工模块可以将 MFU 从 4.5% 提升到 45%（10 倍提升），在相似延迟下实现 100 倍参数扩展。MFU 日益被认为是决定扩展定律能否在生产系统中实际实现的关键因素。

## 要点

- **MFU = 实际吞吐量 / 理论最大吞吐量**
- **传统排序模型**：由于 CPU 时代设计模式，MFU 仅 4.5%
- **硬件感知模型**：通过 GPU 优化设计实现 45%+ MFU
- **使能扩展**：更高的 MFU 意味着更有效地利用计算预算
- **RankMixer 案例**：10 倍 MFU 提升使 100 倍参数扩展成为可能
- **ULTRA-HSTU**：系统协同设计实现训练/推理 5 倍/21 倍扩展加速

## 详情

### 什么是 MFU？

MFU 量化模型如何有效利用可用的硬件计算：

```
MFU = 每秒实际处理的 token 数 / 理论最大每秒 token 数
```

具有 100% MFU 的模型将始终使 GPU 的算术单元饱和。实际上：
- **优化良好的 LLM**：40-60% MFU
- **传统排序模型**：4.5% MFU（RankMixer 测量）
- **硬件感知设计**：45%+ MFU（RankMixer）

### 为什么传统模型的 MFU 低

传统推荐排序模型存在以下问题：

1. **不规则内存访问**：稀疏特征查找导致内存瓶颈，而非计算瓶颈
2. **小批量大小**：严格的延迟限制阻止大批量处理
3. **复杂的特征交叉**：具有不可并行操作的手工模块
4. **CPU 时代模式**：为单线程 CPU 执行优化的设计，而非 GPU 并行
5. **多样化模块库**：针对不同特征类型的手工模块，每个模块的 GPU 利用率都差

### 低 MFU 的影响

| 后果 | 描述 |
|------|------|
| **计算浪费** | 在 4.5% MFU 下 95.5% 的理论 FLOPs 未被使用 |
| **扩展性差** | 增加更多计算产生递减回报 |
| **高成本** | 需要比理论所需更多的 GPU |
| **延迟压力**：低效计算使延迟目标更难实现 |

### 提高 MFU

#### 硬件感知架构设计
- **规则计算模式**：GPU 擅长的矩阵乘法和卷积
- **可并行操作**：所有 token/特征同时处理
- **内存友好访问**：合并的内存访问模式

#### RankMixer 的方法
- **Token 混合**：用规则矩阵操作替换不规则特征交叉
- **逐 token FFN**：在保持特征多样性的同时使用可并行操作
- **Sparse-MoE**：高效地将计算路由到专业专家

#### ULTRA-HSTU 的方法
- **系统协同设计**：架构和基础设施共同优化
- **稀疏注意力模式**：为 GPU 友好执行而设计
- **模型拓扑**：针对每 FLOP 信息流进行优化

### MFU 与扩展定律

MFU 是扩展定律的关键使能因素：

```
Effective Compute = Theoretical Compute × MFU
```

如果 MFU 低，扩展理论计算（更多 GPU、更大模型）产生最小增益。只有通过提高 MFU 才能实现扩展的益处。

RankMixer 清楚地证明了这一点：
- 之前：4.5% MFU → 扩展收益有限
- 之后：45% MFU → 在相似延迟下 100 倍参数扩展

### 测量 MFU

MFU 可以在不同级别测量：

| 级别 | 测量内容 |
|------|---------|
| **训练 MFU** | 训练期间的吞吐量（通常由于更大批量而更高） |
| **推理 MFU** | 服务期间的吞吐量（通常由于延迟约束而更低） |
| **逐层 MFU** | 单个模型层的利用率 |
| **端到端 MFU** | 包括数据加载和后处理的完整系统利用率 |

### LLM 与 RecSys 中的 MFU 对比

| 方面 | LLM | 推荐系统 |
|------|-----|---------|
| 典型 MFU | 40-60% | 4.5-45%（变化很大） |
| 瓶颈 | 内存带宽（注意力） | 不规则特征访问 |
| 批量大小 | 大（训练），小（推理） | 小（训练和推理都是） |
| 优化重点 | FlashAttention、内核融合 | 特征嵌入优化、tokenization |

## 关联

- [RankMixer](../models/RankMixer.md) — 展示 10 倍 MFU 提升
- [ULTRA-HSTU](../models/ULTRA_HSTU.md) — 用于提高 MFU 的系统协同设计
- [扩展定律](./scaling_laws_recsys.md) — MFU 是实际扩展的前提
- [硬件感知设计](./hardware_aware_design.md) — 更广泛的设计哲学

## 开放问题

1. 在延迟约束下，推荐模型的理论最大 MFU 是多少？
2. MFU 在不同 GPU 架构（A100、H100、TPU）之间如何变化？
3. MFU 能否通过神经架构搜索自动优化？
4. MFU 与模型表达能力之间如何权衡——最具表达能力的模型是否天生具有更低的 MFU？
5. MFU 是否应成为 RecSys 论文的标准报告指标？

## 参考文献

- Zhu, J., Fan, Z., Zhu, X., Jiang, Y., Wang, H., Han, X., Ding, H., Wang, X., Zhao, W., Gong, Z., Yang, H., Chai, Z., Chen, Z., Zheng, Y., Chen, Q., Zhang, F., Zhou, X., Xu, P., Yang, X., Wu, D., & Liu, Z. (2025). RankMixer: Scaling Up Ranking Models in Industrial Recommenders. arXiv:2507.15551.
- Ding, Q., Course, K., Ma, L., et al. (2026). Bending the Scaling Law Curve in Large-Scale Recommendation Systems. arXiv:2602.16986.
