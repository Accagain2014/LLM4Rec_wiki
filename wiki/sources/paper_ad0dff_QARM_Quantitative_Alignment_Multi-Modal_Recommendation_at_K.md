---
title: "QARM — Quantitative Alignment Multi-Modal Recommendation at Kuaishou"
category: "sources"
tags: [QARM, multi-modal, quantitative alignment, Kuaishou, representation matching, industrial]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/paper_ad0dff_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md"]
related:
  - "../concepts/representation_alignment.md"
  - "../methods/multi_objective_alignment.md"
  - "../entities/kuaishou.md"
  - "../sources/paper_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation.md"
confidence: "high"
status: "stable"
---

# 源文献摘要：QARM（原始版）

## 论文元数据

- **标题**：QARM: Quantitative Alignment Multi-Modal Recommendation at Kuaishou
- **作者**：Xinchen Luo、Jiangxia Cao、Tianyu Sun、Jinkai Yu 等（20 位作者，包括 Guorui Zhou）
- **arXiv**：2411.11739（2024 年 11 月）
- **机构**：快手
- **状态**：工作进行中

## 核心贡献

1. **定量多模态框架**：为下游推荐定制可训练的多模态信息
2. 解决预训练多模态模型与 RecSys 目标之间的**表示不匹配**
3. 解决缓存表示无法被 RecSys 梯度更新的**表示不可学习**问题

## 问题陈述

工业两阶段范式：
1. 预训练多模态模型以获取通用表示
2. 下游 RecSys 将这些表示作为固定的额外输入使用

两个关键问题：
- **表示不匹配**：预训练多模态模型由 NLP/CV 任务监督，而 RecSys 由用户-物品交互监督 → 表示目标不一致
- **表示不可学习**：多模态表示被缓存为固定输入 → 无法被 RecSys 梯度更新 → 对下游训练不友好

## 方法概述

QARM 引入了一个**定量多模态框架**：
1. 为不同下游模型定制专业化的多模态表示
2. 使表示与推荐任务**端到端可训练**
3. 实现预训练和下游任务之间一致的表示目标
4. 部署于**快手**规模

## 关键发现

- 两阶段预训练然后微调范式存在根本性的表示不匹配
- 使多模态表示可训练（而非缓存）显著提升下游性能
- 定量对齐桥接了通用和任务特定表示之间的差距
- 工业部署验证了可扩展性

## 关联

- [表示对齐](../methods/representation_alignment.md) — QARM 解决的核心技术问题
- [多目标对齐](../methods/multi_objective_alignment.md) — 对齐方法
- [快手](../entities/kuaishou.md) — QARM 部署的工业平台
- [QARM V2](./paper_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation.md) — 集成 LLM 的后续版本

---

*源摘要由 arXiv 论文 2411.11739 生成。*
