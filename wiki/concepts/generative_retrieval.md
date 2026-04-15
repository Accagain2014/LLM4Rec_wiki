---
title: "Generative Retrieval — 生成式检索"
category: "concepts"
tags: [generative retrieval, semantic ID, autoregressive, neural retrieval, DSI, TIGER, GRID, paradigm shift]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/2507_paper_25072222_Generative_Recommendation_with_Semantic_IDs_A_Practitioner'.md", "../sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md"]
related:
  - "../models/DSI.md"
  - "../models/PLUM.md"
  - "../models/HiGR.md"
  - "../concepts/semantic_id.md"
  - "../methods/llm_as_generator.md"
confidence: "high"
status: "stable"
---

# Generative Retrieval — 生成式检索

## 摘要

Generative Retrieval (GR) 是一种**范式转变**：用**自回归生成物品标识符**取代传统的"嵌入 + 近似最近邻搜索"检索流程。GR 的核心是使用 **Semantic ID（语义 ID）**——将物品映射为离散的码字元组——使模型能够直接从用户上下文生成目标物品的标识符。需要明确的是，**GR 是生成式推荐（Generative Recommendation, GenRec）的核心子集**，GenRec 进一步将生成范式扩展至对话交互、可解释推理与个性化内容生成等复合任务。该范式由 Google 在 NeurIPS 2023 首次引入推荐系统，随后在工业界（YouTube、腾讯、快手、美团、Pinterest、今日头条）得到广泛验证与架构演进，正逐步向多业务协同、多目标对齐、端到端单模型范式迈进。[来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)]

## 要点

- **范式转变**：从"检索然后排序"到"生成即推荐"
- **概念边界**：GR 聚焦物品标识符生成，是 GenRec 的子集；GenRec 涵盖更广泛的生成任务（对话、解释、内容生成）
- **技术溯源**：Semantic ID 最初在判别式排序场景验证，后成为 GR 核心标识符范式
- **Semantic ID**：物品映射为离散码字元组，捕捉语义相似性，实现记忆与泛化的平衡
- **自回归生成**：Transformer seq2seq 模型逐个生成 ID codeword
- **更好的泛化**：对长尾和未见物品的推荐显著改善
- **统一架构**：OneRec 系列将召回和排序统一为单一生成过程
- **多业务解耦**：通过业务感知 ID 与动态路由解决跨业务表征干扰与优化冲突
- **结果条件化生成**：动态注入业务指标权重，实现点击、保存等多目标灵活对齐
- **多Token联合解码**：突破单Token自回归瓶颈，提升推理吞吐与长尾覆盖率
- **动态条件化分词**：GR 管线正从固定词表向条件化生成词表演进，Pctx 等方案通过“一物多码”有效缓解前缀坍缩与推荐同质化
- **序列上下文感知分词**：ActionPiece 等前沿工作引入特征共现统计与集合排列正则化，将离散动作序列转化为语义连贯的 Token 空间，显著提升序列建模精度
- **新一代残差量化**：R3-VAE 通过参考向量锚定与点积评分机制解决码本坍塌，提供高稳定、免评估的 SID 生成方案，已在今日头条工业场景验证
- **工业部署成熟**：Pinterest PinRec、今日头条 GR 管线等验证了 GR 在亿级候选池与高并发场景下的工程可行性
- **数据-模型-任务框架**：提供系统化的 GenRec 研究与工程范式
- **开源基准**：GRID 框架提供统一的 GR 实验平台

## 详情

### 历史背景与技术起源

在生成式检索（GR）范式兴起之前，推荐系统长期依赖随机哈希的离散 Item ID 作为物品表征。这种设计虽便于 Embedding 查找，但导致语义相似的物品在向量空间中完全隔离，严重制约了模型对长尾物品与新物品的泛化能力。

