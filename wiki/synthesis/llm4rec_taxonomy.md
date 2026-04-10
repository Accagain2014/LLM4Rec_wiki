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

本页面展示了 LLM4Rec 方法的**综合分类体系**，将多样化的方法、模型和应用组织成一个结构化框架。该分类体系不仅涵盖传统的 **LLM 角色**、**适配策略**、**任务类型**和**部署模式**，更引入了面向工业落地的**演进主线与技术趋势**维度。为夯实技术底座，本次更新新增**基础 LLM 能力层**维度，将预训练、指令对齐、高效微调与推理优化作为底层支撑模块纳入分类树，为浏览 Wiki 内容、追踪技术范式迁移提供了从底层能力到上层应用的动态导航地图。

## 要点

- **基础 LLM 能力层（新增）**：涵盖 Decoder-only 架构演进、MoE 动态路由、上下文扩展、SFT/PEFT 微调范式、RLHF/DPO 偏好对齐及量化/投机解码等推理加速技术
- LLM 承担四种核心角色：**Ranker（排序器）**、**Generator（生成器）**、**Reasoner（推理器）**、**Unifier/Tokenizer（统一主干与语义标记器）**
- 适配策略：**Zero-shot（零样本）**、**Few-shot（少样本）**、**PEFT（参数高效微调）**、**Full Fine-Tuning（全量微调）**、**Alignment-based（偏好对齐适配）**、**Inference-time Scaling（推理期扩展）**
- 任务类别：**Candidate Generation（候选生成）**、**Ranking（排序）**、**Generative One-Model（端到端生成式推荐）**、**Explanation & Dialogue（解释与对话）**
- 部署模式：**Pure LLM（纯 LLM）**、**Hybrid LLM+RecSys（混合架构）**、**Distilled/Serving-Optimized（蒸馏与服务优化）**、**Generative One-Model Pipeline（生成式单模型流水线）**
- **工业演进主线**：大 Ranking Backbone 可扩展化、长序列建模工业化、统一 Backbone 重构、Semantic Token 与生成式 One-Model
- **五大技术趋势**：判别式大模型成熟化、生成式 One-Model 加速落地、Semantic Token 系统级接口化、Serving 与推理优化一等公民化、统一化向分布与平台级演进
- 本分类体系将所有 Wiki 内容组织到一个连贯且具备工业演进视角的框架中

## 详细内容

### 维度一：基础 LLM 能力层（新增底层支撑）

本维度聚焦 LLM 在接入推荐系统前的底层技术栈，涵盖架构基座、训练范式、价值对齐与推理优化，为上层推荐适配提供可复用的能力模块。

```
Foundation LLM Capability Layer
├── 预训练与架构基座 (Pretraining & Architecture)
│   ├── Decoder-only Transformer 变体与位置编码 (RoPE, ALiBi)
│   ├── 混合专家模型 (MoE) 与动态路由机制
│   └── 上下文窗口扩展 (Attention 稀疏化, KV Cache 压缩)
├── 指令微调与监督学习 (Instruction Tuning & SFT)
│   ├── 领域指令构建与高质量数据配比
│   ├── 全参数微调 vs 参数高效微调 (LoRA, Adapter, Prefix-Tuning)
│   └── 垂直领域适配 (推荐冷启动/特征工程/多模态对齐)
├── 偏好对齐与价值优化 (Alignment & Preference Optimization)
│   ├── RLHF (PPO-based 奖励建模)
│   ├── 直接偏好优化 (DPO / IPO / ORPO)
│   └── 推荐场景对齐 (缓解信息茧房/流行度偏差/公平性约束)
└── 推理优化与部署加速 (Inference & Serving Optimization)
    ├── 模型压缩 (INT4/INT8 量化, 结构化剪枝)
    ├── 解码加速 (投机解码, 连续批处理 Continuous Batching)
    └── 显存与计算开销控制 (PEFT 降显存 60%+, 精度损失 <2%)
```
[来源：[A Comprehensive Overview of Large Language Models](../sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md)]

### 维度二：LLM 角色

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
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../sources/rankmixer_to_oneranker.md)]

### 维度三：适配策略

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
│   ├── Prompt/Prefix tuning & Adapters
│   └── Sparse MoE / Memory-based activation (MSN)
├── Full Fine-Tuning
│   ├── Instruction tuning (InstructRec)
│   └── Task-specific fine-tuning
├── Alignment-based Adaptation (新增)
│   ├── DPO/IPO for preference alignment
│   └── Reward modeling for fairness & diversity
└── Inference-Time & Serving Adaptation
    ├── KV Caching & Request-level batching (STCA, OneTrans)
    ├── User-side computation reuse (UG-Separation)
    └── Process reward & dynamic beam serving (GRank, PROMISE)
```
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../sources/rankmixer_to_oneranker.md) | [A Comprehensive Overview of Large Language Models](../sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md)]

### 维度四：推荐任务

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
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../sources/rankmixer_to_oneranker.md)]

### 维度五：数据需求

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
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../sources/rankmixer_to_oneranker.md)]

### 维度六：部署模式

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
    ├── Quantization & Speculative Decoding (INT4/8, 投机解码)
    └── Foundation-Expert paradigm (Meta)
```
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../models/RankMixer.md) | [A Comprehensive Overview of Large Language Models](../sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md)]

### 维度七：工业演进主线与技术趋势（新增）

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

| Wiki 页面 | 基础能力层 | LLM 角色 | 适配策略 | 任务 | 部署模式 | 演进主线/趋势 |
|-----------|------------|----------|----------|------|----------|----------------|
| [P5](../models/P5.md) | SFT/指令微调 | Ranker/Generator | Few-Shot | 多种任务 | Pure LLM | 早期探索 |
| [InstructRec](../models/InstructRec.md) | SFT/数据配比 | Generator/Reasoner | Full FT / Instruction Tuning | 多种任务 | Hybrid | 统一化探索 |
| [TALLRec](../models/TALLRec.md) | PEFT (LoRA) | Ranker | PEFT | Ranking | Hybrid | 判别式成熟化 |
| [RankMixer](../models/RankMixer.md) | MoE/架构基座 | Ranker/Unifier | PEFT / Inference-time | Ranking | Discriminative Backbone | 大 Backbone 可扩展化 |
| [OneRanker](../models/OneRanker.md) | 上下文扩展/对齐 | Unifier/Generator | Alignment / Full FT | Generative One-Model | Generative Pipeline | 生成式 One-Model 落地 |
| [A Comprehensive Overview of LLMs](../sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md) | **全栈底层支撑** | 通用基座 | PEFT/RLHF/DPO/量化 | 通用/多模态/Agent | 压缩/投机解码/连续批处理 | 基础能力向推荐垂直映射 |

> 💡 **维护提示**：新增的“基础 LLM 能力层”为所有上层推荐适配提供技术底座。在撰写新模型页面时，建议优先标注其依赖的预训练架构、对齐策略（如 DPO/RLHF）及推理优化手段（如 INT4 量化、KV Cache 策略），以便自动映射至本分类体系。

---

## 更新完成：2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md
**更新时间**: 2026-04-10 11:41
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
