# LLM4Rec Wiki

> 一个持久化、持续累积的知识库，专注于**大语言模型在推荐系统的应用 (LLM4Rec)**，基于 [karpathy/llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 模式构建，由Qwen Code调用qwen3.6-plus实现，使用阿里百炼Code Plan.

## 概述

本项目实现了一个由 LLM 维护的领域知识库，聚焦于**大语言模型在推荐系统的应用 (LLM4Rec)**。与传统的 RAG（每次查询都重新推导知识）不同，该 wiki **逐步构建并维护**一个结构化的、相互链接的知识库，随着时间推移不断累积。


## Summary

### 知识库统计
- 总页面数：148
- 各类别页面数量分布：`entities` (13), `summary` (6), `models` (28), `sources` (50), `concepts` (27), `methods` (21), `synthesis` (3)

### 核心覆盖领域
1. **生成式检索与语义ID（Semantic ID）**：聚焦以自回归生成替代传统“双塔+ANN”范式，涵盖离散码本构建、量化分词与标识符优化。
2. **端到端统一推荐架构**：打破召回、排序、重排的多阶段流水线，探索单一生成式模型统一处理特征交互、序列建模与多任务预测。
3. **推荐系统扩展定律（Scaling Law）与硬件协同**：验证算力-性能幂律关系，研究稀疏注意力、MoE路由与底层算子优化以提升硬件效率（MFU）。
4. **多模态定量对齐与表征学习**：将通用LLM/多模态特征通过可微对齐层映射至CTR/CVR等业务目标空间，解决语义表征与下游任务脱节问题。
5. **工业级大规模部署与多目标优化**：覆盖头部互联网公司在超大规模流量下的模型训练、推理加速、动态路由与商业价值对齐实践。

### 关键方法与模型
1. **TIGER / PLUM (Google/YouTube)**：开创基于Semantic ID的生成式检索，结合领域持续预训练（CPT）实现数十亿用户规模的工业落地。
2. **OneRec 系列 (快手)**：从统一检索排序的端到端架构，演进至惰性纯解码器（V2）与显式文内推理（Think），大幅降低计算开销并增强可解释性。
3. **FORGE / R3-VAE (阿里/淘宝)**：提出力引导探索机制与参考向量残差量化，有效缓解码本崩溃，并首创免训练SID代理评估指标。
4. **ULTRA-HSTU / Wukong (Meta)**：通过线性化注意力与纯FM堆叠架构，首次在推荐领域实证并成功“弯曲”了Scaling Law曲线。
5. **RankMixer / LONGER (字节跳动)**：硬件感知的排序扩展模型与长序列优化Transformer，结合稀疏MoE与Token融合突破二次复杂度瓶颈。
6. **QARM / QARM V2 (快手)**：定量对齐多模态推荐框架，实现从离线特征增强到端到端业务原生范式的跨越。
7. **P5 / InstructRec / TALLRec**：基于指令微调与参数高效适配（LoRA）的通用LLM推荐基座，支持零样本/少样本迁移与对话式推荐。

### 工业实践与案例
知识库系统梳理了全球头部科技公司的LLM4Rec落地路径：**Google/YouTube** 依托PLUM与Hiformer实现生成式检索在生产环境的规模化服务；**快手** 将OneRec系列与QARM全量部署于短视频主场景与广告系统，验证了端到端生成与多目标对齐的商业收益；**字节跳动** 通过RankMixer与LONGER在万亿级数据上实现排序模型百倍参数扩展与万级长序列高效推理；**阿里/淘宝** 利用FORGE与RecGPT优化十亿级商品目录的语义ID分配与意图驱动推荐；**腾讯、美团、Pinterest** 等亦在列表推荐（HiGR）、多业务解耦（MBGR）与结果条件化生成（PinRec）方面取得显著线上指标提升。

### 研究前沿与开放问题
1. **生成式推荐的泛化与记忆边界**：研究表明GR模型在底层易退化为Token级模式记忆，如何有效平衡记忆型实例与真实泛化能力仍是核心挑战。
2. **语义ID的鲁棒构建与评估体系**：码本崩溃与长尾覆盖不均问题突出，需发展更稳定的量化算法与高置信度的免训练代理评估指标。
3. **显式推理与多目标价值对齐**：从隐式概率生成转向可控的链式推理，并解决商业目标（eCPM、预算消耗）与用户兴趣之间的奖励冲突。
4. **超长序列建模与算力效率的协同**：在保持毫秒级推理SLA的前提下，如何进一步突破$O(L^2)$复杂度并持续提升GPU MFU利用率。

### 未来建议的知识摄入方向
1. **标准化在线评估与安全可控机制**：优先摄入涵盖长期用户价值、公平性、隐私保护及幻觉检测的评测基准与对齐策略文献。
2. **LLM Agent与交互式推荐系统**：补充基于智能体规划、多轮对话反馈与动态环境交互的推荐架构研究，填补当前以静态生成为主的空白。
3. **生成式推荐底层服务优化**：深入摄入KV Cache管理、动态批处理、推测解码（Speculative Decoding）等推理加速与工程部署技术。
4. **跨域迁移与隐私计算下的LLM4Rec**：关注数据孤岛场景下的参数高效微调、知识蒸馏与跨业务/跨平台语义对齐方法，增强知识库的泛化覆盖度。

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

该 wiki 目前包含 **142 个页面**，涵盖：

### Concepts（27 页）
- [concepts/model_flops_utilization_mfu.md](wiki/concepts/model_flops_utilization_mfu.md)
- [concepts/slate_recommendation.md](wiki/concepts/slate_recommendation.md)
- [concepts/all_modality_gr.md](wiki/concepts/all_modality_gr.md)
- [concepts/hierarchical_planning_rec.md](wiki/concepts/hierarchical_planning_rec.md)
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

### Methods（21 页）
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
- [methods/sparse_attention_seq_rec.md](wiki/methods/sparse_attention_seq_rec.md)
- [methods/llm_as_ranker.md](wiki/methods/llm_as_ranker.md)
- [methods/long_context_efficiency.md](wiki/methods/long_context_efficiency.md)

### Models（28 页）
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
- [models/qwen_series.md](wiki/models/qwen_series.md)
- [models/GRID.md](wiki/models/GRID.md)
- [models/HSTU.md](wiki/models/HSTU.md)
- [models/OneRec-V2.md](wiki/models/OneRec-V2.md)
- [models/ULTRA-HSTU.md](wiki/models/ULTRA-HSTU.md)
- [models/MBGR.md](wiki/models/MBGR.md)
- [models/GR4AD.md](wiki/models/GR4AD.md)
- [models/test_generative_rec_model.md](wiki/models/test_generative_rec_model.md)
- [models/QARM.md](wiki/models/QARM.md)

### Entities（13 页）
- [entities/movielens.md](wiki/entities/movielens.md)
- [entities/tencent.md](wiki/entities/tencent.md)
- [entities/guorui_zhou.md](wiki/entities/guorui_zhou.md)
- [entities/google_youtube.md](wiki/entities/google_youtube.md)
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

### Sources（50 页）
- [sources/2603_paper_26031980_How_Well_Does_Generative_Recommendation_Generalize.md](wiki/sources/2603_paper_26031980_How_Well_Does_Generative_Recommendation_Generalize.md)
- [sources/2510_paper_25102610_OneTrans_Unified_Feature_Interaction_and_Sequence_Modeling.md](wiki/sources/2510_paper_25102610_OneTrans_Unified_Feature_Interaction_and_Sequence_Modeling.md)
- [sources/2507_paper_25072222_Generative_Recommendation_with_Semantic_IDs_A_Practitioner'.md](wiki/sources/2507_paper_25072222_Generative_Recommendation_with_Semantic_IDs_A_Practitioner'.md)
- [sources/2509_paper_25092090_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md](wiki/sources/2509_paper_25092090_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md)
- [sources/2604_paper_26041144_R3-VAE_Reference_Vector-Guided_Rating_Residual_Quantization.md](wiki/sources/2604_paper_26041144_R3-VAE_Reference_Vector-Guided_Rating_Residual_Quantization.md)
- [sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md](wiki/sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md)
- [sources/2403_paper_24030254_Wukong_Towards_a_Scaling_Law_for_Large-Scale_Recommendation.md](wiki/sources/2403_paper_24030254_Wukong_Towards_a_Scaling_Law_for_Large-Scale_Recommendation.md)
- [sources/paper_c4a451_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md](wiki/sources/paper_c4a451_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md)
- [sources/2411_paper_24111173_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md](wiki/sources/2411_paper_24111173_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md)
- [sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md](wiki/sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md)
- [sources/paper_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation.md](wiki/sources/paper_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation.md)
- [sources/2508_paper_25082090_OneRec-V2_Technical_Report.md](wiki/sources/2508_paper_25082090_OneRec-V2_Technical_Report.md)
- [sources/2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md](wiki/sources/2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md)
- [sources/paper_ad0dff_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md](wiki/sources/paper_ad0dff_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md)
- [sources/2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md](wiki/sources/2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md)
- [sources/2511_paper_25111096_LEMUR_Large_scale_End-to-end_MUltimodal_Recommendation.md](wiki/sources/2511_paper_25111096_LEMUR_Large_scale_End-to-end_MUltimodal_Recommendation.md)
- [sources/2512_paper_25121450_RecGPT-V2_Technical_Report.md](wiki/sources/2512_paper_25121450_RecGPT-V2_Technical_Report.md)
- [sources/2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md](wiki/sources/2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md)
- [sources/2510_paper_25101163_OneRec-Think_In-Text_Reasoning_for_Generative_Recommendatio.md](wiki/sources/2510_paper_25101163_OneRec-Think_In-Text_Reasoning_for_Generative_Recommendatio.md)
- [sources/2512_paper_25122476_OpenOneRec_Technical_Report.md](wiki/sources/2512_paper_25122476_OpenOneRec_Technical_Report.md)
- [sources/2507_paper_25072287_RecGPT_Technical_Report.md](wiki/sources/2507_paper_25072287_RecGPT_Technical_Report.md)
- [sources/2206_paper_22060735_Rethinking_Reinforcement_Learning_for_Recommendation_A_Prom.md](wiki/sources/2206_paper_22060735_Rethinking_Reinforcement_Learning_for_Recommendation_A_Prom.md)
- [sources/2408_paper_24080458_FORGE_Force-Guided_Exploration_for_Robust_Contact-Rich_Mani.md](wiki/sources/2408_paper_24080458_FORGE_Force-Guided_Exploration_for_Robust_Contact-Rich_Mani.md)
- [sources/2311_paper_23110588_Hiformer_Heterogeneous_Feature_Interactions_Learning_with_T.md](wiki/sources/2311_paper_23110588_Hiformer_Heterogeneous_Feature_Interactions_Learning_with_T.md)
- [sources/2602_paper_26021001_Kunlun_Establishing_Scaling_Laws_for_Massive-Scale_Recommen.md](wiki/sources/2602_paper_26021001_Kunlun_Establishing_Scaling_Laws_for_Massive-Scale_Recommen.md)
- [sources/paper_8edbf8_HiGR_Efficient_Generative_Slate_Recommendation_via_Hierarch.md](wiki/sources/paper_8edbf8_HiGR_Efficient_Generative_Slate_Recommendation_via_Hierarch.md)
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
- [sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md](wiki/sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md)
- [sources/2404_paper_24040057_A_Review_of_Modern_Recommender_Systems_Using_Generative_Mode.md](wiki/sources/2404_paper_24040057_A_Review_of_Modern_Recommender_Systems_Using_Generative_Mode.md)
- [sources/2511_paper_25111013_GPR_Towards_a_Generative_Pre-trained_One-Model_Paradigm_for.md](wiki/sources/2511_paper_25111013_GPR_Towards_a_Generative_Pre-trained_One-Model_Paradigm_for.md)
- [sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md](wiki/sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md)
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
