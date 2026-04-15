---
title: "TIGER — Generative Retrieval for Recommender Systems"
category: "models"
tags: [TIGER, generative retrieval, semantic ID, neural retrieval, Google, NeurIPS]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md"]
related:
  - "../concepts/generative_retrieval.md"
  - "../concepts/semantic_id.md"
  - "../models/PLUM.md"
  - "../models/HiGR.md"
  - "../methods/llm_as_ranker.md"
confidence: "high"
status: "stable"
---

# TIGER — 推荐系统的生成式检索

## 概述

这项工作（通常被称为 **TIGER** 或 **Google TIGER**）引入了推荐系统中首个**基于 Semantic ID 的生成式检索模型**。发表于 **NeurIPS 2023**，它提出了从基于嵌入的检索（双塔 + ANN）到**自回归生成物品标识符**的范式转变。Transformer seq2seq 模型直接从用户会话上下文中预测 Semantic ID——学习到的代表物品的码字元组。

## 要点

- 推荐系统中**首个基于 Semantic ID 的生成式检索模型**
- **取代双塔 + ANN 流水线**，采用自回归生成
- **Semantic ID**：学习到的离散码字元组，捕捉物品语义
- 对长尾和未见物品具有**更好的泛化能力**
- 发表于 **NeurIPS 2023**

## 详情

### 动机：超越双塔检索

传统推荐检索遵循：
1. 将查询和物品嵌入共享向量空间
2. 使用近似最近邻（ANN）搜索找到 top 候选

局限性：
- 检索和排序使用分离的架构
- 对未见物品泛化能力差
- ANN 索引维护开销大
- 嵌入质量瓶颈

### 核心创新：生成式检索

模型不是从索引中检索，而是**生成物品标识符**：

```
User session → [Transformer] → Semantic ID₁, Semantic ID₂, ... → Items
```

#### Semantic ID

- 每个物品被分配一个**码字元组**：`(c₁, c₂, ..., cₖ)`
- 码字在训练期间端到端学习
- **语义结构**：相似物品共享前缀码字
- 实现高效的自回归解码：每个码字缩小候选集

#### 模型架构

- **Transformer seq2seq 模型**（编码器-解码器）
- 输入：用户交互历史作为物品序列
- 输出：Semantic ID 码字的自回归生成
- 使用交叉熵损失在目标物品 ID 上训练

### 训练过程

1. **Semantic ID 分配**：学习保留物品相似性的码字分配
2. **Seq2seq 训练**：训练 Transformer 从用户上下文生成 Semantic ID
3. **端到端优化**：联合优化 ID 质量和生成准确率

### 对未见物品的泛化

一个关键优势：Semantic ID 支持**语义泛化**：
- 模型可以为训练中从未见过的物品生成 ID
- 具有相似码字前缀的物品被视为相似
- 显著提升了**长尾和冷启动物品**的检索性能

## 实验结果

- 在多个数据集上**超越 SOTA**检索模型
- 在**长尾物品推荐**上获得特别显著的增益
- 与随机或基于内容的 ID 相比，Semantic ID 提升了泛化能力
- 可扩展到大型物品目录

## 相关研究与性能对比

TIGER 开创了基于 Semantic ID 的生成式检索范式后，后续研究主要围绕 **ID 分配策略优化**、**分词机制改进** 以及 **架构扩展** 展开。其中，在序列分词与上下文表征方向，**ActionPiece** 代表了重要的演进路径。

### ActionPiece：上下文感知的动作序列分词优化
- **核心定位**：作为 TIGER 在分词优化方向的直接后续工作，ActionPiece（ICML 2025 Spotlight）指出传统生成式推荐模型在序列分词时缺乏上下文感知能力，导致相同动作在不同交互语境下被映射为固定且孤立的 Token。
- **方法创新**：
  - **上下文共现词表构建**：将用户交互动作解构为物品元数据特征集合，借鉴 BPE 思想，依据特征在局部集合内及跨序列相邻集合中的共现频次进行迭代合并，构建动态复合 Token 词表。
  - **集合排列正则化（Set Permutation Regularization）**：针对物品特征无序性带来的线性化偏差，通过随机重排生成多条语义等价序列视图，利用一致性损失约束模型学习排列不变的鲁棒表征。
