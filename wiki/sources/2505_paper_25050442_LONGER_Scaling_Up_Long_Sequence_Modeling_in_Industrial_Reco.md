---
title: "2505 Paper 25050442 Longer Scaling Up Long Sequence Modeling In Industrial Reco"
category: "sources"
tags: ["source", "2026-04-09"]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../../raw/sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要
本文介绍了字节跳动提出的 **LONGER**（Long-sequence Optimized traNsformer for GPU-Efficient Recommenders），旨在解决工业推荐系统中超长用户行为序列建模的计算效率瓶颈与上下游不一致问题。传统两阶段检索或间接建模范式难以在捕获长短期偏好的同时满足实时推理延迟要求。LONGER 通过引入全局 Token 机制稳定长上下文注意力，结合 Token 融合模块、轻量级 InnerTransformer 与混合注意力策略，有效打破了 Transformer 的二次计算复杂度限制。此外，论文系统总结了混合精度训练、激活重计算、KV Cache 服务以及全同步训练/推理框架等底层工程优化，实现了 GPU 密集型计算与稀疏参数更新的统一调度。

实验表明，LONGER 在离线评估与线上 A/B 测试中均显著优于现有强基线，覆盖广告与电商核心业务。该模型已在字节跳动超过 10 个重要场景中全量部署，服务十亿级用户，实证了推荐系统中序列模型规模化扩展的工业 Scaling Law。该工作虽聚焦于判别式 Transformer 架构，但其长上下文处理范式、推理加速策略与大规模部署经验，为 LLM 在推荐场景中的长序列理解、高效微调与工业级落地提供了直接可迁移的架构参考。

### 需要更新的页面
- **`wiki/concepts/sequential_recommendation.md`**：补充“超长序列建模（Ultra-long Sequence Modeling）”的技术挑战与 LONGER 的解决方案，更新工业级序列推荐的技术栈演进路径。
- **`wiki/concepts/scaling_laws_recsys.md`**：补充 LONGER 验证的工业 Scaling Law 证据，说明序列长度扩展、模型容量与业务指标（CTR/CVR/停留时长）之间的正向映射关系。
- **`wiki/entities/tencent.md`** & **`wiki/entities/kuaishou.md`**：在“工业部署对比”章节追加字节跳动 LONGER 的部署规模（>10 场景、十亿用户），形成多厂牌长序列/生成式推荐部署的横向对照。

### 需要创建的新页面
- **`wiki/models/LONGER.md`**：详细记录 LONGER 模型架构、核心模块（Global Token、Token Merge、Hybrid Attention）、工程优化管线及线上业务指标。
- **`wiki/methods/long_context_efficiency.md`**：归纳长上下文高效建模技术栈，涵盖 KV Cache 优化、激活重计算、全同步训练/服务框架、混合注意力机制。
- **`wiki/entities/bytedance.md`**：记录字节跳动推荐系统团队在长序列建模、工业级 Transformer/LLM 部署与 Scaling Law 验证方面的实践与论文贡献。

### 矛盾/冲突
- **未发现冲突**。该工作聚焦于判别式/Transformer 架构的序列优化与工程加速，与知识库中现有的生成式推荐（Generative Rec）文献形成互补。两者共同指向 LLM4Rec 的核心挑战：“长上下文理解”与“工业级推理效率”。LONGER 的工程优化策略可直接迁移至 LLM-as-Ranker/Generator 的部署管线中。

### 提取的关键事实
- 论文发表于 RecSys '25，arXiv:2505.04421（v2, 2025-07）。
- 核心痛点：两阶段检索导致上下游目标不一致；长序列 Transformer 存在 $O(L^2)$ 复杂度瓶颈。
- 架构创新 1：**全局 Token 机制**，用于稳定超长上下文下的注意力分布。
- 架构创新 2：**Token Merge 模块 + 轻量 InnerTransformer + 混合注意力策略**，显著降低计算与显存开销。
- 工程创新：混合精度训练、激活重计算、KV Cache 服务、**全同步训练/推理框架**（统一 GPU 密集与稀疏参数更新）。
- 业务效果：离线指标与线上 A/B 测试全面领先，覆盖广告与电商场景。
- 部署规模：字节跳动 >10 个核心场景全量部署，服务十亿级用户。
- 理论贡献：实证了推荐系统中序列模型的工业 Scaling Law，验证了“更长序列+更大容量→更高业务收益”的扩展规律。

### 建议的源页面内容

