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

本页面展示了 LLM4Rec 方法的**综合分类体系**，将多样化的方法、模型和应用组织成一个结构化框架。该分类体系不仅涵盖传统的 **LLM 角色**、**适配策略**、**任务类型**和**部署模式**，更引入了面向工业落地的**演进主线与技术趋势**维度。为夯实技术底座，本次更新新增**基础 LLM 能力层**维度，将预训练、指令对齐、高效微调与推理优化作为底层支撑模块纳入分类树。同时，**全面整合 2025 年生成式推荐综述提出的“数据-模型-任务”三分基准框架**，在数据层引入 Agent 仿真与知识增强分支，在模型层纳入扩散生成架构与推荐专属对齐损失，在任务层强化动态意图捕捉与创造性生成。本体系为浏览 Wiki 内容、追踪技术范式迁移提供了从底层能力到上层应用的动态导航地图。

## 要点

- **基础 LLM 能力层**：涵盖 Decoder-only 架构演进、MoE 动态路由、上下文扩展、SFT/PEFT 微调范式、RLHF/DPO 偏好对齐及量化/投机解码等推理加速技术
- **生成式推荐三分基准框架（新增）**：以 `Data-Model-Task` 为核心分类基准，解构生成式推荐为数据增强统一、模型对齐训练、任务构建执行三大可操作阶段
- LLM 承担五种核心角色：**Ranker（排序器）**、**Generator（生成器）**、**Reasoner（推理器）**、**Unifier/Tokenizer（统一主干与语义标记器）**、**Agent/Assistant（智能交互助手）**
- 适配策略：**Zero-shot**、**Few-shot**、**PEFT**、**Full Fine-Tuning**、**Alignment-based**、**Diffusion-based Generation（扩散生成适配）**、**Inference-time Scaling**
- 任务类别：**Candidate Generation**、**Ranking**、**Generative One-Model**、**Explanation & Dialogue**、**Creative & Multi-turn Generation**
- 部署模式：**Pure LLM**、**Hybrid LLM+RecSys**、**Discriminative Large Backbone**、**Generative One-Model Pipeline**、**Distilled & Serving-Optimized**
- **数据需求演进**：从交互矩阵扩展至 Agent 仿真轨迹、知识图谱增强、多模态异构信号语义对齐
- **性能与权衡**：冷启动/复杂意图场景 NDCG@10/Recall@20 提升 15%~30%，对话/解释任务 CSAT 提升 20%~40%；但推理延迟增加 2~5 倍，长尾生成幻觉率约 5%~12%
- 本分类体系将所有 Wiki 内容组织到一个连贯且具备工业演进视角的框架中

## 详细内容

### 维度一：基础 LLM 能力层（底层支撑）

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
│   ├── 推荐场景对齐 (缓解信息茧房/流行度偏差/公平性约束)
│   └── 缩放定律应用 (Scaling Laws for RecSys) [新增]
└── 推理优化与部署加速 (Inference & Serving Optimization)
    ├── 模型压缩 (INT4/INT8 量化, 结构化剪枝)
    ├── 解码加速 (投机解码, 连续批处理 Continuous Batching)
    └── 显存与计算开销控制 (PEFT 降显存 60%+, 精度损失 <2%)
```
[来源：[A Comprehensive Overview of Large Language Models](../sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md)] | [来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)]

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
├── LLM-as-Unifier & Tokenizer
│   ├── Unified backbone modeling (OneTrans, MixFormer)
│   ├── Semantic tokenization & indexing (TRM, MERGE)
│   └── Multi-scenario/task token injection (MDL, MTFM)
└── LLM-as-Agent/Assistant (新增)
    ├── Multi-turn conversational recommendation
    ├── Dynamic intent tracking & feedback loop
    └── Autonomous tool-use & external API orchestration
```
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../sources/rankmixer_to_oneranker.md)] | [来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)]

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
├── Alignment-based Adaptation
│   ├── DPO/IPO for preference alignment
│   ├── Reward modeling for fairness & diversity
│   └── Recommendation-specific losses (对比生成损失/排序一致性约束) [新增]
├── Diffusion-based Generation (新增)
│   ├── Latent diffusion for item representation
│   └── Conditional generation with user history
└── Inference-Time & Serving Adaptation
    ├── KV Caching & Request-level batching (STCA, OneTrans)
    ├── User-side computation reuse (UG-Separation)
    └── Process reward & dynamic beam serving (GRank, PROMISE)
