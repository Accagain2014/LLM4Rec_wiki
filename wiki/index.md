# LLM4Rec Wiki — 知识库目录


> 知识库内容目录。由 LLM 自动维护。

> 最后更新：2026-04-09


## Concepts

| 页名 | 摘要 | 标签 |

|------|------|------|

| [Model FLOPs Utilization (MFU) — Measuring Hardware Efficiency in Recommendation Models](concepts/model_flops_utilization_mfu.md) | --- title: "Model FLOPs Utilization (MFU) — Measuring Hardwa... | MFU, hardware efficiency, GPU utilization, compute efficiency, scaling, RankMixer |

| [Slate Recommendation — 列表级推荐](concepts/slate_recommendation.md) | --- title: "Slate Recommendation — 列表级推荐" category: "concept... | slate, listwise, slate optimization, combinatorial, HiGR |

| [全模态生成式推荐概念页面解释多模态内容如何映射到离散](concepts/all_modality_gr.md) | --- title: "全模态生成式推荐概念页面解释多模态内容如何映射到离散" category: "concepts"... | "new", "2026-04-09" |

| [Hierarchical Planning in Recommendation — 层次化规划](concepts/hierarchical_planning_rec.md) | --- title: "Hierarchical Planning in Recommendation — 层次化规划"... | hierarchical planning, two-stage generation, slate-level intent, HiGR, structured generation |

