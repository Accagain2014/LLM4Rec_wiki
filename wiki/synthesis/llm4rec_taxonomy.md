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

本页面展示了 LLM4Rec 方法的**综合分类体系**，将多样化的方法、模型和应用组织成一个结构化框架。该分类体系不仅涵盖传统的 **LLM 角色**、**适配策略**、**任务类型**和**部署模式**，更引入了面向工业落地的**演进主线与技术趋势**维度。为夯实技术底座，本次更新新增**基础 LLM 能力层**维度，将预训练、指令对齐、高效微调与推理优化作为底层支撑模块纳入分类树。同时，**全面整合 2025 年生成式推荐综述提出的“数据-模型-任务”三分基准框架**，在数据层引入 Agent 仿真与知识增强分支，在模型层纳入扩散生成架构与推荐专属对齐损失，在任务层强化动态意图捕捉与创造性生成。本体系进一步对齐 **Gen-RecSys 三大核心范式**（交互序列生成、LLM文本推理、多模态内容生成），明确 VAE/Diffusion/Autoregressive 架构的适用边界，并引入安全性与社会影响力评估框架。此外，**首次纳入 2025 年前沿的个性化动态分词范式（Pctx）**，突破传统静态语义ID映射瓶颈，为生成式推荐提供“一物多码”的上下文自适应表示层，为浏览 Wiki 内容、追踪技术范式迁移提供了从底层能力到上层应用的动态导航地图。

## 要点

- **基础 LLM 能力层**：涵盖 Decoder-only 架构演进、MoE 动态路由、上下文扩展、SFT/PEFT 微调范式、RLHF/DPO 偏好对齐及量化/投机解码等推理加速技术
- **Gen-RecSys 三大核心范式（新增）**：交互序列生成（VAE/Diffusion）、LLM 文本推理（Autoregressive）、多模态内容生成（VLM/Cross-modal），明确各架构在稀疏建模、冷启动推理与跨模态对齐中的适用边界
- **生成式推荐三分基准框架**：以 `Data-Model-Task` 为核心分类基准，解构生成式推荐为数据增强统一、模型对齐训练、任务构建执行三大可操作阶段
- **表示与分词范式升级（新增）**：从静态全局字典迈向个性化动态分词（Pctx），通过条件化概率建模 $P(ID|Item, UserContext)$ 实现“一物多码”，解决自回归生成中的前缀坍缩与同质化问题，NDCG@10 相对提升最高达 11.44%
- LLM 承担五种核心角色：**Ranker（排序器）**、**Generator（生成器）**、**Reasoner（推理器）**、**Unifier/Tokenizer（统一主干与语义标记器）**、**Agent/Assistant（智能交互助手）**
- 适配策略：**Zero-shot**、**Few-shot**、**PEFT**、**Full Fine-Tuning**、**Alignment-based**、**Diffusion-based Generation**、**Inference-time Scaling**，并引入**生成-排序联合损失优化**与**对比正则化**
- 任务类别：**Candidate Generation**、**Ranking**、**Generative One-Model**、**Explanation & Dialogue**、**Creative & Multi-turn Generation**
- 部署模式：**Pure LLM**、**Hybrid LLM+RecSys**、**Discriminative Large Backbone**、**Generative One-Model Pipeline**、**Distilled & Serving-Optimized**
- **数据与评估演进**：从交互矩阵扩展至 Agent 仿真轨迹、知识图谱增强、多模态异构信号语义对齐；评估体系突破传统准确率局限，纳入幻觉检测、公平性、隐私保护与社会危害标准化指标
- **性能与权衡**：冷启动/稀疏场景 Recall@10 提升 8%~15%，NDCG@10 提升 5%~12%；扩散模型覆盖率提升 20%~30%，长尾曝光增加 18%；多模态融合 CTR AUC 提升 3.5%~6.2%；但推理延迟增加 2~5 倍，长尾生成幻觉率约 5%~12%
- 本分类体系将所有 Wiki 内容组织到一个连贯且具备工业演进视角的框架中

## 详细内容

### 维度一：基础 LLM 能力层（底层支撑）

本维度聚焦 LLM 在接入推荐系统前的底层技术栈，涵盖架构基座、训练范式、价值对齐与推理优化，为上层推荐适配提供可复用的能力模块。

