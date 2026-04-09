---
title: "ByteDance — Recommendation Systems at Scale"
category: "entities"
tags: [ByteDance, TikTok, Douyin, industrial recommendation, LONGER, RankMixer, LEMUR, industrial deployment]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md"]
related:
  - "../models/LONGER.md"
  - "../models/RankMixer.md"
  - "../models/LEMUR.md"
  - "../concepts/scaling_laws_recsys.md"
confidence: "high"
status: "stable"
---

# 字节跳动 — 大规模推荐系统

## 概述

字节跳动是一家运营着多个**数亿到数十亿用户**平台的全球科技公司，包括 TikTok/抖音、今日头条等内容平台。推荐系统是所有字节跳动产品的核心，驱动内容发现、参与度和变现。进入 2025—2026 年，字节跳动的推荐技术已系统性迈入“大模型化”深水区，其演进已超越单纯的参数规模扩张，转向**主干可扩展化、长序列工业化、统一建模架构、语义 Token 与生成式 One-Model** 四条并行主线。该公司构建了覆盖 dense backbone 扩展、序列/多模态建模、统一主干、表征与索引层重构的完整工业技术链，并在判别式与生成式双轨并行的背景下，持续验证推荐扩展定律，将算法创新转化为服务于数十亿用户的显著业务指标提升。

## 要点

- **规模**：十亿用户级平台（TikTok、抖音、今日头条）
- **技术主线**：大 Ranking Backbone 扩展、长序列工业化、统一 Backbone、Semantic Token 与生成式 One-Model
- **完整技术链**：RankMixer → TokenMixer-Large/MSN/UG-Separation → STCA/LEMUR → OneTrans/MixFormer/MDL → TRM/MERGE
- **部署范围**：推荐、广告、搜索等 10+ 核心场景，覆盖召回、排序、重排全链路
- **扩展定律验证**：判别式与生成式模型均呈现可预测的性能随算力/数据扩展规律
- **工业影响**：线上 A/B 测试一致增益，Serving 优化与推理时扩展（Inference-time Scaling）成为一等公民
- **开放研究**：在 RecSys、KDD、WWW 等顶会广泛发表，推动行业技术范式演进

## 详情

### 规模与挑战

字节跳动的推荐挑战由以下维度定义：

| 维度 | 规模 |
|------|------|
| **用户** | 数亿到数十亿 |
| **物品** | 数百万视频/文章/商品 |
| **交互** | 每日数万亿交互 |
| **延迟预算** | 每请求 < 10ms |
| **QPS** | 数千到数万 |
| **场景** | 推荐、广告、搜索、多任务/多场景 |

### 技术架构与演进主线

当前工业级推荐大模型化沿四条相互耦合的主线并行推进：

1. **大 Ranking Backbone 可扩展化**：将传统 DLRM 式结构改造为 Token-based 主干，验证推荐排序模型可像语言模型一样随参数、数据与算力共同扩展。
2. **长序列建模工业化**：聚焦训练成本、在线时延、系统存储与效果收益的可持续平衡，实现超长行为序列的在线部署。
3. **统一 Backbone**：将序列建模、特征交互、多场景、多任务从碎片化模块重新统一至单一更强主干，实现更大范围的联合建模。
4. **Semantic Token 与生成式 One-Model**：重构 Item 表示、索引方式与召回/排序接口，将多阶段流水线压缩为端到端生成式架构，并引入推理时优化。

### 关键研究成果与技术链

字节跳动的研究已形成清晰的内部技术分工与演进逻辑，各模块并非孤立迭代，而是协同支撑工业落地：

#### 🔹 主干扩展线：RankMixer 及其演进
- **RankMixer**：首次系统地将工业 Ranking Backbone 改造为可扩展对象。以 Token Mixing 替代传统 Attention 的相似度建模，结合 Per-token FFN 与 SparseMoE，同步提升表达能力、并行性与硬件利用率。验证了推荐模型可围绕统一 Token 交互主干形成 Scaling 路线。
- **TokenMixer-Large**：解决“稳定扩展”问题。引入 mixing-and-reverting、层间残差、辅助损失与 Sparse Per-token MoE，将模型规模推进至 **7B 在线 / 15B 离线** 量级，代表主干本体的结构升级。
- **MSN**：解决“严格算力预算下的容量扩张”。摒弃标准 Sparse MoE，采用基于 Product-Key Memory 的检索式稀疏激活，将个性化记忆注入下游交互模块，实现低成本容量增长。
- **UG-Separation**：解决“超大 Dense 模型在线服务效率”。显式拆分 User-side 与 Item-side 信息流，首次使 Dense Interaction 模型具备“用户侧只计算一次”的 Serving 复用能力。

