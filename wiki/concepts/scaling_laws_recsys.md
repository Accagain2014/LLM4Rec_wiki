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

推荐系统中的扩展定律描述了模型/数据/计算规模与推荐性能之间的**可预测关系**。受大语言模型中已建立的扩展定律（Kaplan 等，2020；Hoffmann 等，2022）启发，近期工业工作证明推荐系统在以下扩展时表现出类似的可预测提升：（1）**模型参数**（更深/更宽的架构），（2）**序列长度**（更长的用户行为历史），以及（3）**训练数据**（更多用户交互）。**Meta 的 HSTU 工作（2024）首次通过大规模实证确立了推荐领域的 Scaling Law**，将推荐任务重构为生成式序列转换问题，并在 1.5T 参数规模下验证了跨越三个数量级的严格幂律增长，证明“生成式范式+架构优化”是使推荐系统遵循缩放定律的核心前提。然而，推荐系统面临独特的挑战——严格的延迟约束、分布偏移和对高 GPU 利用率的需求——使得扩展曲线与 LLM 不同。ULTRA-HSTU 等近期工作证明，扩展定律曲线可以通过协同设计来**弯曲**，在每单位计算中实现更好的性能。

## 要点

- **可预测的性能增益**：更多参数、数据和序列长度产生单调提升
- **三个扩展维度**：模型规模、序列长度、训练数据量
- **生成式范式奠基**：HSTU 首次确立推荐缩放定律，验证 1.5T 参数规模下的幂律增长
- **工业验证**：LONGER、RankMixer、HSTU 和 ULTRA-HSTU 都在生产中确认了扩展定律
- **弯曲曲线**：系统协同设计（线性注意力、统一词表、流式训练）实现每 FLOP 更好的性能
- **独特挑战**：延迟约束、分布偏移、冷启动、可解释性弱、GPU 利用率
- **业务影响**：扩展转化为可衡量的业务指标提升（CTR、CVR、参与度、核心转化 +12.4%）

## 详情

### 扩展定律基础

在 LLM 中，扩展定律描述了幂律关系：

```
Loss ∝ N^(-α) × D^(-β) × C^(-γ)
```

其中 N = 模型参数，D = 训练数据，C = 计算预算。

在推荐系统中，这种关系映射到业务指标。**HSTU 的实证研究首次明确：推荐模型质量随训练算力（FLOPs）增加呈现严格的幂律增长，跨越 3 个数量级（十亿至万亿参数）未出现性能饱和。** 这标志着推荐系统从“手工特征工程与双塔架构”正式迈入“基础模型缩放”时代。

```
Performance ∝ Compute^(-α) ∝ f(model_size, sequence_length, data_volume, compute_efficiency)
```

### 生成式范式与 HSTU 架构奠基

将推荐任务重构为生成式序列转换（Generative Recommenders）是验证缩放定律的关键前提。传统 DLRM 依赖稠密/稀疏特征拼接，难以随算力线性扩展；而生成式范式将用户历史交互序列直接视为离散 Token 序列，在自回归框架下统一建模召回、排序与重排任务。HSTU（Hierarchical Sequential Transduction Unit）作为该范式的核心骨干，通过以下设计突破扩展瓶颈：

- **统一离散化词表**：将海量用户 ID、物品 ID 及异构上下文特征统一映射为共享词表中的 Token，消除传统 Embedding 查找表的内存墙，使模型能够直接处理超大规模稀疏空间。
- **线性化注意力与相对位置偏置**：摒弃计算密集的全局 Softmax 注意力，采用可学习相对位置偏置与低秩投影/分块计算策略，将序列建模复杂度从 $O(L^2)$ 优化至接近 $O(L)$，显著提升长序列训练与推理效率。
- **流式非平稳数据训练**：针对推荐数据分布随时间快速变化的特性，采用在线流式采样、动态学习率调度与混合精度训练，保障万亿参数模型在工业级数据流上的稳定收敛。

[来源：[2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md](../sources/2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md)]

### RecSys 中的三个扩展维度

#### 1. 模型参数扩展
- **HSTU (Meta)**：首次验证推荐模型质量随训练算力呈幂律增长，跨越 **3 个数量级**（1B 至 1.5T 参数）未出现性能饱和，确立缩放定律在推荐领域的普适性。
- **RankMixer**：在相似延迟下从 ~10M 扩展到 1B 参数（100 倍）
- **OneRec-V2**：通过计算效率扩展到 8B 参数
- **OneRec-Foundation**：1.7B 和 8B 变体显示可预测的提升
- 每个维度的增加都产生可衡量的业务指标增益

#### 2. 序列长度扩展
- **LONGER**：证明超长序列（数千次交互）提供一致的增益
- **HSTU**：在处理长度为 **8192** 的超长交互序列时，推理吞吐量达到基于 FlashAttention2 的 Transformer 的 **5.3 倍至 15.2 倍**，显存占用大幅降低，满足工业场景毫秒级延迟要求。
- 更长序列同时捕捉长期偏好和短期意图
- 序列长度与性能之间的关系是**可预测且单调的**
- 注意力效率技术（token 合并、稀疏/线性注意力）支持更长序列

