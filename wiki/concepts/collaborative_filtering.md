---
title: "协同过滤"
category: "concepts"
tags: [CF, traditional, matrix-factorization, basics]
created: "2026-04-08"
updated: "2026-04-08"
sources: []
related:
  - "./llm4rec_overview.md"
  - "../synthesis/traditional_vs_llm.md"
  - "../concepts/sequential_recommendation.md"
confidence: "高"
status: "stable"
---

# 协同过滤 — 基础与局限性

## 摘要

协同过滤 (CF) 是传统推荐系统的基石，其核心原理是**过去有共同偏好的用户未来也会有一致的偏好**。CF 方法从用户-物品交互模式中学习，无需物品内容信息，这使得它们功能强大但本质上受限于可用的交互数据。

## 要点

- CF 依赖**用户-物品交互矩阵**而非物品内容
- **矩阵分解** (MF) 是最有影响力的 CF 方法，学习潜在的用户和物品嵌入
- **神经协同过滤** 用神经架构扩展 MF（NCF、NeuralMF）
- 核心局限性：**冷启动**、**数据稀疏性**、**语义理解有限**
- 这些局限性推动了 LLM 的集成

## 详情

### 基于记忆的协同过滤

最早的 CF 方法使用直接的相似度计算：

- **基于用户的 CF**：找到相似用户，推荐他们喜欢的物品
- **基于物品的 CF**：找到与用户喜欢的物品相似的物品（Amazon 的早期方案）
- **相似度度量**：余弦相似度、皮尔逊相关系数、Jaccard 指数

**局限性**：可扩展性问题（O(n²) 相似度计算）、对稀疏性敏感。

### 基于模型的协同过滤：矩阵分解

矩阵分解将用户-物品交互矩阵分解为 R ≈ U × Vᵀ，其中：
- U ∈ ℝ^(m×k)：用户潜在因子矩阵
- V ∈ ℝ^(n×k)：物品潜在因子矩阵
- k：潜在维度（通常为 8-128）

**优化目标**：min Σ(r_ui - u_uᵀv_i)² + λ(||u_u||² + ||v_i||²)

知名变体：
- **SVD++**：引入隐式反馈
- **Bias-SVD**：添加用户和物品偏置项
- **贝叶斯个性化排序 (BPR)**：优化成对排序而非评分预测
- **加权 MF (WMF)**：按置信度对观测条目加权

### 神经协同过滤

神经 CF 用神经网络替代点积运算：

- **NCF (Neural Collaborative Filtering)**：使用 MLP 对用户-物品交互建模
- **NeuralMF**：将 MF 与神经层结合
- **DeepFM**：将 FM 与深度神经网络结合以学习特征交互
- **YouTube DNN**：双塔架构，包含候选生成和排序

### 为什么 CF 存在不足

| 局限性 | 描述 | LLM4Rec 解决方案 |
|------------|-------------|------------------|
| **冷启动** | 新用户/物品没有交互记录 | LLM 世界知识提供先验 |
| **语义鸿沟** | ID 不携带含义 | LLM 理解文本描述 |
| **数据稀疏性** | 大多数用户-物品对未被观测 | LLM 从语言模式中泛化 |
| **跨领域** | CF 模型是领域特定的 | LLM 知识跨领域迁移 |
| **可解释性** | 潜在因子不透明 | LLM 生成自然语言解释 |

## 关联

- 对比 [LLM4Rec 概述](./llm4rec_overview.md) 了解新范式
- 参见 [传统与基于 LLM 的推荐系统对比](../synthesis/traditional_vs_llm.md) 获取详细比较
- [序列推荐](./sequential_recommendation.md) 在 CF 基础上扩展了时序动态

## 开放问题

1. CF 和 LLM 方法能否在统一架构中整合？
2. LLM  alone 能复现 CF 多少成功经验？
3. 在成熟的 CF 系统中添加 LLM 的边际价值是什么？

## 参考文献

- Koren, Y., Bell, R., & Volinsky, C. (2009). Matrix factorization techniques for recommender systems.
- He, X., et al. (2017). Neural collaborative filtering.
- Rendle, S., et al. (2009). BPR: Bayesian personalized ranking from implicit feedback.