```markdown
---
title: "2505 Paper 25050442 LONGER Scaling Up Long Sequence Modeling in Industrial Recommenders"
category: "sources"
tags: ["source", "long-sequence", "transformer", "industrial", "efficiency", "bytedance", "scaling-law", "2026-04-09"]
created: "2026-04-09"
updated: "2026-04-09"
sources: []
related:
  - "../models/LONGER.md"
  - "../methods/long_context_efficiency.md"
  - "../concepts/sequential_recommendation.md"
  - "../concepts/scaling_laws_recsys.md"
  - "../entities/bytedance.md"
confidence: "high"
status: "stable"
---

# 2505 Paper 25050442 LONGER Scaling Up Long Sequence Modeling in Industrial Recommenders

## 概述
本文档为 arXiv:2505.04421 的摘要与结构化解析页面。论文提出 LONGER 模型，通过架构创新与底层工程优化解决工业推荐系统中超长用户行为序列建模的效率与一致性问题。该工作已在字节跳动大规模部署，验证了序列模型在推荐场景中的工业 Scaling Law。

## 关键要点
- **问题定义**：传统两阶段检索范式存在上下游不一致，且长序列 Transformer 面临二次复杂度瓶颈，难以满足工业实时性要求。
- **核心架构**：引入全局 Token 稳定长上下文注意力；通过 Token Merge、轻量 InnerTransformer 与混合注意力策略降低计算复杂度。
- **工程优化**：集成混合精度、激活重计算、KV Cache 服务与全同步训练/推理框架，实现 GPU 密集与稀疏参数的高效统一。
- **工业验证**：在广告与电商场景离线/线上全面领先，部署于 >10 个核心业务，服务十亿级用户。
- **Scaling Law**：实证了序列长度扩展与模型容量增长对业务指标的正向驱动作用。

## 详情

### 1. 架构设计
- **全局 Token 机制 (Global Token Mechanism)**：在注意力计算中注入可学习的全局表征，缓解超长序列下的注意力稀释与梯度消失问题，提升长程依赖捕获稳定性。
- **Token 融合与混合注意力 (Token Merge & Hybrid Attention)**：
  - 通过轻量级 InnerTransformer 对局部 Token 进行降维与融合。
  - 结合局部窗口注意力与全局稀疏注意力，将复杂度从 $O(L^2)$ 降至近似线性，兼顾精度与吞吐量。

### 2. 系统工程优化
- **训练加速**：采用混合精度训练 (Mixed-Precision) 与激活重计算 (Activation Recomputation)，在有限显存下支持更长序列 batch。
- **推理服务**：引入 KV Cache 持久化与动态管理，减少重复计算；构建全同步训练/服务框架，消除传统异步架构中的参数版本漂移与延迟抖动。
- **参数调度**：统一 GPU 上的密集（Dense）与稀疏（Sparse）参数更新流水线，提升硬件利用率。

### 3. 实验与部署结果
- **离线评估**：在标准工业数据集上，NDCG、GAUC 等核心指标显著优于现有两阶段与长序列基线。
- **线上 A/B 测试**：在广告点击率、电商转化率及用户停留时长等核心业务指标上取得统计学显著提升。
- **规模化部署**：已全量上线字节跳动 >10 个高流量场景，日均服务十亿级用户请求，系统延迟与资源消耗控制在工业可接受范围内。

### 4. 对 LLM4Rec 的启示
- **长上下文迁移**：LLM 在推荐中同样面临长行为序列的上下文窗口限制，LONGER 的注意力优化与 KV Cache 策略可直接应用于 LLM-as-Ranker/Generator 的推理加速。
- **Scaling Law 验证**：为“更大参数/更长序列 → 更好推荐效果”提供了工业级实证，支持 LLM 在推荐管线中继续扩大上下文窗口与模型规模。
- **端到端一致性**：全同步训练/服务框架为 LLM 推荐系统的端到端微调与在线服务提供了架构参考，减少检索-排序割裂带来的性能损失。

## 关联
- [LONGER 模型](../models/LONGER.md)：详细架构与模块实现
- [长上下文高效建模方法](../methods/long_context_efficiency.md)：KV Cache、混合注意力与工程优化汇总
- [序列推荐](../concepts/sequential_recommendation.md)：长序列建模挑战与技术演进
- [推荐系统 Scaling Law](../concepts/scaling_laws_recsys.md)：模型规模、序列长度与业务收益关系
- [字节跳动推荐实践](../entities/bytedance.md)：工业部署与团队贡献

## 开放问题
- **与 LLM 生成式范式的融合**：LONGER 的判别式优化策略如何与 LLM 的自回归生成/指令微调结合？是否存在架构冲突或协同增益？
- **动态序列截断策略**：在十亿级用户场景下，如何根据用户活跃度动态分配序列长度与计算预算？
- **跨域泛化能力**：该架构在冷启动或跨业务域（如从短视频迁移至本地生活）时的迁移效率与微调成本尚未充分披露。

## 参考文献
- Chai, Z., Ren, Q., Xiao, X., et al. (2025). *LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders*. Proceedings of the 19th ACM Conference on Recommender Systems (RecSys '25). arXiv:2505.04421.
- 原始链接：https://arxiv.org/abs/2505.04421
- 期刊/会议：RecSys '25 (September 2025, Prague)
```