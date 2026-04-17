---
title: "腾讯公司推荐系统团队和工业实践包括"
category: "entities"
tags: ["new", "2026-04-08"]
created: "2026-04-08"
updated: "2026-04-08"
sources: ["../sources/paper_8edbf8_HiGR_Efficient_Generative_Slate_Recommendation_via_Hierarch.md"]
related: []
confidence: "medium"
status: "draft"
---

# 腾讯公司推荐系统团队与工业实践

## 概述
腾讯公司推荐系统团队长期致力于前沿推荐算法的研究与大规模工业级落地，技术栈覆盖信息流、广告、视频号、游戏分发及电商等核心业务场景。近年来，团队在生成式推荐（Generative Recommendation）、长序列建模、多模态统一表征及大语言模型推荐（LLM4Rec）方向取得系统性突破，形成了从底层架构创新、高并发工程优化到全量业务部署的完整技术闭环。

---

## 工业实践与验证

### HiGR：高效生成式列表推荐
HiGR（Hierarchical Generative Recommendation）是腾讯在生成式推荐领域的早期重要探索。该模型通过分层生成机制优化 Slate Recommendation（列表推荐）任务，在保持高推理效率的同时显著提升了列表级多样性与用户满意度。HiGR 的成功部署验证了生成式范式在工业推荐场景中的可行性，为后续架构演进奠定了工程基础。

### GPR：视频号广告系统的全量生成式基座
GPR（Generative Pre-trained One-Model Paradigm）标志着腾讯在“一模型”范式上的重大突破。该架构已全量部署于腾讯视频号广告系统，通过统一的生成式预训练骨干网络，实现了多目标、多场景的联合优化。工业验证表明，GPR 在核心业务指标上取得显著提升，包括 GMV（商品交易总额）与 CTCVR（点击-转化率）的双重增长，确立了其在腾讯广告技术栈中的核心基座地位。
*[来源：[2511_paper_25111013_GPR_Towards_a_Generative_Pre-trained_One-Model_Paradigm_for.md](../sources/2511_paper_25111013_GPR_Towards_a_Generative_Pre-trained_One-Model_Paradigm_for.md)]*

### TokenFormer：统一多字段与序列推荐的工业验证
针对推荐系统中长期独立发展的多字段特征交互与用户行为序列建模范式，腾讯广告算法团队提出并部署了 **TokenFormer** 统一架构。该模型在真实高并发、稀疏特征场景下完成了严格的工业级验证，有效解决了统一建模过程中的稳定性难题。
- **核心挑战与发现**：团队首次实证揭示了“序列崩溃传播（Sequence Collapse Propagation, SCP）”现象。研究表明，维度不良的非序列字段（如用户画像、商品属性）在交互过程中会向序列分支传导噪声，导致序列表征发生维度坍缩，严重削弱模型对时序兴趣的捕获能力。
- **架构创新**：
  - **BFTS 注意力调度机制**：采用 Bottom-Full-Top-Sliding 策略。底层使用全自注意力（Full Self-Attention）充分建模全局字段共现关系；顶层引入收缩窗口滑动注意力（Shrinking-Window Sliding Attention），随网络深度增加逐步聚焦近期行为，有效隔离非序列字段干扰，阻断 SCP 传播路径。
  - **NLIR 非线性交互表征**：设计单侧非线性乘法变换模块 $h' = h \odot \sigma(W h + b)$，突破传统线性加和瓶颈，在不显著增加参数量的前提下，大幅提升模型对稀疏长尾字段的敏感度与表征空间的几何可分性。
- **工业部署表现**：在腾讯广告真实业务流中，TokenFormer 在 AUC 与 GAUC 等核心排序指标上均达到 SOTA 水平。消融实验证实，完整架构使序列特征维度崩溃率显著下降，模型在复杂稀疏场景下的泛化稳定性与高并发推理延迟均满足工业级 SLA 要求。
*[来源：[2604_paper_26041373_TokenFormer_Unify_the_Multi-Field_and_Sequential_Recommenda.md](../sources/2604_paper_26041373_TokenFormer_Unify_the_Multi-Field_and_Sequential_Recommenda.md)]*

