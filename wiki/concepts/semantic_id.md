---
title: "Semantic IDs — Discrete Semantic Identifiers for Generative Recommendation"
category: "concepts"
tags: [semantic ID, generative retrieval, item tokenization, RQ-VAE, codebook, hierarchical ID]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/2507_paper_25072222_Generative_Recommendation_with_Semantic_IDs_A_Practitioner'.md"]
related:
  - "../models/GRID.md"
  - "../concepts/generative_retrieval.md"
  - "../methods/rqvae.md"
  - "../models/HiGR.md"
  - "../methods/semantic_id_construction.md"
confidence: "high"
status: "stable"
---

# Semantic ID — 用于生成式推荐的离散语义标识符

## 概述

Semantic ID（SID）是**从连续语义表示（如 LLM 嵌入、物品内容特征、行为序列表征）中导出的离散 token 序列**，使生成式推荐模型能够结合语义信息和协同过滤信号，同时保留离散解码的优势。SID 不使用不透明的整数 ID，而是将物品语义编码为结构化 token 序列（通常通过 RQ-VAE 等向量量化方法），使模型能够通过语义相似性泛化到未见物品，并支持在物品空间上进行高效的自回归生成。

随着工业界大模型推荐架构的演进，Semantic ID 的定位已从早期的“冷启动与检索层辅助表示”跃升为**推荐系统的系统级基础接口**。它正在重构物品表示、索引组织、召回与排序的交互范式，并推动生成式推荐从检索层全面渗透至主排序（Main Ranking）、广告全链路（Ad Pipeline）以及多业务/跨域统一建模场景。

## 要点

- **连续到离散映射**：通过量化将稠密嵌入转换为 token 序列
- **语义泛化**：相似物品共享相似的 token 前缀/后缀
- **协同信号保留**：SID 可以同时捕捉内容语义和 CF 模式
- **离散解码优势**：支持受限词汇表下的高效自回归生成
- **多种构建方法**：RQ-VAE、FORGE、对比自编码器、动态流式聚类（MERGE）、业务感知分词（BID）等
- **生成式检索的关键**：SID 是使 GR 可行的基础
- **系统级基础接口**：统一特征、场景、任务与分布的 token 交互语言
- **全链路渗透**：已突破检索边界，进入主排序、广告多目标优化、多业务解耦与端到端 One-Model 架构

## 详情

### 为什么不使用原始整数 ID？

传统推荐系统使用任意整数 ID：
- 物品 A = 42，物品 B = 1337——无语义关系
- 模型必须从头学习所有物品表示
- 无法泛化到未见物品
- 词汇表随目录规模线性增长
- **大 Backbone 扩展瓶颈**：当排序主干持续向 7B/15B+ 规模扩展时，“一物一符号”的离散 ID 会严重限制模型的参数利用率与特征交互深度，成为 Scaling 的显式瓶颈 [来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]

### Semantic ID 的工作原理

```
Item content/features/behavior → Encoder → Continuous embedding → Quantizer → Discrete token sequence
                                                                    ↓
                                                            [t1, t2, ..., tk]
```

量化步骤将连续嵌入映射到离散码：

1. **学习码本**：划分嵌入空间的语义"词"词汇表
2. **量化**：每个物品的嵌入被映射到最近的码本条目
3. **层次化结构**：多层量化创建从粗到细的 token 层次
   - 第 1 层：类目/类型（粗粒度）
   - 第 2 层：子类目/业务域（中等粒度）
   - 第 3 层：具体物品身份/细粒度特征（细粒度）
4. **动态流式更新**（工业演进）：放弃静态固定码本，支持随数据流动态生成、重置与合并聚类中心，适应实时分布漂移 [来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]

### 构建方法

#### RQ-VAE（残差量化 VAE）
- 使用带残差量化的多个码本
- 每一层量化前一层的残差误差
- 创建自然的层次结构
- GR 文献中最广泛使用的方法

#### FORGE（力引导探索）
- 解决 RQ-VAE 中的码本崩溃问题
- 使用力引导探索确保所有码本条目都被利用
- 产生更平衡、信息更丰富的 SID

#### 对比自编码器
- 结合重建损失与对比约束
- 确保语义相似的物品共享前缀码
- 在 HiGR 中用于 slate 推荐

#### MERGE（动态流式索引构建）
- 针对 Streaming Recommendation 场景设计
- 放弃静态 VQ Codebook，采用动态聚类机制
- 支持 Cluster 随新数据流实时生成、分裂与合并
- 形成层次化动态索引，显著降低冷启动与长尾物品的量化延迟 [来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]

