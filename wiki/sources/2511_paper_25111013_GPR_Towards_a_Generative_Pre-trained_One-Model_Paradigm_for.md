---
title: "2511 Paper 25111013 Gpr Towards A Generative Pre-Trained One-Model Paradigm For"
category: "sources"
tags: ["source", "2026-04-09"]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../../raw/sources/2511_paper_25111013_GPR_Towards_a_Generative_Pre-trained_One-Model_Paradigm_for.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要
本文提出 **GPR（Generative Pre-trained Recommender）**，是首个面向大规模广告推荐的端到端生成式单模型范式。该框架彻底摒弃了传统“召回-粗排-精排”多阶段级联架构，将广告推荐统一建模为序列生成任务，从根本上缓解多阶段目标不一致与误差累积问题。GPR 采用“统一编码器 + 异构分层解码器（HHD）”架构，通过双解码器显式解耦用户深层意图建模与广告 ID 自回归生成过程，兼顾建模能力与训练稳定性。

在训练策略上，GPR 引入多阶段联合优化管线：预训练阶段采用多 Token 预测（MTP）加速长序列收敛；微调阶段引入价值感知监督信号（Value-Aware Fine-Tuning）对齐商业目标；推理阶段结合层级增强策略优化（HEPO）实现探索-利用平衡。该模型已在腾讯视频号广告系统完成全量线上部署，在 GMV 与 CTCVR 等核心商业指标上取得显著提升，验证了生成式范式在超大规模、高并发广告场景下的工业可行性。

### 需要更新的页面
- **`wiki/entities/tencent.md`**：补充 GPR 在腾讯视频号广告系统的全量部署案例、核心业务指标提升（GMV、CTCVR）及技术架构定位。
- **`wiki/concepts/generative_retrieval.md`**：在工业应用章节新增 GPR 作为广告场景下的端到端生成式推荐实践，强调其从多阶段到单模型范式的架构演进。
- **`wiki/concepts/semantic_id.md`**：补充 GPR 中“统一多层级语义 ID 分词”机制，说明其如何将异构广告特征与自然内容映射至共享离散空间以增强语义对齐。
- **`wiki/methods/multi_objective_alignment.md`**：新增 HEPO（层级增强策略优化）与价值感知微调作为推荐系统中商业价值对齐（类 RLHF）的典型方法。

### 需要创建的新页面
- **`wiki/models/GPR.md`**：详细记录 GPR 模型架构（HHD 双解码器设计）、训练管线（MTP/Value-Aware FT/HEPO）、部署规模与业务收益。
- **`wiki/methods/hepo.md`**：独立页面说明 Hierarchical Enhanced Policy Optimization 的层级奖励机制、策略梯度更新方式及其在广告 eCPM/CTCVR 对齐中的作用。
- **`wiki/concepts/value_aware_alignment.md`**：阐述推荐系统中将商业价值（如转化收益、广告主 ROI）作为监督信号或奖励函数进行模型对齐的通用范式。

### 矛盾/冲突
- **未发现冲突**。GPR 的架构理念与现有生成式检索（Generative Retrieval）和 LLM4Rec 范式高度一致，仅在目标函数上从“用户兴趣匹配”扩展至“商业价值对齐”，属于现有知识体系的合理延伸与工业验证。

### 提取的关键事实
- GPR 是首个端到端生成式广告推荐单模型，替代传统多阶段级联流水线。
- 核心架构为“统一编码器 + 异构分层解码器（HHD）”，上层解码意图，下层自回归生成广告 ID。
- 采用统一多层级语义 ID 分词，将广告与自然内容映射至共享离散空间。
- 训练策略包含：多 Token 预测（MTP）、价值感知微调（Value-Aware FT）、层级增强策略优化（HEPO）。
- 已在腾讯视频号（Weixin Channels）广告系统全量部署，显著提升 GMV 与 CTCVR。
- 局限性包括：自回归推理延迟优化需求、冷启动/长尾广告语义映射偏差、多目标联合训练超参调优复杂度高。

