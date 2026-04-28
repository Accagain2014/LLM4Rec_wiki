---
title: "Kuaishou"
category: "entities"
tags: ["new", "2026-04-08"]
created: "2026-04-08"
updated: "2026-04-08"
sources: ["../sources/2510_paper_25101163_OneRec-Think_In-Text_Reasoning_for_Generative_Recommendatio.md"]
related: []
confidence: "medium"
status: "draft"
---

# 快手 (Kuaishou)

快手在 LLM4Rec（大语言模型赋能推荐系统）领域的探索已从早期的单点实验，全面演进为**平台级生成式推荐技术体系**。其技术路线不仅覆盖了短视频主站，还深度拓展至本地生活、电商、广告等核心商业化场景，形成了以 `OneRec` 家族为核心，向多场景、端到端生成式 One-Model 持续迭代的工业范式。[来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]

## 核心模型与技术矩阵
快手的生成式推荐技术已突破传统多阶段流水线的局限，逐步构建起覆盖召回、排序、多场景分发、广告商业化及底层训练优化的完整技术栈：

### 1. OneRec 系列：统一召回与排序的基座
- **OneRec**：业界较早将 Retrieve 与 Rank 统一为端到端生成式推荐模型的工作。该模型在快手短视频主场景成功上线，验证了生成式推荐进入主排序链路的可行性，实现观看时长提升 **1.6%**。[来源：[2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md](../sources/2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md)]
- **OneRec-V2**：在 V1 基础上进一步优化生成架构与训练策略，在最新工业部署中实现停留时长分别提升 **+0.467%** 与 **+0.741%**，标志着生成式基座模型在复杂流量分布下的持续 Scaling 能力。[来源：[2508_paper_25082090_OneRec-V2_Technical_Report.md](../sources/2508_paper_25082090_OneRec-V2_Technical_Report.md)]
- **OneRecThink / ThinkAhead**：引入 In-Text Reasoning（文本内推理）机制，增强模型对用户意图的深层理解与长程规划能力。工业部署后带来停留时长 **+0.159%** 的显著增益，体现了“慢思考”推理能力在推荐系统中的落地价值。[来源：[2510_paper_25101163_OneRec-Think_In-Text_Reasoning_for_Generative_Recommendatio.md](../sources/2510_paper_25101163_OneRec-Think_In-Text_Reasoning_for_Generative_Recommendatio.md)]

### 2. 场景化扩展：多业务生态覆盖
- **OneLoc（本地生活）**：将生成式推荐引入 LBS 场景。通过引入 `geo-aware semantic ID`、`geo-aware self-attention` 与 `neighbor-aware prompt`，结合强化学习联合优化用户兴趣、地理位置与商业目标，有效解决了本地生活推荐中空间约束与兴趣匹配的耦合难题。[来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]
- **OneMall（电商）**：将商品卡片、短视频与直播分发统一至同一生成式家族框架。表明 One-Model 已不再是单一流量场景的优化技巧，而是向平台级多分发入口扩张的基础设施。[来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]

### 3. 广告与商业化深水区：生成式排序与推理优化
- **GR4AD**：面向大规模广告场景的生成式推荐模型。提出 `UA-SID` 统一广告内容与业务信号的 Tokenization，设计面向在线推理预算的 `LazyAR` 解码结构，并结合价值感知监督与 Ranking-guided 偏好优化。该模型已覆盖 **4 亿+** 用户规模，实现广告收入提升 **4.2%**，是架构、学习与 Serving 一体化协同设计的典范。[来源：[2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md](../sources/2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md)]
- **GRank & PROMISE**：进一步推进检索侧的 `generate-rank` 框架，探索 Inference-time Scaling（推理期扩展）与 Process Reward Model（过程奖励模型），将推荐系统的竞争维度从训练阶段延伸至在线推理与动态搜索阶段。[来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]

### 4. 训练范式优化：MEDA 多轮次学习框架
- **MEDA (Multi-Epoch Learning for Deep CTR)**：针对工业界深度CTR模型长期存在的“单轮次过拟合”（One-Epoch Overfitting）瓶颈，快手提出了一种即插即用的多轮次训练调度框架。该框架无需修改模型结构，通过在每个 Epoch 启动时**周期性重初始化（Re-initialization）高维稀疏特征的 Embedding 层**，有效阻断历史梯度累积导致的参数固化路径。
- **隐式增强与正则化机制**：Embedding 的重置操作等效于对高维稀疏特征空间施加动态扰动，使模型在不同轮次中面对“语义相同但表示起点不同”的样本，从而实现隐式数据增强。该机制天然具备强正则化效果，配合标准损失函数可显著提升模型泛化边界与收敛稳定性。
- **LLM4Rec 迁移价值**：MEDA 揭示的“高维稀疏特征过拟合”本质与周期性扰动思想，为 LLM 推荐微调提供了重要工程借鉴。在 LLM 指令微调（Instruction Tuning）或参数高效微调（PEFT/LoRA）中，引入周期性参数重置或扰动策略，可有效缓解模型对特定指令分布的过度拟合与灾难性遗忘，助力构建更稳定、具备持续学习能力的推荐大模型基座。[来源：[2305_paper_23051953_Multi-Epoch_Learning_for_Deep_Click-Through_Rate_Prediction.md](../sources/2305_paper_23051953_Multi-Epoch_Learning_for_Deep_Click-Through_Rate_Prediction.md)]