```
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../sources/rankmixer_to_oneranker.md)] | [来源：[A Comprehensive Overview of Large Language Models](../sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md)] | [来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)]

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
├── Generative One-Model
│   ├── End-to-end Retrieve+Rank (OneRec, GPR)
│   ├── Multi-objective & Value alignment (OneRanker, GR4AD)
│   └── Cross-scenario unified generation (OneMall, OneLoc)
├── Post-Ranking
│   ├── Re-ranking with diversity
│   └── Business rule application
├── Explanation & Dialogue
│   ├── Textual/Visual explanation
│   ├── Conversational recommendation
│   └── CoT-based reasoning & dynamic intent capture [新增]
└── Creative & Multi-turn Generation (新增)
    ├── Personalized content creation (文案/海报/短视频脚本)
    ├── Open-domain recommendation with world knowledge
    └── Interactive feedback-driven refinement
```
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../sources/rankmixer_to_oneranker.md)] | [来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)]

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
├── Semantic & Hierarchical Tokens
│   ├── Dynamic clustering & streaming indexing (MERGE)
│   └── Geo-aware & Business-aware tokens (OneLoc, GR4AD)
├── Agent-Simulated & Feedback Data (新增)
│   ├── Agent-driven user behavior trajectory simulation
│   ├── Closed-loop feedback generation & preference evolution
│   └── Cold-start & OOD scenario augmentation
└── Knowledge-Enhanced & Heterogeneous Alignment (新增)
    ├── External knowledge injection & commonsense grounding
    ├── Semantic alignment of clicks, views, reviews & logs
    └── Cross-platform heterogeneous behavior unification
```
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../sources/rankmixer_to_oneranker.md)] | [来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)]

### 维度六：部署模式

```
Deployment Pattern
├── Pure LLM
│   └── LLM handles entire pipeline
├── Hybrid LLM + RecSys
│   ├── Traditional retriever + LLM ranker
│   └── LLM explanation + CF ranking
├── Discriminative Large Backbone
│   ├── Token-mixer based scalable ranker (RankMixer, SORT)
│   └── Memory-augmented sparse activation (MSN)
├── Generative One-Model Pipeline
│   ├── Unified schema & hierarchical decoder (GPR, OneRanker)
│   └── Lazy decoding & inference budget control (GR4AD)
├── Distilled & Serving-Optimized
│   ├── User/Item decoupling for online reuse (UG-Separation)
│   ├── Near-line reasoning + Online fast decoding (OxygenREC)
│   └── Quantization & Speculative Decoding (INT4/8, 投机解码)
└── Latency & Hallucination Mitigation (新增)
    ├── KV Cache reuse & request-level batching for 2~5x latency reduction
    ├── Fact-checking modules & constrained decoding (幻觉率压至 <5%)
    └── Edge-cloud collaborative serving for real-time constraints
```
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../sources/rankmixer_to_oneranker.md)] | [来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)]

### 维度七：生成式推荐三分基准框架（Data-Model-Task Triad）[新增]

本维度以 2025 年生成式推荐综述提出的统一三分框架为基准，将 LLM4Rec 的技术栈解构为三个可操作、可复现的阶段，为工业落地与学术研究提供标准化分类路径。

```
Generative Rec Tripartite Framework (Data-Model-Task)
├── 数据增强与统一 (Data Augmentation & Unification)
│   ├── 异构信号语义对齐 (点击/浏览/评论/多模态)
│   ├── 知识图谱与常识注入 (Knowledge-Enhanced Data)
│   └── Agent 仿真轨迹生成与反馈闭环构建
├── 模型对齐与训练 (Model Alignment & Training)
│   ├── 基础表征对齐 (Instruction Tuning, Cross-modal Learning)
│   ├── 偏好与价值对齐 (RLHF/DPO, 公平性/多样性约束)
│   └── 推荐专属损失设计 (对比生成损失, 排序一致性约束)
└── 任务构建与执行 (Task Formulation & Execution)
    ├── 序列/ID 生成范式重构 (End-to-End Retrieve+Rank)
    ├── 动态意图捕捉与 CoT 推理链
    └── 多轮对话交互与个性化内容创造性生成
```
[来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)]

### 实验基准、性能权衡与工业挑战 [新增]

基于最新综述的系统性实证整合，生成式推荐在多项公开基准（Amazon, MovieLens, LastFM, 对话推荐数据集）上展现出显著优势，但也暴露出明确的性能权衡与落地瓶颈：

- **核心性能增益**：
  - 在冷启动与复杂意图理解场景下，基于 LLM 的生成式方法相比传统协同过滤与深度判别模型，`NDCG@10` 与 `Recall@20` 平均提升 **15%~30%**。
  - 在可解释性与多轮对话任务中，生成式架构的用户满意度（CSAT）与任务完成率显著优于基线，提升幅度达 **20%~40%**。
- **关键性能权衡**：
  - **推理延迟**：端到端生成式模型的推理延迟通常比传统判别式模型高 **2~5 倍**，对毫秒级实时推荐构成挑战。
  - **幻觉与鲁棒性**：在开放域与长尾物品生成时，事实性错误与过度生成导致的幻觉率约为 **5%~12%**；对噪声数据与分布外（OOD）场景的泛化能力仍需加强。
- **工业优化方向**：
  - 亟需建立针对生成质量、逻辑一致性与多轮交互能力的标准化评测体系。
  - 通过轻量化架构、KV Cache 复用、连续批处理与近线推理+在线快速解码的混合部署策略，压缩 Serving 开销。
  - 引入约束解码、事实校验模块与推荐专属一致性损失，系统性压制幻觉并提升排序稳定性。

[来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)]

---

## 更新完成：2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md
**更新时间**: 2026-04-12 16:57
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
