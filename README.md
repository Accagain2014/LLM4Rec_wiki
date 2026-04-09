# LLM4Rec Wiki

> 一个持久化、持续累积的知识库，专注于**大语言模型在推荐系统的应用 (LLM4Rec)**，基于 [karpathy/llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 模式构建，由Qwen Code调用qwen3.6-plus实现，使用阿里百炼Code Plan.

## 概述

本项目实现了一个由 LLM 维护的领域知识库，聚焦于**大语言模型在推荐系统的应用 (LLM4Rec)**。与传统的 RAG（每次查询都重新推导知识）不同，该 wiki **逐步构建并维护**一个结构化的、相互链接的知识库，随着时间推移不断累积。


## Summary

### 知识库统计
- **总页面数**：118
- **各类别页面数量分布**：
  - 来源文献 (sources)：32
  - 概念理论 (concepts)：26
  - 模型架构 (models)：23
  - 方法技术 (methods)：20
  - 实体机构 (entities)：10
  - 综合总结 (synthesis)：3
  - 摘要记录 (summary)：4

### 核心覆盖领域
- **生成式检索范式**：涵盖从传统嵌入检索向基于 Semantic ID 的自回归生成式检索（Generative Retrieval）的范式转变。
- **工业级扩展与效率**：聚焦推荐系统中的 Scaling Laws、长序列建模及硬件感知的高效架构设计。
- **多模态与意图对齐**：研究多模态内容理解、用户意图驱动推荐及表示与业务目标的定量对齐技术。
- **统一架构设计**：探索检索与排序的统一建模（Unified Architecture），打破传统多阶段流水线局限。
- **评估与基准体系**：建立针对 LLM4Rec 的综合评估基准（如 RecIF-Bench）及免训练代理指标。

### 关键方法与模型
- **OneRec 系列 (快手)**：端到端生成式推荐模型，统一检索与排序，引入显式推理 (OneRec-Think) 及惰性解码架构 (V2)。
- **PLUM (Google/YouTube)**：面向工业规模的预训练 LLM 适配框架，结合 Semantic ID 实现生成式检索落地。
- **TIGER/GRID**：基于 Semantic ID 的生成式检索基础模型与开源模块化框架，确立神经检索新标准。
- **RankMixer/LONGER (字节)**：硬件感知的可扩展排序模型与长序列优化 Transformer，解决工业延迟与计算瓶颈。
- **RecGPT (淘宝)**：意图驱动的生成式推荐模型，全量上线验证了 LLM 在超大规模电商场景的有效性。
- **Wukong/ULTRA-HSTU**：验证推荐系统中的 Scaling Laws，通过协同扩展策略与系统协同设计弯曲性能曲线。
- **QARM (快手)**：多模态推荐中的定量对齐框架，解决表示与业务目标不匹配及端到端学习难题。
- **HiGR (腾讯)**：基于层次化规划的高效生成式列表推荐，优化 Slate 级意图捕捉与多目标对齐。

### 工业实践与案例
- **快手**：OneRec 系列在主场景上线，验证生成式推荐进入主排序链路的可行性，显著提升观看时长。
- **字节跳动**：LONGER 与 RankMixer 实现长序列工业化与排序模型百倍参数扩展，保持低延迟高吞吐。
- **腾讯**：HiGR 在商业平台部署服务数亿用户，广告算法挑战赛推动全模态生成式推荐基准建设。
- **Google/YouTube**：PLUM 在生产环境服务数十亿用户，检索精度与长尾泛化显著超越传统嵌入表模型。
- **阿里巴巴/淘宝**：RecGPT 全量上线提升转化率，FORGE 框架指导 Semantic ID 优化实现交易额增长。

### 研究前沿与开放问题
- **记忆与泛化边界**：生成式推荐模型在实例级泛化能力上是否存在退化为 Token 级模式记忆的风险。
- **显式推理机制**：如何在推荐过程中引入可控的显式推理链（Reasoning Chain）以提升可解释性与准确性。
- **高效评估代理**：如何在不训练完整模型的情况下，通过代理指标快速量化 Semantic ID 质量与推荐性能。
- **多模态端到端对齐**：解决多模态表示与下游推荐任务无法端到端联合优化及业务目标不匹配的问题。
- **扩展定律适用性**：推荐系统中的 Scaling Laws 是否在不同架构与数据规模下具有普适性与可预测性。

### 未来建议的知识摄入方向
- **方法细节补充**：当前部分“方法”与“实体”页面为自动生成且内容简略，需补充具体算法实现与工程细节。
- **负面结果与失败案例**：目前多为 SOTA 性能报告，建议摄入工业界落地中的失败尝试与局限性分析。
- **伦理与偏差研究**：知识库缺乏 LLM4Rec 中的公平性、隐私保护及算法偏差治理相关内容。
- **跨域对比研究**：增加不同公司技术路线（如阿里 vs 字节 vs 快手）的横向对比分析与适用场景总结。
- **实时推理优化**：补充关于生成式推荐在高并发场景下的具体推理优化技术（如 KV Cache 管理、量化部署）。

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API 密钥

```bash
# 获取你的密钥：https://bailian.console.aliyun.com/
export DASHSCOPE_API_KEY="sk-your-api-key-here"
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

该 wiki 目前包含 **114 个页面**，涵盖：

### Concepts（26 页）
- [concepts/model_flops_utilization_mfu.md](concepts/model_flops_utilization_mfu.md)
- [concepts/slate_recommendation.md](concepts/slate_recommendation.md)
- [concepts/all_modality_gr.md](concepts/all_modality_gr.md)
- [concepts/hierarchical_planning_rec.md](concepts/hierarchical_planning_rec.md)
- [concepts/llm4rec_overview.md](concepts/llm4rec_overview.md)
- [concepts/scaling_laws_recsys.md](concepts/scaling_laws_recsys.md)
- [concepts/continued_pretraining.md](concepts/continued_pretraining.md)
- [concepts/session_wise_generation.md](concepts/session_wise_generation.md)
- [concepts/representation_alignment.md](concepts/representation_alignment.md)
- [concepts/generative_retrieval.md](concepts/generative_retrieval.md)
- [concepts/evaluation_llm4rec.md](concepts/evaluation_llm4rec.md)
- [concepts/prompt_engineering_rec.md](concepts/prompt_engineering_rec.md)
- [concepts/multimodal_recommendation.md](concepts/multimodal_recommendation.md)
- [concepts/heterogeneous_feature_interaction.md](concepts/heterogeneous_feature_interaction.md)
- [concepts/unified_transformer_backbone.md](concepts/unified_transformer_backbone.md)
- [concepts/collaborative_filtering.md](concepts/collaborative_filtering.md)
- [concepts/gsu_esu_paradigm.md](concepts/gsu_esu_paradigm.md)
- [concepts/semantic_id.md](concepts/semantic_id.md)
- [concepts/sequential_recommendation.md](concepts/sequential_recommendation.md)
- [concepts/intent_driven_recommendation.md](concepts/intent_driven_recommendation.md)
- [concepts/knowledge_enhanced_rec.md](concepts/knowledge_enhanced_rec.md)
- [concepts/memorization_vs_generalization.md](concepts/memorization_vs_generalization.md)
- [concepts/hybrid_generative_recommendation.md](concepts/hybrid_generative_recommendation.md)
- [concepts/recif_bench.md](concepts/recif_bench.md)
- [concepts/explicit_reasoning_rec.md](concepts/explicit_reasoning_rec.md)
- [concepts/end_to_end_multimodal_training.md](concepts/end_to_end_multimodal_training.md)

### Methods（20 页）
- [methods/quantitative_alignment.md](methods/quantitative_alignment.md)
- [methods/representation_alignment.md](methods/representation_alignment.md)
- [methods/synergistic_upscaling.md](methods/synergistic_upscaling.md)
- [methods/ua_sid.md](methods/ua_sid.md)
- [methods/adaptive_fusion_gr_id.md](methods/adaptive_fusion_gr_id.md)
- [methods/multi_objective_alignment.md](methods/multi_objective_alignment.md)
- [methods/iterative_preference_alignment.md](methods/iterative_preference_alignment.md)
- [methods/rspo.md](methods/rspo.md)
- [methods/weighted_evaluation.md](methods/weighted_evaluation.md)
- [methods/reward_modeling_rec.md](methods/reward_modeling_rec.md)
- [methods/two_stage_training_rec.md](methods/two_stage_training_rec.md)
- [methods/rag_for_recsys.md](methods/rag_for_recsys.md)
- [methods/prompt_finetuning.md](methods/prompt_finetuning.md)
- [methods/llm_as_generator.md](methods/llm_as_generator.md)
- [methods/memory_bank_sequential_rep.md](methods/memory_bank_sequential_rep.md)
- [methods/human_llm_collaborative_evaluation.md](methods/human_llm_collaborative_evaluation.md)
- [methods/lazy_ar.md](methods/lazy_ar.md)
- [methods/sparse_attention_seq_rec.md](methods/sparse_attention_seq_rec.md)
- [methods/llm_as_ranker.md](methods/llm_as_ranker.md)
- [methods/long_context_efficiency.md](methods/long_context_efficiency.md)

### Models（23 页）
- [models/LEMUR.md](models/LEMUR.md)
- [models/OneRec.md](models/OneRec.md)
- [models/RecGPT.md](models/RecGPT.md)
- [models/LLMRank.md](models/LLMRank.md)
- [models/RankMixer.md](models/RankMixer.md)
- [models/P5.md](models/P5.md)
- [models/TIGER.md](models/TIGER.md)
- [models/InstructRec.md](models/InstructRec.md)
- [models/ULTRA_HSTU.md](models/ULTRA_HSTU.md)
- [models/DHEN.md](models/DHEN.md)
- [models/LONGER.md](models/LONGER.md)
- [models/TALLRec.md](models/TALLRec.md)
- [models/HiGR.md](models/HiGR.md)
- [models/OneRec-Think.md](models/OneRec-Think.md)
- [models/Wukong.md](models/Wukong.md)
- [models/Hiformer.md](models/Hiformer.md)
- [models/PLUM.md](models/PLUM.md)
- [models/qwen_series.md](models/qwen_series.md)
- [models/GRID.md](models/GRID.md)
- [models/OneRec-V2.md](models/OneRec-V2.md)
- [models/GR4AD.md](models/GR4AD.md)
- [models/test_generative_rec_model.md](models/test_generative_rec_model.md)
- [models/QARM.md](models/QARM.md)

### Entities（10 页）
- [entities/movielens.md](entities/movielens.md)
- [entities/tencent.md](entities/tencent.md)
- [entities/guorui_zhou.md](entities/guorui_zhou.md)
- [entities/google_youtube.md](entities/google_youtube.md)
- [entities/amazon_reviews.md](entities/amazon_reviews.md)
- [entities/taac.md](entities/taac.md)
- [entities/kuaishou.md](entities/kuaishou.md)
- [entities/taobao.md](entities/taobao.md)
- [entities/bytedance.md](entities/bytedance.md)
- [entities/tencentgr_dataset.md](entities/tencentgr_dataset.md)

### Synthesis（3 页）
- [synthesis/traditional_vs_llm.md](synthesis/traditional_vs_llm.md)
- [synthesis/llm4rec_taxonomy.md](synthesis/llm4rec_taxonomy.md)
- [synthesis/lint_report_2026-04-08.md](synthesis/lint_report_2026-04-08.md)

### Sources（32 页）
- [sources/2603_paper_26031980_How_Well_Does_Generative_Recommendation_Generalize.md](sources/2603_paper_26031980_How_Well_Does_Generative_Recommendation_Generalize.md)
- [sources/2510_paper_25102610_OneTrans_Unified_Feature_Interaction_and_Sequence_Modeling.md](sources/2510_paper_25102610_OneTrans_Unified_Feature_Interaction_and_Sequence_Modeling.md)
- [sources/2507_paper_25072222_Generative_Recommendation_with_Semantic_IDs_A_Practitioner'.md](sources/2507_paper_25072222_Generative_Recommendation_with_Semantic_IDs_A_Practitioner'.md)
- [sources/2509_paper_25092090_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md](sources/2509_paper_25092090_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md)
- [sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md](sources/paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md)
- [sources/2403_paper_24030254_Wukong_Towards_a_Scaling_Law_for_Large-Scale_Recommendation.md](sources/2403_paper_24030254_Wukong_Towards_a_Scaling_Law_for_Large-Scale_Recommendation.md)
- [sources/paper_c4a451_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md](sources/paper_c4a451_FORGE_Forming_Semantic_Identifiers_for_Generative_Retrieval.md)
- [sources/paper_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation.md](sources/paper_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation.md)
- [sources/2508_paper_25082090_OneRec-V2_Technical_Report.md](sources/2508_paper_25082090_OneRec-V2_Technical_Report.md)
- [sources/paper_ad0dff_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md](sources/paper_ad0dff_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md)
- [sources/2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md](sources/2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md)
- [sources/2511_paper_25111096_LEMUR_Large_scale_End-to-end_MUltimodal_Recommendation.md](sources/2511_paper_25111096_LEMUR_Large_scale_End-to-end_MUltimodal_Recommendation.md)
- [sources/2512_paper_25121450_RecGPT-V2_Technical_Report.md](sources/2512_paper_25121450_RecGPT-V2_Technical_Report.md)
- [sources/2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md](sources/2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md)
- [sources/2510_paper_25101163_OneRec-Think_In-Text_Reasoning_for_Generative_Recommendatio.md](sources/2510_paper_25101163_OneRec-Think_In-Text_Reasoning_for_Generative_Recommendatio.md)
- [sources/2512_paper_25122476_OpenOneRec_Technical_Report.md](sources/2512_paper_25122476_OpenOneRec_Technical_Report.md)
- [sources/2507_paper_25072287_RecGPT_Technical_Report.md](sources/2507_paper_25072287_RecGPT_Technical_Report.md)
- [sources/2311_paper_23110588_Hiformer_Heterogeneous_Feature_Interactions_Learning_with_T.md](sources/2311_paper_23110588_Hiformer_Heterogeneous_Feature_Interactions_Learning_with_T.md)
- [sources/paper_8edbf8_HiGR_Efficient_Generative_Slate_Recommendation_via_Hierarch.md](sources/paper_8edbf8_HiGR_Efficient_Generative_Slate_Recommendation_via_Hierarch.md)
- [sources/2604_paper_26040497_Tencent_Advertising_Algorithm_Challenge_2025_All-Modality_G.md](sources/2604_paper_26040497_Tencent_Advertising_Algorithm_Challenge_2025_All-Modality_G.md)
- [sources/test_generative_rec.md](sources/test_generative_rec.md)
- [sources/2203_paper_22031101_DHEN_A_Deep_and_Hierarchical_Ensemble_Network_for_Large-Sca.md](sources/2203_paper_22031101_DHEN_A_Deep_and_Hierarchical_Ensemble_Network_for_Large-Sca.md)
- [sources/paper_1b102d_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md](sources/paper_1b102d_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md)
- [sources/rankmixer_to_oneranker.md](sources/rankmixer_to_oneranker.md)
- [sources/2511_paper_25110607_Make_It_Long,_Keep_It_Fast_End-to-End_10k-Sequence_Modeling.md](sources/2511_paper_25110607_Make_It_Long,_Keep_It_Fast_End-to-End_10k-Sequence_Modeling.md)
- [sources/2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md](sources/2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md)
- [sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md](sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md)
- [sources/2511_paper_25111013_GPR_Towards_a_Generative_Pre-trained_One-Model_Paradigm_for.md](sources/2511_paper_25111013_GPR_Towards_a_Generative_Pre-trained_One-Model_Paradigm_for.md)
- [sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md](sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md)
- [sources/2507_paper_25071555_RankMixer_Scaling_Up_Ranking_Models_in_Industrial_Recommend.md](sources/2507_paper_25071555_RankMixer_Scaling_Up_Ranking_Models_in_Industrial_Recommend.md)
- [sources/paper_2305_05065_Generative_Retrieval_RecSys.md](sources/paper_2305_05065_Generative_Retrieval_RecSys.md)
- [sources/paper_c33d89_Farewell_to_Item_IDs_Unlocking_the_Scaling_Potential_of_Lar.md](sources/paper_c33d89_Farewell_to_Item_IDs_Unlocking_the_Scaling_Potential_of_Lar.md)

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
