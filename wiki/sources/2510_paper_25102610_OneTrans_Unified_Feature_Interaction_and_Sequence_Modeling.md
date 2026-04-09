---
title: "2510 Paper 25102610 Onetrans Unified Feature Interaction And Sequence Modeling"
category: "sources"
tags: ["source", "2026-04-09"]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../../raw/sources/2510_paper_25102610_OneTrans_Unified_Feature_Interaction_and_Sequence_Modeling.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要
本文提出了一种名为 **OneTrans** 的统一 Transformer 骨干网络，旨在解决工业推荐系统中特征交互模块（如 Wukong、RankMixer）与用户行为序列模块（如 LONGER）长期分离优化、缺乏双向信息交换与统一扩展的瓶颈。OneTrans 通过统一分词器将序列与非序列属性映射为单一 Token 序列，并在堆叠的 Transformer 块中采用“序列 Token 参数共享 + 非序列 Token 参数独立”的设计，实现特征交互与序列建模的深度融合。结合因果注意力与跨请求 KV 缓存机制，该架构显著降低了训练与推理阶段的计算开销。

在工业级数据集上的实验表明，OneTrans 能够随参数量增加高效扩展，持续超越现有强基线模型。线上 A/B 测试结果显示，该模型在实际业务场景中实现了人均 GMV 提升 5.68% 的显著收益。该工作为工业推荐系统向统一化、大模型化架构演进提供了重要的工程实践与理论依据，展示了 Transformer 在统一多类型特征与长序列建模中的工业落地潜力。

### 需要更新的页面
- **`wiki/models/RankMixer.md`**：在“架构对比/演进”部分补充 OneTrans 作为统一特征交互与序列建模的下一代范式，说明 RankMixer 仅聚焦特征交互扩展，而 OneTrans 实现了双模块统一与 KV 缓存优化。
- **`wiki/concepts/sequential_recommendation.md`**：在“工业架构演进”章节增加“统一序列与特征建模”段落，引入 OneTrans 的 Token 统一策略与参数共享机制。
- **`wiki/synthesis/llm4rec_taxonomy.md`**：在“工业部署架构”或“统一骨干网络”分类下补充 OneTrans 条目，强调其向 LLM 风格统一 Token 序列与推理缓存优化的靠拢趋势。
- **`wiki/index.md`**：追加新创建的源页面与模型页面索引条目。
- **`wiki/log.md`**：追加本次 `ingest` 操作记录（日期、操作类型、影响页面）。

### 需要创建的新页面
- **`wiki/models/OneTrans.md`**：详细记录 OneTrans 的统一架构设计、分词策略、参数共享机制、KV 缓存优化及工业实验结果。
- **`wiki/concepts/unified_transformer_backbone.md`**：阐述推荐系统中统一 Transformer 骨干网络的概念，对比传统双模块分离架构，涵盖 OneTrans 的核心思想与 LLM4Rec 的关联。
- **`wiki/sources/2510_paper_25102610_OneTrans_Unified_Feature_Interaction_and_Sequence_Modeling.md`**：本源的标准化摘要页（见下文完整内容）。

### 矛盾/冲突
- **未发现冲突**。OneTrans 的工作与现有 LLM4Rec 趋势（统一表示、序列建模、工业级缓存优化、参数高效扩展）高度一致，属于对传统深度推荐架构向大模型范式靠拢的实证补充，未与现有知识库声明产生矛盾。

### 提取的关键事实
- OneTrans 是首个在工业推荐中统一特征交互与用户行为序列建模的 Transformer 骨干网络。
- 采用统一分词器（Unified Tokenizer）将序列与非序列属性转化为单一 Token 序列。
- 参数设计：序列类 Token 共享参数以提升泛化与效率，非序列类 Token 使用独立参数以保留特征特异性。
- 推理/训练优化：结合因果注意力（Causal Attention）与跨请求 KV 缓存（Cross-request KV Caching），支持中间表示预计算，大幅降低延迟与显存占用。
- 实验结果：在工业数据集上随参数量扩展表现稳定提升，线上 A/B 测试实现人均 GMV +5.68%。
- 论文已被 The Web Conference 2026 (WWW 2026) 接收。
- 作者团队包括 Zhaoqi Zhang, Haolei Pei, Jun Guo, Tianyu Wang, Yufei Feng, Hui Sun, Shaowei Liu, Aixin Sun。

