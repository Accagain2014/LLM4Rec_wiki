# LLM4Rec Wiki

> 一个持久化、持续累积的知识库，专注于**大语言模型在推荐系统的应用 (LLM4Rec)**，基于 [karpathy/llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 模式构建，由Qwen Code调用qwen3.6-plus实现，使用阿里百炼Code Plan.

## 概述

本项目实现了一个由 LLM 维护的领域知识库，聚焦于**大语言模型在推荐系统的应用 (LLM4Rec)**。与传统的 RAG（每次查询都重新推导知识）不同，该 wiki **逐步构建并维护**一个结构化的、相互链接的知识库，随着时间推移不断累积。


## Summary

### 知识库统计
- 总页面数：166
- 各类别页面数量分布：entities (16), summary (6), models (29), sources (60), concepts (28), methods (24), synthesis (3)

### 核心覆盖领域
- **生成式推荐与语义标识符（Semantic ID）**：系统梳理从传统双塔+ANN检索向自回归生成离散物品标识符的范式转变，涵盖码本构建、残差量化与免训练代理评估。
- **统一架构与端到端建模**：聚焦打破“召回-粗排-精排”多阶段流水线割裂，探索基于单一Transformer骨干的检索排序统一、特征交互与序列建模深度融合。
- **推荐系统缩放定律与高效计算**：深入记录模型规模、序列长度与算力投入对推荐性能的幂律影响，以及线性注意力、硬件感知调度与系统协同设计技术。
- **多模态对齐与偏好优化**：覆盖多模态特征定量映射、指令微调、DPO/RLHF偏好对齐及多目标业务价值协同优化，推动推荐系统向意图驱动演进。

### 关键方法与模型
- **TIGER / PLUM**：开创基于Semantic ID的生成式检索范式，结合持续预训练与领域适配，在YouTube等工业场景验证了长尾泛化与系统扩展性。
- **OneRec 系列（V1/V2/Think/Open）**：快手主导的端到端生成式推荐架构，演进至纯解码器惰性生成、显式文本推理与开源基座模型，实现检索排序统一。
- **FORGE / R3-VAE**：针对语义ID构建中的码本崩溃问题，提出参考向量锚定、残差量化与双指标正则化，提供高效的免训练质量评估代理指标。
- **HSTU / ULTRA-HSTU / Wukong**：通过相对位置偏置、线性复杂度注意力与纯FM堆叠架构，实证并“弯曲”了推荐领域的Scaling Law，实现算力效率跃升。
- **QARM / LEMUR**：多模态推荐对齐框架，引入定量适配层与记忆库机制，解决通用隐空间与推荐任务分布不匹配及长序列计算瓶颈。
- **OnePiece / OneTrans**：引入上下文工程与分块隐式推理，实现特征交互与序列建模的统一，显著降低工业部署延迟并提升长程依赖建模能力。
- **HiGR / MBGR / GR4AD**：面向列表推荐、超级App多业务场景与广告系统的生成式模型，通过层次规划、业务感知SID与动态路由实现多目标解耦。

### 工业实践与案例
- 知识库深度收录了全球头部互联网企业的落地经验，涵盖快手（OneRec/QARM全量上线）、淘宝（RecGPT/FORGE十亿级商品目录）、腾讯（HiGR/GRAB广告与内容推荐）、美团（MBGR外卖多业务解耦）、京东（OCP嵌入优化）、字节跳动（LONGER/RankMixer/LEMUR长序列与多模态）、Google/YouTube（TIGER/PLUM/Hiformer）及Pinterest/Shopee等。
- 实践聚焦真实业务指标提升（CTR/CVR/GMV显著增长）、毫秒级推理延迟控制、长序列/冷启动场景突破，以及生成式范式在召回、排序、重排全链路的规模化部署验证，标志着LLM4Rec从“架构移植”向“底层机制借鉴”的范式成熟。

### 研究前沿与开放问题
- **语义ID的泛化与记忆边界**：生成式模型在物品级泛化表象下易退化为Token级模式记忆，如何量化并融合GR与ID模型的互补优势仍是核心难点。
- **可解释推理与幻觉控制**：将LLM的显式思维链引入推荐决策虽提升可解释性，但面临推理延迟高、幻觉风险及与业务指标对齐的工程挑战。
- **多业务/多目标冲突解耦**：在超级App与广告场景中，全局统一词表易导致表征混淆，跨域语义隔离与动态价值路由机制仍需深化。
- **标准化评估与开源生态**：当前GR/SID研究在建模协议、超参配置上差异显著，缺乏统一的开源基准平台与免训练评估体系，制约研究迭代效率。

### 未来建议的知识摄入方向
- **标准化基准与评测协议**：优先摄入涵盖多场景、多模态、长序列的统一评测数据集（如扩展RecIF-Bench、TencentGR系列）及标准化消融实验报告，填补GRID指出的基准空白。
- **安全、鲁棒性与幻觉缓解**：补充推荐大模型在对抗攻击、分布外泛化、事实一致性校验及幻觉抑制方面的最新理论与工程实践，回应综述中明确指出的鲁棒性瓶颈。
- **交互式与Agent化推荐**：增加多轮对话推荐、用户意图主动挖掘、智能体规划（Agent Planning）及人机协同反馈机制的前沿研究，推动系统从“隐式匹配”向“智能交互助手”演进。
- **高效推理与系统协同优化**：关注模型压缩、量化、端云协同推理及低功耗硬件适配技术，结合现有LONGER/RankMixer等硬件感知设计，支撑LLM4Rec在资源受限场景的普惠化落地。

## 快速开始
### 0. 创建独立环境
```bash
python -m venv venv_llm4rec_wiki
source venv_llm4rec_wiki/bin/activate
```

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API 密钥

```bash
# 获取你的密钥：https://bailian.console.aliyun.com/
export DASHSCOPE_API_KEY="sk-your-api-key-here or code-plan-api-key"
```

### 3. 使用 CLI

```bash
# 从 URL 抓取网页(Arxiv论文)并自动分析（推荐）
python tools/llm_wiki.py fetch "https://arxiv.org/abs/2307.06435"

# 导入新的源文档, 可以把网络上的碎片文档复制过来
python tools/llm_wiki.py ingest raw/sources/my_source.md


# 仅保存网页内容，不自动分析
python tools/llm_wiki.py fetch "https://example.com/article" --no-ingest

# 基于知识库，查询 wiki
python tools/llm_wiki.py query "生成式推荐和判别式推荐的本质区别？"

# 健康检查 wiki
python tools/llm_wiki.py lint

# 汇总当前 wiki 状态，并利用LLM生成Summary，并更新到README.md的Summary模块
python tools/llm_wiki.py summarize
```

## 项目结构

```
LLM4REC_wiki/
├── AGENTS.md              # Schema：规范与工作流
├── wiki/
│   ├── README.md          # Wiki 概览
│   ├── index.md           # 内容目录
│   ├── log.md             # 操作日志
│   ├── concepts/          # 核心理论
│   ├── methods/           # 算法
│   ├── models/            # 模型架构
│   ├── entities/          # 人物、数据集、平台
│   ├── synthesis/         # 跨主题分析
│   └── sources/           # 每个来源的摘要
├── raw/
│   ├── sources/           # 不可变的源文档
│   └── assets/            # 本地图片、图表
├── tools/
│   └── llm_wiki.py        # 集成百炼的 CLI 工具
├── scripts/               # 实用脚本
└── requirements.txt       # Python 依赖
```

## 当前内容

该 wiki 目前包含 **160 个页面**，涵盖：

### Concepts（28 页）
- [concepts/model_flops_utilization_mfu.md](wiki/concepts/model_flops_utilization_mfu.md)
- [concepts/slate_recommendation.md](wiki/concepts/slate_recommendation.md)
- [concepts/all_modality_gr.md](wiki/concepts/all_modality_gr.md)
- [concepts/hierarchical_planning_rec.md](wiki/concepts/hierarchical_planning_rec.md)
- [concepts/context_engineering_rec.md](wiki/concepts/context_engineering_rec.md)
- [concepts/llm4rec_overview.md](wiki/concepts/llm4rec_overview.md)
- [concepts/scaling_laws_recsys.md](wiki/concepts/scaling_laws_recsys.md)
- [concepts/continued_pretraining.md](wiki/concepts/continued_pretraining.md)
- [concepts/session_wise_generation.md](wiki/concepts/session_wise_generation.md)
- [concepts/representation_alignment.md](wiki/concepts/representation_alignment.md)
- [concepts/generative_retrieval.md](wiki/concepts/generative_retrieval.md)
- [concepts/evaluation_llm4rec.md](wiki/concepts/evaluation_llm4rec.md)
- [concepts/llm_alignment_and_optimization.md](wiki/concepts/llm_alignment_and_optimization.md)
- [concepts/prompt_engineering_rec.md](wiki/concepts/prompt_engineering_rec.md)
- [concepts/multimodal_recommendation.md](wiki/concepts/multimodal_recommendation.md)
- [concepts/heterogeneous_feature_interaction.md](wiki/concepts/heterogeneous_feature_interaction.md)
- [concepts/unified_transformer_backbone.md](wiki/concepts/unified_transformer_backbone.md)
- [concepts/collaborative_filtering.md](wiki/concepts/collaborative_filtering.md)
- [concepts/gsu_esu_paradigm.md](wiki/concepts/gsu_esu_paradigm.md)
- [concepts/semantic_id.md](wiki/concepts/semantic_id.md)
- [concepts/sequential_recommendation.md](wiki/concepts/sequential_recommendation.md)
- [concepts/intent_driven_recommendation.md](wiki/concepts/intent_driven_recommendation.md)
- [concepts/knowledge_enhanced_rec.md](wiki/concepts/knowledge_enhanced_rec.md)
- [concepts/memorization_vs_generalization.md](wiki/concepts/memorization_vs_generalization.md)
- [concepts/hybrid_generative_recommendation.md](wiki/concepts/hybrid_generative_recommendation.md)
- [concepts/recif_bench.md](wiki/concepts/recif_bench.md)
- [concepts/explicit_reasoning_rec.md](wiki/concepts/explicit_reasoning_rec.md)
- [concepts/end_to_end_multimodal_training.md](wiki/concepts/end_to_end_multimodal_training.md)

### Methods（24 页）
- [methods/orthogonal_constrained_projection.md](wiki/methods/orthogonal_constrained_projection.md)
- [methods/quantitative_alignment.md](wiki/methods/quantitative_alignment.md)
- [methods/representation_alignment.md](wiki/methods/representation_alignment.md)
- [methods/synergistic_upscaling.md](wiki/methods/synergistic_upscaling.md)
- [methods/ua_sid.md](wiki/methods/ua_sid.md)
- [methods/adaptive_fusion_gr_id.md](wiki/methods/adaptive_fusion_gr_id.md)
- [methods/multi_objective_alignment.md](wiki/methods/multi_objective_alignment.md)
- [methods/iterative_preference_alignment.md](wiki/methods/iterative_preference_alignment.md)
- [methods/rspo.md](wiki/methods/rspo.md)
- [methods/weighted_evaluation.md](wiki/methods/weighted_evaluation.md)
- [methods/reward_modeling_rec.md](wiki/methods/reward_modeling_rec.md)
- [methods/two_stage_training_rec.md](wiki/methods/two_stage_training_rec.md)
- [methods/rag_for_recsys.md](wiki/methods/rag_for_recsys.md)
- [methods/prompt_finetuning.md](wiki/methods/prompt_finetuning.md)
- [methods/llm_as_generator.md](wiki/methods/llm_as_generator.md)
- [methods/memory_bank_sequential_rep.md](wiki/methods/memory_bank_sequential_rep.md)
- [methods/human_llm_collaborative_evaluation.md](wiki/methods/human_llm_collaborative_evaluation.md)
- [methods/actionpiece_tokenization.md](wiki/methods/actionpiece_tokenization.md)
- [methods/lazy_ar.md](wiki/methods/lazy_ar.md)
- [methods/hybrid_generative_recommendation.md](wiki/methods/hybrid_generative_recommendation.md)
- [methods/sparse_attention_seq_rec.md](wiki/methods/sparse_attention_seq_rec.md)
- [methods/cama_attention.md](wiki/methods/cama_attention.md)
- [methods/llm_as_ranker.md](wiki/methods/llm_as_ranker.md)
- [methods/long_context_efficiency.md](wiki/methods/long_context_efficiency.md)

### Models（29 页）
- [models/2509_paper_25092090_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md](wiki/models/2509_paper_25092090_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md)
- [models/LEMUR.md](wiki/models/LEMUR.md)
- [models/OneRec.md](wiki/models/OneRec.md)
- [models/RecGPT.md](wiki/models/RecGPT.md)
- [models/LLMRank.md](wiki/models/LLMRank.md)
- [models/RankMixer.md](wiki/models/RankMixer.md)
- [models/P5.md](wiki/models/P5.md)
- [models/TIGER.md](wiki/models/TIGER.md)
- [models/InstructRec.md](wiki/models/InstructRec.md)
- [models/ULTRA_HSTU.md](wiki/models/ULTRA_HSTU.md)
- [models/SASRec.md](wiki/models/SASRec.md)
- [models/DHEN.md](wiki/models/DHEN.md)
- [models/LONGER.md](wiki/models/LONGER.md)
- [models/TALLRec.md](wiki/models/TALLRec.md)
- [models/HiGR.md](wiki/models/HiGR.md)
- [models/OneRec-Think.md](wiki/models/OneRec-Think.md)
- [models/Wukong.md](wiki/models/Wukong.md)
- [models/Hiformer.md](wiki/models/Hiformer.md)
- [models/PLUM.md](wiki/models/PLUM.md)
- [models/OnePiece.md](wiki/models/OnePiece.md)
- [models/qwen_series.md](wiki/models/qwen_series.md)
- [models/GRID.md](wiki/models/GRID.md)
- [models/HSTU.md](wiki/models/HSTU.md)
- [models/OneRec-V2.md](wiki/models/OneRec-V2.md)
- [models/ULTRA-HSTU.md](wiki/models/ULTRA-HSTU.md)
- [models/MBGR.md](wiki/models/MBGR.md)
- [models/GR4AD.md](wiki/models/GR4AD.md)
- [models/test_generative_rec_model.md](wiki/models/test_generative_rec_model.md)
- [models/QARM.md](wiki/models/QARM.md)

### Entities（16 页）
- [entities/movielens.md](wiki/entities/movielens.md)
- [entities/tencent.md](wiki/entities/tencent.md)
- [entities/baidu.md](wiki/entities/baidu.md)
- [entities/guorui_zhou.md](wiki/entities/guorui_zhou.md)
- [entities/shopee.md](wiki/entities/shopee.md)
- [entities/google_youtube.md](wiki/entities/google_youtube.md)
- [entities/jd.md](wiki/entities/jd.md)
- [entities/amazon_reviews.md](wiki/entities/amazon_reviews.md)
- [entities/pinterest.md](wiki/entities/pinterest.md)
- [entities/taac.md](wiki/entities/taac.md)
- [entities/kuaishou.md](wiki/entities/kuaishou.md)
- [entities/taobao.md](wiki/entities/taobao.md)
- [entities/meta.md](wiki/entities/meta.md)
- [entities/meituan.md](wiki/entities/meituan.md)
- [entities/bytedance.md](wiki/entities/bytedance.md)
- [entities/tencentgr_dataset.md](wiki/entities/tencentgr_dataset.md)

### Synthesis（3 页）
- [synthesis/traditional_vs_llm.md](wiki/synthesis/traditional_vs_llm.md)
- [synthesis/llm4rec_taxonomy.md](wiki/synthesis/llm4rec_taxonomy.md)
- [synthesis/lint_report_2026-04-08.md](wiki/synthesis/lint_report_2026-04-08.md)

### Sources（60 页）
- [sources/2603_paper_26031980_How_Well_Does_Generative_Recommendation_Generalize.md](wiki/sources/2603_paper_26031980_How_Well_Does_Generative_Recommendation_Generalize.md)
- [sources/2510_paper_25102610_OneTrans_Unified_Feature_Interaction_and_Sequence_Modeling.md](wiki/sources/2510_paper_25102610_OneTrans_Unified_Feature_Interaction_and_Sequence_Modeling.md)
- [sources/2507_paper_25072222_Generative_Recommendation_with_Semantic_IDs_A_Practitioner'.md](wiki/sources/2507_paper_25072222_Generative_Recommendation_with_Semantic_IDs_A_Practitioner'.md)
- [sources/2509_paper_25092090_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md](wiki/sources/2509_paper_25092090_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md)
- [sources/2604_paper_26041144_R3-VAE_Reference_Vector-Guided_Rating_Residual_Quantization.md](wiki/sources/2604_paper_26041144_R3-VAE_Reference_Vector-Guided_Rating_Residual_Quantization.md)
- [sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md](wiki/sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md)
- [sources/2403_paper_24030254_Wukong_Towards_a_Scaling_Law_for_Large-Scale_Recommendation.md](wiki/sources/2403_paper_24030254_Wukong_Towards_a_Scaling_Law_for_Large-Scale_Recommendation.md)
- [sources/paper_c4a451_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md](wiki/sources/paper_c4a451_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md)
- [sources/2601_paper_26011268_HyFormer_Revisiting_the_Roles_of_Sequence_Modeling_and_Feat.md](wiki/sources/2601_paper_26011268_HyFormer_Revisiting_the_Roles_of_Sequence_Modeling_and_Feat.md)
- [sources/2411_paper_24111173_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md](wiki/sources/2411_paper_24111173_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md)
- [sources/2603_paper_26031869_OCP_Orthogonal_Constrained_Projection_for_Sparse_Scaling_in.md](wiki/sources/2603_paper_26031869_OCP_Orthogonal_Constrained_Projection_for_Sparse_Scaling_in.md)
- [sources/2407_paper_24072148_Breaking_the_Hourglass_Phenomenon_of_Residual_Quantization.md](wiki/sources/2407_paper_24072148_Breaking_the_Hourglass_Phenomenon_of_Residual_Quantization.md)
- [sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md](wiki/sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md)
- [sources/paper_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation.md](wiki/sources/paper_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation.md)
- [sources/2508_paper_25082090_OneRec-V2_Technical_Report.md](wiki/sources/2508_paper_25082090_OneRec-V2_Technical_Report.md)
- [sources/2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md](wiki/sources/2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md)
- [sources/paper_ad0dff_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md](wiki/sources/paper_ad0dff_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md)
- [sources/2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md](wiki/sources/2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md)
- [sources/2512_paper_25122238_OxygenREC_An_Instruction-Following_Generative_Framework_for.md](wiki/sources/2512_paper_25122238_OxygenREC_An_Instruction-Following_Generative_Framework_for.md)
- [sources/2511_paper_25111096_LEMUR_Large_scale_End-to-end_MUltimodal_Recommendation.md](wiki/sources/2511_paper_25111096_LEMUR_Large_scale_End-to-end_MUltimodal_Recommendation.md)
- [sources/2512_paper_25121450_RecGPT-V2_Technical_Report.md](wiki/sources/2512_paper_25121450_RecGPT-V2_Technical_Report.md)
- [sources/2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md](wiki/sources/2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md)
- [sources/2509_paper_25091809_OnePiece_Bringing_Context_Engineering_and_Reasoning_to_Indu.md](wiki/sources/2509_paper_25091809_OnePiece_Bringing_Context_Engineering_and_Reasoning_to_Indu.md)
- [sources/2205_paper_22050450_PinnerFormer_Sequence_Modeling_for_User_Representation_at_P.md](wiki/sources/2205_paper_22050450_PinnerFormer_Sequence_Modeling_for_User_Representation_at_P.md)
- [sources/2510_paper_25101163_OneRec-Think_In-Text_Reasoning_for_Generative_Recommendatio.md](wiki/sources/2510_paper_25101163_OneRec-Think_In-Text_Reasoning_for_Generative_Recommendatio.md)
- [sources/2512_paper_25122476_OpenOneRec_Technical_Report.md](wiki/sources/2512_paper_25122476_OpenOneRec_Technical_Report.md)
- [sources/2507_paper_25072287_RecGPT_Technical_Report.md](wiki/sources/2507_paper_25072287_RecGPT_Technical_Report.md)
- [sources/2206_paper_22060735_Rethinking_Reinforcement_Learning_for_Recommendation_A_Prom.md](wiki/sources/2206_paper_22060735_Rethinking_Reinforcement_Learning_for_Recommendation_A_Prom.md)
- [sources/2408_paper_24080458_FORGE_Force-Guided_Exploration_for_Robust_Contact-Rich_Mani.md](wiki/sources/2408_paper_24080458_FORGE_Force-Guided_Exploration_for_Robust_Contact-Rich_Mani.md)
- [sources/2311_paper_23110588_Hiformer_Heterogeneous_Feature_Interactions_Learning_with_T.md](wiki/sources/2311_paper_23110588_Hiformer_Heterogeneous_Feature_Interactions_Learning_with_T.md)
- [sources/2602_paper_26021001_Kunlun_Establishing_Scaling_Laws_for_Massive-Scale_Recommen.md](wiki/sources/2602_paper_26021001_Kunlun_Establishing_Scaling_Laws_for_Massive-Scale_Recommen.md)
- [sources/paper_8edbf8_HiGR_Efficient_Generative_Slate_Recommendation_via_Hierarch.md](wiki/sources/paper_8edbf8_HiGR_Efficient_Generative_Slate_Recommendation_via_Hierarch.md)
- [sources/2602_paper_26020186_GRAB_An_LLM-Inspired_Sequence-First_Click-Through_Rate_Pred.md](wiki/sources/2602_paper_26020186_GRAB_An_LLM-Inspired_Sequence-First_Click-Through_Rate_Pred.md)
- [sources/2604_paper_26040497_Tencent_Advertising_Algorithm_Challenge_2025_All-Modality_G.md](wiki/sources/2604_paper_26040497_Tencent_Advertising_Algorithm_Challenge_2025_All-Modality_G.md)
- [sources/test_generative_rec.md](wiki/sources/test_generative_rec.md)
- [sources/2502_paper_25021358_ActionPiece_Contextually_Tokenizing_Action_Sequences_for_Ge.md](wiki/sources/2502_paper_25021358_ActionPiece_Contextually_Tokenizing_Action_Sequences_for_Ge.md)
- [sources/2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md](wiki/sources/2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md)
- [sources/2203_paper_22031101_DHEN_A_Deep_and_Hierarchical_Ensemble_Network_for_Large-Sca.md](wiki/sources/2203_paper_22031101_DHEN_A_Deep_and_Hierarchical_Ensemble_Network_for_Large-Sca.md)
- [sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](wiki/sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)
- [sources/1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md](wiki/sources/1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md)
- [sources/2205_paper_22051413_FlashAttention_Fast_and_Memory-Efficient_Exact_Attention_wi.md](wiki/sources/2205_paper_22051413_FlashAttention_Fast_and_Memory-Efficient_Exact_Attention_wi.md)
- [sources/paper_1b102d_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md](wiki/sources/paper_1b102d_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md)
- [sources/2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md](wiki/sources/2306_paper_23060812_Better_Generalization_with_Semantic_IDs_A_Case_Study_in_Ran.md)
- [sources/2510_paper_25102127_Pctx_Tokenizing_Personalized_Context_for_Generative_Recomme.md](wiki/sources/2510_paper_25102127_Pctx_Tokenizing_Personalized_Context_for_Generative_Recomme.md)
- [sources/rankmixer_to_oneranker.md](wiki/sources/rankmixer_to_oneranker.md)
- [sources/2006_paper_20060577_Self-Supervised_Reinforcement_Learning_for_Recommender_Syste.md](wiki/sources/2006_paper_20060577_Self-Supervised_Reinforcement_Learning_for_Recommender_Syste.md)
- [sources/2511_paper_25110607_Make_It_Long,_Keep_It_Fast_End-to-End_10k-Sequence_Modeling.md](wiki/sources/2511_paper_25110607_Make_It_Long,_Keep_It_Fast_End-to-End_10k-Sequence_Modeling.md)
- [sources/2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md](wiki/sources/2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md)
- [sources/2411_paper_24111881_Unifying_Generative_and_Dense_Retrieval_for_Sequential_Recom.md](wiki/sources/2411_paper_24111881_Unifying_Generative_and_Dense_Retrieval_for_Sequential_Recom.md)
- [sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md](wiki/sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md)
- [sources/2404_paper_24040057_A_Review_of_Modern_Recommender_Systems_Using_Generative_Mode.md](wiki/sources/2404_paper_24040057_A_Review_of_Modern_Recommender_Systems_Using_Generative_Mode.md)
- [sources/2511_paper_25111013_GPR_Towards_a_Generative_Pre-trained_One-Model_Paradigm_for.md](wiki/sources/2511_paper_25111013_GPR_Towards_a_Generative_Pre-trained_One-Model_Paradigm_for.md)
- [sources/2502_paper_25021647_Unified_Semantic_and_ID_Representation_Learning_for_Deep_Rec.md](wiki/sources/2502_paper_25021647_Unified_Semantic_and_ID_Representation_Learning_for_Deep_Rec.md)
- [sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md](wiki/sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md)
- [sources/2604_paper_26041373_TokenFormer_Unify_the_Multi-Field_and_Sequential_Recommenda.md](wiki/sources/2604_paper_26041373_TokenFormer_Unify_the_Multi-Field_and_Sequential_Recommenda.md)
- [sources/2507_paper_25071555_RankMixer_Scaling_Up_Ranking_Models_in_Industrial_Recommend.md](wiki/sources/2507_paper_25071555_RankMixer_Scaling_Up_Ranking_Models_in_Industrial_Recommend.md)
- [sources/paper_2305_05065_Generative_Retrieval_RecSys.md](wiki/sources/paper_2305_05065_Generative_Retrieval_RecSys.md)
- [sources/2602_paper_26020855_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md](wiki/sources/2602_paper_26020855_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md)
- [sources/paper_c33d89_Farewell_to_Item_IDs_Unlocking_the_Scaling_Potential_of_Lar.md](wiki/sources/paper_c33d89_Farewell_to_Item_IDs_Unlocking_the_Scaling_Potential_of_Lar.md)
- [sources/2504_paper_25041050_PinRec_Outcome-Conditioned,_Multi-Token_Generative_Retrieva.md](wiki/sources/2504_paper_25041050_PinRec_Outcome-Conditioned,_Multi-Token_Generative_Retrieva.md)

## 设计理念

基于 [Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)：

> "Wiki 是一个持久化、持续累积的产物。交叉引用已经存在。矛盾之处已经被标记。综合内容已经反映了你阅读过的所有内容。"

### 三个层次
1. **源文档（Raw Sources）** — 不可变的输入文档
2. **Wiki** — LLM 生成的、相互链接的 Markdown 文件
3. **Schema** — 给 LLM 的指令（AGENTS.md）

### 三项操作
1. **Ingest（导入）** — 添加源文档 → LLM 更新 wiki
2. **Query（查询）** — 提出问题 → LLM 从 wiki 中综合生成答案
3. **Lint（检查）** — 健康检查 → LLM 发现矛盾、空白和孤立页面

## LLM 后端

- **平台**：阿里云百炼（Alibaba Cloud Bailian）
- **API 类型**：OpenAI 兼容 SDK（同时支持标准密钥和 Coding Plan 密钥）
- **Coding Plan 密钥**（`sk-sp-*`）：`qwen3.5-plus`（默认）、`qwen3-coder-plus`、`kimi-k2.5`、`glm-5`
- **标准密钥**（`sk-*`）：`qwen-max`（默认）、`qwen-plus`、`qwen-turbo`
- **自动检测**：CLI 会自动检测你的密钥类型并配置正确的端点

## 添加新源文档

### 方式 A：从 URL 抓取（推荐）
```bash
# 自动：抓取 → 保存 → 分析 → 更新知识库
python tools/llm_wiki.py fetch "https://arxiv.org/abs/2307.06435"

# 仅保存源文件，不自动分析
python tools/llm_wiki.py fetch "https://example.com/article" --no-ingest
```

### 方式 B：手动添加本地文件
1. 将源文件放置于 `raw/sources/`
2. 运行：`python tools/llm_wiki.py ingest raw/sources/your_file.md`
3. 审查建议的 wiki 变更
4. 确认应用变更

## 环境变量

| 变量 | 说明 | 默认值 |
|----------|-------------|---------|
| `DASHSCOPE_API_KEY` | 你的百炼 API 密钥 | （必填） |
| `BAILIAN_MODEL` | 主模型名称 | `qwen-max` |
| `WIKI_AUTO_CONFIRM` | 自动应用 wiki 变更 | `false` |

## 许可证

本知识库用于研究和教育目的。

## 致谢

- Karpathy 提出的 LLM Wiki 模式
- 阿里云百炼提供的 LLM 基础设施
- LLM4Rec 研究社区
