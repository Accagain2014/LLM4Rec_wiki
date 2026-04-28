# LLM4Rec Wiki

> 一个持久化、持续累积的知识库，专注于**大语言模型在推荐系统的应用 (LLM4Rec)**，基于 [karpathy/llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 模式构建，由Qwen Code调用qwen3.6-plus实现，使用阿里百炼Code Plan.

## 概述

本项目实现了一个由 LLM 维护的领域知识库，聚焦于**大语言模型在推荐系统的应用 (LLM4Rec)**。与传统的 RAG（每次查询都重新推导知识）不同，该 wiki **逐步构建并维护**一个结构化的、相互链接的知识库，随着时间推移不断累积。


## Summary

### 知识库统计
- 总页面数：168
- 各类别页面数量分布：entities (16), summary (6), models (29), sources (61), concepts (28), methods (25), synthesis (3)

### 核心覆盖领域
1. **生成式推荐与语义ID（Semantic ID）**：系统记录从传统双塔+ANN检索向自回归生成离散标识符的范式转变，涵盖SID构建、码本优化与免训练代理评估。
2. **缩放定律与长序列建模**：聚焦推荐系统中算力-性能的幂律关系实证，以及针对超长用户行为序列的线性注意力、稀疏化与硬件感知优化。
3. **端到端统一架构**：打破传统“召回-排序-重排”多阶段流水线，探索检索与排序统一、多任务协同的单一Transformer骨干网络。
4. **多模态对齐与指令微调**：涵盖多模态特征的定量映射、参数高效微调（LoRA）及基于指令/提示的个性化推荐与对话式交互。
5. **工业系统协同设计**：强调模型架构与底层算力（GPU显存、KV缓存、算子融合、请求级批处理）的深度结合，以满足毫秒级延迟与高QPS的线上SLA。

### 关键方法与模型
1. **TIGER / PLUM / GRID**：奠定基于语义ID的生成式检索基础，提供开源模块化框架与工业级预训练LLM适配方案。
2. **OneRec 系列（V1/V2/Think）**：快手提出的端到端统一架构，演进至惰性纯解码器与文内显式推理，显著降低计算开销并强化偏好对齐。
3. **HSTU / ULTRA-HSTU / Wukong**：通过相对位置偏置、线性注意力与纯FM堆叠，实证并“弯曲”推荐缩放定律曲线，实现十亿级参数的高效扩展。
4. **HiGR / MBGR / GR4AD**：面向列表推荐、多业务场景与广告商业化的分层规划与动态路由生成模型，有效解耦多目标冲突与跨域表征混淆。
5. **QARM / LEMUR**：引入定量对齐适配层与增量记忆库机制，实现多模态特征与推荐任务空间的端到端联合优化与实时参数更新。
6. **P5 / InstructRec / TALLRec**：探索提示学习、指令微调与LoRA适配，赋予模型零样本/少样本泛化能力与跨领域低成本迁移路径。

### 工业实践与案例
知识库深度收录了头部互联网公司的全量部署经验：**快手**通过OneRec系列与QARM实现短视频主场景与广告系统的端到端生成与多模态对齐；**字节跳动**依托LONGER、RankMixer与LEMUR在十亿级数据上验证长序列扩展与硬件感知排序；**淘宝/阿里**利用FORGE与RecGPT解决十亿级商品目录的码本崩溃与意图驱动推荐；**腾讯、美团、百度、京东、Shopee及Google/YouTube/Meta**等均在各自核心业务中落地了生成式检索、缩放定律验证与统一架构，普遍实现CTR、CVR、GMV或用户停留时长的显著提升（如百度广告收入+3.05%，淘宝交易额+0.35%，美团外卖核心指标全面增长）。

### 研究前沿与开放问题
1. **语义ID的码本均衡与质量评估**：如何避免热门物品主导的“码本崩溃”，并建立无需全量训练即可精准预测SID质量的标准化代理指标。
2. **生成过程的显式推理与可控性**：当前模型多为隐式预测，如何引入思维链（CoT）与快慢思考架构，实现推荐逻辑的可解释与业务规则硬约束。
3. **缩放定律的效率瓶颈与延迟优化**：模型规模与序列长度增加带来的推理延迟与显存压力，亟需更高效的稀疏化、动态计算分配与懒自回归解码方案。
4. **多业务/广告场景的价值对齐**：生成式模型在复杂商业目标（出价、预算、转化）下的多目标优化冲突，以及长尾/冷启动物品的公平曝光与泛化机制。

### 未来建议的知识摄入方向
1. **标准化生成式推荐基准与评测体系**：补充涵盖幻觉控制、鲁棒性、跨域泛化与多目标权衡的统一开源Benchmark，弥补当前评估协议碎片化的问题。
2. **底层推理加速与部署工程指南**：系统摄入针对LLM4Rec的KV缓存优化、动态量化、服务级批处理（RLB）与边缘端轻量化部署的最佳实践。
3. **安全、公平与可解释性研究**：增加生成式推荐中的偏见消除、隐私保护、内容安全过滤及用户意图可追溯性的前沿论文与工业合规规范。
4. **开源可复现管线与高质量数据集**：优先收录类似OpenOneRec、TencentGR、ActionPiece的完整训练代码、数据处理流程与多模态交互数据集，降低研究复现门槛。

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

该 wiki 目前包含 **162 个页面**，涵盖：

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

### Methods（25 页）
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
- [methods/multi_epoch_learning.md](wiki/methods/multi_epoch_learning.md)
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

### Sources（61 页）
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
- [sources/2305_paper_23051953_Multi-Epoch_Learning_for_Deep_Click-Through_Rate_Prediction.md](wiki/sources/2305_paper_23051953_Multi-Epoch_Learning_for_Deep_Click-Through_Rate_Prediction.md)
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