**Semantic ID 的概念并非 GR 专属，其技术起源可追溯至判别式排序场景。** Google 团队于 2023 年发表的《Better Generalization with Semantic IDs: A Case Study in Ranking for Recommendations》首次系统验证了语义 ID 在工业级排序任务中的有效性。该工作指出，若直接用连续内容嵌入替换离散 ID，会严重削弱模型对头部热门物品的记忆能力；因此提出利用 **RQ-VAE** 从冻结的多模态内容嵌入中学习多层级离散码本序列，并结合 LLM 领域的 **SentencePiece 分词技术**进行子序列哈希。该方案在 YouTube 真实排序场景中实现了“记忆-泛化”的有效权衡，显著提升了新物品与长尾物品的推荐效果，且未牺牲全局排序指标。这一里程碑式验证打破了传统协同过滤依赖随机 ID 的范式，证明了离散语义序列在推荐底层表征中的可行性，随后才被 TIGER、PLUM 等生成式检索模型采纳为核心标识符范式，正式开启 GR 时代。[来源：[2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md](../sources/2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md)]

### 传统检索 vs 生成式检索

```
传统检索:
User → [Encoder] → User Embedding
Items → [Encoder] → Item Embeddings
User Embedding + Item Embeddings → [ANN Search] → Top-K Items

生成式检索:
User Context → [Transformer] → Semantic ID₁, Semantic ID₂, ... → Top-K Items
```

### GR 与 GenRec 的概念边界与任务泛化

生成式推荐（GenRec）代表了推荐系统从**判别式打分**向**生成式任务**的根本性重构。GR 作为 GenRec 的关键子集，主要解决“如何高效生成目标物品标识符”的检索/召回问题；而 GenRec 的边界已大幅扩展，形成“数据-模型-任务”三位一体的宏观架构：[来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)]

1. **数据层增强与统一**：利用生成模型注入外部知识图谱与常识，通过 Agent 模拟用户行为轨迹与反馈回路，解决数据稀疏性与冷启动问题，实现点击、浏览、文本评论等多源异构信号的语义级对齐。
2. **模型层对齐与训练**：整合 LLM、专用推荐大模型与扩散生成架构，采用指令微调（Instruction Tuning）、偏好对齐（RLHF/DPO）及跨模态表征学习，使生成模型适配推荐领域的排序与匹配目标。
3. **任务层泛化与扩展**：将传统 Top-K 推荐扩展为多模态生成任务流，实现从“隐式匹配”到“显式生成”的架构跃迁。

### Semantic ID 设计

Semantic ID 是 GR 的核心创新，其本质是“推荐领域的 Tokenization”，使物品具备类似自然语言词汇的语义组合、上下文泛化与零样本推理能力：
- **离散序列结构**：每个物品 = `(c₁, c₂, ..., cₖ)` 其中 `cᵢ` 是离散码字
- **语义层级化**：相似物品共享前缀码字，前缀控制粗粒度（类目/主题），后缀控制细粒度（具体物品）
- **可学习量化**：通过 RQ-VAE 等残差量化机制端到端训练，将高维连续内容空间映射为树状离散码本
- **子序列哈希优化**：引入 SentencePiece (BPE/Unigram) 算法对 ID 序列进行数据驱动的子词切分，自动学习高频共现片段，生成最优哈希桶，显著优于人工设计的 N-gram 策略
- **记忆-泛化联合机制**：高频子序列通过 Embedding 表保留强记忆信号，低频/新序列则通过共享前缀码本触发语义泛化，实现隐式正则化。在 YouTube 排序实验中，该设计使长尾/新物品 CTR 提升 2.8%~3.5%，平均观看时长提升 1.9%，且 Embedding 表参数量减少约 15%。[来源：[2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md](../sources/2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md)]

### Tokenization 与索引构建演进

随着 GR 范式的深入，底层物品表示的构建方式正经历从**静态全局词表**向**条件化动态词表**与**高稳定离散化**的关键演进。传统 GR 管线依赖仅基于物品特征构建的固定语义 ID，强制所有用户共享统一的物品相似性标准。在自回归生成过程中，这种“一刀切”的映射机制会导致相同前缀必然触发相似的概率分布，引发严重的**“前缀坍缩”（Prefix Collapse）**现象，进而造成推荐结果同质化，无法适配用户意图与偏好的多维差异性。同时，传统残差量化方法常面临码本坍塌与训练震荡难题，制约了 LLM 自回归管线的稳定性。

