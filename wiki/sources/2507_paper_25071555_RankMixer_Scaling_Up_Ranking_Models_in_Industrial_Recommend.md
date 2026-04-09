---
title: "2507 Paper 25071555 Rankmixer Scaling Up Ranking Models In Industrial Recommend"
category: "sources"
tags: ["source", "2026-04-09"]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../../raw/sources/2507_paper_25071555_RankMixer_Scaling_Up_Ranking_Models_in_Industrial_Recommend.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要
本文提出 **RankMixer**，一种面向工业推荐系统的硬件感知、高可扩展排序模型架构。针对大语言模型与大规模排序模型在工业部署中面临的严格延迟/QPS约束，以及传统手工特征交叉模块 GPU 算力利用率（MFU）低下的瓶颈，RankMixer 采用多头 Token Mixing 模块替代二次复杂度的自注意力机制，并结合 Per-token FFN 实现特征子空间独立建模与跨空间交互。通过引入稀疏 MoE 变体与动态路由策略，该架构有效缓解了专家训练不平衡问题，成功将模型参数量扩展至 10 亿级别。

在万亿级生产数据集上的实验表明，RankMixer 将模型 MFU 从 4.5% 大幅提升至 45%，在保持推理延迟不变的前提下实现参数量百倍扩展。线上 A/B 测试验证了其在推荐与广告双场景的通用性，全量流量部署后未增加服务成本，同时带来用户活跃天数 +0.3%、总使用时长 +1.08% 的显著业务收益。该工作为工业级推荐系统向大参数、高吞吐架构演进提供了可落地的工程范式。

### 需要更新的页面
- **`wiki/methods/llm_as_ranker.md`**：补充 RankMixer 作为高效工业排序架构的最新实践，添加 Token Mixing 替代 Attention 的硬件优化策略及 MoE 扩展路径。
- **`wiki/concepts/llm4rec_overview.md`**：在“工业部署挑战”部分新增延迟/QPS 约束与 MFU（模型浮点运算利用率）优化趋势，关联 RankMixer 的实证数据。
- **`wiki/synthesis/traditional_vs_llm.md`**：在架构效率对比章节加入 RankMixer 的 MFU 提升数据（4.5% → 45%）与参数扩展能力，强化传统手工特征模块向硬件感知架构演进的论点。

### 需要创建的新页面
- **`wiki/models/RankMixer.md`**：详细记录 RankMixer 架构设计（Token Mixing、Per-token FFN、Sparse-MoE、动态路由）、训练策略、工业部署指标及与现有排序模型的对比。
- **`wiki/concepts/model_flops_utilization_mfu.md`**：定义 MFU 概念，解释其在 GPU 时代推荐模型评估中的核心地位，以及低 MFU 的成因（如内存墙、不规则访存、手工特征交叉）。
- **`wiki/methods/hardware_aware_architecture.md`**：归纳面向硬件优化的推荐模型设计范式，涵盖算子融合、Token 级混合、稀疏化路由与延迟约束下的参数扩展策略。

### 矛盾/冲突
- **未发现冲突**。本文指出的“传统手工特征交叉模块在 GPU 时代 MFU 低下”与现有知识库中关于传统推荐模型扩展瓶颈的共识一致。RankMixer 的硬件感知设计是对现有 LLM-as-Ranker 范式的工程补充，而非理论对立。

### 提取的关键事实
- **模型名称**：RankMixer
- **核心架构**：多头 Token Mixing 替代自注意力；Per-token FFN 处理特征子空间与跨空间交互
- **扩展机制**：1B 参数 Sparse-MoE 变体 + 动态路由策略（解决专家训练不足与不平衡）
- **算力效率**：模型 MFU 从 4.5% 提升至 45%
- **规模扩展**：参数量扩大 100 倍，推理延迟基本保持不变
- **业务收益**：用户活跃天数 +0.3%，总 App 使用时长 +1.08%
- **部署规模**：万亿级生产数据集验证；推荐与广告双场景全量上线；服务成本零增加
- **论文信息**：arXiv:2507.15551，提交于 2025-07-21，修订于 2025-07-26