#### TRM 排序侧分词（Ranking-aware Tokenization）
- 专为大 Ranking Backbone 设计
- 同时兼顾语义相似性、历史行为相关性与细粒度记忆能力
- 将 Tokenization 从“检索侧问题”升级为“排序模型输入语言问题” [来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]

#### BID（业务感知语义ID / Business-aware Semantic ID）
- 针对多业务/跨域统一推荐中的“表征混淆”与“跷跷板效应”设计
- 摒弃全局统一 Tokenizer，采用**共享底层词表 + 业务专属标识符/前缀**的架构
- 通过领域感知分词构建独立的语义子空间，实现跨业务语义解耦与知识迁移
- 结合多业务预测路由（MBP）与标签动态路由（LDR），在自回归生成中实现细粒度业务定制化，有效缓解多目标优化中的梯度冲突 [来源：[2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md](../sources/2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md)]

### 优质 Semantic ID 的属性

| 属性 | 描述 |
|------|------|
| **语义连贯性** | 相似物品共享相似码 |
| **层次化结构** | 从粗到细的 token 组织 |
| **码本利用率** | 所有码都被有意义地使用 |
| **泛化能力** | 未见物品可以映射到合理的码 |
| **紧凑性** | 高效表示（每件物品 token 少） |
| **稳定性** | 随时间一致的映射 |
| **服务友好性** | 支持 Trie 约束、前缀剪枝、Beam Search 等推理优化，适配低延迟在线 Serving |
| **多目标对齐** | 能同时编码兴趣信号与商业/价值信号（如广告场景） |
| **业务解耦性** | 在多业务/跨域场景下，能通过专属标识符隔离语义子空间，避免表征混淆与优化冲突 |

### 在生成式推荐中的作用

SID 实现了以下关键能力：

1. **自回归物品生成**：模型生成 token 序列 `[t1, t2, ..., tk]` 解码为物品
2. **语义感知检索**：相似 token 序列对应相似物品
3. **冷启动处理**：新物品可根据内容特征分配 SID
4. **多物品生成**：通过控制生成可以生成多个相关物品（slate）
5. **统一特征接口**：将序列特征、非序列特征、场景/任务条件统一为 Token 接口，供单一 Backbone 交互 [来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]
6. **推理时扩展（Inference-time Scaling）**：基于离散 Token 空间，可引入 Beam 设计、路径级 Reward、动态 Beam Serving 与用户侧计算复用，将推荐竞争拉向推理阶段优化 [来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]

### 工业演进：从检索技巧到系统级基础接口

在 2025—2026 年的工业实践中，Semantic ID/Token 的意义已远超“更有利于冷启动”的局部优势，正演变为推荐系统的**系统级基础接口**。这一演进体现在三个维度：
- **表示层统一**：物品不再只是原子化 ID，而是可组合、可迁移、可生成、可索引的 Token 序列。异构特征（文本、图像、行为、商业信号）被映射至共享离散空间。
- **架构层重构**：传统 `Retrieve → Rank → Rerank` 的多阶段流水线正被端到端生成式 One-Model 重新组织。SID 成为连接召回候选生成、主排序打分与广告价值建模的统一语言。
- **部署层协同**：离散 Token 天然适配受限解码（Trie/Prefix Constraint），使生成过程与在线 Serving 的计算图、存储访问模式深度耦合，推理效率成为一等公民 [来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]

### 在排序与广告全链路中的落地

生成式推荐已跨越检索试水阶段，在主排序与广告链路中形成体系化落地：
- **主排序（Main Ranking）**：TRM 等工作验证了基于 Semantic Token 的 Ranker 可直接替代传统 ID Embedding 层，通过 Token Mixing 与 Sparse MoE 实现主干扩展，同时保持在线服务可行性。
- **广告 One-Model**：GPR 与 OneRanker 将广告推荐重写为端到端生成问题。通过多级 Semantic ID 与异构层次化解码器，系统性处理超长序列、多目标价值建模与在线生成效率。OneRanker 进一步引入 Task Tokens、Ranking Decoder 与 Distribution Consistency Loss，将生成与排序从“阶段串联”推进为“架构级协同”，缓解兴趣目标与商业价值目标的张力。
- **多业务/超级App统一建模**：美团 MBGR 框架首次系统性解决生成式推荐在多业务场景下的落地难题。通过 BID 模块构建解耦的语义 ID 空间，配合多业务预测（MBP）结构与标签动态路由（LDR）模块，将稀疏的跨业务交互标签转化为稠密监督信号。该架构有效缓解了多目标优化中的梯度冲突与“跷跷板现象”，在美团外卖平台实现全量部署，核心业务指标（CTR/CVR/GMV）显著提升，验证了 SID 在复杂工业系统中的扩展性与工程可行性 [来源：[2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md](../sources/2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md)]

