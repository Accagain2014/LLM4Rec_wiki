---
title: "2508 Paper 25082090 Onerec-V2 Technical Report"
category: "sources"
tags: ["source", "2026-04-09"]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../../raw/sources/2508_paper_25082090_OneRec-V2_Technical_Report.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要
OneRec-V2 技术报告针对 OneRec-V1 在工业部署中暴露的两大核心瓶颈——计算资源分配极度不均（97.66% 消耗于序列编码）以及强化学习仅依赖奖励模型的局限性——提出了系统性升级方案。该版本首创 Lazy Decoder-Only 架构，彻底消除编码器瓶颈，使总计算量降低 94%，训练资源需求下降 90%，并成功将模型规模扩展至 8B 参数。同时，引入基于真实用户交互的偏好对齐机制，结合 Duration-Aware Reward Shaping 与 Adaptive Ratio Clipping，实现多目标推荐的有效平衡。在快手的大规模 A/B 测试中，OneRec-V2 使 App 停留时长显著提升 0.467% 至 0.741%，标志着端到端生成式推荐在可扩展性与真实业务对齐方面取得关键突破。

### 需要更新的页面
- **`wiki/models/OneRec.md`**：补充 V2 的架构演进路线、Lazy Decoder 设计动机、8B 扩展能力及快手线上指标，将页面升级为 `OneRec 系列` 综述页。
- **`wiki/entities/kuaishou.md`**：追加 OneRec-V2 在快手的最新工业部署数据（停留时长 +0.467%/0.741%），更新技术团队贡献记录与业务场景。
- **`wiki/entities/guorui_zhou.md`**：添加其作为 OneRec-V2 核心负责人/第一作者的最新贡献，强化其在生成式推荐规模化与真实反馈对齐方向的学术与工业领导力。
- **`wiki/methods/lazy_ar.md`**：补充 OneRec-V2 中 Lazy Decoder-Only 架构的具体实现路径与工业级收益（计算降低 94%、训练资源降 90%），作为该方法的标杆落地案例。
- **`wiki/methods/reward_modeling_rec.md`**：新增 Duration-Aware Reward Shaping 与 Adaptive Ratio Clipping 技术细节，说明其如何将隐式时长反馈转化为强化学习优化信号。

### 需要创建的新页面
- **`wiki/models/OneRec-V2.md`**：独立记录 OneRec-V2 的架构设计、对齐策略、实验设置与工业指标，与 V1 形成版本对照与演进追踪。
- **`wiki/methods/duration_aware_reward.md`**：详细阐述时长感知奖励塑形机制，解释其如何将连续型停留时长离散化/归一化并融入 RLHF/RLAIF 流程。
- **`wiki/sources/2508_paper_25082090_OneRec-V2_Technical_Report.md`**：本源的完整摘要页（见下方完整内容）。

### 矛盾/冲突
- **未发现冲突**。OneRec-V2 明确针对 V1 的已知瓶颈进行优化，属于技术迭代而非范式冲突。现有知识库中关于“生成式推荐计算开销大”、“RL 依赖模拟奖励导致分布偏移”的论述与此高度一致，且 V2 的解决方案直接回应了这些开放问题。

### 提取的关键事实
- OneRec-V1 存在严重计算瓶颈：97.66% 的 FLOPs 用于序列编码，仅 2.34% 用于自回归生成。
- Lazy Decoder-Only 架构消除独立编码器，总计算量降低 94%，训练资源降低 90%。
- 模型规模成功扩展至 8B 参数，验证了生成式推荐的可扩展性（Scaling Law）。
- 引入 Duration-Aware Reward Shaping 和 Adaptive Ratio Clipping 进行真实交互偏好对齐，摆脱纯奖励模型依赖。
- 快手线上 A/B 测试显示 App 停留时长提升 0.467% / 0.741%，并有效平衡多目标推荐。
- 核心作者：Guorui Zhou, Hengrui Hu, Hongtao Cheng 等（共 75 人）。
- 提交/修订时间：2025-08-28 提交，2025-10-28 更新至 v4。
- 定位：端到端生成式推荐系统的可扩展性与真实反馈对齐。

