---
title: "DSI / TIGER — Generative Retrieval for Recommender Systems"
category: "models"
tags: [DSI, TIGER, generative retrieval, semantic ID, neural retrieval, Google, NeurIPS]
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

# DSI / TIGER — 推荐系统的生成式检索

## 概述

这项工作（通常被称为 **TIGER** 或 **DSI for Rec**）引入了推荐系统中首个**基于 Semantic ID 的生成式检索模型**。发表于 **NeurIPS 2023**，它提出了从基于嵌入的检索（双塔 + ANN）到**自回归生成物品标识符**的范式转变。Transformer seq2seq 模型直接从用户会话上下文中预测 Semantic ID——学习到的代表物品的码字元组。

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

### 实验结果

- 在多个数据集上**超越 SOTA**检索模型
- 在**长尾物品推荐**上获得特别显著的增益
- 与随机或基于内容的 ID 相比，Semantic ID 提升了泛化能力
- 可扩展到大型物品目录

### 影响与贡献

这项工作为后续工业级生成式检索系统奠定了基础：
- **PLUM**（Google/YouTube）：通过 CPT 和生产部署进行了扩展
- **HiGR**（腾讯）：添加了层次化 slate 级规划
- **OneRec** 系列：通过生成统一检索和排序
- 推动了从"先检索后排序"到"生成即推荐"的研究范式转变

## 关联

- [生成式检索](../concepts/generative_retrieval.md) — 本文引入 RecSys 的核心概念
- [Semantic ID](../concepts/semantic_id.md) — 使生成成为可能的标识符方案
- [PLUM](./PLUM.md) — Google/YouTube 对此方法的生产级扩展
- [HiGR](./HiGR.md) — 腾讯添加层次化规划的扩展
- [DSI](../concepts/generative_retrieval.md) — IR 中原始的 DSI 范式

## 开放问题

1. 自回归生成与 ANN 搜索在检索中的理论极限是什么？
2. 如何使用 Semantic ID 处理实时物品目录更新？
3. 码字结构能否做到可解释（例如，码字 = 类目、子类目）？

## 参考文献

- Rajput, S., Mehta, N., Singh, A., Keshavan, R.H., Vu, T., Heldt, L., Hong, L., Tay, Y., Tran, V.Q., Samost, J., Kula, M., Chi, E.H., & Sathiamoorthy, M. (2023). Recommender Systems with Generative Retrieval. NeurIPS 2023. arXiv:2305.05065.
- arXiv: https://arxiv.org/abs/2305.05065
