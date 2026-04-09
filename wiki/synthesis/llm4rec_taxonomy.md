---
title: "LLM4Rec 分类体系"
category: "synthesis"
tags: [taxonomy, survey, classification, framework]
created: "2026-04-08"
updated: "2026-04-08"
sources: []
related:
  - "../concepts/llm4rec_overview.md"
  - "../synthesis/traditional_vs_llm.md"
confidence: "high"
status: "stable"
---

# LLM4Rec 分类体系 — 综合分类框架

## 摘要

本页面展示了 LLM4Rec 方法的**综合分类体系**，将多样化的方法、模型和应用组织成一个结构化框架。该分类体系涵盖了 **LLM 的角色**、**适配策略**、**任务类型**和**部署模式**，为浏览 Wiki 内容提供了导航地图。

## 要点

- LLM 承担三种角色：**Ranker（排序器）**、**Generator（生成器）**、**Reasoner（推理器）**
- 适配策略：**Zero-shot（零样本）**、**Few-shot（少样本）**、**Fine-tuned（微调）**、**PEFT（参数高效微调）**
- 任务类别：**Candidate Generation（候选生成）**、**Ranking（排序）**、**Explanation（解释）**、**Dialogue（对话）**
- 部署模式：**Pure LLM（纯 LLM）**、**Hybrid LLM+RecSys（混合 LLM+推荐系统）**、**Distilled LLM（蒸馏 LLM）**
- 本分类体系将所有 Wiki 内容组织到一个连贯的框架中

## 详细内容

### 维度一：LLM 角色

```
LLM Role in RecSys
├── LLM-as-Ranker
│   ├── Pointwise scoring
│   ├── Pairwise comparison
│   └── Listwise ranking (LLMRank)
├── LLM-as-Generator
│   ├── Explanation generation
│   ├── Review synthesis
│   ├── Item description
│   └── Synthetic data generation
└── LLM-as-Reasoner
    ├── Intent inference
    ├── Preference decomposition
    ├── Cross-domain reasoning
    └── Planning & strategy
```

### 维度二：适配策略

```
Adaptation Strategy
├── Zero-Shot
│   ├── Direct prompting
│   └── In-context learning
├── Few-Shot
│   ├── Demonstration examples
│   └── Chain-of-thought examples
├── Parameter-Efficient Fine-Tuning
│   ├── LoRA (TALLRec)
│   ├── Prompt tuning
│   └── Prefix tuning
└── Full Fine-Tuning
    ├── Instruction tuning (InstructRec)
    └── Task-specific fine-tuning
```

### 维度三：推荐任务

```
RecSys Task
├── Candidate Generation
│   ├── Retrieval
│   └── Pre-ranking
├── Ranking
│   ├── Score-based
│   ├── Order-based
│   └── Set-based (diverse)
├── Post-Ranking
│   ├── Re-ranking with diversity
│   └── Business rule application
├── Explanation
│   ├── Textual explanation
│   └── Visual explanation
└── Dialogue
    ├── Conversational recommendation
    └── Preference elicitation
```

### 维度四：数据需求

```
Data Requirements
├── Interaction-only (CF-style)
│   └── User-item matrix only
├── Interaction + Content
│   ├── Item descriptions
│   └── Review text
├── Interaction + Knowledge
│   ├── Knowledge graphs
│   └── External databases
└── Multi-Modal
    ├── Text + Images
    └── Text + Audio + Video
```

### 维度五：部署模式

```
Deployment Pattern
├── Pure LLM
│   └── LLM handles entire pipeline
├── Hybrid LLM + RecSys
│   ├── Traditional retriever + LLM ranker
│   └── LLM explanation + CF ranking
└── Distilled LLM
    └── Train small model on LLM outputs
```

### Wiki 内容到分类体系的映射

| Wiki 页面 | LLM 角色 | 适配策略 | 任务 | 模式 |
|-----------|----------|----------|------|------|
| [P5](../models/P5.md) | Ranker/Generator | Few-Shot | 多种任务 | Pure LLM |
| [InstructRec](../models/InstructRec.md) | 全部角色 | Full FT | 多种任务 | Pure LLM |
| [TALLRec](../models/TALLRec.md) | Ranker | LoRA | Ranking | Hybrid |
| [LLMRank](../models/LLMRank.md) | Ranker | Zero/Few-Shot | Listwise Ranking | Hybrid |
| [Qwen](../models/qwen_series.md) | 任意 | 任意 | 任意 | 任意 |

## 关联

- [LLM4Rec 概述](../concepts/llm4rec_overview.md) 提供了高层范式
- [传统方法与 LLM 方法对比](./traditional_vs_llm.md) 比较了不同方法
- 每个方法和模型页面都映射到特定的分类类别

## 开放问题

1. 当前研究中，哪些分类单元格尚未充分探索？
2. 如何分类跨越多个单元格的混合方法？
3. 随着领域发展，会出现哪些新的维度？

## 参考文献

- 本分类体系综合了所有 Wiki 页面的见解
- 灵感来源于 LLM4Rec 综述论文


## 更新于 2026-04-08

**来源**: paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md
：分类体系需要更新以包含"生成式检索"作为独立的集成模式，与 LLMasRanker、LLMasReasoner 并列。


## 更新于 2026-04-09

**来源**: 2604_paper_26040497_Tencent_Advertising_Algorithm_Challenge_2025_All-Modality_G.md
：在数据集分类中添加腾讯广告数据集类别
