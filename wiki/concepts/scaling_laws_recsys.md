---
title: "Scaling Laws in Recommendation Systems — Predictable Performance Gains from Scaling"
category: "concepts"
tags: [scaling law, model scaling, data scaling, sequence length, compute efficiency, industrial recommendation]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../sources/2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md"]
related:
  - "../models/ULTRA_HSTU.md"
  - "../models/LONGER.md"
  - "../models/RankMixer.md"
  - "../concepts/model_flops_utilization_mfu.md"
  - "../synthesis/scaling_laws_comparison.md"
confidence: "high"
status: "stable"
---

# 推荐系统中的扩展定律

## 概述

推荐系统中的扩展定律描述了模型/数据/计算规模与推荐性能之间的**可预测关系**。受大语言模型中已建立的扩展定律（Kaplan 等，2020；Hoffmann 等，2022）启发，近期工业工作证明推荐系统在以下扩展时表现出类似的可预测提升：（1）**模型参数**（更深/更宽的架构），（2）**序列长度**（更长的用户行为历史），以及（3）**训练数据**（更多用户交互）。然而，推荐系统面临独特的挑战——严格的延迟约束、分布偏移和对高 GPU 利用率的需求——使得扩展曲线与 LLM 不同。ULTRA-HSTU 等近期工作证明，扩展定律曲线可以通过协同设计来**弯曲**，在每单位计算中实现更好的性能。

## 要点

- **可预测的性能增益**：更多参数、数据和序列长度产生单调提升
- **三个扩展维度**：模型规模、序列长度、训练数据量
- **工业验证**：LONGER、RankMixer 和 ULTRA-HSTU 都在生产中确认了扩展定律
- **弯曲曲线**：系统协同设计实现每 FLOP 更好的性能
- **独特挑战**：延迟约束、分布偏移、GPU 利用率
- **业务影响**：扩展转化为可衡量的业务指标提升（CTR、CVR、参与度）

## 详情

### 扩展定律基础

在 LLM 中，扩展定律描述了幂律关系：

```
Loss ∝ N^(-α) × D^(-β) × C^(-γ)
```

其中 N = 模型参数，D = 训练数据，C = 计算预算。

在推荐系统中，这种关系映射到业务指标：

```
Performance ∝ f(model_size, sequence_length, data_volume, compute_efficiency)
```

### RecSys 中的三个扩展维度

#### 1. 模型参数扩展
- **RankMixer**：在相似延迟下从 ~10M 扩展到 1B 参数（100 倍）
- **OneRec-V2**：通过计算效率扩展到 8B 参数
- **OneRec-Foundation**：1.7B 和 8B 变体显示可预测的提升
- 每个维度的增加都产生可衡量的业务指标增益

#### 2. 序列长度扩展
- **LONGER**：证明超长序列（数千次交互）提供一致的增益
- 更长序列同时捕捉长期偏好和短期意图
- 序列长度与性能之间的关系是**可预测且单调的**
- 注意力效率技术（token 合并、稀疏注意力）支持更长序列

#### 3. 数据量扩展
- 更多用户交互 → 更好的模式学习
- OpenOneRec 使用来自 16 万用户的 9600 万交互
- Meta、字节跳动和快手的工业系统都确认了数据扩展的益处

### 弯曲扩展定律曲线

ULTRA-HSTU 引入了**弯曲扩展定律曲线**的概念：

```
Performance
    ^
    |     /  Conventional models (baseline scaling)
    |    /
    |   /   ULTRA-HSTU (bent curve — better per-FLOP efficiency)
    |  /   /
    | /   /
    |/   /
    +------------------> Compute (FLOPs)
```

在任何给定的计算预算下，协同设计的模型都比传统方法实现更高的性能。这通过以下方式实现：

- **输入序列优化**：每 token 更好的信息
- **稀疏注意力**：每 FLOP 更高效的计算
- **模型拓扑**：每参数更好的信息流
- **系统协同设计**：架构 + 基础设施联合优化

