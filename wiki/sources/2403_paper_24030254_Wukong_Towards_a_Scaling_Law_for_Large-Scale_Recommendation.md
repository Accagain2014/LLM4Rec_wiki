---
title: "2403 Paper 24030254 Wukong Towards A Scaling Law For Large-Scale Recommendation"
category: "sources"
tags: ["source", "2026-04-09"]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../../raw/sources/2403_paper_24030254_Wukong_Towards_a_Scaling_Law_for_Large-Scale_Recommendation.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要
Wukong 论文首次在推荐系统领域验证了缩放定律（Scaling Laws），打破了传统推荐模型在参数量与计算量扩大时性能易饱和或退化的瓶颈。该工作提出了一种极简的纯堆叠分解机（Factorization Machines, FM）架构，摒弃了复杂的显式交叉网络、注意力机制或手工特征工程，仅通过纵向堆叠 FM 层即可自适应捕获任意阶特征交互。

配合其设计的“协同扩展策略”（Synergistic Upscaling），该架构在同步扩展网络深度与宽度时，通过特定的参数初始化、层归一化与学习率调度保持优化曲面平滑。实验表明，当模型计算复杂度跨越两个数量级（突破 100 GFLOP/样本）时，推荐质量仍保持稳定的单调上升趋势。该研究为工业级推荐系统的算力规划、架构选型及“轻量级大推荐模型”路径提供了坚实的理论依据。

### 需要更新的页面
- **`wiki/concepts/scaling_laws_recsys.md`**：补充 Wukong 作为推荐领域首个确立缩放定律的里程碑工作；更新 100+ GFLOP 阈值下的单调增益数据；增加“纯 FM 堆叠 vs Transformer 扩展”的对比视角。
- **`wiki/synthesis/traditional_vs_llm.md`**：在架构范式讨论中引入 Wukong 的发现，说明推荐系统无需盲目依赖庞大 Transformer 结构，合理的架构简化与协同扩展同样可逼近大模型规模下的性能上限。
- **`wiki/index.md` & `wiki/log.md`**：按工作流规范追加新页面条目与 `ingest` 操作日志。

### 需要创建的新页面
- **`wiki/models/Wukong.md`**：记录 Wukong 模型架构、纯 FM 堆叠设计原理、协同扩展策略实现细节及在公开/工业数据集上的缩放实验结果。
- **`wiki/methods/synergistic_upscaling.md`**：详细阐述协同扩展策略的数学/工程实现（深度/宽度同步比例、初始化方案、归一化位置、学习率衰减机制），作为大模型/大推荐系统扩展的通用方法参考。
- **`wiki/sources/2403_paper_24030254_Wukong_Towards_a_Scaling_Law_for_Large-Scale_Recommendation.md`**：本文档对应的源摘要页（完整内容见下方）。

### 矛盾/冲突
- **未发现直接事实冲突**。但存在**架构范式张力**：当前 LLM4Rec 工业实践（如 ULTRA-HSTU、LONGER、OneRec 系列）普遍依赖 Transformer/MoE 架构进行扩展，而 Wukong 证明纯 FM 堆叠在同等规模下同样有效且计算路径更轻量。这并非矛盾，而是提供了“架构简化+协同扩展”的替代路径，需在相关页面中作为对比视角明确标注，避免读者误认为 Transformer 是扩展的唯一路径。

### 提取的关键事实
- 首次在推荐系统中建立可预测的 Scaling Law，证明“规模扩大→质量提升”的幂律关系在推荐领域成立。
- 核心架构为纯堆叠 Factorization Machines (FM)，无显式交叉网络或注意力模块，依靠深度累积自然涌现高阶交互。
- 提出“协同扩展策略”（Synergistic Upscaling），同步扩展网络深度与隐藏层维度，配合特定初始化、层归一化与 LR 调度保持梯度稳定。
- 实验验证：在 6 个公开基准数据集上 AUC/LogLoss 一致超越 SOTA；内部超大规模测试中，计算复杂度提升两个数量级（>100 GFLOP/样本）时性能仍单调上升。
- 局限性：未深入探讨分布式训练通信瓶颈、显存优化、在线推理延迟；对极度稀疏长尾特征、动态兴趣漂移及多模态场景的泛化能力待验证。
- 对 LLM4Rec 启示：为算力分配、数据配比与模型选型提供量化决策依据；揭示特征交互能力可通过深度堆叠涌现，与 LLM 上下文学习机制高度同构。

### 建议的源页面内容