### 建议的源页面内容
```markdown
---
title: "OneRec-V2 Technical Report"
category: "sources"
tags: ["OneRec", "generative-rec", "lazy-decoder", "preference-alignment", "industrial-deployment", "kuaishou"]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../raw/sources/2508_paper_25082090_OneRec-V2_Technical_Report.md"]
related:
  - "../models/OneRec.md"
  - "../models/OneRec-V2.md"
  - "../methods/lazy_ar.md"
  - "../methods/reward_modeling_rec.md"
  - "../entities/kuaishou.md"
confidence: "high"
status: "stable"
---

# OneRec-V2 Technical Report

## 概述
本报告系统阐述了 OneRec 系列生成式推荐框架的第二代版本（OneRec-V2）。针对 V1 版本在工业部署中暴露的计算资源分配失衡与强化学习对齐局限，V2 提出 Lazy Decoder-Only 架构与基于真实交互的偏好对齐策略，成功将模型扩展至 8B 参数，并在快手线上实现停留时长显著提升。

## 核心要点
- **计算瓶颈突破**：V1 中 97.66% 的计算消耗于序列编码，V2 通过 Lazy Decoder-Only 架构消除编码器，总计算量降低 94%，训练资源下降 90%。
- **规模扩展**：架构优化使模型成功扩展至 8B 参数，验证了生成式推荐在大规模参数下的 Scaling 潜力。
- **真实偏好对齐**：摒弃纯奖励模型依赖，引入 Duration-Aware Reward Shaping 与 Adaptive Ratio Clipping，直接利用真实用户停留时长优化策略。
- **工业验证**：快手大规模 A/B 测试显示 App 停留时长提升 0.467% / 0.741%，多目标推荐平衡性显著改善。
- **端到端范式**：进一步巩固了“检索-排序-生成”统一为单一自回归任务的工业可行性。

## 详情

### 1. 背景与动机
OneRec-V1 虽在端到端生成式推荐中取得初步成功，但在工业级部署中面临两大挑战：
1. **计算分配极度不均**：序列编码阶段占用 97.66% 的 FLOPs，生成阶段仅占 2.34%，导致 Model FLOPs Utilization (MFU) 极低。
2. **强化学习对齐局限**：过度依赖离线训练的奖励模型（Reward Model），难以捕捉动态、细粒度的真实用户偏好，易引发分布偏移。

### 2. Lazy Decoder-Only 架构
- **设计原理**：将传统 Encoder-Decoder 结构中的独立编码器移除，改为在解码器内部通过层间依赖放松（Lazy Dependency）隐式处理上下文。
- **性能收益**：
  - 总计算量降低 **94%**
  - 训练资源需求降低 **90%**
  - 支持参数规模平滑扩展至 **8B**
  - 显著提升训练吞吐量与推理延迟表现

### 3. 偏好对齐策略
- **Duration-Aware Reward Shaping**：将连续型停留时长映射为离散奖励信号，通过非线性变换放大高价值交互的梯度贡献。
- **Adaptive Ratio Clipping**：在策略优化过程中动态调整裁剪阈值，防止奖励塑形导致的策略崩溃（Policy Collapse），提升训练稳定性。
- **数据源**：直接利用线上真实用户交互日志，替代纯模拟或静态标注数据。

### 4. 实验与工业部署
- **离线评估**：在标准推荐基准上验证架构有效性，NDCG@K 与 Recall@K 均优于 V1 及传统两阶段基线。
- **线上 A/B 测试（快手）**：
  - App 停留时长提升：**+0.467% / +0.741%**
  - 多目标优化：在点击率、转化率与时长之间实现更优 Pareto 前沿
  - 部署规模：支持亿级日活场景下的实时生成推理

## 关联
- 架构演进：[OneRec](../models/OneRec.md) → [OneRec-V2](../models/OneRec-V2.md)
- 核心方法：[懒自回归解码器](../methods/lazy_ar.md)、[奖励建模](../methods/reward_modeling_rec.md)
- 工业落地：[快手](../entities/kuaishou.md)
- 相关研究：[OneRec-Think](../models/OneRec-Think.md)（侧重推理增强，V2 侧重架构与对齐）

## 开放问题
- Lazy Decoder 在超长序列（>10k tokens）下的注意力稀疏化策略是否需进一步优化？
- Duration-Aware Reward 对冷启动用户或新物品的泛化能力尚未充分披露。
- 8B 模型在边缘设备或低延迟场景下的量化/蒸馏方案仍需探索。

## 参考文献
- Zhou, G., Hu, H., Cheng, H., et al. (2025). *OneRec-V2 Technical Report*. arXiv:2508.20900.
- 原始链接：https://arxiv.org/abs/2508.20900
- 版本历史：v1 (2025-08-28) → v4 (2025-10-28)
```