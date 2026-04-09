---
title: "OneRec — Unifying Retrieve and Rank with Generative Recommendation"
category: "models"
tags: [OneRec, generative retrieval, MoE, DPO, preference alignment, Kuaishou, unified architecture]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md"]
related:
  - "../concepts/generative_retrieval.md"
  - "../models/OneRec-V2.md"
  - "../models/OneRec-Think.md"
  - "../methods/prompt_finetuning.md"
confidence: "high"
status: "stable"
---

# OneRec — 用生成式推荐器统一检索与排序

## 概述

OneRec 是**首个端到端生成式推荐模型**，将检索和排序统一为单一生成式模型，取代了传统的级联检索-然后-排序流水线。由**快手**开发，它采用编码器-解码器架构，结合**稀疏 MoE**进行扩展、**会话级生成**以及**带 DPO 的迭代偏好对齐**。部署于快手主场景，实现了 **+1.6% 的观看时长提升**。

## 要点

- **首个统一的生成式模型**，取代检索+排序级联
- **稀疏 MoE**用于扩展容量，而不按比例增加 FLOPs
- **会话级生成**而非逐点预测
- 面向 RecSys 定制的**带 DPO 的迭代偏好对齐**
- **生产级部署**：快手观看时长 +1.6%

## 详情

### 架构

#### 编码器-解码器结构
- 编码用户行为历史序列
- 自回归解码用户可能感兴趣的物品
- 使用**稀疏混合专家（MoE）**高效扩展模型容量

#### 会话级生成
- 传统方法：下一物品预测（逐点）
- OneRec：一次性生成整个**推荐会话**
- 比组合单个预测更优雅、上下文更连贯
- 避免了合并生成结果的手动规则

#### 带 DPO 的迭代偏好对齐（IPA）
- 将 NLP 中的**直接偏好优化（DPO）**适配到推荐领域
- **挑战**：RecSys 每次请求只能展示一次结果 → 无法同时获取正/负样本
- **解决方案**：
  - 奖励模型模拟用户反馈
  - 定制化的偏好对采样策略
  - 有限的 DPO 样本显著提升生成质量

### 性能

- **超越**复杂精心设计的生产级推荐系统
- 快手主推荐场景 **+1.6% 观看时长**
- 离线实验显示相比检索-排序基线有显著提升

### 与传统流水线对比

| 方面 | 传统（检索+排序） | OneRec |
|------|------------------|--------|
| 架构 | 级联（2+ 阶段） | 统一（单一模型） |
| 训练 | 每阶段独立 | 端到端 |
| 生成 | 从候选中选择 | 自回归生成 |
| 偏好 | 隐含在标签中 | 显式 DPO 对齐 |

## 关联

- [OneRec-V2](./OneRec-V2.md) — V2 带 Lazy Decoder 和 8B 扩展
- [OneRec-Think](./OneRec-Think.md) — V3 带文内推理
- [生成式检索](../concepts/generative_retrieval.md) — 底层范式
- [DSI](./DSI.md) — 基础生成式检索工作

## 开放问题

1. OneRec 如何处理训练词汇表中不存在的冷启动物品？
2. 偏好对齐的最优 DPO 样本数量是多少？
3. 会话级生成如何扩展到非常长的推荐列表？

## 参考文献

- Deng, J., Wang, S., Cai, K., Ren, L., Hu, Q., Ding, W., Luo, Q., & Zhou, G. (2025). OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment. arXiv:2502.18965.
- arXiv: https://arxiv.org/abs/2502.18965
