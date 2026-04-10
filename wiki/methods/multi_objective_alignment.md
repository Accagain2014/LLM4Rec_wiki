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

Multi-Objective Alignment 在推荐系统中指将 LLM 或生成模型的输出同时对齐到**多个业务目标**的技术。与单一目标优化（如仅优化 CTR）不同，多目标对齐联合优化用户偏好、内容多样性、公平性、平台商业目标等。HiGR 和 QARM V2 是该方法的代表性工作，分别通过**列表级偏好对齐**和**定量多模态对齐**实现多目标优化。随着生成式推荐向工业级“超级App”场景演进，MBGR 提出了**多业务预测路由（MBP）**与**标签动态稠密化（LDR）**范式，在自回归生成管线中实现了业务级目标的解耦与协同对齐。

## 要点

- 推荐系统天然具有**多目标性**：CTR、观看时长、多样性、公平性、新鲜度、跨业务转化
- 单一目标优化导致**过滤气泡**、**生态失衡**与工业场景中的**“跷跷板效应”**
- HiGR：使用**隐式反馈**进行列表级多目标偏好对齐
- QARM V2：**定量对齐** LLM 表示与多模态推荐业务目标
- MBGR：通过**业务感知ID(BID)**、**多业务预测路由(MBP)**与**标签动态稠密化(LDR)**解决生成式推荐中的表征混淆与多业务协同难题
- 对齐粒度演进：token-level → embedding-level → task-level → list-level → **business-level routing**

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
- 多目标信号（点击、时长、分享、跳过、跨业务转化）需要**联合建模**
- **工业多业务场景痛点**：在统一大模型中同时服务外卖、到店、酒旅等多条业务线时，传统 Next Token Prediction (NTP) 易引发**“跷跷板效应”**（优化A业务损害B业务）与**跨业务表征混淆**，亟需业务级解耦与动态路由对齐机制。

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

### MBGR 的多业务动态路由与标签稠密化

MBGR 针对生成式推荐在工业多业务场景中的落地瓶颈，提出了一套面向自回归生成范式的多目标对齐新路径：

1. **业务感知语义ID（BID）**：摒弃全局统一 Tokenizer，为不同业务线构建独立的语义子空间。通过共享底层词表与业务专属标识符实现语义隔离，从根本上解决跨业务表征混淆问题。
2. **多业务预测路由（MBP）**：在 NTP 解码过程中引入业务条件门控，使模型在生成每一步时能自适应聚焦当前业务上下文。该机制避免了单一全局损失导致的梯度冲突，实现细粒度的业务定制化生成。
3. **标签动态稠密化（LDR）**：利用动态路由算法将用户跨业务的稀疏点击/转化标签映射为连续稠密监督信号。结合辅助对比学习损失，有效缓解数据稀疏性对生成质量的负面影响，提升模型对冷启动与长尾业务的覆盖能力。

### 传统列表级对齐 vs 业务级动态路由

| 维度 | HiGR（列表级对齐） | MBGR（业务级动态路由） |
|------|-------------------|------------------------|
| **优化粒度** | Slate/列表级联合打分 | Token/Step级业务条件路由 |
| **目标解耦方式** | 损失函数加权（α, β, γ） | 业务专属预测分支 + 门控激活 |
| **标签处理** | 隐式反馈直接建模 | 稀疏标签动态稠密化（LDR） |
| **适用场景** | 单业务/垂直内容推荐 | 超级App多业务线统一生成 |
| **核心优势** | 列表多样性与用户体验平衡 | 缓解跷跷板效应，跨业务协同生成 |

### 对齐方法分类

| 方法 | 粒度 | 成本 | 效果 | 代表工作 |
|------|------|------|------|---------|
| 提示对齐 | Task | 低 | 中 | P5, InstructRec |
| 投影对齐 | Embedding | 中 | 中高 | QARM |
| CPT 对齐 | Token+Task | 高 | 高 | PLUM |
| 微调对齐 | 全部 | 最高 | 最高 | TALLRec |
| 列表级多目标对齐 | List+Task | 中高 | 高 | HiGR |
| **业务级动态路由对齐** | **Business+Token** | **中高** | **高(工业级)** | **MBGR** |

### 技术实现

#### 隐式反馈与多业务信号建模
- 观看时长/播放次数 → 用户真实兴趣信号（比点击更可靠）
- 跳过行为 → 负反馈
- 分享/收藏/跨业务跳转 → 强正反馈与业务协同信号
- **稀疏标签稠密化（LDR）**：通过动态权重分配与对比学习，将离散稀疏的交互日志转化为连续监督梯度，稳定多业务联合训练。

