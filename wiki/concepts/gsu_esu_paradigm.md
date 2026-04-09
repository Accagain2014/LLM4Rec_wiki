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

The **General Search Unit (GSU) + Exact Search Unit (ESU)** paradigm is the dominant industrial architecture for large-scale recommendation systems. **GSU** performs efficient recall from massive catalogs (millions of items), while **ESU** performs precise ranking on the recalled candidates. This two-stage design balances **efficiency** and **accuracy** but faces limitations in information density, knowledge sharing, and generalization when enhanced with LLM representations.

## 要点

- **GSU（通用搜索单元）**：大规模召回，从百万级物品中筛选千级候选
- **ESU（精确搜索单元）**：精细排序，对候选物品进行精确评分
- 工业标准架构：抖音、快手、腾讯、YouTube 等均采用类似设计
- LLM 增强的核心挑战：表示不匹配与表示不可学习
- 生成式推荐正在**统一两阶段**为单一生成过程

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
| 信息密度低 | ID embedding 仅编码共现信号，无语义 |
| 知识隔离 | 每个物品独立表示，无法跨物品泛化 |
| 泛化能力弱 | 对冷启动/长尾物品效果差 |
| 表示不匹配 | LLM 语义表示与召回目标不一致 |

#### ESU 层面的问题
| 问题 | 描述 |
|------|------|
| 特征工程依赖 | 需要大量人工特征工程 |
| 表示不可学习 | 缓存的 LLM 表示无法端到端训练 |
| 多目标冲突 | CTR、时长、多样性难以联合优化 |

### 生成式推荐的范式转变

生成式推荐（Generative Retrieval）正在统一两阶段：

```
Traditional: GSU (recall) → ESU (rank) → Top-K
Generative:  User Context → [Generator] → Top-K IDs
```

- **OneRec** 系列：统一召回与排序为单一生成过程
- **PLUM**：用 LLM 生成 Semantic ID 替代 GSU + ESU
- **HiGR**：层次化规划同时处理召回和排序

### 工业部署考量

| 公司 | GSU 技术 | ESU 技术 | LLM 增强 |
|------|---------|---------|---------|
| 快手 | QARM (多模态) | 多目标 CTR | 定量对齐 |
| 腾讯 | HiGR (生成式) | 列表级优化 | 层次化规划 |
| YouTube | PLUM (Semantic ID) | 生产级排序 | CPT + 微调 |

### 未来方向

1. **统一架构**：生成式模型替代两阶段流水线
2. **端到端训练**：消除缓存表示，实现完全可学习
3. **多模态召回**：文本 + 图像 + 视频联合召回
4. **实时 GSU**：支持动态更新的索引和实时偏好

## Connections

- [QARM](../models/QARM.md) — 快手在 GSU/ESU 上的定量对齐方法
- [Representation Alignment](./representation_alignment.md) — GSU/ESU 中 LLM 表示的核心挑战
- [LLM as Ranker](../methods/llm_as_ranker.md) — ESU 的 LLM 增强
- [RAG for RecSys](../methods/rag_for_recsys.md) — GSU 可以视为检索阶段

## Open Questions

1. 生成式推荐能否在延迟约束下完全替代两阶段架构？
2. GSU 和 ESU 之间最优的信息传递是什么？
3. 如何在 GSU 阶段注入 ESU 的多目标信号？
4. 实时 GSU 索引更新的最优策略是什么？

## References

- Covington, P., Adams, J., & Sargin, E. (2016). Deep neural networks for YouTube recommendations. RecSys 2016.
- Luo, X., et al. (2024). QARM: Quantitative Alignment Multi-Modal Recommendation at Kuaishou. arXiv:2411.11739.
- Xia, T., et al. (2026). QARM V2: Quantitative Alignment Multi-Modal Recommendation. arXiv:2602.08559.
