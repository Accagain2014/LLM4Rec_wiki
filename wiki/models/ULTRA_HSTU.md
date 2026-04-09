---
title: "ULTRA-HSTU — Bending the Scaling Law Curve in Recommendation"
category: "models"
tags: [ULTRA-HSTU, HSTU, scaling law, sparse attention, Meta, sequential recommendation, system co-design]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../sources/2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md"]
related:
  - "../concepts/scaling_laws_recsys.md"
  - "../concepts/model_flops_utilization_mfu.md"
  - "../methods/sparse_attention_seq_rec.md"
  - "../entities/meta.md"
confidence: "high"
status: "stable"
---

# ULTRA-HSTU — 弯曲大规模推荐中的扩展定律曲线

## 概述

ULTRA-HSTU 是 Meta 开发的下一代序列推荐模型，通过**端到端模型与系统协同设计**开发。它解决了严重依赖交叉注意力机制来解决二次计算瓶颈的方法的局限性——这种策略可能限制从自注意力中获得的表示能力。ULTRA-HSTU 在三个维度上进行创新：**输入序列设计**、**稀疏注意力机制**和**模型拓扑**，相比传统模型实现**5 倍更快的训练扩展**和**21 倍更快的推理扩展**。全面部署后，它每日服务数十亿用户，在生产中驱动 **4% 到 8% 的消费和参与度提升**。

## 要点

- **端到端模型 + 系统协同设计**：联合优化架构和基础设施
- **输入序列创新**：改进序列构建以获得更好的表示
- **稀疏注意力机制**：在不牺牲自注意力能力的前提下解决二次瓶颈
- **模型拓扑创新**：重构信息流以实现更好的扩展
- 相比传统模型**训练扩展加速 5 倍**，**推理扩展加速 21 倍**
- Meta 生产中 **4-8% 参与度提升**
- **每日服务数十亿用户**

## 详情

### 扩展定律挑战

最近的 LLM 进展揭示了有希望的扩展定律，激发了对推荐领域长序列建模和更深层次架构的研究。然而，许多方法面临根本性的权衡：

- **交叉注意力方法**：通过关注压缩表示来降低计算复杂度，但这限制了自注意力可以捕捉的表示能力
- **完整自注意力**：最大化表示能力，但随序列长度二次扩展

ULTRA-HSTU 旨在**弯曲扩展定律曲线**——通过使每个 FLOP 更有效，在每单位计算中获得更好的性能。

### 三个创新维度

#### 1. 输入序列设计

ULTRA-HSTU 改进了用户交互历史的构建和输入方式：

- **更丰富的特征编码**：将时间、上下文和行为信号纳入输入表示
- **序列组织**：优化不同交互类型（点击、浏览、点赞、分享）的排序和加权
- **多粒度 token**：在同一序列中支持细粒度（单个交互）和粗粒度（会话摘要）token

#### 2. 稀疏注意力机制

ULTRA-HSTU 不是放弃自注意力转向交叉注意力，而是使自注意力更高效：

- **选择性注意力模式**：并非所有 token 对都需要相互关注；稀疏模式将计算集中在重要的地方
- **层次化稀疏**：不同的注意力头使用不同的稀疏模式，捕捉局部和全局依赖
- **硬件感知的稀疏模式**：设计为在不规则计算模式下最大化 GPU 利用率

这在大幅降低计算成本的同时保留了自注意力的**表示能力**。

#### 3. 模型拓扑

ULTRA-HSTU 重构了信息在模型中的流动方式：

- **优化的层连接**：层之间的连接并非同等重要；拓扑设计为每参数最大信息流
- **高效的残差连接**：确保梯度流动，无冗余计算
- **专业化层角色**：不同的层关注序列建模的不同方面（局部模式、全局趋势、用户意图）

### 扩展效率

"弯曲扩展定律曲线"的比喻指在每个计算点实现更好的性能：

```
Performance
    ^
    |     /  Conventional models
    |    /
    |   /   ULTRA-HSTU (bent curve)
    |  /   /
    | /   /
    |/   /
    +------------------> Compute (FLOPs)
```

在任何给定的计算预算下，ULTRA-HSTU 都比传统方法实现更高的性能。

### 性能

| 指标 | 结果 |
|------|------|
| 训练扩展加速 | 相比传统模型 5 倍 |
| 推理扩展加速 | 相比传统模型 21 倍 |
| 参与度提升 | 4-8%（生产 A/B 测试） |
| 部署规模 | 每日数十亿用户 |
| 平台 | Meta 生产系统 |

### 与 HSTU 的关系

ULTRA-HSTU 建立在 Meta 早期的 HSTU（Hierarchical Sequential Transduction Unit）架构之上：

| 方面 | HSTU | ULTRA-HSTU |
|------|------|------------|
| 注意力 | 层次化转导 | 稀疏注意力 + 拓扑优化 |
| 扩展 | 线性 | 弯曲扩展定律（更好的每 FLOP 效率） |
| 系统设计 | 以模型为中心 | 端到端模型 + 系统协同设计 |
| 部署 | 生产 | 更大规模的生产 |

## 关联

- [推荐中的扩展定律](../concepts/scaling_laws_recsys.md) — ULTRA-HSTU 弯曲了扩展曲线
- [模型 FLOPs 利用率](../concepts/model_flops_utilization_mfu.md) — 系统协同设计提升 MFU
- [稀疏注意力](../methods/sparse_attention_seq_rec.md) — 核心效率机制
- [Meta](../entities/meta.md) — 开发组织
- [LONGER](./LONGER.md) — 字节跳动的长序列效率方法
- [RankMixer](./RankMixer.md) — 另一种硬件感知扩展方法

## 开放问题

1. ULTRA-HSTU 使用什么具体的稀疏注意力模式（滑动窗口、空洞、学习型）？
2. 模型拓扑与标准 Transformer 堆叠有何不同？
3. 输入序列设计与稀疏注意力之间的交互是什么——它们是联合优化的吗？
4. ULTRA-HSTU 与纯解码器生成式推荐方法相比如何？
5. 系统协同设计原则能否迁移到其他组织的基础设施？

## 参考文献

- Ding, Q., Course, K., Ma, L., Sun, J., Liu, R., Zhu, Z., Yin, C., Li, W., Li, D., Shi, Y., Cao, X., Yang, Z., Li, H., Liu, X., Xue, B., Li, H., Jian, R., He, D. S., Qian, J., Ma, M., Zhang, Q., & Li, R. (2026). Bending the Scaling Law Curve in Large-Scale Recommendation Systems. arXiv:2602.16986.
- arXiv: https://arxiv.org/abs/2602.16986