### 腾讯广告算法挑战赛 2025
为推动多模态与生成式推荐技术的产学研融合，团队于 2025 年主办了腾讯广告算法挑战赛。赛事发布了大规模工业级数据集，吸引了全球顶尖高校与企业团队参与。该挑战赛不仅验证了 HiGR 等前沿架构在开放基准上的有效性，也为工业界提供了高质量的数据飞轮与算法迭代反馈。
*[来源：[2604_paper_26040497_Tencent_Advertising_Algorithm_Challenge_2025_All-Modality_G.md](../sources/2604_paper_26040497_Tencent_Advertising_Algorithm_Challenge_2025_All-Modality_G.md)]*

---

## 工业部署策略横向对比
腾讯在生成式与长序列推荐的部署策略，与业界其他头部厂商形成鲜明对照，共同推动了推荐系统架构的范式演进：
- **Google/YouTube (PLUM)**：侧重于预训练语言模型（PLM）的适配与微调，通过参数高效微调（PEFT）与检索增强生成（RAG）策略，在海量视频推荐中实现语义理解与个性化生成的平衡。
*[来源：[paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md](../sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md)]*
- **字节跳动/快手 (LONGER)**：聚焦超长序列建模的规模化落地。LONGER 架构已覆盖 >10 个核心业务场景，服务十亿级用户，通过高效的序列压缩与分布式推理优化，验证了长上下文推荐在工业界的可行性。
*[来源：[2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md](../sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md)]*

---

## 技术演进与 LLM4Rec 关联
腾讯推荐系统的工业实践与大语言模型推荐（LLM4Rec）的发展路径高度契合。TokenFormer 揭示的“维度崩溃传播”问题为 LLM 统一骨干设计提供了重要警示：盲目拼接多模态 Token 可能导致序列表征被结构化噪声淹没。其 BFTS 注意力调度策略与 LLM 社区的稀疏注意力/滑动窗口优化（如 Longformer、Mistral 的 Sliding Window Attention）理念高度一致，可为 LLM 处理混合模态推荐数据提供高效的计算范式。此外，NLIR 模块的非线性交互思想亦可启发 LLM 推荐中的特征融合层（如 Adapter、LoRA 变体）设计，推动大模型在工业级推荐场景中的轻量化、高鲁棒性落地，为构建真正统一的“大模型推荐基座”提供架构级参考。

---

## 更新日志
- **2026-04-08**：添加 PLUM/YouTube 作为对比案例，说明不同公司的生成式推荐部署策略。
- **2026-04-09**：添加腾讯广告算法挑战赛 2025 信息，包括数据集发布、竞赛规模、与 HiGR 的关联。
- **2026-04-09**：在“工业部署对比”章节追加字节跳动 LONGER 的部署规模（>10 场景、十亿用户），形成多厂牌长序列/生成式推荐部署的横向对照。
- **2026-04-09**：补充 GPR 在腾讯视频号广告系统的全量部署案例、核心业务指标提升（GMV、CTCVR）及技术架构定位。
- **2026-04-17**：在“工业实践与验证”章节追加 TokenFormer 在腾讯广告业务流中的部署验证记录，补充其在真实高并发、稀疏特征场景下的性能表现及 LLM4Rec 架构启示。

---

## 相关页面
- [HiGR 生成式列表推荐](../entities/HiGR.md)
- [GPR 统一生成式推荐基座](../entities/GPR.md)
- [TokenFormer 统一推荐架构](../entities/TokenFormer.md)
- [PLUM 预训练语言模型推荐适配](../entities/PLUM.md)
- [LONGER 长序列推荐工业部署](../entities/LONGER.md)
- [LLM4Rec 知识库首页](../index.md)

---

## 更新完成：2604_paper_26041373_TokenFormer_Unify_the_Multi-Field_and_Sequential_Recommenda.md
**更新时间**: 2026-04-17 10:13
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2604_paper_26041373_TokenFormer_Unify_the_Multi-Field_and_Sequential_Recommenda.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