- **性能对比**：在保持与 TIGER **相同的自回归生成骨干网络**的前提下，ActionPiece 仅通过替换前端分词模块即实现了对 TIGER 的**稳定超越**。在 Amazon 公开数据集上，Recall@10 与 NDCG@10 均取得显著提升（例如 Beauty 数据集 Recall@10 提升 +2.41%，Sports 数据集提升 +2.15%），验证了高质量上下文分词对生成式推荐序列建模精度的关键作用。
- **局限性**：分词质量高度依赖物品元数据的完整性；在特征稀疏或冷启动场景下共现统计易失真；词表规模与合并阈值需针对数据集进行网格搜索调优。

[来源：[2502_paper_25021358_ActionPiece_Contextually_Tokenizing_Action_Sequences_for_Ge.md](../sources/2502_paper_25021358_ActionPiece_Contextually_Tokenizing_Action_Sequences_for_Ge.md)]

## 影响与贡献

这项工作为后续工业级生成式检索系统奠定了基础：
- **PLUM**（Google/YouTube）：通过 CPT 和生产部署进行了扩展
- **HiGR**（腾讯）：添加了层次化 slate 级规划
- **OneRec** 系列：通过生成统一检索和排序
- **ActionPiece** 等后续工作：推动了生成式推荐从“固定 ID 映射”向“上下文感知分词”的演进，验证了前端 Tokenization 对自回归骨干性能的决定性影响
- 整体推动了从"先检索后排序"到"生成即推荐"的研究范式转变

## 关联

- [生成式检索](../concepts/generative_retrieval.md) — 本文引入 RecSys 的核心概念
- [Semantic ID](../concepts/semantic_id.md) — 使生成成为可能的标识符方案
- [PLUM](./PLUM.md) — Google/YouTube 对此方法的生产级扩展
- [HiGR](./HiGR.md) — 腾讯添加层次化规划的扩展
- [ActionPiece](./ActionPiece.md) — 面向生成式推荐的上下文感知分词优化
- [DSI](../concepts/generative_retrieval.md) — IR 中原始的 DSI 范式

## 开放问题

1. 自回归生成与 ANN 搜索在检索中的理论极限是什么？
2. 如何使用 Semantic ID 处理实时物品目录更新？
3. 码字结构能否做到可解释（例如，码字 = 类目、子类目）？
4. 上下文感知分词（如 ActionPiece）能否与端到端学习的 Semantic ID 分配机制融合，以兼顾语义先验与数据驱动的表征优化？

## 参考文献

- Rajput, S., Mehta, N., Singh, A., Keshavan, R.H., Vu, T., Heldt, L., Hong, L., Tay, Y., Tran, V.Q., Samost, J., Kula, M., Chi, E.H., & Sathiamoorthy, M. (2023). Recommender Systems with Generative Retrieval. NeurIPS 2023. arXiv:2305.05065.
- arXiv: https://arxiv.org/abs/2305.05065
- Hou, Y., Ni, J., He, Z., Sachdeva, N., Kang, W.C., Chi, E.H., McAuley, J., & Cheng, D.Z. (2025). ActionPiece: Contextually Tokenizing Action Sequences for Generative Recommendation. ICML 2025 (Spotlight). arXiv:2502.13581.

---

## 更新完成：2502_paper_25021358_ActionPiece_Contextually_Tokenizing_Action_Sequences_for_Ge.md
**更新时间**: 2026-04-14 16:04
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2502_paper_25021358_ActionPiece_Contextually_Tokenizing_Action_Sequences_for_Ge.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