```markdown
---
title: "Wukong: Towards a Scaling Law for Large-Scale Recommendation"
category: "sources"
tags: ["scaling-law", "factorization-machine", "synergistic-upscaling", "Wukong", "Meta", "arXiv-2024"]
created: "2026-04-09"
updated: "2026-04-09"
sources: []
related:
  - "../concepts/scaling_laws_recsys.md"
  - "../models/Wukong.md"
  - "../methods/synergistic_upscaling.md"
  - "../concepts/unified_transformer_backbone.md"
confidence: "high"
status: "stable"
---

# Wukong: Towards a Scaling Law for Large-Scale Recommendation

## 概述
本文首次在推荐系统领域验证了缩放定律（Scaling Laws），提出了一种基于纯堆叠分解机（FM）的极简架构与协同扩展策略。研究证明，推荐模型在计算复杂度跨越两个数量级（突破 100 GFLOP/样本）时仍能保持性能单调增长，为工业级大推荐模型的算力规划与架构简化提供了理论依据。

## 关键要点
- **首个推荐缩放定律**：打破传统推荐模型规模扩大易饱和的瓶颈，确立“规模→质量”的可预测幂律关系。
- **纯 FM 堆叠架构**：摒弃显式交叉网络与注意力机制，通过纵向堆叠 FM 层自适应捕获任意阶特征交互。
- **协同扩展策略**：同步调整深度与宽度，配合特定初始化、归一化与学习率调度，保障极端规模下的优化稳定性。
- **100+ GFLOP 单调增益**：在超大规模工业测试中，计算量提升两个数量级仍保持推荐质量稳定上升。
- **架构范式启示**：挑战 Transformer 中心主义，证明合理简化+协同扩展同样可逼近大模型性能上限。

## 详细内容

### 核心架构：纯 FM 堆叠
Wukong 完全由堆叠的 Factorization Machines 层构成。与传统模型依赖 DCN、xDeepFM 或序列注意力不同，该架构采用统一的 FM 块进行纵向堆叠。每一层独立进行特征嵌入与二阶交互计算，通过残差连接与非线性激活传递信息。高阶交互能力不依赖硬编码模块，而是随网络深度累积自然涌现。

### 协同扩展策略 (Synergistic Upscaling)
实现缩放定律的关键在于扩展过程的系统性控制：
- **深度/宽度同步**：按比例同步增加网络层数与隐藏层维度，避免单一维度扩展导致的表征瓶颈或优化困难。
- **优化稳定性保障**：采用特定的参数初始化方案、层归一化（LayerNorm）位置调整与学习率衰减调度，确保参数量指数级增长时梯度传播平滑、损失曲面稳定。
- **可预测增益函数**：将扩展操作转化为可拟合的幂律函数，使算力投入与性能提升具备明确的映射关系。

### 实验结果
- **公开基准**：在 6 个标准数据集上，AUC 与 LogLoss 指标一致超越当前 SOTA 模型。
- **工业扩展测试**：模型复杂度从基础规模逐步提升至 **100+ GFLOP/样本**（跨越两个数量级），性能保持严格单调上升。传统基线在同等阈值下已出现饱和或退化。
- **效率对比**：在同等计算预算下，Wukong 的架构复杂度显著低于 Transformer/MoE 方案，训练吞吐与收敛稳定性更优。

### 局限性与未来方向
- 未深入探讨超大规模分布式训练中的通信开销、显存优化策略及在线推理延迟控制。
- 纯 FM 堆叠在极度稀疏长尾特征、动态用户兴趣漂移、多模态/跨域场景下的泛化能力仍需验证。
- 未来可结合动态路由、稀疏化训练或混合专家（MoE）机制进一步提升扩展效率与部署可行性。

## 关联页面
- [推荐系统中的缩放定律](../concepts/scaling_laws_recsys.md)
- [Wukong 模型架构](../models/Wukong.md)
- [协同扩展策略](../methods/synergistic_upscaling.md)
- [统一 Transformer 骨干网络](../concepts/unified_transformer_backbone.md)（对比视角）

## 开放问题
- 纯 FM 堆叠架构在千亿参数规模下的分布式训练通信瓶颈如何突破？
- 协同扩展策略是否可迁移至多模态推荐或生成式检索（Generative Retrieval）场景？
- 如何将 Wukong 的缩放规律与 LLM4Rec 的指令微调/偏好对齐阶段进行联合算力规划？

## 参考文献
- Zhang, B., et al. (2024). *Wukong: Towards a Scaling Law for Large-Scale Recommendation*. arXiv:2403.02545.
- 相关工业实践参考：[ULTRA-HSTU](../models/ULTRA_HSTU.md), [LONGER](../models/LONGER.md), [OneRec](../models/OneRec.md)
```