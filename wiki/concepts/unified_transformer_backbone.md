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

统一 Transformer 主干是推荐系统中的一种核心设计范式，其中**单一 Transformer 架构**同时承担**特征交互**（建模用户、物品和上下文特征之间的关系）、**序列建模**（捕捉用户行为历史中的时间模式），并逐步扩展至**多场景分布与多任务目标**的统一建模。传统推荐架构通常将上述任务拆分为独立模块（如 Wukong/RankMixer 用于特征交互，LONGER 用于序列建模，多场景/多任务依赖浅层条件拼接），这种碎片化设计阻碍了深层双向信息交换，限制了全局优化与模型扩展能力。

以 **OneTrans** 为起点，工业界逐步验证了统一范式的可行性。随后，**MixFormer**、**MDL**、**MTFM** 等工作进一步将统一对象从“特征结构”推向“分布与目标结构”，通过协同扩展（Co-scaling）、分布级 Token 化（Domain Tokens）与免对齐骨干（Alignment-free Backbone）等机制，使单一主干能够承载更复杂的工业推荐需求。近期，**OnePiece** 进一步将统一范式延伸至**召回与精排的级联流水线**，并首次将 LLM 的上下文工程与隐式推理机制引入工业排序。最新进展中，**HyFormer** 通过交替优化机制彻底打破了传统的“序列压缩+特征融合”解耦范式，将长序列建模与异构特征交互深度耦合于单一骨干。然而，工业实践也揭示出简单统一可能引发**序列崩溃传播（SCP）**等稳定性挑战，促使 **TokenFormer** 等工作提出 BFTS 注意力调度与 NLIR 非线性交互等解耦设计模式，为统一骨干的鲁棒性扩展提供了关键路径。该范式不仅提升了模型表达能力，还通过跨请求 KV 缓存、用户-物品解耦等系统级优化，保障了在线服务的低延迟与高吞吐。

## 要点

- **统一架构**：单一 Transformer 取代分离的特征交互、序列建模及多任务模块
- **统一 Tokenization**：所有属性（序列、非序列、场景、任务）转换为通用 Token 格式
- **参数共享与协同扩展**：相似序列 Token 共享参数，非序列 Token 专用参数；MixFormer 提出序列与稠密模块的 Co-scaling 机制
- **分布级统一**：MDL 将场景与任务 Token 化，以 Prompt 式条件注入主干深层
- **级联统一与隐式推理**：OnePiece 打破召回/精排割裂，共享隐空间实现端到端优化；引入分块隐式推理模拟多步思维链
- **交替优化与深度耦合**：HyFormer 摒弃两阶段流水线，通过 Query 解码与增强机制在 Transformer 层间交替执行，实现序列与特征的逐层精炼与高效 Scaling
- **核心挑战与解耦设计**：简单统一易引发“序列崩溃传播（SCP）”；TokenFormer 提出 BFTS 注意力调度与 NLIR 非线性表征，有效解耦全局交互与局部时序
- **跨请求 KV 缓存与服务优化**：支持预计算缓存、用户侧复用与推理期扩展（Inference-time Scaling）
- **代表模型**：OneTrans、MixFormer、MDL、MTFM、OnePiece、HyFormer、TokenFormer
- **业务收益**：OneTrans 在线 A/B 测试实现每用户 GMV +5.68%；OnePiece 在 Shopee 主搜实现 GMV/UU +2%、广告收入 +2.90%；HyFormer 在十亿级数据集与线上 A/B 中验证显著 CTR/GAUC 提升；TokenFormer 在腾讯广告业务流实现 AUC/GAUC 显著提升；统一架构显著降低多场景/多任务及级联系统维护成本

## 详情

### 碎片化问题

传统推荐架构将建模分为多个独立轨道，导致系统复杂且优化割裂：

