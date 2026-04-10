---
title: "2402 Paper 24021715 Actions Speak Louder Than Words Trillion-Parameter Sequenti"
category: "sources"
tags: ["source", "2026-04-10"]
created: "2026-04-10"
updated: "2026-04-10"
sources: ["../../raw/sources/2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要
该论文（ICML'24）是 LLM4Rec 与工业推荐系统演进中的里程碑工作，首次将推荐任务正式重构为**生成式序列转换（Generative Sequence Transduction）**问题，并提出专为高基数、非平稳流式数据优化的 **HSTU（Hierarchical Sequential Transduction Unit）** 架构。通过摒弃传统双塔/多塔架构与全局 Softmax 注意力，HSTU 采用相对位置偏置与线性化注意力机制，在保持长程依赖捕获能力的同时大幅降低计算复杂度。

研究在真实工业场景中训练并部署了 **1.5 万亿参数** 的生成式推荐模型，首次实证了推荐系统质量与训练算力之间存在严格的**幂律缩放关系（Scaling Law）**，跨越 3 个数量级未出现性能饱和。线上 A/B 测试显示核心转化指标提升 12.4%，推理吞吐量较 FlashAttention2 Transformer 提升 5.3–15.2 倍，标志着推荐系统正式迈入“基础模型（Foundation Model）”时代。

### 需要更新的页面
- **`wiki/concepts/scaling_laws_recsys.md`**：补充该论文作为推荐领域缩放定律的**奠基性实证工作**。明确 1.5T 参数规模、3 个数量级的算力-性能幂律关系，以及“生成式范式使 Scaling Law 成立”的核心结论。
- **`wiki/concepts/llm4rec_overview.md`** & **`wiki/concepts/generative_retrieval.md`**：更新范式定义，强调“将用户交互序列视为离散 Token 序列进行自回归生成”的架构演进路径，补充 HSTU 作为该范式的早期工业验证。
- **`wiki/models/ULTRA_HSTU.md`**：在架构演进章节补充初代 HSTU 的背景，明确 ULTRA-HSTU 是其在稀疏注意力与交互拓扑上的下一代迭代，建立双向 `related` 链接。
- **`wiki/entities/meta.md`**（若不存在）：记录 Meta 在生成式推荐、万亿参数模型部署及流式训练策略上的工业实践。

### 需要创建的新页面
- **`wiki/models/HSTU.md`**：初代 HSTU 架构页。涵盖相对位置偏置、线性化注意力、GLU 门控前馈网络、高基数特征离散化及 1.5T 参数工业部署指标。
- **`wiki/entities/meta.md`**：Meta 推荐系统团队实体页。记录其在生成式推荐基础模型、HSTU/ULTRA-HSTU 架构演进及十亿级用户平台部署中的技术路线。

### 矛盾/冲突
- **未发现直接矛盾**。需注意与现有 `wiki/models/ULTRA_HSTU.md` 的表述衔接：本文是 Scaling Law 的**确立者**（证明幂律存在），而 ULTRA-HSTU 是**优化者**（通过稀疏注意力与拓扑重构“弯曲”曲线、提升扩展效率）。两者为明确的继承与演进关系，非冲突。
- 现有索引中 `wiki/models/ULTRA-HSTU.md` 与 `wiki/models/ULTRA-HSTU.md`（重复条目）需在后续 Lint 阶段清理，建议保留带连字符的标准命名。

### 提取的关键事实
- **架构创新**：HSTU 移除全局 Softmax 注意力，采用相对位置偏置 + 线性化注意力 + GLU 门控，复杂度从 $O(L^2)$ 降至近似 $O(L)$。
- **参数与部署规模**：1.5 万亿参数生成式推荐模型，已稳定部署于十亿级用户平台。
- **性能指标**：离线 NDCG 最高提升 65.8%；线上核心转化指标 +12.4%；序列长度 8192 时推理吞吐量为 FlashAttention2 Transformer 的 5.3–15.2 倍。
- **缩放定律验证**：模型质量随训练算力呈严格幂律增长，跨越 3 个数量级（十亿至万亿级）未出现性能 plateau。
- **训练策略**：采用在线流式采样、动态学习率调度、混合精度与大规模数据并行，适配非平稳推荐数据分布。
- **局限性**：算力门槛极高；冷启动/长尾覆盖依赖外部先验；端到端生成缺乏特征级可解释性。

### 建议的源页面内容
```markdown
---
title: "Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations"
category: "sources"
tags: ["source", "HSTU", "scaling law", "generative recommendation", "Meta", "ICML24", "trillion-parameter"]
created: "2026-04-10"
updated: "2026-04-10"
sources: ["../../raw/sources/2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md"]
related: ["../models/HSTU.md", "../concepts/scaling_laws_recsys.md", "../concepts/llm4rec_overview.md", "../entities/meta.md"]
confidence: "high"
status: "stable"
---

# Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations

## 概述
本文（ICML'24）首次将工业推荐任务重构为**生成式序列转换问题**，并提出专为高基数、非平稳流式数据优化的 **HSTU** 架构。研究成功训练并部署了 **1.5 万亿参数** 的生成式推荐模型，首次实证了推荐系统质量与训练算力之间存在严格的**幂律缩放关系**，跨越 3 个数量级未出现性能饱和。该工作标志着推荐系统从“手工特征工程+双塔检索”正式迈入“统一基础模型+自回归生成”时代。

## 核心要点
- **范式转换**：将用户历史交互序列视为离散 Token 序列，在自回归框架下统一建模召回、排序与重排。
- **HSTU 架构**：摒弃全局 Softmax 注意力，采用相对位置偏置与线性化注意力机制，计算复杂度降至近似 $O(L)$。
- **缩放定律确立**：模型性能随训练算力呈稳定幂律增长（十亿至万亿级），打破传统 DLRM 的性能饱和瓶颈。
- **工业级验证**：1.5T 参数模型在十亿级平台上线，核心转化指标 +12.4%，长序列推理吞吐量提升 5.3–15.2 倍。
- **工程挑战**：依赖超大规模分布式集群与流式训练策略；冷启动与可解释性仍需外部机制增强。

## 详情

### 1. 生成式推荐新范式
传统推荐系统依赖稠密/稀疏特征拼接与多阶段流水线（召回→粗排→精排）。本文提出将推荐重构为序列到序列的生成任务：
- 用户行为历史被离散化为共享词表中的 Token 序列。
- 模型以自回归方式逐 Token 预测下一个交互物品，端到端输出推荐结果。
- 消除独立 Embedding 查找表的内存瓶颈，直接处理超大规模稀疏空间。

### 2. HSTU 架构设计
**Hierarchical Sequential Transduction Unit (HSTU)** 是生成式推荐的核心骨干：
- **相对位置偏置**：替代绝对位置编码，更适配推荐场景中时间衰减与相对顺序的归纳偏置。
- **线性化注意力**：结合低秩投影与分块计算，避免 $O(L^2)$ 显存爆炸，支持 8192+ 超长序列。
- **GLU 门控前馈网络**：增强非线性表征能力，提升高维离散特征的融合效率。
- **流式训练适配**：在线流式采样 + 动态学习率调度 + 混合精度训练，保障非平稳数据分布下的稳定收敛。

### 3. 缩放定律（Scaling Law）实证
- 跨越 **3 个数量级**（1B → 100B → 1.5T 参数）进行系统实验。
- 验证了推荐模型质量与训练算力之间存在可预测的幂律关系，未出现传统架构常见的性能 plateau。
- 为“更大算力+更大模型”在推荐领域的持续投入提供了理论依据。

### 4. 实验与部署结果
| 指标 | 结果 |
|------|------|
| **离线 NDCG 提升** | 最高 +65.8%（vs SASRec/FlashAttention2 Transformer） |
| **线上转化指标** | +12.4%（真实业务 A/B 测试） |
| **推理吞吐量** | 5.3x – 15.2x（Seq Len=8192） |
| **部署规模** | 十亿级用户平台，1.5T 参数稳定服务 |

### 5. 局限性
- **算力门槛**：万亿级训练与推理依赖定制化通信优化与专用硬件，中小团队复现成本高。
- **冷启动/长尾**：高度依赖历史行为密度，零交互用户或极度稀疏物品需结合知识图谱/外部先验。
- **可解释性弱**：端到端自回归生成缺乏特征权重可视化，在强归因/合规审计场景中受限。

## 关联页面
- [HSTU 模型架构](../models/HSTU.md)
- [推荐系统中的缩放定律](../concepts/scaling_laws_recsys.md)
- [LLM4Rec 概述](../concepts/llm4rec_overview.md)
- [Meta 推荐系统实践](../entities/meta.md)
- [ULTRA-HSTU（下一代迭代）](../models/ULTRA_HSTU.md)

## 开放问题
- 如何在保持 Scaling Law 收益的同时，降低 HSTU 架构的推理延迟与显存占用？
- 生成式范式下的冷启动与长尾覆盖，能否通过多模态对齐或检索增强（RAG）有效缓解？
- 自回归生成的可解释性机制如何与工业推荐的业务归因需求兼容？

## 参考文献
- Zhai, J., Liao, L., Liu, X., et al. (2024). *Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations*. ICML 2024. arXiv:2402.17152.
```