针对这些根本缺陷，序列分词与 Tokenization 技术正朝着**上下文感知（Context-Aware）**与**量化稳定化**方向快速迭代，代表性工作包括：

#### 1. 个性化上下文分词（Pctx）
打破物品与 ID 的一对一静态绑定，将用户历史交互序列显式引入分词过程，通过条件概率建模 $P(ID|Item, UserContext)$ 实现“一物多码”的个性化映射。在自回归解码时，用户历史行为序列对 ID 前缀生成形成强约束，自然引导模型将注意力聚焦于与当前意图高度相关的候选子集，有效缓解前缀坍缩与推荐同质化。[来源：[2510_paper_25102127_Pctx_Tokenizing_Personalized_Context_for_Generative_Recomme.md](../sources/2510_paper_25102127_Pctx_Tokenizing_Personalized_Context_for_Generative_Recomme.md)]

#### 2. 动作序列共现分词（ActionPiece）
传统分词往往将用户交互动作视为独立单元进行固定 Token 分配，割裂了序列上下文中的细粒度语义关联。**ActionPiece** 提出了一种面向生成式推荐的上下文感知动作序列分词框架，直击 LLM4Rec 中离散序列到 Token 空间映射的语义鸿沟：[来源：[2502_paper_25021358_ActionPiece_Contextually_Tokenizing_Action_Sequences_for_Ge.md](../sources/2502_paper_25021358_ActionPiece_Contextually_Tokenizing_Action_Sequences_for_Ge.md)]
- **特征共现词表构建**：将用户交互动作解构为无序物品特征集合（如品类、品牌、价格段等），借鉴 BPE 思想扩展至集合层面。通过统计特征在局部集合内及跨序列相邻集合中的共现频率，迭代合并高频共现特征对，生成兼顾局部属性与全局序列模式的复合 Token 词表，使相同动作在不同交互语境下获得差异化、语义更丰富的表征。
- **集合排列正则化（Set Permutation Regularization）**：针对物品特征集合的无序本质，固定线性化顺序会引入人为归纳偏置。该方法在训练阶段对特征集合进行多次随机排列，生成多条语义等价但分割路径不同的序列视图，通过一致性损失约束模型输出分布，迫使模型学习对排列不变的鲁棒表征，显著提升序列建模的语义连贯性。
- **即插即用与零推理开销**：作为前置表示层无缝对接主流 GR/LLM 框架，无需修改底层 Transformer 生成架构。推理阶段无需额外计算，保持与基线模型相同的生成效率。在 Amazon 公开数据集上，Recall@10 与 NDCG@10 均取得稳定提升（较 TIGER 等基线最高提升 +2.41%），验证了共现统计与排列正则化对语义表征的实质性增强。

