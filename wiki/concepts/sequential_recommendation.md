---
title: "序列推荐"
category: "concepts"
tags: [sequential, behavior, temporal, sequence-modeling]
created: "2026-04-08"
updated: "2026-04-08"
sources: []
related:
  - "./llm4rec_overview.md"
  - "../methods/llm_as_reasoner.md"
  - "../models/P5.md"
confidence: "高"
status: "stable"
---

# 序列推荐 — 对行为随时间变化的建模

## 摘要

序列推荐对**用户交互的有序序列**进行建模以预测下一个物品。与静态 CF 不同，它捕捉了**时序动态**——用户偏好如何演变、物品选择如何依赖于先前的选择，以及上下文如何随时间变化。由于其**自回归**架构和处理序列的能力，LLM 天然适合此任务。

## 要点

- 序列推荐系统将用户历史视为**有序序列**而非集合
- 传统方法：**马尔可夫链**、**RNN/GRU**、**自注意力机制**（SASRec、BERT4Rec）
- LLM 提供**原生的序列理解**和**长程依赖建模**能力
- 关键任务：**下一物品预测**、**基于会话的推荐**、**轨迹预测**
- LLM 可以推理用户**为什么**在物品间转换，而不仅仅是**什么**是他们下一个点击

## 详情

### 传统序列模型

**马尔可夫链方法：**
- FPMC (Factorized Personalized Markov Chains)：将 MF 与马尔可夫链结合
- 假设下一个行为仅依赖于最近的历史（马尔可夫性质）
- 受限于短上下文窗口

**基于 RNN 的方法：**
- GRU4Rec：使用门控循环单元进行基于会话的推荐
- 捕捉较长期的依赖关系，但难以处理非常长的序列
- 受梯度消失问题困扰

**基于注意力机制的方法：**
- **SASRec** (Self-Attentive Sequential Recommendation)：使用因果自注意力机制
- **BERT4Rec**：使用双向 Transformer 进行掩码物品预测
- **TiSASRec**：加入时间间隔感知
- 这些是最强的传统序列模型

### 为什么 LLM 在序列推荐中表现出色

1. **原生序列处理**：LLM 在文本序列上训练——用户历史自然映射到此格式
2. **长上下文窗口**：现代 LLM 可处理 32K-128K token，捕捉大量用户历史
3. **语义转换**：LLM 理解用户*为什么*可能从《盗梦空间》转向《星际穿越》（同为诺兰电影，科幻主题）
4. **多模态序列**：LLM 可以处理混合文本（评论）、物品（电影）和上下文（时间戳）的序列
5. **指令引导行为**："推荐一些与他们平时不同的东西"——LLM 可以遵循此类指令

### 序列推荐的提示词设计

```
用户历史：[电影 A] → [电影 B] → [电影 C] → [电影 D]
任务：预测用户将观看的下一部电影。
考虑：类型模式、导演偏好、主题演变、近因效应。
```

### 挑战

- **序列长度**：用户历史可能超出 LLM 上下文窗口
- **时间粒度**：时间戳需要仔细编码
- **位置编码**：标准位置嵌入可能无法捕捉真实的时间间隔
- **效率**：处理长历史在计算上代价高昂

## 关联

- [LLM-as-Reasoner](../methods/llm_as_reasoner.md) 解释了 LLM 如何推理序列中的用户意图
- [P5 模型](../models/P5.md) 通过提示词模板处理序列任务
- [协同过滤](./collaborative_filtering.md) 是非序列基线方法

## 开放问题

1. 如何最好地为 LLM 编码时间信息？
2. LLM 能否捕捉周期性行为模式（如周末与工作日的偏好差异）？
3. 压缩长用户历史以供 LLM 输入的最佳方式是什么？

## 参考文献

- Kang, W. C., & McAuley, J. (2018). Self-attentive sequential recommendation.
- Sun, F., et al. (2019). BERT4Rec: Sequential recommendation with bidirectional encoder representations.
- Hidasi, B., et al. (2016). Session-based recommendations with recurrent neural networks.


## 更新于 2026-04-08

**来源**: paper_1b102d_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md
：需要更新用户序列建模部分，添加 LLM 增强的序列建模方法，对比传统 IDbased 嵌入与 LLM 语义表示的差异。


## 更新于 2026-04-08

**来源**: paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md
：此论文明确将生成式检索应用于序列推荐任务（预测用户会话中的下一个物品语义 ID）。需添加生成式方法作为序列推荐的新范式。


## 更新于 2026-04-08

**来源**: paper_260110_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md
：添加 HSTU 作为序列推荐的最新架构进展，更新传统序列模型（RNN/Transformer）与新型转导器的对比
