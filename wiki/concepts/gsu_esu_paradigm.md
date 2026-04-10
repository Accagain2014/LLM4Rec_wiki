---
title: "GSU/ESU Paradigm — 通用搜索单元与精确搜索单元"
category: "concepts"
tags: [GSU, ESU, two-stage retrieval, industrial architecture, recall, ranking, Kuaishou, Tencent]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/paper_1b102d_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md", "../sources/paper_ad0dff_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md"]
related:
  - "../concepts/representation_alignment.md"
  - "../methods/llm_as_ranker.md"
  - "../methods/rag_for_recsys.md"
  - "../models/QARM.md"
confidence: "high"
status: "stable"
---

# GSU/ESU Paradigm — 两阶段检索架构

## 摘要

The **General Search Unit (GSU) + Exact Search Unit (ESU)** paradigm is the dominant industrial architecture for large-scale recommendation systems. **GSU** performs efficient recall from massive catalogs (millions of items), while **ESU** performs precise ranking on the recalled candidates. This two-stage design balances **efficiency** and **accuracy** but faces limitations in information density, knowledge sharing, and generalization when enhanced with LLM representations. Recent industrial breakthroughs, such as **QARM V2**, demonstrate that quantitative alignment and end-to-end semantic reasoning can effectively bridge the gap between LLM representations and business metrics, offering a viable path to replace traditional ID-based retrieval pipelines.

## 要点

- **GSU（通用搜索单元）**：大规模召回，从百万级物品中筛选千级候选
- **ESU（精确搜索单元）**：精细排序，对候选物品进行精确评分
- 工业标准架构：抖音、快手、腾讯、YouTube 等均采用类似设计
- LLM 增强的核心挑战：表示不匹配与表示不可学习
- **架构演进**：生成式推荐与语义意图推理正在**统一两阶段**为单一可微过程
- **QARM V2 实践**：通过定量对齐机制打破 ID 检索信息瓶颈，实现端到端序列联合优化

## 详情

### 传统两阶段架构

```
                    ┌──────────────┐     ┌──────────────┐
User Context ─────→ │    GSU       │────→│    ESU       │──→ Top-K Items
                    │  (Recall)    │     │  (Ranking)   │
                    │  M items     │     │  N items     │
                    │  → ~1000     │     │  → Top-K     │
                    └──────────────┘     └──────────────┘
                   Complexity: O(M)     Complexity: O(N²)
```

#### GSU (General Search Unit) — 召回层
- **目标**：从百万/千万级物品池中快速筛选 ~1000 个候选
- **方法**：
  - 双塔模型（Two-Tower/DSSM）：用户塔 + 物品塔
  - ANN 检索（Approximate Nearest Neighbor）：FAISS、HNSW
  - 规则召回：热门、新用户偏好、多样性
- **约束**：低延迟（<10ms）、高吞吐
- **表示**：ID-based embeddings（信息密度低）

#### ESU (Exact Search Unit) — 排序层
- **目标**：对 ~1000 个候选进行精确排序
- **方法**：
  - Deep CTR 模型：DeepFM, DIN, DIEN, SIM
  - 多任务学习：MMOE, PLE
  - 特征交叉：DCN, xDeepFM
- **约束**：高精度、多目标优化
- **表示**：稠密特征 + 交叉特征

### LLM 增强 GSU/ESU

引入 LLM 后面临的挑战：

#### GSU 层面的问题
| 问题 | 描述 |
|------|------|
| 信息密度低 | ID embedding 仅编码共现信号，缺乏语义与多模态信息 |
| 知识隔离 | 每个物品独立表示，无法跨物品/跨域泛化 |
| 泛化能力弱 | 对冷启动/长尾物品效果差，依赖大量交互数据 |
| 表示不匹配 | LLM 语义表示与召回目标（如点击率）不一致 |

#### ESU 层面的问题
| 问题 | 描述 |
|------|------|
| 特征工程依赖 | 需要大量人工特征工程与交叉设计 |
| 表示不可学习 | 缓存的 LLM 表示通常冻结，无法端到端训练 |
| 多目标冲突 | CTR、时长、多样性难以联合优化，梯度易冲突 |

### 架构演进与替代方案

传统 GSU/ESU 流水线正逐步向**生成式与语义推理驱动**的统一架构演进。

#### 生成式推荐的统一趋势
```
Traditional: GSU (recall) → ESU (rank) → Top-K
Generative:  User Context → [Generator] → Top-K IDs
```
- **OneRec** 系列：统一召回与排序为单一生成过程
- **PLUM**：用 LLM 生成 Semantic ID 替代 GSU + ESU
- **HiGR**：层次化规划同时处理召回和排序

#### 工业实践案例：QARM V2 的语义意图推理架构
QARM V2 是工业界基于语义意图推理替代传统 GSU/ESU 两阶段检索的代表性实践，直击 ID 检索的信息瓶颈与 LLM 表征落地难题。