### 建议的源页面内容
```markdown
---
title: "GPR: Towards a Generative Pre-trained One-Model Paradigm for Large-Scale Advertising Recommendation"
category: "sources"
tags: ["generative-recommendation", "advertising", "end-to-end", "semantic-id", "tencent", "HHD", "HEPO", "value-alignment"]
created: "2026-04-09"
updated: "2026-04-09"
sources: []
related:
  - "../models/GPR.md"
  - "../concepts/generative_retrieval.md"
  - "../concepts/semantic_id.md"
  - "../entities/tencent.md"
  - "../methods/multi_objective_alignment.md"
confidence: "high"
status: "stable"
---

# GPR: Towards a Generative Pre-trained One-Model Paradigm for Large-Scale Advertising Recommendation

## 摘要
本文提出 GPR（Generative Pre-trained Recommender），首个面向大规模广告推荐的端到端生成式单模型范式。该工作将传统多阶段推荐流水线重构为统一的序列生成任务，通过异构分层解码器（HHD）解耦意图建模与内容生成，并结合多阶段联合训练策略（MTP、价值感知微调、HEPO）实现用户兴趣与商业价值的全局对齐。模型已在腾讯视频号广告系统全量部署，显著提升 GMV 与 CTCVR。

## 关键要点
- **架构革新**：摒弃“召回-粗排-精排”级联结构，采用端到端生成式单模型，消除阶段间目标不一致与误差累积。
- **HHD 双解码器**：上层提取深层用户意图与长期兴趣，下层基于意图自回归生成目标广告 ID，提升训练稳定性。
- **统一语义 ID**：通过层次化聚类将广告特征与自然内容映射至共享离散空间，降低词表规模并保留商业属性。
- **多阶段训练管线**：MTP 加速长序列收敛；价值感知微调对齐 eCPM/CTCVR；HEPO 引入层级强化学习优化探索-利用平衡。
- **工业验证**：腾讯视频号全量上线，验证超大规模流量下的低延迟推理与核心商业指标提升。

## 详细内容
### 1. 统一输入与分词机制
GPR 将用户历史行为、上下文特征与候选广告池统一编码为离散 Token 序列。针对广告与自然内容的异构性，设计多层级语义 ID 映射方案，通过聚类与对齐技术压缩高维稀疏特征，同时保留类目、出价倾向、转化概率等细粒度商业信号。

### 2. 异构分层解码器（HHD）
- **上层解码器**：专注于用户意图表征学习，捕获长期兴趣与上下文依赖。
- **下层解码器**：接收上层意图向量，执行自回归广告 ID 生成。显式解耦避免了单一解码器在复杂多目标场景下的梯度冲突与训练震荡。

### 3. 多阶段联合训练策略
| 阶段 | 技术 | 作用 |
|------|------|------|
| 预训练 | 多 Token 预测 (MTP) | 并行预测未来多步 Token，加速长序列建模收敛 |
| 微调 | 价值感知微调 (Value-Aware FT) | 引入广告商业价值作为辅助监督，使生成目标与平台收益对齐 |
| 策略优化 | 层级增强策略优化 (HEPO) | 结合 RL 思想设计层级奖励，动态平衡探索与利用，优化线上生成策略 |

### 4. 实验与部署
- **部署环境**：腾讯视频号（Weixin Channels）广告推荐系统
- **核心指标**：GMV 与 CTCVR 实现显著提升（具体相对增益详见论文正文）
- **系统表现**：验证了生成式架构在超大规模、高并发场景下的稳定性与毫秒级响应能力

## 局限性
- 自回归生成在超大规模候选集下的推理延迟仍需进一步优化
- 多层级语义 ID 构建依赖高质量聚类，冷启动/长尾广告映射可能存在偏差
- 多目标联合训练超参数敏感，调优与稳定性控制复杂度高

## 关联与扩展
- 与 [生成式检索](../concepts/generative_retrieval.md) 共享 Next-Token Prediction 范式，但聚焦广告商业化场景
- 价值对齐机制与 [多目标对齐](../methods/multi_objective_alignment.md) 高度相关，可视为 RLHF 在推荐收益优化中的变体
- 部署实践为 [腾讯](../entities/tencent.md) 工业推荐架构演进提供关键案例

## 参考文献
- Zhang, J., Li, Y., Liu, Y., et al. (2025). *GPR: Towards a Generative Pre-trained One-Model Paradigm for Large-Scale Advertising Recommendation*. arXiv:2511.10138.
```