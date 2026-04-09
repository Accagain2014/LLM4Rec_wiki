---
title: "Representation Alignment — 表示对齐"
category: "concepts"
tags: [representation alignment, semantic gap, LLM embedding, recommendation objectives, quantitative alignment]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/paper_1b102d_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md", "../sources/paper_ad0dff_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md"]
related:
  - "../methods/multi_objective_alignment.md"
  - "../concepts/gsu_esu_paradigm.md"
  - "../models/QARM.md"
  - "../concepts/prompt_engineering_rec.md"
confidence: "high"
status: "stable"
---

# Representation Alignment — 表示对齐

## 摘要

Representation Alignment 研究如何将 **LLM 的语义表示**与**推荐系统的业务目标**对齐。LLM 在通用语义空间上预训练，而推荐系统优化的是用户交互信号（点击、观看、购买）。这两个目标之间的**语义鸿沟（semantic gap）**导致直接使用 LLM embedding 往往效果不佳。表示对齐的目标是搭建这座桥梁。

## 要点

- **核心问题**：LLM 语义表示 ≠ 推荐业务目标的最优表示
- **Representation Unmatching**：预训练目标（NLP/CV）与推荐目标（user-item interaction）不一致
- **Representation Unlearning**：缓存的 LLM 表示无法被推荐任务梯度更新
- **定量对齐（Quantitative Alignment）**：QARM 系列提出的对齐框架
- 这是 LLM4Rec 的**核心挑战**之一

## 详情

### 为什么需要对齐？

LLM 在以下任务上预训练：
- 语言建模（预测下一个 token）
- 掩码语言建模（填空）
- 图像-文本匹配
- 视觉问答

推荐系统优化：
- CTR（点击率）预估
- 观看时长最大化
- 用户留存
- 多目标优化（engagement + diversity + fairness）

**目标函数的根本差异**导致 LLM 表示不是推荐任务的最优表示。

### 两种不对齐问题

#### 1. Representation Unmatching（表示不匹配）
- LLM 表示空间与推荐表示空间不同
- 语义相似的物品在推荐空间中可能有不同价值
- 例：两部电影在叙事上相似（LLM 语义），但在推荐系统中一个热门一个冷门

#### 2. Representation Unlearning（表示不可学习）
- 工业实践中 LLM 表示通常被缓存为固定输入
- 推荐模型无法通过梯度更新这些表示
- 导致表示无法适应特定下游任务

### 对齐方法

#### 定量对齐（Quantitative Alignment）— QARM
- 提出**可训练的多模态表示**而非固定缓存
- 使多模态表示能够端到端地与推荐任务联合优化
- 针对不同下游模型定制专用表示

#### 多目标对齐（Multi-Objective Alignment）
- 同时对齐多个业务目标（点击、观看、多样性）
- 使用隐式反馈作为对齐信号
- Listwise 优化而非 pointwise

#### 提示对齐（Prompt-based Alignment）
- 通过提示工程将推荐任务映射到 LLM 语义空间
- 利用 LLM 的指令跟随能力
- 无需修改 LLM 权重（低成本）

#### 微调对齐（Fine-tuning Alignment）
- 在推荐数据上继续预训练（CPT）
- 指令微调（InstructRec、TALLRec）
- 完全对齐但成本高

### 对齐的层次

| 层次 | 描述 | 方法 |
|------|------|------|
| Token-level | 物品 ID/名称与 LLM token 对齐 | Semantic ID, Tokenization |
| Embedding-level | LLM embedding 与推荐 embedding 对齐 | 投影层、对比学习 |
| Task-level | 推荐目标与 LLM 能力对齐 | 指令微调、CPT |
| Multi-objective | 多个业务目标的联合对齐 | 多任务学习 |

### 工业挑战

- **规模**：十亿级用户 + 百万级物品 → 对齐计算成本高
- **实时性**：用户偏好变化 → 表示需要持续更新
- **多模态**：文本、图像、视频、音频 → 多模态对齐更复杂
- **冷启动**：新物品无交互数据 → 仅依赖语义对齐

## Connections

- [QARM](../models/QARM.md) — 定量对齐的代表性工作
- [Multi-Objective Alignment](../methods/multi_objective_alignment.md) — 多目标对齐方法
- [GSU/ESU Paradigm](./gsu_esu_paradigm.md) — 工业架构中对齐的关键位置
- [Prompt Engineering](./prompt_engineering_rec.md) — 低成本对齐方法

## Open Questions

1. 是否存在通用的"推荐语义空间"，还是每个领域需要独立对齐？
2. 如何平衡对齐质量与计算效率？
3. 零样本对齐是否可能（无需推荐数据）？
4. 多模态对齐的最优融合策略是什么？

## References

- Luo, X., et al. (2024). QARM: Quantitative Alignment Multi-Modal Recommendation at Kuaishou. arXiv:2411.11739.
- Xia, T., et al. (2026). QARM V2: Quantitative Alignment Multi-Modal Recommendation. arXiv:2602.08559.
- Zhang, J., et al. (2023). On the representation collapse of LLM fine-tuning for recommendation.
