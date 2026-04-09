---
title: "RankMixer — Hardware-Aware Scalable Ranking Model"
category: "models"
tags: [RankMixer, ranking model, hardware-aware, MFU, Sparse-MoE, ByteDance, feature interaction, scaling]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../sources/2507_paper_25071555_RankMixer_Scaling_Up_Ranking_Models_in_Industrial_Recommend.md"]
related:
  - "../concepts/model_flops_utilization_mfu.md"
  - "../concepts/scaling_laws_recsys.md"
  - "../concepts/unified_transformer_backbone.md"
  - "../models/LONGER.md"
  - "../entities/bytedance.md"
confidence: "high"
status: "stable"
---

# RankMixer — 工业推荐中排序模型的扩展

## 概述

RankMixer 是字节跳动提出的**硬件感知可扩展排序模型**，解决了在严格延迟和 QPS 约束下扩展推荐排序模型的实际挑战。它解决了两个关键问题：（1）传统特征交叉模块继承自 CPU 时代，无法利用现代 GPU，导致模型 FLOPs 利用率（MFU）低下；（2）多样化手工模块阻碍统一扩展。RankMixer 用**统一的 token 混合架构**替代这些模块，在保持 Transformer 级并行性的同时，用高效的多头 token 混合取代二次自注意力。Sparse-MoE 变体扩展到 **10 亿参数**，实现 **MFU 10 倍提升**（从 4.5% 到 45%）和**在相似延迟下 100 倍参数扩展**。已部署于推荐和广告场景，使用户活跃天数提升 0.3%，应用内使用时长提升 1.08%。

作为工业推荐系统大模型化演进的关键起点，RankMixer 首次系统地将 ranking backbone 改造为适合大规模扩展的结构，验证了推荐排序模型可围绕统一的 token 交互主干形成独立的 scaling 路线，为后续判别式大模型的工业化奠定了架构基础。[来源：rankmixer_to_oneranker.md]

## 要点

- **硬件感知设计**：针对 GPU 并行优化，而非 CPU 时代模式
- **多头 token 混合**：用线性复杂度替代方案取代二次自注意力
- **逐 token FFN**：保持独立特征子空间建模和跨特征交互
- **Sparse-MoE 变体**：通过动态专家路由扩展到 1B 参数
- **MFU 提升**：从 4.5% 到 45%（10 倍提升）
- **100 倍参数扩展**：在近似相同推理延迟下
- **生产级部署**：推荐和广告的全流量服务
- **历史定位**：可扩展 Ranking Backbone 的技术起点与验证基石
- **后续演进**：直接催生 TokenMixer-Large、MSN、UG-Separation 等补强工作

## 详情

### 两个实际障碍

#### 1. 成本和延迟约束
工业排序模型必须在以下约束下运行：
- 严格延迟限制（通常 < 10ms/请求）
- 高 QPS 需求（每秒数千查询）
- 固定的服务成本预算

#### 2. 传统设计的低 MFU
大多数排序模型使用 **CPU 时代设计的手工特征交叉模块**：
- 具有不规则内存访问模式的复杂特征交互
- GPU 利用率低（MFU 低至 4.5%）
- 无法随计算增加有效扩展

### RankMixer 架构

#### 多头 Token 混合
```
Feature tokens → Multi-head token mixing → Per-token FFNs → Output
```

- **Token 混合**：信息通过矩阵乘法在 token（特征）间流动，这在 GPU 上高度可并行化
- **取代自注意力**：O(N*d) 而非 O(N^2) 复杂度，其中 N 是特征数量
- **保持并行性**：所有 token 同时处理，不同于序列化的 RNN 式方法

#### 逐 Token FFN
- 每个 token（特征子空间）有自己的前馈网络
- 保持**独立特征子空间建模**（用户特征、物品特征、上下文特征）
- 通过 token 混合层实现**跨特征空间交互**
- 比共享 FFN 更灵活，同时保持计算效率

#### Sparse-MoE 变体
用于进一步扩展：
- **动态路由策略**：每个 token 被路由到最合适的专家
- **解决专家不足和不平衡问题**：自适应路由防止 token 坍缩到少数主导专家
- **10 亿稠密参数**：生产排序模型前所未有的规模
- **更高 ROI**：MoE 比稠密扩展提供每 FLOP 更多容量

### 动态路由策略

MoE 排序模型中的一个关键挑战是，朴素路由导致：
- **专家不足**：某些专家从未收到有意义的 token
- **专家不平衡**：大多数 token 路由到少数热门专家

RankMixer 的动态路由通过以下方式解决：
- 负载均衡约束，确保所有专家都被利用
- 根据训练动态调整的自适应路由
- 促进专家多样性的辅助损失

### 性能

| 指标 | 结果 |
|------|------|
| MFU 提升 | 4.5% → 45%（10 倍） |
| 参数扩展 | 在相似延迟下 100 倍 |
| 用户活跃天数 | +0.3% |
| 应用内使用时长 | +1.08% |
| 模型规模 | 1B 参数（Sparse-MoE） |
| 部署 | 推荐 + 广告（全流量） |

### 与先前方法对比

| 方面 | 传统排序 | RankMixer |
|------|---------|-----------|
| 架构 | 多样化手工模块 | 统一 token 混合 |
| GPU 利用率 | 4.5% MFU | 45% MFU |
| 扩展 | 受延迟限制 | 100 倍参数增加 |
| 特征交互 | 固定交叉模式 | 学习的 token 混合 |
| 服务成本 | 随模型规模增加 | 保持在相同水平 |

### 历史地位与架构演进