#### 3. 数据量扩展
- 更多用户交互 → 更好的模式学习
- OpenOneRec 使用来自 16 万用户的 9600 万交互
- **流式数据扩展**：HSTU 采用在线流式采样策略应对推荐数据分布随时间快速变化的特性，证明在动态非平稳数据流上持续扩展数据量仍能带来稳定收益。
- Meta、字节跳动和快手的工业系统都确认了数据扩展的益处

### 弯曲扩展定律曲线

ULTRA-HSTU 与 HSTU 的架构演进引入了**弯曲扩展定律曲线**的概念：

```
Performance
    ^
    |     /  Conventional models (baseline scaling)
    |    /
    |   /   ULTRA-HSTU / HSTU (bent curve — better per-FLOP efficiency)
    |  /   /
    | /   /
    |/   /
    +------------------> Compute (FLOPs)
```

在任何给定的计算预算下，协同设计的模型都比传统方法实现更高的性能。这通过以下方式实现：

- **输入序列优化**：统一离散化词表实现每 token 更好的信息密度，消除稀疏特征内存瓶颈
- **稀疏/线性注意力**：HSTU 的相对位置偏置与线性化注意力将复杂度降至 $O(L)$，实现每 FLOP 更高效的计算
- **模型拓扑**：GLU 门控前馈网络与层级转换单元优化信息流，提升每参数表征能力
- **系统协同设计**：架构 + 基础设施（混合精度、大规模数据并行、动态计算图）联合优化

### 工业证据

| 系统 | 扩展维度 | 结果 |
|------|---------|------|
| **HSTU** | 算力/参数规模 | 1.5T 参数，跨越 3 个数量级幂律增长，A/B 测试核心转化 +12.4% |
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
| **推理扩展效率** | 每单位额外推理计算的性能增益（HSTU 在 8192 序列长度下达 5.3x-15.2x 吞吐提升） |
| **业务 ROI** | 每美元计算的业务指标提升 |

### RecSys 扩展的挑战

1. **延迟约束**：与 LLM 不同，推荐器必须在 < 10ms 内响应
2. **分布偏移**：用户偏好变化，需要频繁重新训练与流式数据适配
3. **冷启动与长尾覆盖**：生成式范式高度依赖历史行为序列的上下文密度，对于零交互新用户或极度稀疏的长尾物品，仍需结合传统特征工程、知识图谱或外部先验进行增强
4. **算力与工程门槛**：万亿参数训练与推理依赖超大规模分布式集群、定制化通信优化与专用硬件，中小团队难以直接复现或低成本部署
5. **可解释性与业务归因**：端到端自回归生成过程缺乏传统推荐模型的特征权重可视化能力，在需要强业务归因、合规审计或策略干预的场景中应用受限
6. **多目标优化**：扩展必须同时改善多个指标（CTR、CVR、时长、多样性）
7. **服务成本**：更大模型在服务大规模时成本更高（每天数十亿请求）

### 扩展定律 vs 收益递减

一个关键问题：扩展定律最终会饱和吗？

- 当前工业证据表明在所探索的范围内**尚未饱和**。**HSTU 在 1.5T 参数规模下仍保持严格的幂律增长**，证明“生成式范式+架构优化”有效推迟了收益递减拐点。
- LONGER 验证了在非常长序列上的一致增益
- RankMixer 验证了高达 1B 参数的一致增益
- ULTRA-HSTU 表明协同设计可以扩展范围

## 关联

- [HSTU / 生成式推荐](../models/HSTU.md) — 确立推荐缩放定律的万亿参数序列转换器
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
6. 生成式推荐范式与传统判别式模型在缩放定律上的收敛路径是否存在本质差异？

## 参考文献

- Zhai, J., Liao, L., Liu, X., et al. (2024). Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations. ICML 2024. arXiv:2402.17152.
- Ding, Q., Course, K., Ma, L., et al. (2026). Bending the Scaling Law Curve in Large-Scale Recommendation Systems. arXiv:2602.16986.
- Chai, Z., et al. (2025). LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders. RecSys 2025. arXiv:2505.04421.
- Zhu, J., et al. (2025). RankMixer: Scaling Up Ranking Models in Industrial Recommenders. arXiv:2507.15551.

## 更新于 2026-04-10

**来源**: [2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md](../sources/2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md)
：补充 HSTU 作为推荐领域缩放定律的奠基性实证工作；明确 1.5T 参数规模、3 个数量级的算力性能幂律关系；新增“生成式范式与 HSTU 架构奠基”小节；更新工业证据表与挑战分析；强化“生成式范式使 Scaling Law 成立”的核心结论。

## 更新于 2026-04-09

**来源**: 2403_paper_24030254_Wukong_Towards_a_Scaling_Law_for_Large-Scale_Recommendation.md
：补充 Wukong 作为推荐领域首个确立缩放定律的里程碑工作；更新 100+ GFLOP 阈值下的单调增益数据；增加“纯 FM 堆叠 vs Transformer 扩展”的对比视角。

## 更新于 2026-04-09

**来源**: 2203_paper_22031101_DHEN_A_Deep_and_Hierarchical_Ensemble_Network_for_Large-Sca.md
：在“训练效率与系统协同优化”小节中，引用 DHEN 的协同训练系统作为工业界突破深层网络算力瓶颈的早期实践，补充动态计算图裁剪与混合精度在推荐场景的应用背景。

---

## 更新完成：2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md
**更新时间**: 2026-04-10 11:48
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