```
┌─────────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│ Feature Interaction  │    │ Sequence Modeling    │    │ Multi-Scenario/Task │
│ (Wukong, RankMixer) │    │ (LONGER, HSTU)       │    │ (Shallow Conditions)│
│                      │    │                      │    │                      │
│ User × Item features │    │ Behavior history     │    │ Scenario/Task IDs   │
│ Context features     │    │ Temporal patterns    │    │ Independent Heads   │
└─────────┬───────────┘    └─────────┬────────────┘    └─────────┬───────────┘
          │                          │                           │
          └──────────┬───────────────┴───────────────────────────┘
                     ↓
              Late Fusion / Separate Optimization
```

这种分离导致：
1. **无双向交换**：特征交互无法从序列模式中受益，序列建模缺乏静态特征的强先验
2. **容量压制**：分离模块独立扩展时，一侧的容量增长会压制另一侧的表达能力
3. **分布割裂**：多场景/多任务依赖浅层条件或独立 Head，无法调动主干深层参数潜力
4. **级联信息损耗**：召回与精排模型独立训练与部署，特征表示难以跨阶段流转，导致延迟累积与优化目标不一致
5. **冗余计算与维护成本**：相似模式重复学习，多套代码库与部署流水线增加工程负担

### 统一 Transformer 设计

统一方法将多类任务合并为单一架构，并通过结构化设计保障工业可行性：

```
Unified Tokenizer
    ↓
[User features] [Item features] [Context] [History token 1] ... [History token N] [Scenario token] [Task token]
    ↓
Stacked Transformer Blocks (Mixed Parameterization & Co-scaling)
    ↓
Unified representation for prediction / generation
```

#### 统一 Tokenization
- **全属性转换**：将序列属性（行为历史）、非序列属性（用户画像、物品元数据、上下文）以及**场景/任务标识**统一转换为通用 Token 格式
- **异构特征对齐**：类别型、连续型、文本、图像等特征通过专用 Embedding 层映射至同一语义空间
- **单一词汇表**：支持跨域、跨场景的注意力计算，消除传统多模态/多场景的接口壁垒

#### 参数共享与协同扩展 (Co-scaling)
- **混合参数化 (Mixed Parameterization)**：序列 Token 在相似位置共享变换参数以捕捉时序共性；非序列 Token 使用特定参数保留特征独特性
- **协同扩展机制 (MixFormer)**：针对序列模块与稠密交互模块分离导致的容量压制问题，通过 `Query Mixer`、`Cross Attention` 与 `Output Fusion` 将两者置于同一 Block 内交互，并引入 `user-item decoupling` 补偿在线推理效率
- **免对齐骨干 (MTFM)**：面向多场景推荐，不要求严格输入对齐，直接将异构场景数据转为 Heterogeneous Tokens，由单一 Backbone 吸收不同业务分布

#### 分布与任务级统一 (Domain & Task Tokens)
- **MDL 的分布统一**：将 Scenario 与 Task 一并 Token 化，形成可深入主干多层交互的 `Domain Tokens`。该设计借鉴 LLM 的 Prompt 思想，使场景与任务不再是浅层条件，而是参与深层计算的动态条件信息
- **多目标联合优化**：统一主干通过共享底层表征与任务特定 Head/Decoder，实现 CTR、CVR、GMV 等多目标的端到端联合训练，避免梯度冲突与表征割裂

#### 级联统一与 LLM 机制借鉴 (OnePiece)
- **召回与精排统一**：传统级联系统依赖独立召回模型与精排模型串联，导致信息损耗与延迟累积。OnePiece 采用纯 Transformer 骨干，在共享隐空间内同时处理检索与排序任务，实现端到端级联流水线优化，支持跨阶段特征与表示的无缝流转。
- **结构化上下文工程**：突破传统推荐依赖稀疏 ID 与手工特征拼接的局限，将离散行为序列、显式偏好信号与实时场景特征统一编码为连续 Token 序列。通过自注意力机制显式建模长程依赖，为冷启动与长尾商品匹配提供高信息密度的初始表征。
- **分块隐式推理 (Block-wise Latent Reasoning)**：将 Transformer 隐藏层划分为多个独立推理块，每个块执行一次局部表示精炼与全局信息聚合。通过动态调整分块大小（Block Size）灵活扩展推理带宽，使模型具备类似 LLM“思维链”的中间态推理路径，显著提升复杂意图理解与多步逻辑推演能力。
- **渐进式多任务训练**：利用真实用户反馈链（曝光-点击-加购-转化）构建分层监督信号，对推理过程中的中间步骤进行渐进式约束。该策略有效缓解多任务梯度冲突，确保模型在工业复杂场景下的稳定收敛，避免过拟合与梯度震荡。