## 关键技术特征
基于上述模型矩阵，快手在 LLM4Rec 的工业化实践中呈现出以下核心特征：
1. **Semantic Token 系统化**：Item 表示从原子化 ID 演进为可组合、可迁移、可生成的语义 Token 序列，成为跨场景推荐的新基础接口。
2. **端到端 One-Model 架构**：打破传统 Retrieve-Rank-Rerank 多阶段流水线，通过统一输入 Schema 与生成式解码器实现全链路重构。
3. **推理期优化（Inference-time Scaling）**：将 Beam Search、动态路径奖励、用户侧计算复用等策略引入在线服务，使 Serving 与推理优化成为一等公民。
4. **强化学习与价值对齐**：在生成过程中深度融合商业价值建模（Value Modeling）与偏好优化，解决生成目标与排序/商业目标之间的张力。
5. **训练稳定性与持续学习优化**：突破传统单轮次训练瓶颈，通过周期性参数重置与隐式增强机制（如 MEDA），提升高维稀疏特征下的模型泛化边界，为 LLM 推荐微调的抗遗忘与稳定收敛提供底层范式支撑。

## 工业部署与业务指标
| 模型/系统 | 部署场景 | 核心业务指标 | 技术亮点 |
|---|---|---|---|
| `OneRec` | 短视频主站 | 观看时长 +1.6% | Retrieve & Rank 统一生成 |
| `OneRec-V2` | 短视频/多场景 | 停留时长 +0.467% / +0.741% | 架构优化与持续 Scaling |
| `OneRecThink` | 主站推理增强 | 停留时长 +0.159% | In-Text Reasoning / 思维链 |
| `GR4AD` | 广告推荐 | 覆盖 4 亿+ 用户，收入 +4.2% | LazyAR 解码 / UA-SID / 价值对齐 |
| `ULTRAHSTU` | 序列推荐基座 | 日均十亿级服务，指标 +4%~8% | 序列建模规模化 / 高效 Serving |
| `MEDA` | CTR预估/多模型训练管线 | AUC +0.15%，训练步数 -28% | 嵌入层周期性重初始化 / 隐式数据增强 |

## 技术团队背景
快手推荐算法团队（核心成员包括 **Guorui Zhou、Bi Xue、Ben Xue** 等）在序列推荐规模化、生成式架构设计、底层训练优化与大规模在线 Serving 优化方面积累了深厚经验。团队主导的 `ULTRAHSTU` 等序列模型已实现日均十亿级服务，业务指标提升 **4%~8%**；同时，在深度CTR训练范式（如 MEDA）上的突破，为后续生成式 One-Model 的平滑演进与 LLM 推荐微调奠定了坚实的工程、数据与算法基座。[来源：[2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md](../sources/2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md)]

## 相关主题
- [源文档](../sources/rankmixer_to_oneranker.md)
- [OneRec](../models/OneRec.md)
- [GR4AD](../models/GR4AD.md)
- [MEDA](../models/MEDA.md)
- [生成式推荐 (Generative Recommendation)](../concepts/Generative_Recommendation.md)
- [语义 Token 化 (Semantic Tokenization)](../concepts/Semantic_Tokenization.md)

## 扩展阅读
- [知识库首页](../README.md)
- [全部模型](../models/)
- [全部概念](../concepts/)

---

*本页面由 LLM 自动生成，内容可能需要人工审查和补充。*

## 更新日志
- **2026-04-28**：补充 `MEDA` 多轮次训练框架在快手工业场景的验证结果（AUC +0.15%，训练步数 -28%），拓展底层训练优化技术矩阵，并阐述其对 LLM 推荐微调的迁移价值。[来源：[2305_paper_23051953_Multi-Epoch_Learning_for_Deep_Click-Through_Rate_Prediction.md](../sources/2305_paper_23051953_Multi-Epoch_Learning_for_Deep_Click-Through_Rate_Prediction.md)]
- **2026-04-09**：基于行业综述文档，全面重构页面结构，补充 `OneLoc`、`OneMall`、`GRank`、`PROMISE` 的部署定位与技术细节，体现生成式推荐向平台级/广告深水区扩展的趋势。[来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]
- **2026-04-09**：整合 `OneRecThink` / `ThinkAhead` 工业部署案例与业务指标（+0.159% 停留时长），补充技术团队背景。[来源：[2510_paper_25101163_OneRec-Think_In-Text_Reasoning_for_Generative_Recommendatio.md](../sources/2510_paper_25101163_OneRec-Think_In-Text_Reasoning_for_Generative_Recommendatio.md)]
- **2026-04-09**：添加 `GR4AD` 部署案例，补充 4 亿用户规模、4.2% 收入提升等工业指标，更新技术团队背景（Ben Xue、Guorui Zhou 等）。[来源：[2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md](../sources/2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md)]
- **2026-04-09**：添加 `OneRec` 部署案例，补充 1.6% 观看时长提升指标，更新技术团队背景（Guorui Zhou 等）。[来源：[2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md](../sources/2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md)]
- **2026-04-09**：追加 `OneRecV2` 在快手的最新工业部署数据（停留时长 +0.467%/0.741%），更新技术团队贡献记录与业务场景。[来源：[2508_paper_25082090_OneRec-V2_Technical_Report.md](../sources/2508_paper_25082090_OneRec-V2_Technical_Report.md)]
- **2026-04-09**：追加 `ULTRAHSTU` 的工业部署记录（日均十亿级服务、4%~8% 业务指标提升），更新核心作者团队（Bi Xue 等）在序列推荐规模化方向的贡献。[来源：[2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md](../sources/2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md)]

---

## 更新完成：2305_paper_23051953_Multi-Epoch_Learning_for_Deep_Click-Through_Rate_Prediction.md
**更新时间**: 2026-04-28 09:31
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2305_paper_23051953_Multi-Epoch_Learning_for_Deep_Click-Through_Rate_Prediction.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