| [用于推荐系统的大语言模型 — 概述](concepts/llm4rec_overview.md) | --- title: "用于推荐系统的大语言模型 — 概述" category: "concepts" tags: [L... | LLM, RecSys, paradigm, overview |

| [Scaling Laws in Recommendation Systems — Predictable Performance Gains from Scaling](concepts/scaling_laws_recsys.md) | --- title: "Scaling Laws in Recommendation Systems — Predict... | scaling law, model scaling, data scaling, sequence length, compute efficiency, industrial recommendation |

| [Continued Pretraining — Domain Adaptation for LLM-based Recommendation](concepts/continued_pretraining.md) | --- title: "Continued Pretraining — Domain Adaptation for LL... | continued pretraining, domain adaptation, co-pretraining, LLM4Rec, catastrophic forgetting, OpenOneRec |

| [会话级生成概念解释与逐点生成的区别及优势](concepts/session_wise_generation.md) | --- title: "会话级生成概念解释与逐点生成的区别及优势" category: "concepts" tags:... | "new", "2026-04-09" |

| [Representation Alignment — 表示对齐](concepts/representation_alignment.md) | --- title: "Representation Alignment — 表示对齐" category: "conc... | representation alignment, semantic gap, LLM embedding, recommendation objectives, quantitative alignment |

| [Generative Retrieval — 生成式检索](concepts/generative_retrieval.md) | --- title: "Generative Retrieval — 生成式检索" category: "concept... | generative retrieval, semantic ID, autoregressive, neural retrieval, DSI, TIGER, GRID, paradigm shift |

| [Evaluation of LLM4Rec — Benchmarks and Protocols for Generative Recommendation](concepts/evaluation_llm4rec.md) | --- title: "Evaluation of LLM4Rec — Benchmarks and Protocols... | evaluation, benchmark, RecIF-Bench, protocol, LLM4Rec, generative recommendation, metrics |

| [推荐系统中的提示词工程](concepts/prompt_engineering_rec.md) | --- title: "推荐系统中的提示词工程" category: "concepts" tags: [prompt-... | prompt-engineering, instruction, formatting, recsys |

| [Multimodal Recommendation](concepts/multimodal_recommendation.md) | --- title: "Multimodal Recommendation" category: "concepts"... | "new", "2026-04-09" |

| [异构特征交互概念页面解释推荐系统中不同类型特征交互的建模挑战和方法](concepts/heterogeneous_feature_interaction.md) | --- title: "异构特征交互概念页面解释推荐系统中不同类型特征交互的建模挑战和方法" category: "co... | "new", "2026-04-09" |

| [Unified Transformer Backbone — Single Architecture for Feature Interaction and Sequence Modeling](concepts/unified_transformer_backbone.md) | --- title: "Unified Transformer Backbone — Single Architectu... | unified transformer, feature interaction, sequence modeling, OneTrans, unified architecture, tokenization |

| [协同过滤](concepts/collaborative_filtering.md) | --- title: "协同过滤" category: "concepts" tags: [CF, traditiona... | CF, traditional, matrix-factorization, basics |

| [GSU/ESU Paradigm — 通用搜索单元与精确搜索单元](concepts/gsu_esu_paradigm.md) | --- title: "GSU/ESU Paradigm — 通用搜索单元与精确搜索单元" category: "con... | GSU, ESU, two-stage retrieval, industrial architecture, recall, ranking, Kuaishou, Tencent |

| [Semantic IDs — Discrete Semantic Identifiers for Generative Recommendation](concepts/semantic_id.md) | --- title: "Semantic IDs — Discrete Semantic Identifiers for... | semantic ID, generative retrieval, item tokenization, RQ-VAE, codebook, hierarchical ID |

| [序列推荐](concepts/sequential_recommendation.md) | --- title: "序列推荐" category: "concepts" tags: [sequential, be... | sequential, behavior, temporal, sequence-modeling |

| [知识增强推荐](concepts/knowledge_enhanced_rec.md) | --- title: "知识增强推荐" category: "concepts" tags: [knowledge-gr... | knowledge-graph, external-knowledge, semantic, reasoning |

| [定义推荐系统中的记忆Memorization与泛化Generalization能力阐述实例级分类方法及对模型评估的指导意义](concepts/memorization_vs_generalization.md) | --- title: "定义推荐系统中的记忆Memorization与泛化Generalization能力阐述实例级分类... | "new", "2026-04-08" |

| [RecIF-Bench — Recommendation Intelligence Framework Benchmark](concepts/recif_bench.md) | --- title: "RecIF-Bench — Recommendation Intelligence Framew... | RecIF-Bench, benchmark, evaluation, open data, LLM4Rec, OpenOneRec, multi-task |

| [Explicit Reasoning in Recommendation — Making the Recommendation Process Transparent](concepts/explicit_reasoning_rec.md) | --- title: "Explicit Reasoning in Recommendation — Making th... | explicit reasoning, reasoning, interpretable recommendation, OneRec-Think, think-ahead, transparent recommendation |

| [阐述端到端多模态推荐训练范式对比传统两阶段预训练冻结的优劣说明其在动态数据适应目标对齐与实时参数更新上的优势](concepts/end_to_end_multimodal_training.md) | --- title: "阐述端到端多模态推荐训练范式对比传统两阶段预训练冻结的优劣说明其在动态数据适应目标对齐与实时参数... | "new", "2026-04-09" |



- **24 个页面**


## Methods

| 页名 | 摘要 | 标签 |

|------|------|------|

| [定量对齐方法涵盖表示匹配和可训练表示技术](methods/quantitative_alignment.md) | --- title: "定量对齐方法涵盖表示匹配和可训练表示技术" category: "methods" tags:... | "new", "2026-04-08" |

| [Representation Alignment](methods/representation_alignment.md) | --- title: "Representation Alignment" category: "methods" ta... | "new", "2026-04-09" |

| [统一广告语义](methods/ua_sid.md) | --- title: "统一广告语义" category: "methods" tags: ["new", "2026-... | "new", "2026-04-09" |

| [详细介绍论文提出的记忆感知指标MemorizationAware](methods/adaptive_fusion_gr_id.md) | --- title: "详细介绍论文提出的记忆感知指标MemorizationAware" category: "met... | "new", "2026-04-08" |

| [Multi-Objective Alignment — 多目标对齐](methods/multi_objective_alignment.md) | --- title: "Multi-Objective Alignment — 多目标对齐" category: "me... | multi-objective, listwise optimization, preference alignment, implicit feedback, slate optimization |

| [迭代偏好对齐方法涵盖推荐场景下](methods/iterative_preference_alignment.md) | --- title: "迭代偏好对齐方法涵盖推荐场景下" category: "methods" tags: ["new... | "new", "2026-04-09" |

| [排序引导的](methods/rspo.md) | --- title: "排序引导的" category: "methods" tags: ["new", "2026-0... | "new", "2026-04-09" |

| [加权评估方法用于高价值转化事件的评估协议](methods/weighted_evaluation.md) | --- title: "加权评估方法用于高价值转化事件的评估协议" category: "methods" tags:... | "new", "2026-04-09" |

| [推荐系统中的奖励建模涵盖模拟用户生成和定制采样策略](methods/reward_modeling_rec.md) | --- title: "推荐系统中的奖励建模涵盖模拟用户生成和定制采样策略" category: "methods" t... | "new", "2026-04-09" |

| [RAG for RecSys](methods/rag_for_recsys.md) | --- title: "RAG for RecSys" category: "方法" tags: [RAG, 检索, 生... | RAG, 检索, 生成, 增强, 知识 |

| [面向推荐系统的提示式微调](methods/prompt_finetuning.md) | --- title: "面向推荐系统的提示式微调" category: "方法" tags: [微调, PEFT, Lo... | 微调, PEFT, LoRA, 提示微调, 适配 |

| [LLM-as-Generator](methods/llm_as_generator.md) | --- title: "LLM-as-Generator" category: "方法" tags: [生成, 解释,... | 生成, 解释, 推荐文本, 创意 |

| [详细说明](methods/memory_bank_sequential_rep.md) | --- title: "详细说明" category: "methods" tags: ["new", "2026-04... | "new", "2026-04-09" |

| [懒自回归解码器方法页面说明层间依赖放松机制](methods/lazy_ar.md) | --- title: "懒自回归解码器方法页面说明层间依赖放松机制" category: "methods" tags:... | "new", "2026-04-09" |

| [Sparse Attention for Sequential Recommendation — Efficient Long-Sequence Modeling](methods/sparse_attention_seq_rec.md) | --- title: "Sparse Attention for Sequential Recommendation —... | sparse attention, sequential recommendation, long sequence, efficiency, ULTRA-HSTU, LONGER |

| [LLM-as-Ranker](methods/llm_as_ranker.md) | --- title: "LLM-as-Ranker" category: "方法" tags: [排序, LLM, 评分... | 排序, LLM, 评分, listwise, pointwise, pairwise |

| [Long Context Efficiency — Optimizing Transformer Inference for Long Sequences](methods/long_context_efficiency.md) | --- title: "Long Context Efficiency — Optimizing Transformer... | long context, efficiency, KV cache, token merge, STCA, RLB, length extrapolation, industrial optimization |



- **17 个页面**


## Models

| 页名 | 摘要 | 标签 |

|------|------|------|

| [LEMUR](models/LEMUR.md) | --- title: "LEMUR" category: "models" tags: ["new", "2026-04... | "new", "2026-04-09" |

| [OneRec — Unifying Retrieve and Rank with Generative Recommendation](models/OneRec.md) | --- title: "OneRec — Unifying Retrieve and Rank with Generat... | OneRec, generative retrieval, MoE, DPO, preference alignment, Kuaishou, unified architecture |

| [LLMRank](models/LLMRank.md) | --- title: "LLMRank" category: "models" tags: [LLMRank, list... | LLMRank, listwise, ranking, pointwise, pairwise |

| [RankMixer — Hardware-Aware Scalable Ranking Model](models/RankMixer.md) | --- title: "RankMixer — Hardware-Aware Scalable Ranking Mode... | RankMixer, ranking model, hardware-aware, MFU, Sparse-MoE, ByteDance, feature interaction, scaling |

| [P5 — 个性化提示学习](models/P5.md) | --- title: "P5 — 个性化提示学习" category: "models" tags: [P5, prom... | P5, prompt, personalization, unified, multi-task |

| [InstructRec](models/InstructRec.md) | --- title: "InstructRec" category: "models" tags: [InstructR... | InstructRec, instruction-tuning, LLM, conversational |

| [ULTRA-HSTU — Bending the Scaling Law Curve in Recommendation](models/ULTRA_HSTU.md) | --- title: "ULTRA-HSTU — Bending the Scaling Law Curve in Re... | ULTRA-HSTU, HSTU, scaling law, sparse attention, Meta, sequential recommendation, system co-design |

| [LONGER — Long-Sequence Optimized Transformer for Industrial Recommenders](models/LONGER.md) | --- title: "LONGER — Long-Sequence Optimized Transformer for... | LONGER, long sequence, transformer, ByteDance, sparse attention, token merge, industrial deployment, scaling law |

| [TALLRec](models/TALLRec.md) | --- title: "TALLRec" category: "models" tags: [TALLRec, effi... | TALLRec, efficient-tuning, LoRA, LLM, adaptation |

| [HiGR — Hierarchical Planning for Generative Slate Recommendation](models/HiGR.md) | --- title: "HiGR — Hierarchical Planning for Generative Slat... | HiGR, slate recommendation, hierarchical planning, semantic ID, multi-objective, Tencent, generative retrieval |

| [OneRec-Think — In-Text Reasoning for Generative Recommendation](models/OneRec-Think.md) | --- title: "OneRec-Think — In-Text Reasoning for Generative... | OneRec, reasoning, explicit reasoning, generative recommendation, Kuaishou, itemic alignment, Think-Ahead |

| [Hiformer](models/Hiformer.md) | --- title: "Hiformer" category: "models" tags: ["new", "2026... | "new", "2026-04-09" |

| [PLUM — Adapting Pre-trained LLMs for Industrial Generative Recommendations](models/PLUM.md) | --- title: "PLUM — Adapting Pre-trained LLMs for Industrial... | PLUM, semantic ID, continued pre-training, generative retrieval, YouTube, Google, industrial deployment |

| [Qwen 系列](models/qwen_series.md) | --- title: "Qwen 系列" category: "models" tags: [Qwen, Bailian... | Qwen, Bailian, Alibaba, model-family, cloud |

| [GRID — Generative Recommendation with Semantic IDs Framework](models/GRID.md) | --- title: "GRID — Generative Recommendation with Semantic I... | GRID, semantic ID, generative recommendation, open-source, benchmarking, modular framework, Snap Research |

| [DSI / TIGER — Generative Retrieval for Recommender Systems](models/DSI.md) | --- title: "DSI / TIGER — Generative Retrieval for Recommend... | DSI, TIGER, generative retrieval, semantic ID, neural retrieval, Google, NeurIPS |

| [OneRec-V2 — Lazy Decoder-Only Generative Recommendation](models/OneRec-V2.md) | --- title: "OneRec-V2 — Lazy Decoder-Only Generative Recomme... | OneRec, generative recommendation, decoder-only, preference alignment, Kuaishou, MoE, duration-aware |

| [GR4AD](models/GR4AD.md) | --- title: "GR4AD" category: "models" tags: ["new", "2026-04... | "new", "2026-04-09" |

| [QARM](models/QARM.md) | --- title: "QARM" category: "models" tags: ["new", "2026-04-... | "new", "2026-04-08" |



- **19 个页面**


## Entities

| 页名 | 摘要 | 标签 |

|------|------|------|

| [MovieLens 数据集](entities/movielens.md) | --- title: "MovieLens 数据集" category: "entities" tags: [datas... | dataset, movielens, movies, benchmark, ratings |

| [腾讯公司推荐系统团队和工业实践包括](entities/tencent.md) | --- title: "腾讯公司推荐系统团队和工业实践包括" category: "entities" tags: ["... | "new", "2026-04-08" |

| [Guorui Zhou](entities/guorui_zhou.md) | --- title: "Guorui Zhou" category: "entities" tags: ["new",... | "new", "2026-04-08" |

| [GoogleYouTube](entities/google_youtube.md) | --- title: "GoogleYouTube" category: "entities" tags: ["new"... | "new", "2026-04-08" |

| [Amazon 评论数据集](entities/amazon_reviews.md) | --- title: "Amazon 评论数据集" category: "entities" tags: [datase... | dataset, amazon, e-commerce, reviews, benchmark |

| [腾讯广告算法挑战赛Tencent](entities/taac.md) | --- title: "腾讯广告算法挑战赛Tencent" category: "entities" tags: ["n... | "new", "2026-04-09" |

| [Kuaishou](entities/kuaishou.md) | --- title: "Kuaishou" category: "entities" tags: ["new", "20... | "new", "2026-04-08" |

| [Taobao — E-Commerce Recommendation Platform](entities/taobao.md) | --- title: "Taobao — E-Commerce Recommendation Platform" cat... | Taobao, Alibaba, e-commerce, generative retrieval, FORGE, industrial recommendation |

| [ByteDance — Recommendation Systems at Scale](entities/bytedance.md) | --- title: "ByteDance — Recommendation Systems at Scale" cat... | ByteDance, TikTok, Douyin, industrial recommendation, LONGER, RankMixer, LEMUR, industrial deployment |

| [TencentGR1M](entities/tencentgr_dataset.md) | --- title: "TencentGR1M" category: "entities" tags: ["new",... | "new", "2026-04-09" |



- **10 个页面**


## Synthesis

| 页名 | 摘要 | 标签 |

|------|------|------|

| [传统推荐系统与基于 LLM 的推荐系统对比](synthesis/traditional_vs_llm.md) | --- title: "传统推荐系统与基于 LLM 的推荐系统对比" category: "synthesis" tag... | comparison, traditional, LLM, tradeoffs, paradigm-shift |

| [LLM4Rec 分类体系](synthesis/llm4rec_taxonomy.md) | --- title: "LLM4Rec 分类体系" category: "synthesis" tags: [taxon... | taxonomy, survey, classification, framework |

| [知识库健康检查报告 — 2026-04-08](synthesis/lint_report_2026-04-08.md) | --- title: "知识库健康检查报告 — 2026-04-08" category: "synthesis" ta... | "lint", "maintenance" |



- **3 个页面**


## Sources

| 页名 | 摘要 | 标签 |

|------|------|------|

| [2603 Paper 26031980 How Well Does Generative Recommendation Generalize](sources/2603_paper_26031980_How_Well_Does_Generative_Recommendation_Generalize.md) | --- title: "2603 Paper 26031980 How Well Does Generative Rec... | "source", "2026-04-08" |

| [2510 Paper 25102610 Onetrans Unified Feature Interaction And Sequence Modeling](sources/2510_paper_25102610_OneTrans_Unified_Feature_Interaction_and_Sequence_Modeling.md) | --- title: "2510 Paper 25102610 Onetrans Unified Feature Int... | "source", "2026-04-09" |

| [2507 Paper 25072222 Generative Recommendation With Semantic Ids A Practitioner](sources/2507_paper_25072222_Generative_Recommendation_with_Semantic_IDs_A_Practitioner'.md) | --- title: "2507 Paper 25072222 Generative Recommendation Wi... | "source", "2026-04-08" |

| [2509 Paper 25092090 Forge Forming Semantic Identifiers For Generative Retrieval](sources/2509_paper_25092090_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md) | --- title: "2509 Paper 25092090 Forge Forming Semantic Ident... | "source", "2026-04-08" |

| [Paper 4Ddaf2 Recommender Systems With Generative Retrieval](sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md) | --- title: "Paper 4Ddaf2 Recommender Systems With Generative... | "source", "2026-04-08" |

| [Paper C4A451 Forge Forming Semantic Identifiers For Generative Retrieval](sources/paper_c4a451_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md) | --- title: "Paper C4A451 Forge Forming Semantic Identifiers... | "source", "2026-04-08" |

| [QARM V2 — Quantitative Alignment Multi-Modal Recommendation](sources/paper_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation.md) | --- title: "QARM V2 — Quantitative Alignment Multi-Modal Rec... | QARM V2, multi-modal, quantitative alignment, GSU/ESU, LLM embedding, user sequence, industrial |

| [2508 Paper 25082090 Onerec-V2 Technical Report](sources/2508_paper_25082090_OneRec-V2_Technical_Report.md) | --- title: "2508 Paper 25082090 Onerec-V2 Technical Report"... | "source", "2026-04-09" |

| [QARM — Quantitative Alignment Multi-Modal Recommendation at Kuaishou](sources/paper_ad0dff_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md) | --- title: "QARM — Quantitative Alignment Multi-Modal Recomm... | QARM, multi-modal, quantitative alignment, Kuaishou, representation matching, industrial |

| [2602 Paper 26022273 Generative Recommendation For Large-Scale Advertising](sources/2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md) | --- title: "2602 Paper 26022273 Generative Recommendation Fo... | "source", "2026-04-09" |

| [2511 Paper 25111096 Lemur Large Scale End-To-End Multimodal Recommendation](sources/2511_paper_25111096_LEMUR_Large_scale_End-to-end_MUltimodal_Recommendation.md) | --- title: "2511 Paper 25111096 Lemur Large Scale End-To-End... | "source", "2026-04-09" |

| [OneRec: Unifying Retrieve and Rank with Generative Recommender](sources/2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md) | --- title: "OneRec: Unifying Retrieve and Rank with Generati... | "source", "2026-04-09", "generative-retrieval", "unified-model", "kuaishou", "preference-alignment" |

| [2510 Paper 25101163 Onerec-Think In-Text Reasoning For Generative Recommendatio](sources/2510_paper_25101163_OneRec-Think_In-Text_Reasoning_for_Generative_Recommendatio.md) | --- title: "2510 Paper 25101163 Onerec-Think In-Text Reasoni... | "source", "2026-04-08" |

| [2512 Paper 25122476 Openonerec Technical Report](sources/2512_paper_25122476_OpenOneRec_Technical_Report.md) | --- title: "2512 Paper 25122476 Openonerec Technical Report"... | "source", "2026-04-08" |

| [2311 Paper 23110588 Hiformer Heterogeneous Feature Interactions Learning With T](sources/2311_paper_23110588_Hiformer_Heterogeneous_Feature_Interactions_Learning_with_T.md) | --- title: "2311 Paper 23110588 Hiformer Heterogeneous Featu... | "source", "2026-04-09" |

| [Paper 8Edbf8 Higr Efficient Generative Slate Recommendation Via Hierarch](sources/paper_8edbf8_HiGR_Efficient_Generative_Slate_Recommendation_via_Hierarch.md) | --- title: "Paper 8Edbf8 Higr Efficient Generative Slate Rec... | "source", "2026-04-08" |

| [2604 Paper 26040497 Tencent Advertising Algorithm Challenge 2025 All-Modality G](sources/2604_paper_26040497_Tencent_Advertising_Algorithm_Challenge_2025_All-Modality_G.md) | --- title: "2604 Paper 26040497 Tencent Advertising Algorith... | "source", "2026-04-09" |

| [Paper 1B102D Qarm V2 Quantitative Alignment Multi-Modal Recommendation F](sources/paper_1b102d_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md) | --- title: "Paper 1B102D Qarm V2 Quantitative Alignment Mult... | "source", "2026-04-08" |

| [2511 Paper 25110607 Make It Long, Keep It Fast End-To-End 10K-Sequence Modeling](sources/2511_paper_25110607_Make_It_Long,_Keep_It_Fast_End-to-End_10k-Sequence_Modeling.md) | --- title: "2511 Paper 25110607 Make It Long, Keep It Fast E... | "source", "2026-04-09" |

| [2602 Paper 26021698 Bending The Scaling Law Curve In Large-Scale Recommendation](sources/2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md) | --- title: "2602 Paper 26021698 Bending The Scaling Law Curv... | "source", "2026-04-09" |

| [Paper 81Ec38 Plum Adapting Pre-Trained Language Models For Industrial-Sc](sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md) | --- title: "Paper 81Ec38 Plum Adapting Pre-Trained Language... | "source", "2026-04-08" |

| [2505 Paper 25050442 Longer Scaling Up Long Sequence Modeling In Industrial Reco](sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md) | --- title: "2505 Paper 25050442 Longer Scaling Up Long Seque... | "source", "2026-04-09" |

| [2507 Paper 25071555 Rankmixer Scaling Up Ranking Models In Industrial Recommend](sources/2507_paper_25071555_RankMixer_Scaling_Up_Ranking_Models_in_Industrial_Recommend.md) | --- title: "2507 Paper 25071555 Rankmixer Scaling Up Ranking... | "source", "2026-04-09" |

| [Recommender Systems with Generative Retrieval (NeurIPS 2023)](sources/paper_2305_05065_Generative_Retrieval_RecSys.md) | --- title: "Recommender Systems with Generative Retrieval (N... | generative retrieval, semantic ID, DSI, TIGER, neural retrieval, Google, NeurIPS 2023 |

| [Paper C33D89 Farewell To Item Ids Unlocking The Scaling Potential Of Lar](sources/paper_c33d89_Farewell_to_Item_IDs_Unlocking_the_Scaling_Potential_of_Lar.md) | --- title: "Paper C33D89 Farewell To Item Ids Unlocking The... | "source", "2026-04-08" |



- **25 个页面**


---

**统计**：

- 总页面数：98