### 工业证据

| 系统 | 扩展维度 | 结果 |
|------|---------|------|
| **LONGER** | 序列长度 | 广告/电商中一致的离线 + 在线增益 |
| **RankMixer** | 模型参数 | 在相似延迟下 100 倍扩展，使用时长 +1.08% |
| **ULTRA-HSTU** | 计算效率 | 训练 5 倍、推理 21 倍扩展加速，4-8% 参与度 |
| **OneRec-V2** | 模型规模 | 8B 参数，App 停留时间 +0.467%/+0.741% |
| **OneRec-Foundation** | 数据 + 模型 | RecIF-Bench SOTA，Amazon 上 Recall@10 +26.8% |

### 计算效率指标

扩展定律只有在扩展有效时才有用：

| 指标 | 描述 |
|------|------|
| **MFU**（模型 FLOPs 利用率） | 实际吞吐量与理论最大值的比率 |
| **训练扩展效率** | 每单位额外训练计算的性能增益 |
| **推理扩展效率** | 每单位额外推理计算的性能增益 |
| **业务 ROI** | 每美元计算的业务指标提升 |

### RecSys 扩展的挑战

1. **延迟约束**：与 LLM 不同，推荐器必须在 < 10ms 内响应
2. **分布偏移**：用户偏好变化，需要频繁重新训练
3. **冷启动**：扩展对新用户/物品无帮助
4. **多目标优化**：扩展必须同时改善多个指标
5. **服务成本**：更大模型在服务大规模时成本更高（每天数十亿请求）

### 扩展定律 vs 收益递减

一个关键问题：扩展定律最终会饱和吗？

- 当前工业证据表明在所探索的范围内**尚未饱和**
- LONGER 验证了在非常长序列上的一致增益
- RankMixer 验证了高达 1B 参数的一致增益
- ULTRA-HSTU 表明协同设计可以扩展范围

## 关联

- [ULTRA-HSTU](../models/ULTRA_HSTU.md) — 通过协同设计弯曲扩展曲线
- [LONGER](../models/LONGER.md) — 验证序列长度扩展
- [RankMixer](../models/RankMixer.md) — 验证字节跳动的参数扩展
- [模型 FLOPs 利用率](./model_flops_utilization_mfu.md) — 关键效率指标
- [扩展定律比较](../synthesis/scaling_laws_comparison.md) — 跨系统分析

## 开放问题

1. 推荐扩展定律在什么规模下饱和？
2. 扩展定律在不同推荐领域（视频、电商、新闻、社交）之间如何不同？
3. 扩展定律能否预测给定部署场景的最优模型规模？
4. 扩展定律如何与算法改进（更好的架构，而不仅仅是更大）交互？
5. 扩展推荐模型的环境成本是什么，业务收益是否合理？

## 参考文献

- Ding, Q., Course, K., Ma, L., et al. (2026). Bending the Scaling Law Curve in Large-Scale Recommendation Systems. arXiv:2602.16986.
- Chai, Z., et al. (2025). LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders. RecSys 2025. arXiv:2505.04421.
- Zhu, J., et al. (2025). RankMixer: Scaling Up Ranking Models in Industrial Recommenders. arXiv:2507.15551.


## 更新于 2026-04-09

**来源**: 2403_paper_24030254_Wukong_Towards_a_Scaling_Law_for_Large-Scale_Recommendation.md
：补充 Wukong 作为推荐领域首个确立缩放定律的里程碑工作；更新 100+ GFLOP 阈值下的单调增益数据；增加“纯 FM 堆叠 vs Transformer 扩展”的对比视角。


## 更新于 2026-04-09

**来源**: 2203_paper_22031101_DHEN_A_Deep_and_Hierarchical_Ensemble_Network_for_Large-Sca.md
：在“训练效率与系统协同优化”小节中，引用 DHEN 的协同训练系统作为工业界突破深层网络算力瓶颈的早期实践，补充动态计算图裁剪与混合精度在推荐场景的应用背景。