#### 3. 参考向量引导残差量化（R3-VAE）
传统残差量化方法（如 RQ-VAE）在生成语义 ID 时，常面临训练不稳定、码本坍塌（Codebook Collapse）以及依赖昂贵下游任务评估等瓶颈。**R3-VAE** 作为新一代残差量化方案，专为生成式推荐与 LLM 自回归生成的高兼容性而设计，通过引入参考向量锚定与点积评分机制，显著提升了离散标识符的语义质量与训练鲁棒性：[来源：[2604_paper_26041144_R3-VAE_Reference_Vector-Guided_Rating_Residual_Quantization.md](../sources/2604_paper_26041144_R3-VAE_Reference_Vector-Guided_Rating_Residual_Quantization.md)]
- **参考向量语义锚定（Reference Vector Guidance）**：在量化初期注入预定义的参考向量作为语义先验，有效降低随机初始化方差，使量化器快速收敛至合理的语义簇，避免陷入局部最优。
- **点积评分稳定机制（Dot Product-based Rating）**：摒弃传统硬分配与直通估计器（STE），采用点积相似度进行软评分与梯度近似。该设计优化了梯度传播路径，确保离散化过程中的平滑更新，从根本上抑制码本坍塌，最大化离散码本利用率。
- **免训练双指标正则化**：创新性地提出“语义内聚性”与“偏好判别力”两项评估指标，并直接融入损失函数进行端到端优化。模型无需依赖下游 GR 训练或 A/B 测试即可自主迭代出高判别力 SID，大幅降低研发迭代成本。
- **LLM 自回归兼容性与工业验证**：R3-VAE 生成的 SID 具备高度语义连贯性，可直接无缝接入 LLM 的自回归解码管线，提升长序列上下文建模效率。在**今日头条**的真实流量生成式推荐任务中，该方法使 MRR 提升 **1.62%**，用户停留时长（StayTime/U）提升 **0.83%**；在内容冷启动场景下，替换传统 Item ID 后推荐效果显著提升 **15.36%**，充分验证了其在超大规模工业推荐系统中的泛化能力与商业价值。

### 关键技术组件

#### 1. ID 构建方法
| 方法 | 描述 | 代表工作 |
|------|------|---------|
| RQ-VAE | 残差量化 VQ-VAE，逐层离散化连续特征 | TIGER, HiGR |
| RQ-VAE + SentencePiece | 结合 LLM 分词技术进行子序列哈希，优化记忆-泛化权衡 | Google Ranking (2023) |
| KD-Tree | 聚类树划分 | DSI |
| 语义聚类 | K-means on embeddings | PLUM, GRID |
| **条件化动态分词** | **基于用户上下文动态生成个性化 ID，实现一物多码，缓解前缀坍缩** | **Pctx (2025)** |
| **序列共现分词** | **基于特征共现统计构建动态词表，引入集合排列正则化提升语义连贯性** | **ActionPiece (2025)** |
| **参考向量残差量化** | **引入参考向量锚定与点积评分，解决码本坍塌，提供免训练评估的高稳定 SID** | **R3-VAE (2026)** |

#### 2. 生成模型架构
- **Encoder-Decoder** (T5-style)：编码用户上下文，解码物品 ID
- **Decoder-only** (LLM-style)：自回归生成，支持更长上下文
- **层次化生成**：先生成 slate 意图，再生成具体物品（HiGR）
- **多Token联合解码**：突破传统单Token逐步生成的效率瓶颈，采用并行预测或改进的束搜索策略，在单步内生成多个连续码字，显著降低自回归累积误差与推理延迟，同时提升候选集多样性与长尾覆盖率。

#### 3. 训练与对齐策略
- **监督微调**：在交互数据上训练 ID 生成
- **持续预训练**（CPT）：在领域数据上继续预训练（PLUM）
- **指令微调**：用推荐指令调优（Instruction Tuning）使模型理解复杂推荐意图与多轮交互逻辑
- **偏好对齐**：基于人类反馈（RLHF/DPO）优化生成序列的排序质量与业务指标对齐度
- **免训练表征优化**：利用 R3-VAE 等新型量化正则化机制，在底层离散化阶段直接注入业务判别信号，实现表征学习与下游生成目标的解耦优化。

## 相关页面
- [Generative Recommendation (GenRec) — 生成式推荐](./Generative_Recommendation.md)
- [Semantic ID — 语义标识符](./Semantic_ID.md)
- [LLM4Rec Tokenization — 大模型推荐分词技术](./LLM4Rec_Tokenization.md)
- [Residual Quantization in RecSys — 推荐系统残差量化](./Residual_Quantization_RecSys.md)

---

## 更新完成：2604_paper_26041144_R3-VAE_Reference_Vector-Guided_Rating_Residual_Quantization.md
**更新时间**: 2026-04-15 01:30
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2604_paper_26041144_R3-VAE_Reference_Vector-Guided_Rating_Residual_Quantization.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