#### 🔹 序列与多模态支柱：STCA / LEMUR / LONGER
- **LONGER**：面向超长用户行为序列。通过 Token 合并、全局 Token、混合注意力与 GPU 优化，在广告与电商场景实现一致的离线/在线增益。
- **STCA**：聚焦超长序列的目标感知建模。将历史内部 Self-Attention 改写为 Stacked Target-to-History Cross Attention，结合 Request-level Batching 显式引入在线复用机制，以更低复杂度提升序列建模上限。
- **LEMUR**：端到端多模态推荐。将多模态表示学习与 Ranking Objective 直接闭环，通过 Memory Bank 控制长历史重复编码成本，使多模态从“外部特征工程”升级为“主排序系统内生组件”。

#### 🔹 统一建模线：OneTrans / MixFormer / MDL
- **OneTrans**：首次彻底统一 Sequential 与 Non-sequential 特征的 Tokenization，以单一 Transformer 主干同时承担序列建模与特征交互。针对异构 Token 设计 Mixed Parameterization，结合 Pyramid Pruning 与 Cross-request KV Caching 保障工业部署可行性。
- **MixFormer**：解决 Sequence Module 与 Dense Module 的 Co-scaling 矛盾。通过 Query Mixer、Cross Attention 与 Output Fusion 将两者置于同一 Block，辅以 User-Item Decoupling 补偿在线效率，推动统一主干下的协同扩展。
- **MDL**：将统一对象从“特征结构”扩展至“分布结构”。将 Scenario 与 Task 一并 Token 化为 Domain Tokens，使其深入主干多层交互。本质是将 LLM Prompt 思想迁移至多场景/多任务推荐，回答“大 Backbone 如何真正调动多分布参数潜力”。

#### 🔹 表征与索引重构线：TRM / MERGE
- **TRM (Farewell to Item IDs)**：指出 Item ID 在模型持续扩张时成为 Scaling 瓶颈。重新设计兼顾语义相似性、行为相关性与细粒度记忆的 Tokenization 体系，使 Ranker 主干直接基于 Semantic Tokens 工作，将 Tokenization 从检索侧问题升级为 Ranking Model 的输入语言问题。
- **MERGE**：面向流式推荐的动态索引层。放弃静态 VQ Codebook，使 Cluster 随流式数据动态生成、重置与合并，形成层次化动态索引，与 TRM 共同完成 Item 表示与索引组织方式的系统性重写。

#### 📊 技术链分工与演进逻辑图
```
[主干扩展] RankMixer → TokenMixer-Large / MSN / UG-Separation
      ↓ (提供统一 Token 交互基座)
[统一建模] OneTrans → MixFormer → MDL (特征/场景/任务全面统一)
      ↕ (协同输入与序列侧)
[序列/多模态] LONGER / STCA (长序列) + LEMUR (多模态端到端)
      ↓ (重构底层表示与索引)
[表征/索引] TRM (Semantic Token 替代 ID) + MERGE (动态层次索引)
      ↓ (支撑上层架构)
[生成式 One-Model] 检索-排序-重排流水线端到端化 / 推理时扩展优化
```

### 技术哲学

字节跳动的推荐研究遵循以下演进原则：

1. **工业优先与双轨并行**：研究必须转化为生产部署；判别式大 Ranking 与生成式 One-Model 并非替代关系，而是根据场景实时性、吞吐与多目标约束协同演进。
2. **硬件与 Serving 感知**：为 GPU 执行与在线推理预算优化设计，Serving 复用、KV Cache、推理时扩展（Inference-time Scaling）已成为一等公民创新。
3. **面向扩展与统一化**：验证改进随计算/数据可预测扩展；统一对象从特征交互逐步延伸至序列、场景、任务乃至数据分布本身。
4. **系统级接口重构**：Semantic Token 不再仅是冷启动技巧，而是推荐系统新的基础接口；Item 表示、索引、召回与排序边界被系统性重写。
5. **开放研究**：广泛发表完整技术链，为更广泛的工业与学术社区提供可复现的 Scaling 范式。

### 基础设施

字节跳动的推荐基础设施支撑上述技术链的落地：
- **GPU 稠密训练与稀疏调度**：支持 7B~15B 级模型的大规模训练与 SparseMoE/Memory 高效调度
- **实时 Serving 架构**：海量 QPS 下的低延迟推理，支持 User-side 复用、Cross-request KV Caching 与动态 Beam 解码
- **A/B 测试与在线评估平台**：对算法变更进行严格的离线/在线一致性验证
- **特征与 Token 仓库**：跨模型、跨场景的共享特征计算与 Semantic Token 动态管理
- **流式索引系统**：支持 MERGE 等动态层次化索引的实时更新与合并

### 与其他工业实验室对比

