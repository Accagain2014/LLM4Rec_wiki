---
title: "2511 Paper 25110607 Make It Long, Keep It Fast End-To-End 10K-Sequence Modeling"
category: "sources"
tags: ["source", "2026-04-09"]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../../raw/sources/2511_paper_25110607_Make_It_Long,_Keep_It_Fast_End-to-End_10k-Sequence_Modeling.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要
本文提出了一套面向工业级短视频推荐系统的端到端长序列建模方案，成功在抖音（Douyin）十亿级用户流量下将历史行为序列长度扩展至 10k，同时严格满足线上延迟与算力预算。核心创新包括三项：引入堆叠目标-历史交叉注意力（STCA）替代传统历史自注意力，将序列复杂度从二次方降至线性；设计请求级批处理（RLB）机制，通过聚合同一用户/请求的多个目标共享用户侧编码，显著降低存储、通信与计算开销；提出长度外推训练策略，在较短窗口上训练即可直接推理超长序列，无需额外训练成本。

线上全量部署结果表明，该系统在关键互动指标上取得显著提升，且随着历史序列长度与模型容量的增加，性能呈现可预测的单调增长，验证了推荐系统中类似大语言模型的 Scaling Law 行为。该工作为工业界在严格延迟约束下规模化应用端到端长序列推荐提供了可复现的工程与算法范式。

### 需要更新的页面
- **`wiki/entities/bytedance.md`**：当前为占位页面。需补充抖音长序列推荐系统的工业部署细节（十亿级流量、10k 序列长度、延迟达标、业务指标提升）及核心作者团队信息。
- **`wiki/methods/long_context_efficiency.md`**：当前为占位页面。需将 STCA（线性复杂度交叉注意力）、RLB（请求级批处理共享编码）及长度外推训练作为工业级长上下文效率优化的核心方法纳入。
- **`wiki/concepts/scaling_laws_recsys.md`**：当前为占位页面。需补充本文实证发现：推荐系统中历史序列长度与模型容量扩展可带来可预测、单调的性能收益，与 LLM Scaling Law 高度一致。

### 需要创建的新页面
- **`wiki/methods/stca_rlb_optimization.md`**：详细记录 STCA 与 RLB 的架构设计、复杂度分析、工程实现细节及在抖音推荐流中的具体收益，作为长序列效率优化的专项方法页。
- **`wiki/sources/2511_paper_25110607_Make_It_Long,_Keep_It_Fast_End-to-End_10k-Sequence_Modeling.md`**：本源的标准化摘要页（内容见下文）。

### 矛盾/冲突
- 未发现与现有知识库内容的矛盾。本文结论与 `LONGER`、`ULTRA_HSTU` 等工业长序列工作方向一致，且首次明确在十亿级流量下验证了推荐场景的 Scaling Law 行为，属于对现有知识的有效补充而非冲突。

### 提取的关键事实
- **部署规模**：抖音全量线上流量，覆盖十亿级用户。
- **序列长度**：端到端支持 10k 历史行为序列建模。
- **STCA（Stacked Target-to-History Cross Attention）**：用目标到历史的堆叠交叉注意力替代历史自注意力，复杂度从 $O(L^2)$ 降至 $O(L)$，支持高效端到端训练。
- **RLB（Request Level Batching）**：用户中心批处理策略，聚合同一请求的多个目标共享用户侧编码，降低存储、通信与计算成本，不改变学习目标。
- **长度外推训练**：在短窗口训练，直接推理长窗口（10k），无需额外训练成本即可泛化。
- **性能表现**：关键互动指标显著提升，严格满足生产延迟预算。
- **Scaling Law 验证**：历史长度与模型容量扩展带来可预测、单调的收益，复现了 LLM 的缩放规律。
- **作者机构**：字节跳动/抖音推荐算法团队。

