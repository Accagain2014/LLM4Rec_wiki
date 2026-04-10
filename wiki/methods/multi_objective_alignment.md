---
title: "Multi-Objective Alignment — 多目标对齐"
category: "methods"
tags: [multi-objective, listwise optimization, preference alignment, implicit feedback, slate optimization]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/paper_8edbf8_HiGR_Efficient_Generative_Slate_Recommendation_via_Hierarch.md", "../sources/paper_1b102d_QARM_V2_Quantitative_Alignment_Multi-Modal_Recommendation_f.md"]
related:
  - "../concepts/representation_alignment.md"
  - "../models/HiGR.md"
  - "../concepts/slate_recommendation.md"
  - "../methods/llm_as_ranker.md"
confidence: "high"
status: "stable"
---

# Multi-Objective Alignment — 多目标对齐

## 摘要

Multi-Objective Alignment 在推荐系统中指将 LLM 或生成模型的输出同时对齐到**多个业务目标**的技术。与单一目标优化（如仅优化 CTR）不同，多目标对齐联合优化用户偏好、内容多样性、公平性、平台商业目标等。HiGR 和 QARM V2 是该方法的代表性工作，分别通过**列表级偏好对齐**和**定量多模态对齐**实现多目标优化。

## 要点

- 推荐系统天然具有**多目标性**：CTR、观看时长、多样性、公平性、新鲜度
- 单一目标优化导致**过滤气泡**和**生态失衡**
- HiGR：使用**隐式反馈**进行列表级多目标偏好对齐
- QARM V2：**定量对齐** LLM 表示与多模态推荐业务目标
- 对齐粒度：token-level → embedding-level → task-level → multi-objective

## 详情

### 为什么需要多目标对齐？

推荐系统中的目标冲突：
- **CTR vs 多样性**：高 CTR 物品往往同质化
- **短期 engagement vs 长期留存**：点击诱饵提升短期但损害长期
- **个性化 vs 探索**：过度个性化导致信息茧房
- **用户体验 vs 商业变现**：广告与有机内容的平衡

LLM/生成模型加剧了这些挑战：
- 生成模型倾向于**模式崩溃**（mode collapse）→ 缺乏多样性
- LLM 的语义空间与业务目标空间**不对齐**
- 多目标信号（点击、时长、分享、跳过）需要**联合建模**

### HiGR 的多目标列表级对齐

HiGR 的多目标偏好对齐机制：

1. **列表级优化**：优化整个 slate 的质量，而非单个物品
2. **隐式反馈利用**：使用观看时长、播放次数、跳过等信号
3. **多目标联合**：
   - 用户偏好匹配（用户想看什么）
   - 业务目标达成（平台希望优化什么）
   - 多样性约束（slate 不应该太同质）

```
Slate Quality = f(User Preference, Business Objectives, Diversity)
```

### QARM V2 的定量多模态对齐

QARM V2 从多模态角度实现多目标对齐：

1. **多模态表示**：融合文本、图像、视频特征
2. **定量对齐**：使多模态表示与 RecSys 业务目标数值对齐
3. **端到端可训练**：表示不再是固定缓存，而是可学习的

### 对齐方法分类

| 方法 | 粒度 | 成本 | 效果 | 代表工作 |
|------|------|------|------|---------|
| 提示对齐 | Task | 低 | 中 | P5, InstructRec |
| 投影对齐 | Embedding | 中 | 中高 | QARM |
| CPT 对齐 | Token+Task | 高 | 高 | PLUM |
| 微调对齐 | 全部 | 最高 | 最高 | TALLRec |
| 多目标对齐 | 全部+业务 | 高 | 最高 | HiGR, QARM V2 |

### 技术实现

#### 隐式反馈建模
- 观看时长 → 用户真实兴趣信号（比点击更可靠）
- 播放次数 → 内容吸引力
- 跳过行为 → 负反馈
- 分享/收藏 → 强正反馈

#### 列表级损失函数
```
L_slate = α · L_preference + β · L_business + γ · L_diversity
```
- `L_preference`：用户偏好匹配损失
- `L_business`：业务目标达成损失
- `L_diversity`：多样性正则化

#### 多任务学习框架
- MMOE（Multi-gate Mixture of Experts）
- PLE（Progressive Layered Extraction）
- 自定义门控机制融合多目标信号

### 评估

| 指标类别 | 具体指标 |
|---------|---------|
| 用户偏好 | CTR, CVR, 观看时长, 满意度评分 |
| 多样性 | 类目覆盖率, 基尼系数, 新颖度 |
| 业务目标 | 留存率, 转化率, 收入 |
| 公平性 | 物品曝光分布, 创作者公平性 |

## Connections

- [HiGR](../models/HiGR.md) — 列表级多目标偏好对齐的实现
- [QARM V2](../models/QARM.md) — 定量多模态多目标对齐
- [Representation Alignment](representation_alignment.md) — 单目标对齐的基础
- [Slate Recommendation](../concepts/slate_recommendation.md) — 多目标优化的主要场景
- [LLM as Ranker](./llm_as_ranker.md) — 排序阶段的多目标优化

## Open Questions

1. 如何自动学习多目标的最优权重（而非手动设置 α, β, γ）？
2. 多目标对齐是否会导致某个目标的性能下降（Pareto 最优 vs 单目标最优）？
3. 如何在在线学习场景中动态调整多目标对齐？
4. 用户的长期满意度如何纳入多目标对齐框架？

## References

- Pang, Y., et al. (2025). HiGR: Efficient Generative Slate Recommendation. arXiv:2512.24787.
- Xia, T., et al. (2026). QARM V2: Quantitative Alignment Multi-Modal Recommendation. arXiv:2602.08559.
- Ma, J., et al. (2018). Modeling task relationships in multi-task learning with multi-gate mixture-of-experts. KDD 2018.


## 更新于 2026-04-09

**来源**: paper_a1f46d_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md
：补充 MBP 与 LDR 作为多业务/多目标优化的新范式，对比传统列表级对齐（HiGR）与业务级动态路由的差异，强调稀疏标签稠密化在生成式管线中的作用。


## 更新于 2026-04-09

**来源**: 2511_paper_25111013_GPR_Towards_a_Generative_Pre-trained_One-Model_Paradigm_for.md
：新增 HEPO（层级增强策略优化）与价值感知微调作为推荐系统中商业价值对齐（类 RLHF）的典型方法。