### 挑战

- **码本崩溃**：许多码本条目从未被使用的倾向
- **量化误差**：连续到离散映射中的信息损失
- **时间漂移**：物品语义随时间变化，需要 SID 更新
- **跨域迁移**：在一个领域训练的 SID 可能无法很好地迁移
- **构建成本**：构建高质量 SID 需要大量计算
- **在线服务延迟**：自回归生成与 Trie 约束在严格时延约束下的计算图优化
- **多目标价值对齐**：在广告/电商场景中，如何使 SID 同时编码用户兴趣与商业价值，避免生成结果偏离排序约束
- **动态索引维护**：流式数据下的码本/聚类中心实时合并与一致性保障
- **多业务表征混淆与跷跷板效应**：统一语义空间下，不同业务线的行为模式与优化目标易产生梯度冲突，导致模型在跨业务生成时出现性能互斥 [来源：[2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md](../sources/2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md)]
- **跨域知识迁移与隔离的平衡**：如何在共享底层语义表征的同时，保持各业务/领域语义子空间的独立性与特异性 [来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]

### 实践中的变体

- **UASID**（统一自适应 SID）：用于广告的 SID 变体，除内容语义外还捕捉商业信息
- **BID（Business-aware SID）**：针对多业务/跨域场景设计。采用“共享底层词表+业务专属标识符”策略，构建领域感知的独立语义子空间，从根本上解决跨业务表征混淆问题，并结合动态路由机制实现细粒度业务定制化生成 [来源：[2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md](../sources/2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md)]
- **混合 ID**：将 SID 与传统 ID 结合用于回退
- **动态 SID**：适应时间上下文的 SID
- **TRM 排序 Token**：面向大 Ranking Backbone 优化的分词体系，强化行为相关性与细粒度记忆
- **MERGE 动态索引 SID**：基于流式聚类动态生成与合并的层次化 Token，适配实时推荐场景 [来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]

## 关联

- [生成式检索](./generative_retrieval.md) — SID 是基础
- [GRID](../models/GRID.md) — 用于实验不同 SID 方法的框架
- [HiGR](../models/HiGR.md) — 使用对比自编码器构建 SID
- [RQ-VAE](../methods/rqvae.md) — 主要 SID 构建方法
- [FORGE](../methods/forge.md) — 解决 SID 构建中的码本崩溃
- [TRM](../models/TRM.md) — 基于 Semantic Token 的大规模排序主干
- [MERGE](../methods/merge.md) — 动态流式索引与 SID 构建
- [GR4AD](../models/GR4AD.md) — 广告场景下的统一 SID 与生成式排序
- [GPR / OneRanker](../models/GPR.md) — 广告端到端生成式 One-Model 与多级 SID 协同
- [MBGR](../models/MBGR.md) — 美团多业务生成式推荐框架，提出 BID 与 MBP 结构

## 开放问题

1. 不同推荐领域的最优码本大小与层次深度是多少？
2. 当物品内容、用户偏好或业务分布变化时，SID 应如何在线更新与保持一致性？
3. SID 能否有效捕捉多模态语义（文本 + 图像 + 视频 + 行为序列）并实现跨模态对齐？
4. SID 质量与下游推荐/排序/广告性能之间的量化关系如何建立？
5. 是否存在比向量量化保留更多信息的替代离散化方案？
6. 在严格在线时延约束下，如何设计更高效的 Inference-time Scaling 策略（如动态 Beam、路径级 Reward、用户侧复用）？
7. 多业务/多场景统一 SID 空间中，如何平衡全局共享表征与业务特异性隔离？
8. 在多业务/跨域统一 SID 空间中，如何设计更高效的动态路由与标签稠密化机制，以彻底消除多目标优化中的“跷跷板效应”并保障长尾业务的生成质量？[来源：[2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md](../sources/2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md)]

## 参考文献

- Ju, C. M., Collins, L., Neves, L., Kumar, B., Wang, L. Y., Zhao, T., & Shah, N. (2025). Generative Recommendation with Semantic IDs: A Practitioner's Handbook. arXiv:2507.22224.
- Pang, Y., et al. (2025). HiGR: Efficient Generative Recommendation with Hierarchical Semantic IDs.
- Li, C., Yin, J., Zeng, Z., Kou, S., Wang, S., Chen, W., Zhu, Y., Wang, H., & Wang, X. (2026). MBGR: Multi-Business Prediction for Generative Recommendation at Meituan. arXiv:2604.02684.

---

## 更新完成：2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md
**更新时间**: 2026-04-10 10:39
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