**1. 核心架构设计**
采用 `语义编码 → 定量对齐 → 序列推理` 三层统一架构，彻底替代传统 GSU/ESU 的 ID 检索范式：
- **底层（语义编码）**：接入文本、图像、行为序列等多模态特征，通过轻量级 LLM 编码器提取高密度语义表征，打破 ID 嵌入的知识壁垒。
- **中层（定量对齐）**：部署可微对齐模块，将高维语义空间投影至与推荐业务指标强相关的定量空间，解决 LLM 通用语义与业务目标（CTR/CVR）的映射失配。
- **顶层（序列推理）**：构建用户序列推理单元，基于语义意图进行动态召回与精排，实现跨物品知识共享与长尾泛化。

**2. 打破 ID 瓶颈的关键技术**
- **定量对齐损失设计**：结合对比学习与业务指标回归构建多任务联合损失，强制 LLM 表征在保持语义一致性的同时，与点击/转化等业务信号保持单调正相关。
- **端到端训练策略**：采用“语义空间预对齐 → 部分冻结 LLM 层 → 开放对齐模块与下游网络全链路微调”的两阶段范式，实现表征学习与下游任务的梯度同步反向传播。
- **序列动态推理机制**：引入注意力掩码与时间衰减机制，对用户历史交互进行语义级因果建模，显著提升长序列下的意图捕捉精度与噪声鲁棒性。

**3. 工业效果与局限性**
- **性能提升**：离线 AUC 提升 1.8%~2.5%，NDCG@10 提升 3.1%；在线 CTR 提升 1.6%，CVR 提升 2.0%，推理延迟控制在 45ms 以内。长尾物品召回与跨域迁移任务的泛化误差降低 12.4%。
- **部署挑战**：LLM 语义推理与端到端微调带来较高算力开销，需依赖模型蒸馏、KV Cache 优化或异步推理策略；在数据分布剧烈偏移时存在对齐稳定性风险，且高度依赖高质量多模态特征输入。

[来源：[2602_paper_26020855_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md](../sources/2602_paper_26020855_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md)]

### 工业部署考量

| 公司/项目 | GSU 技术 | ESU 技术 | LLM 增强与架构演进 |
|------|---------|---------|---------|
| 快手 (QARM) | QARM (多模态双塔) | 多目标 CTR | 定量对齐初步探索 |
| 快手 (QARM V2) | **语义意图推理替代** | **端到端联合精排** | 定量对齐+序列动态推理，延迟<45ms |
| 腾讯 | HiGR (生成式) | 列表级优化 | 层次化规划统一召回排序 |
| YouTube | PLUM (Semantic ID) | 生产级排序 | CPT + 微调，生成式 ID 映射 |

### 未来方向

1. **统一架构**：生成式与语义推理模型逐步替代两阶段流水线，实现召回-排序-重排的端到端一体化
2. **端到端训练**：消除缓存表示，通过定量对齐与可微路由实现完全可学习的业务适配
3. **多模态召回**：文本 + 图像 + 视频 + 行为序列的联合语义索引与实时检索
4. **实时 GSU 与动态对齐**：支持动态更新的语义索引、在线校准机制与实时偏好捕捉
5. **算力与稳定性优化**：模型蒸馏、KV Cache 压缩、动态正则化以应对对齐漂移与部署成本

## Connections

- [QARM](../models/QARM.md) — 快手在 GSU/ESU 上的定量对齐方法
- [QARM V2](../models/QARM_V2.md) — 基于语义意图推理替代两阶段检索的端到端多模态推荐框架
- [Representation Alignment](./representation_alignment.md) — GSU/ESU 中 LLM 表示的核心挑战
- [LLM as Ranker](../methods/llm_as_ranker.md) — ESU 的 LLM 增强
- [RAG for RecSys](../methods/rag_for_recsys.md) — GSU 可以视为检索阶段
- [Generative Retrieval](../methods/generative_retrieval.md) — 统一召回与排序的生成式范式

## Open Questions

1. 生成式推荐与语义推理架构能否在严格延迟约束（<20ms）下完全替代传统两阶段流水线？
2. GSU 和 ESU 之间最优的信息传递是什么？定量对齐模块能否作为通用中间层？
3. 如何在召回阶段高效注入 ESU 的多目标信号（如时长、互动、多样性）？
4. 实时语义索引更新与在线对齐校准的最优工程策略是什么？
5. 在纯 ID 主导的遗留系统中，如何低成本迁移至高密度多模态语义架构？

## References

- Covington, P., Adams, J., & Sargin, E. (2016). Deep neural networks for YouTube recommendations. RecSys 2016.
- Luo, X., et al. (2024). QARM: Quantitative Alignment Multi-Modal Recommendation at Kuaishou. arXiv:2411.11739.
- Xia, T., et al. (2026). QARM V2: Quantitative Alignment Multi-Modal Recommendation for Reasoning User Sequence Modeling. arXiv:2602.08559.

---

## 更新完成：2602_paper_26020855_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md
**更新时间**: 2026-04-10 08:23
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2602_paper_26020855_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
