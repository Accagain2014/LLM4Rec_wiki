---
title: "QARM V2 — Quantitative Alignment Multi-Modal Recommendation"
category: "sources"
tags: [QARM V2, multi-modal, quantitative alignment, GSU/ESU, LLM embedding, user sequence, industrial]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/paper_1b102d_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md"]
related:
  - "../concepts/gsu_esu_paradigm.md"
  - "../concepts/representation_alignment.md"
  - "../methods/multi_objective_alignment.md"
confidence: "high"
status: "stable"
---

# 源文献摘要：QARM V2

## 论文元数据

- **标题**：QARM V2: Quantitative Alignment Multi-Modal Recommendation for Reasoning User Sequence Modeling
- **作者**：Tian Xia、Jiaqi Zhang、Yueyang Liu、Hongjian Dou 等（28 位作者）
- **arXiv**：2602.08559（2026 年 2 月）
- **状态**：工作进行中

## 核心贡献

1. **统一框架**：桥接 LLM 语义理解与 RecSys 业务需求
2. **定量对齐**方法：使 LLM 表示与推荐目标匹配
3. 解决 **GSU/ESU 范式**的局限：信息密度低、知识隔离、泛化能力弱

## 问题陈述

传统 RecSys 在通用搜索单元（GSU）和精确搜索单元（ESU）范式中使用基于 ID 的嵌入进行用户序列建模，存在以下问题：
- **信息密度低**：ID 嵌入携带的语义信息有限
- **知识隔离**：每个 ID 独立，无跨物品知识共享
- **泛化能力弱**：在未见或冷启动物品上表现差

虽然 LLM 提供稠密语义表示和强大的泛化能力，但直接应用面临：
- **表示不匹配**：LLM 嵌入与 RecSys 业务目标不一致
- **表示不可学习**：难以与下游任务进行端到端训练

## 方法概述

QARM V2 提出了一个统一框架：
1. 利用 LLM 语义理解进行用户序列建模
2. 定量对齐 LLM 表示与推荐业务目标
3. 支持多模态输入（文本、图像等）以获得更丰富的物品理解
4. 使能具备推理能力的用户序列建模

## 关键发现

- LLM 语义嵌入可以补充传统的基于 ID 的方法
- 定量对齐对于桥接表示差距至关重要
- 多模态信号在正确对齐时提升推荐质量
- 框架设计用于工业级规模部署

## 关联

- 关联到 [GSU/ESU 范式](../concepts/gsu_esu_paradigm.md) — QARM V2 改进的工业架构
- 连接到 [表示对齐](../concepts/representation_alignment.md) — 核心技术挑战
- 关联到 [多目标对齐](../methods/multi_objective_alignment.md) — 对齐方法

---

*源摘要由 arXiv 论文 2602.08559 生成。*
