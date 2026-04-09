---
title: "Generative Retrieval — 生成式检索"
category: "concepts"
tags: [generative retrieval, semantic ID, autoregressive, neural retrieval, DSI, TIGER, GRID, paradigm shift]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/2507_paper_25072222_Generative_Recommendation_with_Semantic_IDs_A_Practitioner'.md", "../sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md"]
related:
  - "../models/DSI.md"
  - "../models/PLUM.md"
  - "../models/HiGR.md"
  - "../concepts/semantic_id.md"
  - "../methods/llm_as_generator.md"
confidence: "high"
status: "stable"
---

# Generative Retrieval — 生成式检索

## 摘要

Generative Retrieval (GR) 是一种**范式转变**：用**自回归生成物品标识符**取代传统的"嵌入 + 近似最近邻搜索"检索流程。GR 的核心是使用 **Semantic ID（语义 ID）**——将物品映射为离散的码字元组——使模型能够直接从用户上下文生成目标物品的标识符。这一范式由 Google 在 NeurIPS 2023 首次引入推荐系统，随后在工业界（YouTube、腾讯、快手）得到广泛验证。

## 要点

- **范式转变**：从"检索然后排序"到"生成即推荐"
- **Semantic ID**：物品映射为离散码字元组，捕捉语义相似性
- **自回归生成**：Transformer seq2seq 模型逐个生成 ID codeword
- **更好的泛化**：对长尾和未见物品的推荐显著改善
- **统一架构**：OneRec 系列将召回和排序统一为单一生成过程
- **开源基准**：GRID 框架提供统一的 GR 实验平台

## 详情

### 传统检索 vs 生成式检索

```
传统检索:
User → [Encoder] → User Embedding
Items → [Encoder] → Item Embeddings
User Embedding + Item Embeddings → [ANN Search] → Top-K Items

生成式检索:
User Context → [Transformer] → Semantic ID₁, Semantic ID₂, ... → Top-K Items
```

### Semantic ID 设计

Semantic ID 是 GR 的核心创新：
- 每个物品 = `(c₁, c₂, ..., cₖ)` 其中 `cᵢ` 是离散码字
- **语义结构**：相似物品共享前缀码字
- **层次化**：前缀控制粗粒度（类目），后缀控制细粒度（具体物品）
- **可学习**：端到端训练，而非预定义

### 关键技术组件

#### 1. ID 构建方法
| 方法 | 描述 | 代表工作 |
|------|------|---------|
| RQ-VAE | 残差量化 VQ-VAE | TIGER, HiGR |
| KD-Tree | 聚类树划分 | DSI |
| 语义聚类 | K-means on embeddings | PLUM, GRID |

#### 2. 生成模型架构
- **Encoder-Decoder** (T5-style)：编码用户上下文，解码物品 ID
- **Decoder-only** (LLM-style)：自回归生成，支持更长上下文
- **层次化生成**：先生成 slate 意图，再生成具体物品（HiGR）

#### 3. 训练策略
- **监督微调**：在交互数据上训练 ID 生成
- **持续预训练**（CPT）：在领域数据上继续预训练（PLUM）
- **指令微调**：用推荐指令调优（InstructRec, TALLRec）
- **推理增强**：生成推理过程辅助推荐（OneRec-Think）

### 优势

1. **统一检索与排序**：单一模型完成两阶段任务
2. **语义泛化**：对未见物品有更好的推荐能力
3. **灵活的条件生成**：可注入多样性、公平性等约束
4. **可扩展性**：PLUM 已部署到 YouTube 十亿级用户
5. **开源工具成熟**：GRID 提供统一实验框架

### 挑战

| 挑战 | 描述 |
|------|------|
| ID 质量 | Semantic ID 的质量决定上限 |
| 训练稳定性 | 离散量化导致梯度不连续 |
| 推理延迟 | 自回归生成比 ANN 慢 |
| 冷启动 | 新物品的 ID 分配策略 |
| 动态目录 | 物品库更新时的 ID 维护 |

### GR 模型生态

| 模型 | 机构 | 核心贡献 |
|------|------|---------|
| TIGER/DSI | Google | 首次引入推荐系统 |
| PLUM | Google/YouTube | 工业生产部署 |
| HiGR | 腾讯 | 层次化 slate 规划 |
| OneRec | 快手 | 统一检索+排序 |
| OneRec-V2 | 快手 | Lazy Decoder, 8B 扩展 |
| OneRec-Think | 快手 | 推理增强 |
| GRID | Snap/CMU | 开源统一框架 |
| LEMUR | — | 大规模多模态 GR |
| FORGE | — | 改进的 Semantic ID 形成 |

### 评估基准

- **Amazon Reviews**：多类目推荐基准
- **MovieLens**：电影推荐
- **TencentGR**：腾讯广告算法大赛数据集
- **OpenOneRec**：开源 GR 评估框架

## Connections

- [DSI/TIGER](../models/DSI.md) — GR 范式的开创性工作
- [Semantic ID](./semantic_id.md) — GR 的核心标识符方案
- [PLUM](../models/PLUM.md) — Google/YouTube 的工业生产版 GR
- [HiGR](../models/HiGR.md) — 腾讯的层次化 GR
- [OneRec](../models/OneRec.md) — 统一检索与排序的 GR
- [LLM as Generator](../methods/llm_as_generator.md) — GR 的方法论基础

## Open Questions

1. GR 能否在延迟约束下完全替代 ANN 检索？
2. 最优的 Semantic ID 长度和基数是多少？
3. 如何实现 GR 模型的在线持续学习？
4. GR 如何处理实时更新的物品目录？
5. 多模态 GR 的最优融合策略是什么？

## References

- Rajput, S., et al. (2023). Recommender Systems with Generative Retrieval. NeurIPS 2023.
- Ju, C.M., et al. (2025). Generative Recommendation with Semantic IDs: A Practitioner's Handbook. arXiv:2507.22224.
- He, R., et al. (2025). PLUM: Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations. arXiv:2510.07784.
- Pang, Y., et al. (2025). HiGR: Efficient Generative Slate Recommendation. arXiv:2512.24787.


## 更新于 2026-04-09

**来源**: paper_a1f46d_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md
：在“挑战”或“工业部署”章节补充多业务场景下的 GR 瓶颈（跷跷板效应、表征混淆），并将 MBGR 列为多业务 GR 的代表性工业工作，更新 GR 模型生态表。


## 更新于 2026-04-09

**来源**: paper_a1f46d_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md
：在“挑战与前沿”部分新增多业务GR特有的“跷跷板效应”与“跨业务表征干扰”问题，并引用MBGR作为工业级解决方案。


## 更新于 2026-04-09

**来源**: paper_a1f46d_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md
：在“工业挑战与架构演进”章节新增多业务 GR 瓶颈说明，补充业务解耦预测与动态路由作为 GR 范式的重要扩展方向。