| 公司 | 关键贡献 | 技术侧重 | 规模 |
|------|---------|----------|------|
| **字节跳动** | RankMixer、OneTrans、MixFormer、TRM、LEMUR | 完整技术链、Token 化主干、统一建模、生成式/判别式双轨 | 十亿用户 |
| **Meta** | HSTU、ULTRA-HSTU、Foundation-Expert Paradigm | 中心 Foundation Model + Surface-specific Experts 迁移 | 十亿用户 |
| **阿里** | SORT | Request-centric 组织、Local Attention、判别式 Transformer 改造 | 十亿级电商 |
| **美团** | MTFM、MTmixAtt、MTGR | 无对齐 Heterogeneous Token 统一、AutoToken 分组、生成/判别并行 | 多场景本地生活/电商 |
| **腾讯** | GPR、OneRanker | 广告生成式 One-Model、Task/Fake Item Token、架构级 Generation-Ranking 协同 | 十亿级社交/广告 |
| **快手** | OneRec、GR4AD、OneMall | 平台级生成式推荐体系、LazyAR 解码、多场景/广告统一 | 数亿用户 |
| **Google/YouTube** | PLUM、DLRM 变体 | 大规模判别式排序、多目标优化 | 十亿用户 |

### 行业核心趋势

基于字节跳动及头部大厂的实践，推荐系统大模型化呈现五大明确趋势：
1. **判别式大 Ranking 进入成熟期**：并未被生成式取代，而是向更统一的 Token 接口、更深一体化主干、更明确 Scaling 目标演进。
2. **生成式 One-Model 加速落地**：从检索试水进入主排序、广告与电商链路，天然契合多目标优化、页面级生成与全局收益建模。
3. **Semantic Token 成为系统级接口**：Item 从原子 ID 演化为可组合、可迁移、可生成的 Token 序列，重构检索、排序与推理范式。
4. **Serving 与推理时优化成为一等公民**：训练创新必须转化为在线可控计算图；Beam 设计、Path-level Reward、动态 Serving 成为竞争焦点。
5. **统一化走向分布与目标级**：从统一特征扩展至统一场景分布、多任务目标与平台级分发入口。

## 关联

- [LONGER](../models/LONGER.md) — 字节跳动的长序列建模系统
- [RankMixer](../models/RankMixer.md) — 字节跳动的硬件感知排序模型
- [LEMUR](../models/LEMUR.md) — 字节跳动的多模态推荐系统
- [TokenMixer-Large](../models/TokenMixer-Large.md) — RankMixer 的稳定扩展版本（7B/15B）
- [MSN](../models/MSN.md) — 基于 Product-Key Memory 的容量扩展机制
- [UG-Separation](../models/UG-Separation.md) — 用户/物品侧解耦的 Serving 优化架构
- [STCA](../models/STCA.md) — 目标感知长序列交叉注意力建模
- [OneTrans](../models/OneTrans.md) — 序列与非序列特征统一 Transformer 主干
- [MixFormer](../models/MixFormer.md) — 序列与 Dense 模块协同扩展架构
- [MDL](../models/MDL.md) — 多场景/多任务 Domain Token 统一建模
- [TRM](../models/TRM.md) — 基于 Semantic Token 的 Item 表示重构
- [MERGE](../models/MERGE.md) — 流式推荐动态层次化索引
- [扩展定律](../concepts/scaling_laws_recsys.md) — 在字节跳动规模下验证
- [生成式推荐](../concepts/generative_recommendation.md) — One-Model 与 Semantic Token 范式
- [Meta](./meta.md) — 另一个工业级规模推荐实验室

## 开放问题

1. 字节跳动的推荐方法在国内（抖音）和国际（TikTok）产品之间，因数据分布、合规与商业化策略差异，技术栈如何差异化适配？
2. 生成式 One-Model 与判别式大 Ranking 在字节跳动未来路线图中将如何动态分配算力与场景边界？
3. Semantic Token 体系如何建立跨业务、跨模态的标准化接口，以支撑平台级多场景统一？
4. 推理时扩展（Inference-time Scaling）与动态 Beam/Path Reward 在严格 <10ms 延迟预算下的工程极限与优化路径是什么？
5. 基于 LLM 的推荐在字节跳动生产系统中从近线推理（Near-line Reasoning）到在线实时生成的部署时间线与成本收益模型如何演进？

## 参考文献

- Chai, Z., et al. (2025). LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders. RecSys 2025. arXiv:2505.04421.
- Zhu, J., et al. (2025). RankMixer: Scaling Up Ranking Models in Industrial Recommenders. arXiv:2507.15551.
- "Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling." arXiv:2511.06077.
- "LEMUR: Large-scale End-to-end Multimodal Recommendation." arXiv:2511.10966.
- Leopold. (2025). 从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线. [来源：rankmixer_to_oneranker.md]
- 字节跳动推荐团队内部技术报告与公开论文合集 (2024-2026). [来源：rankmixer_to_oneranker.md]

---
*[注：本页面已根据最新工业技术路线文档进行实质性扩充，重点补充了字节跳动完整技术链的上下文关系、四大演进主线、Serving/推理优化趋势及行业对比视角。]*

---

## 更新完成：rankmixer_to_oneranker.md
**更新时间**: 2026-04-09 12:35
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 rankmixer_to_oneranker.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