```
Foundation LLM Capability Layer
├── 预训练与架构基座 (Pretraining & Architecture)
│   ├── Decoder-only Transformer 变体与位置编码 (RoPE, ALiBi)
│   ├── 混合专家模型 (MoE) 与动态路由机制
│   ├── 上下文窗口扩展 (Attention 稀疏化, KV Cache 压缩)
│   └── 生成式表征学习基座 (VAE / Diffusion 潜在空间映射) [新增]
├── 指令微调与监督学习 (Instruction Tuning & SFT)
│   ├── 领域指令构建与高质量数据配比
│   ├── 全参数微调 vs 参数高效微调 (LoRA, Adapter, Prefix-Tuning)
│   ├── 垂直领域适配 (推荐冷启动/特征工程/多模态对齐)
│   └── 课程学习策略 (Curriculum Learning for Long-tail) [新增]
├── 偏好对齐与价值优化 (Alignment & Preference Optimization)
│   ├── RLHF (PPO-based 奖励建模)
│   ├── 直接偏好优化 (DPO / IPO / ORPO)
│   ├── 推荐场景对齐 (缓解信息茧房/流行度偏差/公平性约束)
│   └── 缩放定律应用 (Scaling Laws for RecSys)
└── 推理优化与部署加速 (Inference & Serving Optimization)
    ├── 模型压缩 (INT4/INT8 量化, 结构化剪枝)
    ├── 解码加速 (投机解码, 连续批处理 Continuous Batching)
    └── 显存与计算开销控制 (PEFT 降显存 60%+, 精度损失 <2%)
```
[来源：[A Comprehensive Overview of Large Language Models](../sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md)] | [来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)] | [来源：[2404_paper_24040057_A_Review_of_Modern_Recommender_Systems_Using_Generative_Mode.md](../sources/2404_paper_24040057_A_Review_of_Modern_Recommender_Systems_Using_Generative_Mode.md)]

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
│   ├── Intent inference & Preference decomposition
│   ├── Cross-domain reasoning & Knowledge transfer
│   ├── Planning & strategy formulation
│   └── CoT-based dynamic intent capture [新增]
├── LLM-as-Unifier & Tokenizer
│   ├── Unified backbone modeling (OneTrans, MixFormer)
│   ├── 表示与分词（Representation & Tokenization）
│   │   ├── 静态语义索引与全局字典映射 (TRM, MERGE)
│   │   ├── 多场景/任务标记注入 (MDL, MTFM)
│   │   └── Personalized/Dynamic Tokenization (Pctx) [2025 新兴方向] [新增]
└── LLM-as-Agent/Assistant
    ├── Multi-turn conversational recommendation
    ├── Dynamic intent tracking & feedback loop
    └── Autonomous tool-use & external API orchestration
```

#### 表示与分词（Representation & Tokenization）深度解析
传统生成式推荐（GR）模型依赖静态、非个性化的分词机制，仅基于物品特征构建全局统一的语义相似性，强制所有用户共享同一套物品-ID映射标准。在自回归生成范式下，相同前缀必然导致相似的概率分布，这种“一刀切”机制严重违背了推荐场景中“同一物品因用户意图不同而产生差异化解读”的客观规律，易引发**前缀坍缩（Prefix Collapse）**与推荐同质化。

2025年新兴的 **Personalized/Dynamic Tokenization（以 Pctx 为代表）** 彻底重构了这一底层表示逻辑：
- **核心机制**：设计上下文感知的动态分词模块，将用户历史交互序列显式引入语义ID生成过程。通过条件化概率建模 $P(ID|Item, UserContext)$，实现“一物多码”的个性化映射，使同一物品在不同用户语境下映射为不同的语义ID序列。
- **架构设计**：作为生成式推荐模型的前置表示层，接收目标物品原始特征与用户历史序列作为联合输入。通过上下文编码器进行跨序列特征融合与意图提取，随后利用条件自回归解码机制动态生成专属语义ID。该设计采用即插即用范式，无需修改底层 Transformer/LLM 主干，大幅降低工程迁移成本。
- **性能增益**：在三个主流公开数据集上验证，相较于非个性化基线，Pctx 在 **NDCG@10** 指标上实现最高 **11.44%** 的相对提升。个性化语义ID能更精准刻画用户意图，在检索召回与精排阶段带来一致增益，且未引入显著的额外推理延迟瓶颈。
- **局限与挑战**：动态分词需在推理阶段实时结合用户上下文生成ID，对高并发在线服务的缓存策略与计算资源调度提出更高要求；冷启动或交互极度稀疏场景下，上下文信息不足可能导致分词质量退化或语义漂移；如何在保证个性化ID多样性的同时维持全局语义空间的拓扑稳定性与跨用户可解释性，仍是未来探索重点。

该工作推动了生成式推荐从“统一语义空间”向“用户自适应语义空间”的范式演进，为 LLM4Rec 提供了关键的架构启示：推荐系统的 Tokenization 不应是预定义的静态字典，而应具备条件化、个性化的动态生成能力，从底层表示层面缓解大模型在推荐场景中的“幻觉”与“偏好对齐”难题。

[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../sources/rankmixer_to_oneranker.md)] | [来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)] | [来源：[2404_paper_24040057_A_Review_of_Modern_Recommender_Systems_Using_Generative_Mode.md](../sources/2404_paper_24040057_A_Review_of_Modern_Recommender_Systems_Using_Generative_Mode.md)] | [来源：[2510_paper_25102127_Pctx_Tokenizing_Personalized_Context_for_Generative_Recomme.md](../sources/2510_paper_25102127_Pctx_Tokenizing_Personalized_Context_for_Generative_Recomme.md)]

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
│   ├── 推荐专属联合损失 (Generative CE/Denoising + BPR/InfoNCE) [新增]
│   └── 对比正则化防表征坍塌 (Contrastive Regularization) [新增]
├── Diffusion-based Generation
│   ├── Latent diffusion for item representation
│   └── Conditional generation with user history
└── Inference-Time & Serving Adaptation
    ├── KV Caching & Request-level batching (STCA, OneTrans)
    ├── User-side computation reuse (UG-Separation)
    └── Process reward & dynamic beam serving (GRank, PROMISE)
```
[来源：[从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线](../sources/rankmixer_to_oneranker.md)] | [来源：[A Comprehensive Overview of Large Language Models](../sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md)] | [来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)] | [来源：[2404_paper_24040057_A_Review_of_Modern_Recommender_Systems_Using_Generative_Mode.md](../sources/2404_paper_24040057_A_Review_of_Modern_Recommender_Systems_Using_Generative_Mode.md)]

---

## 更新完成：2510_paper_25102127_Pctx_Tokenizing_Personalized_Context_for_Generative_Recomme.md
**更新时间**: 2026-04-14 15:35
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2510_paper_25102127_Pctx_Tokenizing_Personalized_Context_for_Generative_Recomme.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