#### 核心挑战与解耦设计模式 (TokenFormer)
随着统一架构的深入应用，工业界发现**简单拼接多字段与序列特征会引发“序列崩溃传播（Sequence Collapse Propagation, SCP）”现象**。即维度不良或噪声较大的非序列字段（如稀疏画像、长尾商品属性）在底层全量交互时，其表征坍缩会通过共享注意力机制向序列分支传导，导致序列表征维度崩溃、时序动态被结构化噪声淹没。为应对该挑战，**TokenFormer** 提出以下解耦设计模式：
- **BFTS 注意力调度 (Bottom-Full-Top-Sliding)**：打破传统单一注意力模式，采用分层调度策略。底层使用 **Full Self-Attention** 充分捕获多字段全局共现关系与高阶交互；顶层引入 **Shrinking-Window Sliding Attention**，随网络深度增加逐步收缩注意力窗口，强制模型聚焦近期行为序列的局部时序动态。该机制有效隔离非序列字段噪声，阻断 SCP 现象的传播路径，实现全局交互与局部演化的解耦协同。
- **NLIR 非线性交互表征 (Non-Linear Interaction Representation)**：在隐藏层引入单侧非线性乘法变换 $h' = h \odot \sigma(W h + b)$，突破传统线性加和交互的表达能力瓶颈。该门控式非线性缩放在不显著增加参数量的前提下，增强了特征融合的非线性边界，提升了对稀疏长尾字段的敏感度与表征空间的几何可分性，显著改善统一架构下的维度鲁棒性。
- **工业验证**：在公开基准（Criteo、Avazu）及腾讯广告真实业务流中，TokenFormer 通过 BFTS 与 NLIR 的协同，使序列特征维度崩溃率显著下降，AUC/GAUC 等核心排序指标达到 SOTA，验证了该解耦范式在工业级统一骨干中的有效性。[来源：[2604_paper_26041373_TokenFormer_Unify_the_Multi-Field_and_Sequential_Recommenda.md](../sources/2604_paper_26041373_TokenFormer_Unify_the_Multi-Field_and_Sequential_Recommenda.md)]

#### 因果注意力 + 跨请求 KV 缓存与服务优化
- **因果注意力**：严格防止未来行为 Token 的信息泄漏，保障序列建模的时序正确性
- **跨请求 KV 缓存**：预计算并缓存高频/静态特征的中间表示
  - 用户画像变化低频 → 缓存其 KV 状态，实现用户侧计算复用
  - 物品特征跨用户共享 → 全局缓存，降低重复编码开销
- **系统级协同**：结合 `UG-Separation`（用户/物品信息流显式拆分）、`Pyramid Pruning` 与推理期扩展策略，使统一主干在严格时延约束下仍具备工业部署可行性

### 统一架构的益处