RankMixer 并非传统意义上的“又一个 CTR 模型”，而是**可扩展 Ranking Backbone 演进的起点**。其核心贡献在于验证了推荐排序模型可以围绕统一的 token 交互主干形成自己的 scaling 路线。在这一命题被验证后，字节跳动沿三个方向持续深化，形成了完整的工业化补强路径：[来源：rankmixer_to_oneranker.md]

1. **TokenMixer-Large（主干结构升级）**：解决“能够扩展之后，如何稳定扩展”的问题。在 RankMixer 基础上引入 mixing-and-reverting、inter-layer residuals、auxiliary loss 及 Sparse Per-token MoE，将模型规模推进至 7B 在线、15B 离线量级。
2. **MSN（容量扩张机制升级）**：解决“在严格算力预算下，如何继续扩大模型容量”的问题。摒弃标准 Sparse MoE 路线，引入基于 Product-Key Memory 的 memory-based sparse activation，将容量增长从“激活更大 expert”转化为“检索式注入个性化参数”。
3. **UG-Separation（部署与复用机制升级）**：解决“超大 dense 模型如何在线高效服务”的问题。将 RankMixer 内部深度耦合的 user-side 与 item-side 信息流显式拆分，首次使 dense interaction 模型具备“用户侧只计算一次”的 serving 复用能力。

这三项工作共同覆盖了大模型工业化最典型的三个命题：主干如何变大、容量如何继续扩展、系统如何在线承载。

### 产业定位与技术主线

在 2025—2026 年推荐系统大模型化的技术图谱中，RankMixer 位于**“大 ranking backbone 的可扩展化”**主线之首。该主线关注的核心是工业排序模型如何像语言模型一样具备随参数、数据与算力共同扩展的能力。[来源：rankmixer_to_oneranker.md]

- **判别式路线的成熟化**：与生成式 one-model 并行发展，RankMixer 及其后续工作表明，判别式大 ranking 并未终结，而是正演变为具备统一 token 接口、一体化主干、明确 scaling 目标与系统 serving 优化的 foundation model 形态。
- **外部工业对照**：阿里 SORT（通过 request-centric 组织、local attention 与工程优化改造 Transformer 本体）与美团 MTmixAtt（AutoToken 聚合 + Multi-Mix Attention）均属于同一问题域的不同技术解法。RankMixer 代表了“更适合推荐异构特征的 Transformer 变体”路线。
- **Serving 优化的一等公民地位**：RankMixer 的硬件感知设计开启了工业论文将线上部署、计算图优化与推理策略作为核心创新的先河，推动推荐系统竞争从纯训练阶段延伸至推理与复用阶段。

## 关联

- [模型 FLOPs 利用率](../concepts/model_flops_utilization_mfu.md) — RankMixer 优化的核心指标
- [推荐中的扩展定律](../concepts/scaling_laws_recsys.md) — RankMixer 使实际扩展成为可能
- [统一 Transformer 主干](../concepts/unified_transformer_backbone.md) — OneTrans 进一步扩展了这一思路
- [LONGER](./LONGER.md) — 字节跳动序列建模的互补方法
- [TokenMixer-Large](../models/tokenmixer_large.md) — RankMixer 的稳定扩展与规模升级
- [MSN](../models/msn.md) — 基于记忆检索的稀疏激活容量扩展
- [UG-Separation](../models/ug_separation.md) — 用户/物品侧解耦的在线服务优化
- [SORT](../models/sort.md) — 阿里判别式大 ranking backbone 的对照路线
- [MTmixAtt](../models/mtmixatt.md) — 美团多场景自适应 token 混合架构
- [OneRanker](../models/oneranker.md) — 生成式广告 one-model 的架构级协同
- [Hiformer](../models/hiformer.md) — 类似的硬件感知异构特征交互排序模型

## 开放问题

1. RankMixer 的 token 混合与线性注意力变体（如 Performer、Linear Transformer）相比如何？
2. Sparse-MoE 变体中的专家专业化模式是什么——专家是否学习不同的特征交互模式？
3. 1B 模型的训练稳定性与较小变体相比如何？
4. RankMixer 的方法能否扩展到特征空间差异显著的跨域推荐？
5. 在判别式 backbone 与生成式 one-model 并行发展的背景下，RankMixer 的 token 混合范式如何与 semantic token 及生成式解码器深度融合？
6. UG-Separation 提出的用户侧计算复用机制，能否反向指导 RankMixer 主干的早期结构设计以进一步降低在线延迟？[来源：rankmixer_to_oneranker.md]

## 参考文献

- Zhu, J., Fan, Z., Zhu, X., Jiang, Y., Wang, H., Han, X., Ding, H., Wang, X., Zhao, W., Gong, Z., Yang, H., Chai, Z., Chen, Z., Zheng, Y., Chen, Q., Zhang, F., Zhou, X., Xu, P., Yang, X., Wu, D., & Liu, Z. (2025). RankMixer: Scaling Up Ranking Models in Industrial Recommenders. arXiv:2507.15551.
- arXiv: https://arxiv.org/abs/2507.15551
- Leopold. (2025). 从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线. [来源：rankmixer_to_oneranker.md]

## 更新于 2026-04-09

- 在“架构演进”部分明确其作为“可扩展 Ranking Backbone 起点”的历史地位，并补充链接至后续补强工作（TokenMixer-Large、MSN、UG-Separation）。
- 新增“产业定位与技术主线”小节，梳理其在判别式大模型演进中的位置及与阿里 SORT、美团 MTmixAtt 的对照关系。
- 更新关联页面与开放问题，纳入生成式融合、推理期优化等前沿方向。
- 在相关模型中添加 Hiformer 作为类似的硬件感知排序模型参考。

---

## 更新完成：rankmixer_to_oneranker.md
**更新时间**: 2026-04-09 12:40
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 rankmixer_to_oneranker.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