### 建议的源页面内容
```markdown
---
title: "OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender"
category: "sources"
tags: ["unified-transformer", "feature-interaction", "sequence-modeling", "kv-caching", "industrial-recsys", "WWW2026"]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../raw/sources/2510.26104.pdf"]
related: ["../models/OneTrans.md", "../concepts/unified_transformer_backbone.md", "../models/RankMixer.md"]
confidence: "high"
status: "stable"
---

# OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender

## 概述
本文提出 OneTrans，一种面向工业推荐系统的统一 Transformer 骨干网络，旨在打破传统架构中特征交互模块与用户行为序列模块分离优化的局限。通过统一分词、参数共享/独立策略与跨请求 KV 缓存，OneTrans 在保持高效推理的同时实现了双向信息融合，并在真实业务中取得显著收益。

## 核心要点
- **统一架构**：单一 Transformer 同时处理特征交互与长序列行为建模，消除模块间信息孤岛。
- **统一分词器**：将序列属性（如点击历史）与非序列属性（如用户画像、物品静态特征）映射为同一 Token 空间。
- **参数解耦设计**：序列 Token 共享参数以提升泛化能力，非序列 Token 使用独立参数保留特征特异性。
- **推理加速**：结合因果注意力与跨请求 KV 缓存，支持中间状态预计算，显著降低训练/推理开销。
- **工业验证**：线上 A/B 测试实现人均 GMV +5.68%，且随参数量增加呈现稳定 Scaling 趋势。

## 详情

### 架构设计
OneTrans 摒弃了传统推荐系统中“特征交互塔 + 序列建模塔”的双流设计，采用单流 Transformer 统一处理。输入经过统一分词器后，序列与非序列特征被拼接为单一 Token 序列。堆叠的 OneTrans 块内部采用混合参数策略：
- **序列 Token**：跨位置共享权重，利用 Transformer 的归纳偏置捕获时序依赖。
- **非序列 Token**：分配独立权重，避免静态特征被序列动态噪声稀释。

### 计算优化机制
针对工业场景的高并发与低延迟要求，OneTrans 引入：
- **因果注意力（Causal Attention）**：确保序列建模的自回归性质，防止未来信息泄露。
- **跨请求 KV 缓存（Cross-request KV Caching）**：在批量推理时复用历史请求的 Key-Value 状态，支持中间表示预计算，减少重复计算与显存带宽压力。

### 实验与业务指标
- **离线评估**：在多个工业级数据集上，OneTrans 随参数量扩展持续超越 RankMixer、Wukong 等强基线。
- **线上 A/B 测试**：部署于真实推荐流后，实现 **人均 GMV +5.68%** 的提升，同时推理延迟满足工业 SLA 要求。
- **扩展性**：验证了统一 Transformer 在推荐场景下的 Scaling Law 潜力，为后续接入 LLM 预训练权重奠定基础。

## 关联
- 与 [RankMixer](../models/RankMixer.md) 对比：RankMixer 专注特征交互扩展，OneTrans 实现交互与序列的统一。
- 概念延伸：[统一 Transformer 骨干网络](../concepts/unified_transformer_backbone.md) 详细阐述该架构范式。
- 工业部署：为 [LLM-as-Ranker](../methods/llm_as_ranker.md) 提供底层高效推理与缓存优化参考。

## 开放问题
- OneTrans 的统一分词策略如何与多模态内容（图像、视频帧）的离散化 Token 兼容？
- 跨请求 KV 缓存在用户行为分布剧烈漂移（Distribution Shift）时的失效边界与更新策略尚未明确。
- 该架构是否可直接初始化自开源 LLM（如 Qwen、Llama），以利用其先验语义知识？

## 参考文献
- Zhang, Z., Pei, H., Guo, J., Wang, T., Feng, Y., Sun, H., Liu, S., & Sun, A. (2026). *OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender*. Accepted at The Web Conference 2026 (WWW 2026). arXiv:2510.26104.
```