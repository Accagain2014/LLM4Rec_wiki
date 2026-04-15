---
title: "GoogleYouTube"
category: "entities"
tags: ["new", "2026-04-08"]
created: "2026-04-08"
updated: "2026-04-08"
sources: ["../sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md"]
related: []
confidence: "medium"
status: "draft"
---

# Google/YouTube 推荐系统

：Google/YouTube 推荐系统团队和工业实践

## 概述
Google/YouTube 推荐系统团队是全球推荐算法工业实践的标杆之一。近年来，该团队在深度学习排序、多模态内容理解、生成式推荐（Generative Recommendation）以及大语言模型与推荐系统的深度融合（LLM4Rec）方面开展了大量前沿探索与大规模线上部署。其技术路线已从传统的协同过滤与深度特征交叉模型，逐步演进至基于语义表征、离散序列建模与生成式检索的新一代推荐架构，持续推动工业级推荐系统在泛化能力、长尾覆盖与参数效率上的突破。

## 核心技术演进与工业实践

### 1. 异构特征交互与 Transformer 架构落地
在深度学习向推荐系统渗透的早期阶段，Google 团队重点探索了如何高效处理异构特征（如用户行为序列、上下文特征、多模态内容等）。以 **Hiformer** 为代表的工作，针对传统 Transformer 在推荐场景中处理异构特征时存在的计算冗余与表征对齐难题，设计了异构特征交互学习机制。该架构已在 **Google Play** 应用推荐场景中完成大规模工业部署，显著提升了特征交叉效率与排序精度，验证了 Transformer 架构在超大规模稀疏推荐场景中的可扩展性。[来源：[2311_paper_23110588_Hiformer_Heterogeneous_Feature_Interactions_Learning_with_T.md](../sources/2311_paper_23110588_Hiformer_Heterogeneous_Feature_Interactions_Learning_with_T.md)]

### 2. 预训练语言模型适配与生成式检索
随着大语言模型（LLM）的崛起，Google Research（包括 Yi Tay、Ed H. Chi 等核心研究员）率先探索了如何将预训练语言模型的能力迁移至推荐系统。**PLUM** 等工作系统研究了工业场景下适配预训练 LM 的范式，解决了推荐数据分布与通用语料分布差异带来的微调难题。同时，团队在 **生成式检索（Generative Retrieval）** 方向取得重要突破，提出将物品检索转化为序列生成任务，通过自回归解码直接输出目标物品标识，大幅简化了传统“召回-粗排-精排”的多阶段流水线。[来源：[paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md](../sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md)] [来源：[paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md](../sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md)]

在生成式推荐的部署策略上，Google 与 Meta/Facebook 呈现出不同的技术路径。Meta 侧重于基于万亿参数序列模型（Trillion-Parameter Sequential Model）的端到端行为建模，而 Google 则更强调通过底层 ID 表征革新（如 Semantic ID）与轻量级生成架构的结合，在保持工业级推理延迟约束的前提下实现语义泛化。[来源：[paper_260110_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md](../sources/paper_260110_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md)]

### 3. 语义ID（Semantic IDs）与底层表征范式革新
传统推荐系统依赖随机哈希的离散 Item ID，导致语义相似的物品无法共享表征，长尾及新物品面临严重的冷启动与泛化瓶颈。2023年，YouTube 推荐团队发表奠基性工作，正式在工业排序场景中引入 **语义ID（Semantic IDs）** 替代传统离散 ID。

该方案的核心技术路径如下：
- **RQ-VAE 层级离散化**：利用残差量化变分自编码器（RQ-VAE）将冻结的多模态内容连续嵌入逐层量化为离散码本序列。每一层码本捕获不同粒度的语义概念（如粗粒度类别→细粒度主题），使相似物品在 ID 序列的前缀或中段共享相同码字。
- **SentencePiece 子序列哈希**：将语义 ID 序列视为“伪文本”，引入 LLM 领域成熟的 SentencePiece 分词器（BPE/Unigram 算法）进行数据驱动的子词切分。该方法自动学习高频共现的 ID 子片段，生成最优哈希桶，显著优于人工设计的固定窗口 N-gram 策略。
- **记忆-泛化联合优化**：高频子序列通过 Embedding 表保留强记忆信号，低频/新序列则通过共享前缀码本触发语义泛化，实现隐式正则化。模型保持原有排序架构（如 DCN/DeepFM）不变，仅替换 ID 特征输入。[来源：[2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md](../sources/2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md)]

## 关键实验数据与线上收益
在 YouTube 真实工业级视频推荐排序模型上的离线评估与在线 A/B 测试表明，Semantic ID 方案在多项核心指标上取得显著收益：
- **长尾与新物品泛化**：在曝光量后 10% 的长尾切片及全新上架物品上，点击率（CTR）相对基线提升约 **2.8%~3.5%**，平均观看时长提升约 **1.9%**。
- **全局性能与参数效率**：全局 AUC 与 NDCG@10 与随机 Hash ID 基线持平（差异 <0.05%），验证了“泛化提升不损记忆”的假设；同时，Embedding 表参数量减少约 **15%**，SentencePiece 分片策略较 N-gram 基线额外带来 0.7% 的长尾 CTR 相对增益。
- **消融验证**：移除 RQ-VAE 层级结构或改用连续内容嵌入，长尾指标分别下降 1.2% 与 2.1%，凸显离散语义序列与子序列哈希在工业落地中的必要性。[来源：[2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md](../sources/2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md)]

## 与 LLM4Rec 的关联与启示
该系列工作是 LLM 技术向推荐系统底层表征迁移的里程碑。其核心贡献在于将大语言模型中成熟的**分词技术（Tokenizer）**与**离散序列建模思想**引入推荐 ID 学习，打破了传统协同过滤依赖随机 ID 的范式。Semantic ID 本质上是一种“推荐领域的 Tokenization”，使物品具备类似自然语言词汇的语义组合、上下文泛化与零样本推理能力。这为 LLM4Rec 中“将推荐任务转化为序列生成/理解任务”提供了统一的底层 ID 表征基础，验证了离散语义表征在工业级排序中的可行性，为构建多模态-文本-推荐联合大模型及生成式推荐系统的落地铺平了道路。[来源：[2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md](../sources/2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md)]

## 相关页面
- [PLUM：工业场景预训练语言模型适配](../sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md)
- [生成式检索（Generative Retrieval）](../sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md)
- [Hiformer：异构特征交互学习](../sources/2311_paper_23110588_Hiformer_Heterogeneous_Feature_Interactions_Learning_with_T.md)
- [Meta 万亿参数序列模型对比](../sources/paper_260110_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md)
- [Semantic ID：推荐排序中的语义表征案例](../sources/2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md)

## 更新日志
- **2026-04-08**：新增 Google Research 生成式检索论文（Yi Tay, Ed H. Chi 等），补充 Meta/Facebook 生成式推荐部署策略对比。
- **2026-04-09**：补充 Hiformer 在 Google Play 的部署案例，完善 Transformer 架构在推荐系统的工业实践记录。
- **2026-04-14**：新增 2023 年 Semantic ID 奠基性工作，详细补充 RQ-VAE 离散化、SentencePiece 分片策略及 YouTube 线上收益数据（长尾 CTR +2.8%~3.5%，Embedding 参数 -15%），强化 LLM4Rec 底层表征关联分析。

---

## 更新完成：2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md
**更新时间**: 2026-04-14 15:10
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
