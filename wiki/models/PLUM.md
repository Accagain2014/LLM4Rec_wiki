---
title: "PLUM — Adapting Pre-trained LLMs for Industrial Generative Recommendations"
category: "models"
tags: [PLUM, semantic ID, continued pre-training, generative retrieval, YouTube, Google, industrial deployment]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md"]
related:
  - "../concepts/generative_retrieval.md"
  - "../concepts/representation_alignment.md"
  - "../models/DSI.md"
  - "../models/HiGR.md"
  - "../methods/prompt_finetuning.md"
confidence: "high"
status: "stable"
---

# PLUM — 面向工业级规模生成式推荐的预训练 LLM 适配框架

## 概述

PLUM 是 Google/YouTube 提出的一个框架，用于将**预训练大语言模型**适配到工业级规模的生成式推荐。它结合了 **Semantic ID tokenization**、面向领域数据的**持续预训练（CPT）**和**任务特定微调**，用于生成式检索。PLUM 已部署服务于 **YouTube 上数十亿用户**，证明了基于 LLM 的生成式检索能够超越经过重度优化的、带有大型嵌入表的生产模型。

## 要点

- **三阶段流水线**：Semantic ID tokenization → CPT → 任务特定微调
- **生成式检索**：模型直接生成推荐物品的 Semantic ID
- 在 YouTube 视频推荐中**超越了生产级嵌入模型**
- **部署于 YouTube 规模**（数十亿用户）
- **扩展性研究**：对模型规模、数据量和 ID 质量的系统分析

## 详情

### 架构概览

PLUM 遵循三阶段适配范式：

#### 1. Semantic ID Tokenization
- 每个物品被分配一个 **Semantic ID**——一个离散码字的元组
- Semantic ID 的学习方式使得相似物品共享码字前缀
- 使 LLM 能够**生成物品标识符**，而非从固定词汇表中选择
- 在 DSI（生成式检索）方法基础上进行了工业级规模的改进

#### 2. 持续预训练（CPT）
- 预训练 LLM 在**领域特定推荐数据**上进一步训练
- 使模型接触推荐模式、物品分布和用户行为序列
- 弥合通用语言理解与推荐特定知识之间的差距
- 关键发现：CPT 显著提升了下游推荐质量

#### 3. 任务特定微调
- 在**生成式检索目标**上微调 CPT 模型
- 输入：用户上下文（历史、查询、特征）
- 输出：推荐物品的 Semantic ID 序列
- 作为序列到序列的生成任务进行训练

### 用于推荐的生成式检索

与传统检索（嵌入 + ANN 搜索）不同，PLUM：
1. **自回归生成**目标物品的 Semantic ID
2. 不需要单独的嵌入表或 ANN 索引
3. 通过语义泛化自然处理**长尾和未见物品**
4. 为检索和排序提供**统一架构**

### 扩展性研究

PLUM 提出了系统的扩展分析：
- **模型规模**：更大的模型提升推荐质量
- **数据规模**：更多交互数据提升 CPT 效果
- **ID 质量**：更好的 Semantic ID 带来更好的生成
- **CPT 策略**：领域自适应预训练至关重要

### YouTube 部署

- 在生产环境中服务**数十亿用户**
- 替代/增强传统的双塔检索架构
- 高效处理 YouTube 海量视频目录
- 与 YouTube 现有排序和服务基础设施集成

### 与先前工作的对比

| 方面 | 传统（双塔） | PLUM |
|------|-------------|------|
| 检索 | 嵌入 + ANN | 生成式（ID 解码） |
| 物品表示 | 稠密向量 | Semantic ID 元组 |
| 长尾物品 | 泛化能力差 | 语义泛化 |
| 架构 | 检索 + 排序分离 | 统一生成 |

## 关联

- [DSI/TIGER](./DSI.md) — PLUM 构建的基础生成式检索方法
- [生成式检索](../concepts/generative_retrieval.md) — 更广泛的范式
- [HiGR](./HiGR.md) — 另一个工业级生成式框架（腾讯），具有 slate 级规划
- [表示对齐](../methods/representation_alignment.md) — Semantic ID 学习与对齐相关

## 开放问题

1. 对于不同目录，最优的 Semantic ID 长度和基数是多少？
2. PLUM 如何处理 CPT 期间未见的冷启动物品？
3. 在 YouTube 规模下，自回归生成的服务延迟影响是什么？
4. PLUM 的方法能否从视频推荐泛化到电商或社交信息流？

## 参考文献

- He, R., Heldt, L., Hong, L., Keshavan, R., Mao, S., Mehta, N., Su, Z., Tsai, A., Wang, Y., Wang, S.-C., Yi, X., Baugher, L., Cakici, B., Chi, E., Goodrow, C., Han, N., Ma, H., Rosales, R., Van Soest, A., Tandon, D., Wu, S.-L., Yang, W., & Zheng, Y. (2025). PLUM: Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations. arXiv:2510.07784.
- arXiv: https://arxiv.org/abs/2510.07784