| 益处 | 描述 |
|------|------|
| **双向信息交换** | 静态特征与序列模式通过共享注意力深度交互，互为增强 |
| **统一优化** | 单一目标函数联合优化特征、序列、场景与任务，逼近全局最优 |
| **协同扩展 (Co-scaling)** | 打破模块容量压制，参数与数据规模可同步扩展 |
| **分布级统一** | 场景/任务 Token 化实现 Prompt 式条件注入，充分调用大模型参数潜力 |
| **级联端到端优化** | 共享隐空间打通召回与精排，消除信息孤岛与延迟累积 |
| **交替迭代精炼** | HyFormer 验证层间交替优化可最大化信息流动效率，实现表征质量逐层跃升 |
| **解耦与鲁棒性增强** | BFTS 与 NLIR 机制有效阻断 SCP 传播，保障统一骨干在异构稀疏场景下的稳定性 |
| **KV 缓存与复用** | 预计算减少冗余计算，显著降低在线延迟与存储成本 |
| **工程简化** | 单一架构替代多模块拼接，降低训练、部署与维护复杂度 |
| **生成式兼容** | 统一 Token 接口天然适配 Semantic ID 与端到端生成式 One-Model 演进 |

### 工业验证与代表模型

| 模型 | 核心贡献 | 工业定位 |
|------|----------|----------|
| **OneTrans** (WWW 2026) | 首次彻底统一序列与非序列特征 Tokenization；混合参数化 + 跨请求 KV 缓存；每用户 GMV +5.68% | 统一范式奠基者，验证工业可行性 |
| **MixFormer** | 提出序列与稠密模块 Co-scaling；Query Mixer + Cross Attention + Output Fusion；User-Item Decoupling 保障在线效率 | 统一主干下的协同扩展与部署优化 |
| **MDL** | 将场景与任务 Token 化为 Domain Tokens；Prompt 式深层条件注入；统一多分布学习 | 从“特征统一”迈向“分布与目标统一” |
| **MTFM** | Alignment-free Backbone；直接吸收异构场景数据；免严格输入对齐的多场景 Foundation Model | 跨业务线数据统一与快速迁移 |
| **OnePiece** (arXiv 2025) | 首次统一召回与精排级联流水线；引入上下文工程与分块隐式推理；渐进式多任务训练；GMV/UU +2% | 级联统一与 LLM 机制借鉴的工业标杆 |
| **HyFormer** (arXiv 2026) | 提出交替优化机制打破“序列压缩+特征融合”范式；Query Decoding/Boosting 双组件；十亿级数据验证显著 Scaling Law 与线上 CTR/GAUC 提升 | 序列-特征深度耦合的最新 SOTA，验证统一骨干的高效扩展路径 |
| **TokenFormer** (arXiv 2026) | 揭示序列崩溃传播（SCP）现象；提出 BFTS 注意力调度与 NLIR 非线性交互；在腾讯广告业务流实现 AUC/GAUC 显著提升 | 统一骨干稳定性与解耦设计的工业级标杆 |

### 与分离架构对比

| 方面 | 分离模块架构 | 统一 Transformer 架构 |
|------|-------------|---------------------|
| **架构形态** | 多个专业模块（特征/序列/多任务独立） | 单一共享 Transformer 主干 |
| **信息流** | 单向或晚期融合，缺乏深层交互 | 共享注意力实现全向双向交换 |
| **优化目标** | 逐模块独立优化，易陷入局部最优 | 端到端联合优化，支持多目标协同 |
| **扩展能力** | 模块独立扩展，存在容量压制 | Co-scaling 与交替优化机制支持参数/数据同步扩展 |
| **场景/任务处理** | 浅层条件拼接或独立 Head | Domain Tokens 深层 Prompt 注入，动态参与计算 |
| **级联流水线** | 召回/精排割裂，特征表示跨阶段损耗 | 共享隐空间端到端流转，支持隐式推理与渐进监督 |
| **稳定性挑战** | 天然隔离，无跨模态干扰风险 | 需防范 SCP 等维度崩溃传播，依赖 BFTS/NLIR 等解耦设计 |
| **工程维护** | 多套代码库、独立部署、高运维成本 | 单一架构、统一训练/推理管线、显著降本增效 |

---

## 更新完成：2604_paper_26041373_TokenFormer_Unify_the_Multi-Field_and_Sequential_Recommenda.md
**更新时间**: 2026-04-17 10:10
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2604_paper_26041373_TokenFormer_Unify_the_Multi-Field_and_Sequential_Recommenda.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
