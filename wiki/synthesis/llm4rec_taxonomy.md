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

本页面展示了 LLM4Rec 方法的**综合分类体系**，将多样化的方法、模型和应用组织成一个结构化框架。该分类体系不仅涵盖传统的 **LLM 角色**、**适配策略**、**任务类型**和**部署模式**，更引入了面向工业落地的**演进主线与技术趋势**维度，为浏览 Wiki 内容、追踪技术范式迁移提供了动态导航地图。

## 要点

- LLM 承担四种核心角色：**Ranker（排序器）**、**Generator（生成器）**、**Reasoner（推理器）**、**Unifier/Tokenizer（统一主干与语义标记器）**
- 适配策略：**Zero-shot（零样本）**、**Few-shot（少样本）**、**PEFT（参数高效微调）**、**Full Fine-Tuning（全量微调）**、**Inference-time Scaling（推理期扩展）**
- 任务类别：**Candidate Generation（候选生成）**、**Ranking（排序）**、**Generative One-Model（端到端生成式推荐）**、**Explanation & Dialogue（解释与对话）**
- 部署模式：**Pure LLM（纯 LLM）**、**Hybrid LLM+RecSys（混合架构）**、**Distilled/Serving-Optimized（蒸馏与服务优化）**、**Generative One-Model Pipeline（生成式单模型流水线）**
- **工业演进主线**：大 Ranking Backbone 可扩展化、长序列建模工业化、统一 Backbone 重构、Semantic Token 与生成式 One-Model
- **五大技术趋势**：判别式大模型成熟化、生成式 One-Model 加速落地、Semantic Token 系统级接口化、Serving 与推理优化一等公民化、统一化向分布与平台级演进
- 本分类体系将所有 Wiki 内容组织到一个连贯且具备工业演进视角的框架中

## 详细内容

### 维度一：LLM 角色

```
LLM Role in RecSys
├── LLM-as-Ranker
│   ├── Pointwise scoring
│   ├── Pairwise comparison
│   └── Listwise ranking (LLMRank, RankGPT)
├── LLM-as-Generator
│   ├── Explanation generation
│   ├── Review synthesis
│   ├── Item description
│   └── Synthetic data generation
├── LLM-as-Reasoner
│   ├── Intent inference
│   ├── Preference decomposition
│   ├── Cross-domain reasoning
│   └── Planning & strategy
└── LLM-as-Unifier & Tokenizer (新增)
    ├── Unified backbone modeling (OneTrans, MixFormer)
    ├── Semantic tokenization & indexing (TRM, MERGE)
    └── Multi-scenario/task token injection (MDL, MTFM)
```
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../models/RankMixer.md)]

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
│   ├── Prompt/Prefix tuning
│   └── Sparse MoE / Memory-based activation (MSN)
├── Full Fine-Tuning
│   ├── Instruction tuning (InstructRec)
│   └── Task-specific fine-tuning
└── Inference-Time & Serving Adaptation (新增)
    ├── KV Caching & Request-level batching (STCA, OneTrans)
    ├── User-side computation reuse (UG-Separation)
    └── Process reward & dynamic beam serving (GRank, PROMISE)
```
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../models/RankMixer.md)]

### 维度三：推荐任务

```
RecSys Task
├── Candidate Generation
│   ├── Retrieval (ANN, Semantic ID)
│   └── Pre-ranking
├── Ranking
│   ├── Score-based (CTR/CVR)
│   ├── Order-based (Listwise)
│   └── Set-based (diverse)
├── Generative One-Model (新增)
│   ├── End-to-end Retrieve+Rank (OneRec, GPR)
│   ├── Multi-objective & Value alignment (OneRanker, GR4AD)
│   └── Cross-scenario unified generation (OneMall, OneLoc)
├── Post-Ranking
│   ├── Re-ranking with diversity
│   └── Business rule application
├── Explanation & Dialogue
│   ├── Textual/Visual explanation
│   └── Conversational recommendation
└── Multi-Business Prediction (新增)
    └── Cross-domain generative recommendation (MBGR)
