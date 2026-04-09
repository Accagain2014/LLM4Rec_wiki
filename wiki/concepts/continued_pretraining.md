---
title: "Continued Pretraining — Domain Adaptation for LLM-based Recommendation"
category: "concepts"
tags: [continued pretraining, domain adaptation, co-pretraining, LLM4Rec, catastrophic forgetting, OpenOneRec]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/2512_paper_25122476_OpenOneRec_Technical_Report.md"]
related:
  - "../models/OpenOneRec.md"
  - "../concepts/llm4rec_training_paradigms.md"
  - "../methods/continual_learning_rec.md"
  - "../concepts/evaluation_llm4rec.md"
confidence: "high"
status: "stable"
---

# 持续预训练 — 面向 LLM 推荐的领域自适应

## 概述

持续预训练（也称为协同预训练或领域自适应预训练）是面向基于 LLM 推荐系统的关键训练范式。在获得通用 LLM 后，持续预训练将模型暴露于**领域特定数据**（用户交互、物品目录、推荐特定文本），同时保持模型的通用知识。这弥合了通用语言理解与推荐特定能力之间的差距。OpenOneRec 技术报告证明，持续预训练使推荐能力能够**可预测地扩展**，同时**缓解通用知识的灾难性遗忘**——这是将 LLM 适配到专业领域时的关键挑战。

## 要点

- **领域适配桥梁**：将通用 LLM 转变为具备推荐能力的模型
- **灾难性遗忘缓解**：在学习推荐模式的同时保持通用知识
- **可预测扩展**：推荐能力随更多数据/计算可预测地提升
- **训练流水线**：数据处理 → 协同预训练 → 后训练（SFT + 对齐）
- **OpenOneRec 验证**：使用来自 16 万用户的 9600 万交互进行持续预训练
- **基础模型创建**：产出 OneRec-Foundation（1.7B、8B）等模型

## 详情

### 为什么需要持续预训练

通用 LLM 在推荐方面有两个局限：

1. **领域差距**：LLM 在通用文本上训练，但缺乏对推荐特定模式（用户行为序列、物品目录、交互历史）的暴露
2. **知识差距**：LLM 缺乏世界知识与推荐模式的整合——它们作为领域专家运作，但没有更广泛的理解

持续预训练通过在保留通用能力的同时将模型暴露于推荐数据来解决这两个问题。

### 训练流水线

OpenOneRec 框架定义了一个全面的三阶段流水线：

```
Stage 1: Data Processing
    ↓
Stage 2: Continued Pretraining (Co-pretraining)
    ↓
Stage 3: Post-Training (SFT + Alignment)
```

#### 阶段 1：数据处理
- 将原始用户-物品交互转换为文本格式的训练数据
- 构建交互历史、物品描述和行为信号
- 创建多样化任务格式（预测、推理、解释）

#### 阶段 2：持续预训练
- **目标**：在推荐特定文本上进行下一个 token 预测
- **数据混合**：结合推荐数据与一部分通用文本以防止遗忘
- **规模**：OpenOneRec 使用来自 16 万用户的 9600 万交互
- **关键挑战**：平衡领域适配与通用知识保留

#### 阶段 3：后训练
- **监督微调（SFT）**：任务特定指令微调
- **偏好对齐**：面向推荐特定偏好的 DPO 或 RLHF
- **评估**：在 RecIF-Bench 的 8 个多样化任务上测试

### 灾难性遗忘缓解

持续预训练的一个根本性挑战：

| 问题 | 描述 |
|------|------|
| **灾难性遗忘** | 模型在领域数据上训练时失去通用语言能力 |
| **过度专业化** | 模型变得过于狭窄，失去指令跟随能力 |
| **数据混合比例** | 应包含多少通用数据与领域数据？ |

OpenOneRec 证明，仔细的数据混合和训练策略可以缓解这些问题，产出在推荐方面表现出色同时保持通用能力的模型。

### 扩展属性

OpenOneRec 的关键发现：推荐能力在持续预训练中**可预测地扩展**：

- 更多领域数据 → 更好的推荐性能
- 更多模型参数 → 更好的模式学习
- 扩展曲线是可预测的，类似于 LLM 扩展定律
- 通过适当的数据混合可以控制灾难性遗忘

### 性能验证

OpenOneRec 的持续预训练产出的 OneRec-Foundation 模型：

- 在 RecIF-Bench 的所有 8 个任务上达到 SOTA
- 在 Amazon 基准上迁移良好：10 个数据集上平均 Recall@10 提升 +26.8%
- 保持通用语言能力（指令跟随、推理）

### 与其他适配方法对比

| 方法 | 描述 | 优点 | 缺点 |
|------|------|------|------|
| **持续预训练** | 领域自适应 MLM/NTP | 广泛适配、可扩展 | 计算成本高 |
| **提示工程** | 为现有 LLM 设计提示 | 无需训练 | 受模型先验知识限制 |
| **指令微调** | 任务特定微调 | 任务优化 | 范围狭窄 |
| **Adapter/LoRA** | 参数高效微调 | 高效 | 容量有限 |

## 关联

- [OpenOneRec](../models/OpenOneRec.md) — 在大规模下验证持续预训练
- [RecIF-Bench](./recif_bench.md) — 持续预训练结果的评估基准
- [LLM4Rec 评估](./evaluation_llm4rec.md) — 如何评估持续预训练质量
- [LLM4Rec 训练范式](./llm4rec_training_paradigms.md) — 更广泛的训练框架

## 开放问题

1. 持续预训练的最优数据混合比例（通用 vs 领域）是多少？
2. 持续预训练如何与模型规模交互——更大的模型遗忘更少吗？
3. 持续预训练能否随着新交互数据的到来增量进行？
4. 有效持续预训练所需的最小领域数据量是多少？
5. 不同的持续预训练目标（MLM、NTP、对比）在推荐方面如何比较？

## 参考文献

- Zhou, G., Bao, H., Huang, J., Deng, J., Zhang, J., She, J., Cai, K., Ren, L., Ren, L., Luo, Q., Wang, Q., Hu, Q., Zhang, R., Tang, R., Wang, S., Li, W., Wu, X., Luo, X., Wang, X., Hu, Y., Wu, Y., Liu, Z., Zhang, Z., & others. (2025). OpenOneRec Technical Report. arXiv:2512.24762.
- arXiv: https://arxiv.org/abs/2512.24762
