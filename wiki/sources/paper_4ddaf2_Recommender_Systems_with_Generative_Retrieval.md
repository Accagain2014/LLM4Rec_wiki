---
title: "Paper 4Ddaf2 Recommender Systems With Generative Retrieval"
category: "sources"
tags: ["source", "2026-04-08"]
created: "2026-04-08"
updated: "2026-04-08"
sources: ["../../raw/sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要

这篇论文提出了**生成式检索（Generative Retrieval）**作为推荐系统的新范式，取代传统的"嵌入 + 近似最近邻搜索"架构。核心创新是为每个物品创建**语义 ID（Semantic ID）**——由有意义的词元（codewords）组成的元组，然后通过 Transformer 序列到序列模型自回归地解码目标候选物品的标识符。

这是首个基于语义 ID 的推荐任务生成模型。实验表明，该方法在多个数据集上显著超越当前 SOTA 模型，并且在处理无历史交互历史的物品（冷启动场景）时展现出更强的泛化能力。论文发表于 NeurIPS 2023，作者团队来自 Google Research。

该方法代表了推荐系统检索阶段的范式转变：从"检索嵌入空间中的近邻"转变为"直接生成物品标识符"，为 LLM4Rec 提供了新的架构选择。

### 需要更新的页面

- **wiki/concepts/semantic_id.md**：需要大幅扩展。当前页面可能仅涵盖基本概念，此论文提供了语义 ID 的正式定义、构建方法（词元元组）、以及在生成式检索中的具体应用。需添加技术细节和实验结果。

- **wiki/concepts/sequential_recommendation.md**：此论文明确将生成式检索应用于序列推荐任务（预测用户会话中的下一个物品语义 ID）。需添加生成式方法作为序列推荐的新范式。

- **wiki/methods/llm_as_generator.md**：需要添加"生成式检索"作为 LLM-as-Generator 的重要子类别。当前方法页面可能侧重于推荐文本生成，而此论文展示了物品 ID 生成。

- **wiki/synthesis/llm4rec_taxonomy.md**：分类体系需要更新以包含"生成式检索"作为独立的集成模式，与 LLM-as-Ranker、LLM-as-Reasoner 并列。

- **wiki/entities/google_youtube.md**：作者团队来自 Google Research（包括 Yi Tay、Ed H. Chi 等知名研究员）。需添加此论文作为 Google 在推荐系统领域的重要研究成果。

### 需要创建的新页面

- **wiki/models/DSI.md**：创建"DSI（Differentiable Search Index）/Generative Retrieval"模型页面。虽然论文没有明确命名模型，但这是生成式检索的代表性工作，需要独立页面记录其架构、训练方法和性能。

- **wiki/concepts/generative_retrieval.md**：创建"生成式检索"概念页面，系统阐述这一新范式与传统检索的区别、优势、挑战和适用场景。

- **wiki/sources/paper_2305_05065_Generative_Retrieval_RecSys.md**：创建此源文档的摘要页面（见下文完整内容）。

### 矛盾/冲突

- **未发现直接冲突**，但存在需要澄清的张力：
  1. 现有知识库中的"语义 ID"概念页面可能未充分说明其构建方法。此论文明确提出使用"词元元组"（tuple of codewords），需确认与其他语义 ID 实现的一致性。
  2. 生成式检索与现有"LLM-as-Ranker"范式的边界需要澄清——生成式检索是检索阶段还是排序阶段？论文表明这是检索阶段的替代方案。
  3. 需要确认此方法与 P5、InstructRec 等统一框架的区别：P5 使用固定提示模板，而生成式检索直接生成物品 ID。

### 提取的关键事实

- **论文标题**：Recommender Systems with Generative Retrieval
- **发表 venue**：NeurIPS 2023（第 37 届神经信息处理系统会议）
- **arXiv 编号**：2305.05065（v3 最终版本）
- **作者机构**：Google Research（主要作者团队）
- **核心创新**：首个基于语义 ID 的推荐任务生成模型
- **语义 ID 结构**：由有意义的词元（codewords）组成的元组
- **模型架构**：Transformer 基础的序列到序列模型
- **训练目标**：自回归解码用户下一个交互物品的语义 ID
- **性能声明**：在多个数据集上显著优于当前 SOTA 模型
- **冷启动优势**：对无历史交互历史的物品展现更好的检索性能
- **范式对比**：替代传统"嵌入 + 近似最近邻搜索"架构
- **提交历史**：v1（2023-05-08）、v2（2023-09-23）、v3（2023-11-03）

### 建议的源页面内容

```markdown
---
title: "Recommender Systems with Generative Retrieval — NeurIPS 2023"
category: "sources"
tags: ["generative-retrieval", "semantic-id", "neurips-2023", "google", "seq2seq"]
created: "2026-04-08"
updated: "2026-04-08"
sources: ["../raw/sources/paper_2305_05065_generative_retrieval.pdf"]
related:
  - "../concepts/semantic_id.md"
  - "../concepts/generative_retrieval.md"
  - "../concepts/sequential_recommendation.md"
  - "../methods/llm_as_generator.md"
  - "../entities/google_youtube.md"
confidence: "high"
status: "stable"
---

# Recommender Systems with Generative Retrieval — NeurIPS 2023

## 摘要

本文提出**生成式检索**作为推荐系统的新范式，使用语义 ID 和序列到序列模型直接生成目标物品标识符，替代传统的嵌入 + 近似最近邻搜索架构。这是首个基于语义 ID 的推荐任务生成模型，在多个数据集上显著优于 SOTA，并在冷启动场景展现更强泛化能力。

## 元数据

| 字段 | 值 |
|------|-----|
| **arXiv ID** | 2305.05065 |
| **版本** | v3（2023-11-03） |
| **会议** | NeurIPS 2023 |
| **领域** | Information Retrieval, Machine Learning |
| **机构** | Google Research |
| **PDF** | https://arxiv.org/pdf/2305.05065 |

## 作者团队

| 作者 | 机构 |
|------|------|
| Shashank Rajput | Google |
| Nikhil Mehta | Google |
| Anima Singh | Google |
| Raghunandan H. Keshavan | Google |
| Trung Vu | Google |
| Lukasz Heldt | Google |
| Lichan Hong | Google |
| Yi Tay | Google |
| Vinh Q. Tran | Google |
| Jonah Samost | Google |
| Maciej Kula | Google |
| Ed H. Chi | Google |
| Maheswaran Sathiamoorthy | Google |

## 核心贡献

1. **生成式检索范式**：提出用自回归解码替代近似最近邻搜索的检索架构
2. **语义 ID 设计**：创建由有意义词元元组组成的物品标识符
3. **序列建模**：使用 Transformer seq2seq 模型预测用户下一个交互物品的语义 ID
4. **冷启动泛化**：证明语义 ID 增强模型对无历史物品的检索能力
5. **SOTA 性能**：在多个基准数据集上超越现有最佳模型

## 方法概述

### 传统检索架构
```
Query → Embedding → ANN Search → Top Candidates
```

### 生成式检索架构
```
User Session (Semantic IDs) → Seq2Seq Model → Next Item Semantic ID
```

### 语义 ID 构建
- 每个物品分配唯一的语义 ID
- 语义 ID 由词元（codewords）元组组成
- 词元具有语义意义（非随机 ID）
- 支持层次化物品表示

### 模型训练
- **输入**：用户会话中的物品语义 ID 序列
- **输出**：下一个交互物品的语义 ID
- **架构**：Transformer 序列到序列模型
- **目标**：自回归解码最大化似然

## 关键发现

| 发现 | 说明 |
|------|------|
| **SOTA 超越** | 在多个数据集上显著优于当前最佳模型 |
| **冷启动优势** | 对无历史交互物品展现更好检索性能 |
| **泛化能力** | 语义 ID 增强模型泛化能力 |
| **架构效率** | 消除 ANN 搜索的复杂索引维护 |

## 与现有研究的关系

- **与 P5 的区别**：P5 使用固定提示模板进行多任务学习，本工作专注于检索阶段的生成式方法
- **与 DSI 的关系**：借鉴 Differentiable Search Index 思想，但专门针对推荐任务优化
- **与语义 ID 研究**：首次将语义 ID 正式应用于推荐系统检索任务

## 局限性（论文提及）

- 语义 ID 构建需要预处理的物品层次结构
- 长尾物品的语义 ID 分配策略需要进一步优化
- 大规模物品目录的解码效率需要验证

## 工业应用潜力

- Google 内部推荐系统可能采用类似架构
- 适合物品元数据丰富的场景（可构建有意义的语义 ID）
- 减少传统检索系统的索引维护成本

## 开放问题

1. 语义 ID 的最优构建策略是什么？
2. 如何扩展到亿级物品目录？
3. 如何与传统检索系统混合部署？
4. 语义 ID 能否跨领域迁移？

## 参考文献

- Rajput, S., Mehta, N., Singh, A., et al. (2023). Recommender Systems with Generative Retrieval. NeurIPS 2023.
- arXiv:2305.05065 [cs.IR]
- DOI: https://doi.org/10.48550/arXiv.2305.05065

## 相关 Wiki 页面

- [语义 ID](../concepts/semantic_id.md) — 核心概念
- [生成式检索](../concepts/generative_retrieval.md) — 范式详解
- [序列推荐](../concepts/sequential_recommendation.md) — 应用场景
- [LLM-as-Generator](../methods/llm_as_generator.md) — 方法类别
- [Google/YouTube](../entities/google_youtube.md) — 研究机构
```

---

**摄入报告**：
- **创建页面**：3 个（DSI 模型、生成式检索概念、源页面）
- **更新页面**：5 个（语义 ID、序列推荐、LLM-as-Generator、分类体系、Google 实体）
- **矛盾发现**：0 个直接冲突，3 个需要澄清的张力点
- **可信度评估**：高（NeurIPS 2023 同行评审论文，Google 研究团队）