```
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../models/RankMixer.md)]

### 维度四：数据需求

```
Data Requirements
├── Interaction-only (CF-style)
│   └── User-item matrix only
├── Interaction + Content
│   ├── Item descriptions & Reviews
│   └── Multi-modal (Text + Images/Audio/Video) (LEMUR)
├── Interaction + Knowledge
│   ├── Knowledge graphs
│   └── External databases
├── Semantic & Hierarchical Tokens (新增)
│   ├── Dynamic clustering & streaming indexing (MERGE)
│   └── Geo-aware & Business-aware tokens (OneLoc, GR4AD)
└── Industrial Ad & Multi-Scenario Datasets (新增)
    ├── Tencent Advertising Challenge Datasets
    └── Cross-platform heterogeneous behavior logs
```
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../models/RankMixer.md)]

### 维度五：部署模式

```
Deployment Pattern
├── Pure LLM
│   └── LLM handles entire pipeline
├── Hybrid LLM + RecSys
│   ├── Traditional retriever + LLM ranker
│   └── LLM explanation + CF ranking
├── Discriminative Large Backbone (新增)
│   ├── Token-mixer based scalable ranker (RankMixer, SORT)
│   └── Memory-augmented sparse activation (MSN)
├── Generative One-Model Pipeline (新增)
│   ├── Unified schema & hierarchical decoder (GPR, OneRanker)
│   └── Lazy decoding & inference budget control (GR4AD)
└── Distilled & Serving-Optimized (新增)
    ├── User/Item decoupling for online reuse (UG-Separation)
    ├── Near-line reasoning + Online fast decoding (OxygenREC)
    └── Foundation-Expert paradigm (Meta)