#### 列表级/业务级损失函数
传统多目标加权损失：
```
L_slate = α · L_preference + β · L_business + γ · L_diversity
```
MBGR 动态路由生成损失：
```
L_gen = Σ_{t=1}^T [ L_NTP(x_t | x_{<t}, b_t) + λ · L_LDR(y_t, ŷ_t) + μ · L_contrast ]
```
- `b_t`：当前生成步的业务条件标识
- `L_LDR`：标签稠密化监督损失，缓解长尾业务梯度消失
- `L_contrast`：跨业务表征对比正则，防止语义空间坍缩

#### 多任务学习与动态路由框架
- **传统架构**：MMOE（Multi-gate Mixture of Experts）、PLE（Progressive Layered Extraction）
- **生成式路由架构**：业务条件门控（Business-Conditional Gating）、动态专家激活（Dynamic Expert Routing）、自回归解码中的业务上下文注入
- **训练策略**：多业务混合采样 + 梯度裁剪 + 标签平滑稠密化，保障 Scaling Law 下的训练稳定性

### 评估

| 指标类别 | 具体指标 |
|---------|---------|
| 用户偏好 | CTR, CVR, 观看时长, 满意度评分, 跨业务跳转率 |
| 多样性 | 类目覆盖率, 基尼系数, 新颖度, 业务分布熵 |
| 业务目标 | 留存率, 转化率, 收入/GMV, 跷跷板效应抑制率 |
| 公平性 | 物品曝光分布, 创作者/商户公平性, 长尾业务覆盖率 |
| 生成质量 | Recall@K, NDCG@K, 序列连贯性, 推理延迟 |

## Connections

- [HiGR](../models/HiGR.md) — 列表级多目标偏好对齐的实现
- [QARM V2](../models/QARM.md) — 定量多模态多目标对齐
- [MBGR](../models/MBGR.md) — 多业务预测路由与标签稠密化生成框架
- [Representation Alignment](representation_alignment.md) — 单目标对齐的基础
- [Slate Recommendation](../concepts/slate_recommendation.md) — 多目标优化的主要场景
- [LLM as Ranker](./llm_as_ranker.md) — 排序阶段的多目标优化

## Open Questions

1. 如何自动学习多目标的最优权重（而非手动设置 α, β, γ）？
2. 多目标对齐是否会导致某个目标的性能下降（Pareto 最优 vs 单目标最优）？
3. 如何在在线学习场景中动态调整多目标对齐？
4. 用户的长期满意度如何纳入多目标对齐框架？
5. **业务级路由的泛化边界**：当新增业务线或面临极端冷启动时，MBP 路由机制如何实现零样本/少样本快速对齐？
6. **标签稠密化的偏差控制**：LDR 在将稀疏信号稠密化时，如何避免引入分布偏移或过度平滑导致的业务特征失真？
7. **多目标帕累托前沿搜索**：在自回归生成管线中，如何结合强化学习（如 HEPO）实现多业务目标的动态权衡与策略优化？

## References

- Pang, Y., et al. (2025). HiGR: Efficient Generative Slate Recommendation. arXiv:2512.24787.
- Xia, T., et al. (2026). QARM V2: Quantitative Alignment Multi-Modal Recommendation. arXiv:2602.08559.
- Li, C., et al. (2026). MBGR: Multi-Business Prediction for Generative Recommendation at Meituan. arXiv:2604.02684.
- Ma, J., et al. (2018). Modeling task relationships in multi-task learning with multi-gate mixture-of-experts. KDD 2018.

## 更新于 2026-04-10

**来源**: [2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md](../sources/2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md)
- 补充 MBGR 框架，引入**业务感知语义ID(BID)**、**多业务预测路由(MBP)**与**标签动态稠密化(LDR)**技术，作为多目标对齐在自回归生成范式下的新实现路径。
- 对比传统列表级对齐（HiGR）与业务级动态路由的差异，明确生成式管线中稀疏标签稠密化对缓解“跷跷板效应”与跨业务表征混淆的关键作用。
- 更新对齐方法分类表、技术实现细节与评估指标，新增业务级路由相关 Open Questions。

---

## 更新完成：2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md
**更新时间**: 2026-04-10 10:41
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2604_paper_26040268_MBGR_Multi-Business_Prediction_for_Generative_Recommendatio.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