### 建议的源页面内容
```markdown
---
title: "Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling at Billion Scale on Douyin"
category: "sources"
tags: ["long-sequence", "douyin", "stca", "rlb", "scaling-law", "industrial-deployment", "efficiency"]
created: "2026-04-09"
updated: "2026-04-09"
sources: []
related: 
  - "../methods/long_context_efficiency.md"
  - "../methods/stca_rlb_optimization.md"
  - "../concepts/scaling_laws_recsys.md"
  - "../entities/bytedance.md"
confidence: "high"
status: "stable"
---

# Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling at Billion Scale on Douyin

## 摘要
本文提出了一套面向工业级短视频推荐系统的端到端长序列建模架构，在抖音十亿级流量下成功将用户历史行为序列扩展至 10k，同时满足严格的线上延迟与算力约束。通过引入 STCA 交叉注意力、RLB 请求级批处理及长度外推训练策略，系统实现了线性复杂度与高效推理，并在线上验证了推荐场景中序列长度与模型容量的 Scaling Law 行为。

## 关键要点
- **STCA 架构**：用堆叠目标-历史交叉注意力替代历史自注意力，复杂度降至 $O(L)$。
- **RLB 批处理**：同一用户请求多目标共享用户侧编码，大幅降低存储/通信/计算开销。
- **长度外推训练**：短窗训练、长窗推理，零额外训练成本实现 10k 泛化。
- **工业部署**：抖音全量上线，十亿级用户，关键互动指标显著提升且延迟达标。
- **Scaling Law 实证**：历史长度与模型容量扩展带来可预测、单调的性能收益。

## 详情

### 核心方法
1. **Stacked Target-to-History Cross Attention (STCA)**
   - 传统序列模型依赖历史自注意力（$O(L^2)$），在 10k 长度下计算与显存开销不可接受。
   - STCA 将计算范式转为从目标 Item 到历史序列的交叉注意力，通过多层堆叠捕获高阶交互，复杂度严格线性 $O(L)$。
   - 支持端到端训练，无需分阶段检索-排序流水线。

2. **Request Level Batching (RLB)**
   - 工业推荐单次请求通常包含多个候选目标（如 Feed 流多卡位）。
   - RLB 将同一用户/请求下的多个目标聚合，复用已计算的用户侧历史编码。
   - 在不改变损失函数与学习目标的前提下，显著削减 KV Cache 存储、跨节点通信与重复计算。

3. **Length-Extrapolative Training Strategy**
   - 训练阶段使用较短历史窗口（如 1k-2k），推理阶段直接扩展至 10k。
   - 模型通过位置编码外推与注意力掩码设计，实现长度泛化，避免长序列训练带来的数据稀疏与算力浪费。

### 部署与实验结果
- **线上规模**：抖音全量真实流量，覆盖十亿级日活用户。
- **延迟表现**：在严格的生产 SLA 下保持端到端推理延迟达标。
- **业务指标**：关键互动指标（停留时长、点击率、转化率）取得显著提升。
- **Scaling 规律**：离线与在线实验均显示，随着历史序列长度与模型参数量的增加，性能呈现可预测的单调增长，行为特征与大语言模型的 Scaling Law 高度一致。

## 关联
- 与 [长上下文效率优化](../methods/long_context_efficiency.md) 中的工业实践形成互补，提供具体的注意力与批处理实现。
- 为 [推荐系统中的 Scaling Law](../concepts/scaling_laws_recsys.md) 提供了首个十亿级流量下的实证支撑。
- 属于 [字节跳动/抖音](../entities/bytedance.md) 推荐系统工业部署的重要案例。

## 开放问题
- STCA 在跨模态（视频/音频/文本）长序列中的泛化能力尚未充分验证。
- RLB 在动态请求长度波动场景下的自适应批处理策略仍需优化。
- 长度外推训练在极端长尾用户（历史极稀疏）上的稳定性与校准方法待研究。

## 参考文献
- Guan, L., Yang, J.-Q., Zhao, Z., et al. (2025). *Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling at Billion Scale on Douyin*. arXiv:2511.06077.
- 关联工业工作：[LONGER](../models/LONGER.md), [ULTRA_HSTU](../models/ULTRA_HSTU.md)
```