```
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../models/RankMixer.md)]

### 维度六：工业演进主线与技术趋势（新增）

本维度从静态分类转向动态技术演进视角，刻画 2025—2026 年推荐系统大模型化的核心路径。

#### 📈 四条工业演进主线
1. **大 Ranking Backbone 的可扩展化**：关注工业排序模型如何具备随参数、数据与算力共同扩展的能力。代表工作：`RankMixer`、`TokenMixer-Large`、`SORT`、`MTmixAtt`。
2. **长序列建模的工业化**：聚焦训练成本、在线时延、系统存储与效果收益的可持续平衡。代表工作：`LONGER`、`STCA`、`LEMUR`、`LASER`、`Feed-SR`。
3. **统一 Backbone 重构**：将 sequence modeling、feature interaction、multi-scenario、multi-task 统一到更强主干中。代表工作：`OneTrans`、`MixFormer`、`MDL`、`MTFM`。
4. **Semantic Token 与生成式 One-Model**：重构 item 表示、索引方式、召回与排序接口，实现端到端流水线重组。代表工作：`TRM`、`MERGE`、`GPR`、`OneRanker`、`OneRec`、`GR4AD`、`OxygenREC`。

#### 🔮 五大技术趋势
- **趋势一：判别式大 Ranking 进入成熟期**。判别式路线未被放弃，而是向 Foundation Model 演进（统一 Token 接口、一体化主干、明确 Scaling 目标）。
- **趋势二：生成式 One-Model 加速落地**。从检索试水走向主排序、广告与电商链路，天然契合多目标优化与全局收益建模。
- **趋势三：Semantic Token 成为系统级接口**。Item 从原子 ID 演化为可组合、可生成、可索引的 Token 序列，重塑检索、排序与推理约束。
- **趋势四：Serving 与 Inference-time Scaling 成为一等公民**。训练创新必须转化为在线可控计算图；Beam 设计、Path-level Reward、动态 Serving 成为竞争焦点。
- **趋势五：统一化向分布、目标与平台级演进**。从特征统一扩展至场景/任务 Token 化，并走向“中心大模型 + 轻专家部署”的平台组织逻辑。

[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../models/RankMixer.md)]

### Wiki 内容到分类体系的映射

| Wiki 页面 | LLM 角色 | 适配策略 | 任务 | 部署模式 | 演进主线/趋势 |
|-----------|----------|----------|------|----------|----------------|
| [P5](../models/P5.md) | Ranker/Generator | Few-Shot | 多种任务 | Pure LLM | 早期探索 |
| [InstructRec](../models/InstructRec.md) | 全部角色 | Full FT | 多种任务 | Pure LLM | 早期探索 |
| [TALLRec](../models/TALLRec.md) | Ranker | LoRA | Ranking | Hybrid | 判别式扩展 |
| [LLMRank](../models/LLMRank.md) | Ranker | Zero/Few-Shot | Listwise Ranking | Hybrid | 判别式扩展 |
| [RankMixer](../models/RankMixer.md) | Unifier/Ranker | Full FT + SparseMoE | Ranking | Discriminative Large Backbone | 主线一：可扩展化 |
| [OneTrans](../models/OneTrans.md) | Unifier | Mixed Param + KV Cache | Unified Modeling | Hybrid / Serving-Optimized | 主线三：统一主干 |
| [TRM](../models/TRM.md) | Tokenizer | Semantic Tokenization | Generative Retrieval/Rank | Generative One-Model | 主线四：语义Token |
| [GPR](../models/GPR.md) | Generator/Unifier | Heterogeneous Decoder | End-to-End Ad Rec | Generative One-Model | 主线四 / 趋势二 |
| [OneRanker](../models/OneRanker.md) | Generator/Ranker | Task Token + Ranking Decoder | Multi-Obj Alignment | Generative One-Model | 主线四 / 趋势二 |
| [SORT](../models/SORT.md) | Ranker | Generative Pre-training | E-commerce Ranking | Discriminative Large Backbone | 主线一 / 趋势一 |
| [MTmixAtt](../models/MTmixAtt.md) | Unifier | AutoToken + Multi-Mix Attn | Multi-Scenario | Hybrid / Discriminative | 主线一、三 |
| [MBGR](../models/MBGR.md) | Generator | Multi-Business Prompt | Cross-Domain GenRec | Pure/Hybrid LLM | 趋势二、五 |
| [Qwen](../models/qwen_series.md) | 任意 | 任意 | 任意 | 任意 | 基础底座 |

## 关联

- [LLM4Rec 概述](../concepts/llm4rec_overview.md) 提供了高层范式
- [传统方法与 LLM 方法对比](./traditional_vs_llm.md) 比较了不同方法
- [生成式检索与推荐](../concepts/generative_retrieval.md) 详解 Semantic Token 与 One-Model 架构
- [工业部署与推理优化](../concepts/serving_optimization.md) 涵盖 KV Cache、复用与 Inference-time Scaling
- 每个方法和模型页面都映射到特定的分类类别与演进主线

## 开放问题

1. 当前研究中，哪些分类单元格（如生成式多目标对齐、跨模态统一主干）尚未充分探索？
2. 如何标准化 Semantic Token 的构建协议，使其在不同业务线间具备可迁移性？
3. 判别式大 Backbone 与生成式 One-Model 在长期演进中是融合还是分化？
4. Inference-time Scaling 与动态 Serving 策略如何与现有推荐系统 SLA 深度耦合？
5. 随着领域发展，会出现哪些新的维度（如 Agent-based RecSys、World Model for Rec）？

## 参考文献

- 本分类体系综合了所有 Wiki 页面的见解与工业界最新技术报告
- 灵感来源于 LLM4Rec 综述论文及头部大厂 2025—2026 技术路线总结
- [来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../models/RankMixer.md)]

---

## 更新于 2026-04-08

**来源**: paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md
：分类体系需要更新以包含"生成式检索"作为独立的集成模式，与 LLMasRanker、LLMasReasoner 并列。

## 更新于 2026-04-09

**来源**: 2604_paper_26040497_Tencent_Advertising_Algorithm_Challenge_2025_All-Modality_G.md
：在数据集分类中添加腾讯广告数据集类别

## 更新于 2026-04-09

**来源**: 2510_paper_25102610_OneTrans_Unified_Feature_Interaction_and_Sequence_Modeling.md
：在“工业部署架构”或“统一骨干网络”分类下补充 OneTrans 条目，强调其向 LLM 风格统一 Token 序列与推理缓存优化的靠拢趋势。

## 更新于 2026-04-09

**来源**: paper_a1f46d_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md
：在“工业部署架构”或“生成式推荐”分支下新增“多业务生成式推荐”节点，标注 MBGR 及美团实践。

## 更新于 2026-04-10

**来源**: 从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线
：引入“四条主线+五大趋势”工业演进分类框架，全面扩充维度一至五的工业模型映射，新增维度六（工业演进主线与技术趋势），更新映射表与开放问题，强化 Serving 优化、Semantic Token 接口化与生成式 One-Model 的分类地位。

---

## 更新完成：rankmixer_to_oneranker.md
**更新时间**: 2026-04-09 12:29
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 rankmixer_to_oneranker.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