### 建议的源页面内容
```markdown
---
title: "RankMixer: Scaling Up Ranking Models in Industrial Recommenders"
category: "sources"
tags: ["source", "ranking", "MoE", "hardware-aware", "industrial", "2025-07"]
created: "2026-04-09"
updated: "2026-04-09"
sources: []
related:
  - "../models/RankMixer.md"
  - "../concepts/model_flops_utilization_mfu.md"
  - "../methods/llm_as_ranker.md"
confidence: "high"
status: "stable"
---

# RankMixer: Scaling Up Ranking Models in Industrial Recommenders

## 概述
本文提出 RankMixer，一种面向工业推荐系统的硬件感知、高可扩展排序模型架构。通过用多头 Token Mixing 替代自注意力机制，并结合 Per-token FFN 与 Sparse-MoE 动态路由，该模型在万亿级生产数据上实现了 MFU 从 4.5% 到 45% 的跃升，参数量扩展 100 倍的同时保持推理延迟不变，线上业务指标显著提升。

## 关键要点
- **痛点**：传统手工特征交叉模块在 GPU 时代存在严重的算力浪费（低 MFU），且难以满足工业级延迟与高 QPS 要求
- **架构创新**：引入多头 Token Mixing 与 Per-token FFN，实现高效特征子空间建模与跨空间交互
- **扩展策略**：1B 参数 Sparse-MoE 配合动态路由，解决专家训练不平衡问题
- **效率指标**：MFU 提升 10 倍（4.5% → 45%），参数量 ×100，延迟持平
- **业务收益**：全量部署后用户活跃天数 +0.3%，总使用时长 +1.08%，服务成本零增加

## 详情

### 核心架构设计
- **Token Mixing 替代 Attention**：摒弃 $O(N^2)$ 复杂度的自注意力，采用线性复杂度的多头 Token 混合机制，大幅降低显存占用与计算冗余
- **Per-token FFN**：为每个特征 Token 分配独立的前馈网络，保留特征子空间的独特性，同时通过跨层交互实现特征融合
- **Sparse-MoE 扩展**：将稠密架构扩展至 10 亿参数稀疏混合专家模型，提升模型容量与表达能力

### 训练与优化策略
- **动态路由（Dynamic Routing）**：针对 MoE 训练中常见的专家负载不均与部分专家欠训练问题，引入自适应路由权重调整机制
- **硬件感知优化**：算子设计与内存布局针对现代 GPU 架构定制，最大化并行度与内存带宽利用率

### 实验与工业部署
- **数据集**：万亿级规模生产交互数据
- **离线指标**：MFU 从 4.5% 提升至 45%；参数量扩展 100 倍，推理延迟维持原水平
- **线上 A/B 测试**：覆盖推荐与广告两大核心场景
- **全量上线**：1B 稠密参数版本 RankMixer 已全量服务，未增加额外推理成本，实现用户活跃天数 +0.3%、总使用时长 +1.08%

## 关联
- [RankMixer 模型](../models/RankMixer.md) 详细架构与实现细节
- [模型浮点运算利用率 MFU](../concepts/model_flops_utilization_mfu.md) 评估概念解析
- [LLM-as-Ranker](../methods/llm_as_ranker.md) 排序范式与工业扩展路径

## 开放问题
- Token Mixing 在极端长序列推荐场景下的信息衰减边界尚未明确
- 动态路由策略在冷启动或分布外（OOD）流量下的稳定性需进一步验证
- 1B 参数 MoE 版本在边缘设备或低算力集群的部署可行性待探索

## 参考文献
- Zhu, J., Fan, Z., Zhu, X., et al. (2025). *RankMixer: Scaling Up Ranking Models in Industrial Recommenders*. arXiv:2507.15551.
- 原始链接：https://arxiv.org/abs/2507.15551
```