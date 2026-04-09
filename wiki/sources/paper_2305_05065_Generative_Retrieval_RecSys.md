---
title: "Recommender Systems with Generative Retrieval (NeurIPS 2023)"
category: "sources"
tags: [generative retrieval, semantic ID, DSI, TIGER, neural retrieval, Google, NeurIPS 2023]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md"]
related:
  - "../models/DSI.md"
  - "../concepts/generative_retrieval.md"
  - "../concepts/semantic_id.md"
  - "../models/PLUM.md"
confidence: "high"
status: "stable"
---

# 源文献摘要：推荐系统的生成式检索（NeurIPS 2023）

## 论文元数据

- **标题**：Recommender Systems with Generative Retrieval
- **作者**：Shashank Rajput、Nikhil Mehta、Anima Singh、Raghunandan H. Keshavan、Trung Vu、Lukasz Heldt、Lichan Hong、Yi Tay、Vinh Q. Tran、Jonah Samost、Maciej Kula、Ed H. Chi、Maheswaran Sathiamoorthy
- **会议**：NeurIPS 2023
- **arXiv**：2305.05065（2023 年 5 月，2023 年 11 月修订）
- **机构**：Google

## 核心贡献

1. 推荐系统中**首个基于 Semantic ID 的生成式检索模型**
2. 提出用**自回归生成**取代传统的双塔 + ANN 检索范式
3. 引入 **Semantic ID**——学习到的码字元组，捕捉物品语义
4. 证明对长尾和未见物品具有更优的泛化能力

## 方法概述

### 生成式检索范式
- 传统：嵌入查询 + 物品 → ANN 搜索 → top 候选
- 生成式：用户上下文 → Transformer → 自回归解码目标物品 Semantic ID

### Semantic ID
- 每个物品被分配一个离散码字元组：`(c₁, c₂, ..., cₖ)`
- 端到端学习以保留物品相似性
- 相似物品共享前缀码字 → 支持高效层次化解码

### 训练
- Transformer seq2seq 模型训练从用户会话生成 Semantic ID
- 联合优化 ID 质量和生成准确率
- 在目标物品 Semantic ID 上使用交叉熵损失

## 关键发现

- 生成式检索**显著超越** SOTA 检索模型
- 在**长尾和冷启动物品**上获得特别显著的增益
- Semantic ID 使能对训练中未见物品的**语义泛化**
- 建立新范式："生成即推荐"而非"先检索后排序"

## 影响

本文是整个生成式推荐范式的**奠基性工作**。它直接启发了：
- **PLUM**（Google/YouTube）：结合 CPT 的生产部署
- **HiGR**（腾讯）：层次化 slate 级规划
- **OneRec** 系列：通过生成统一检索 + 排序
- **FORGE**：改进的 Semantic ID 形成

## 关联

- [DSI/TIGER 模型](../models/DSI.md) — 本文描述的模型
- [生成式检索](../concepts/generative_retrieval.md) — 本文建立的范式
- [Semantic ID](../concepts/semantic_id.md) — 使生成成为可能的标识符方案
- [PLUM](../models/PLUM.md) — Google/YouTube 的工业级扩展

---

*源摘要由 NeurIPS 2023 论文 arXiv:2305.05065 生成。*
