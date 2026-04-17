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

Multi-Objective Alignment 在推荐系统中指将 LLM 或生成模型的输出同时对齐到**多个业务目标**的技术。与单一目标优化（如仅优化 CTR）不同，多目标对齐联合优化用户偏好、内容多样性、公平性、平台商业目标等。HiGR 和 QARM V2 是该方法的代表性工作，分别通过**列表级偏好对齐**和**定量多模态对齐**实现多目标优化。随着生成式推荐向工业级“超级App”场景演进，MBGR 提出了**多业务预测路由（MBP）**与**标签动态稠密化（LDR）**范式，在自回归生成管线中实现了业务级目标的解耦与协同对齐。近期，PinRec 进一步提出了**结果条件化生成（Outcome-Conditioned Generation）**范式，通过条件信号直接动态重塑生成概率分布以替代传统加权损失，并结合**多Token联合解码**在工业级检索场景中实现了多目标权衡与推理效率的突破。与此同时，OnePiece 将 LLM 的上下文工程与推理机制引入级联排序，提出**渐进式多任务训练**范式，利用用户行为反馈链构建分层损失函数，为复杂工业场景下的多目标稳定收敛提供了新路径。

## 要点

- 推荐系统天然具有**多目标性**：CTR、观看时长、多样性、公平性、新鲜度、跨业务转化
- 单一目标优化导致**过滤气泡**、**生态失衡**与工业场景中的**“跷跷板效应”**
- HiGR：使用**隐式反馈**进行列表级多目标偏好对齐
- QARM V2：**定量对齐** LLM 表示与多模态推荐业务目标
- MBGR：通过**业务感知ID(BID)**、**多业务预测路由(MBP)**与**标签动态稠密化(LDR)**解决生成式推荐中的表征混淆与多业务协同难题
- PinRec：提出**结果条件化生成**，以条件信号动态调整生成概率分布替代传统加权损失，结合**多Token生成**提升检索多样性与吞吐
- OnePiece：提出**渐进式多任务训练**，基于用户行为反馈链（曝光→点击→加购→转化）构建分层损失，实现从浅层表征到深层推理的稳定对齐
- 对齐粒度演进：token-level → embedding-level → task-level → list-level → business-level routing → outcome-conditioned probability shaping → **chain-level progressive alignment**

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
- **复杂级联排序痛点**：召回与精排阶段目标差异大，传统多任务联合训练易因梯度冲突导致收敛震荡，高阶稀疏目标（如转化、GMV）难以稳定优化。

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

### PinRec 的结果条件化生成与多Token解码

PinRec 将多目标对齐范式从“损失函数加权”推进至“生成概率分布条件化控制”，为工业级生成式检索提供了可动态配置的对齐路径：

1. **结果条件化生成（Outcome-Conditioned Generation）**：摒弃传统的线性加权损失（如 $L = \alpha L_{ctr} + \beta L_{save}$），在训练与推理阶段将业务指标权重（如点击率、保存率、停留时长）作为显式条件信号注入模型。该机制直接干预自回归解码过程中的 Token 概率分布 $P(x_t | x_{<t}, \mathbf{w}_{obj})$，使模型能够根据实时业务策略灵活重塑输出分布，实现多目标的动态权衡而无需重新训练。
2. **多Token联合生成（Multi-Token Generation）**：突破传统单Token自回归生成的效率瓶颈与累积误差。通过改进的束搜索（Beam Search）或并行Token预测策略，模型在单步解码中联合预测多个Token，显著降低推理延迟，同时扩大候选集的探索空间，有效提升长尾物品覆盖率与输出多样性。
3. **工业级可扩展性验证**：在 Pinterest 海量数据规模上完成端到端部署，验证了条件化生成范式在超大规模候选池中的工程可行性。模型在性能（准确率/召回率）、多样性（新颖性/长尾覆盖）与系统效率（吞吐/延迟）之间取得了优异平衡。

[来源：[2504_paper_25041050_PinRec_Outcome-Conditioned,_Multi-Token_Generative_Retrieva.md](../sources/2504_paper_25041050_PinRec_Outcome-Conditioned,_Multi-Token_Generative_Retrieva.md)]

### OnePiece 的渐进式多任务训练与分层对齐

OnePiece 针对工业级级联排序中多目标信号稀疏、梯度冲突导致训练不稳定的问题，提出**渐进式多任务训练（Progressive Multi-Task Training）**范式。该方法摒弃了传统多目标联合优化中“一步到位”的静态加权策略，转而利用用户真实行为反馈链构建**分层监督信号**，实现从浅层表征到深层推理的渐进式对齐：

1. **行为链分层建模**：将用户交互路径解耦为多个递进阶段（曝光 → 点击 → 加购/收藏 → 转化/支付），每个阶段对应不同的业务目标与优化难度。训练初期聚焦基础曝光-点击对齐，稳定模型底层表征与注意力分布；中后期逐步引入加购、转化等高阶稀疏信号，引导模型进行复杂意图推理与价值预估。
2. **分层损失函数设计**：构建与行为阶段严格匹配的分层损失 $L_{progressive} = \sum_{i=1}^{N} \lambda_i(t) \cdot L_{task_i}$，其中权重 $\lambda_i(t)$ 随训练步数 $t$ 动态调度。早期强化浅层任务（如 CTR）的梯度主导，确保表征空间快速收敛；后期平滑过渡至深层任务（如 CVR/GMV），通过任务间一致性约束缓解多目标梯度冲突与优化震荡。
3. **稳定复杂场景收敛**：通过分阶段注入监督信号，模型在保持强推理能力的同时避免了对稀疏高阶目标的过拟合。该机制与结构化上下文工程、分块隐式推理协同，在 Shopee 工业级搜索排序场景中实现了 GMV/UU +2% 与广告收入 +2.90% 的稳定提升，验证了渐进式对齐在复杂多目标场景下的工程有效性。

[来源：[2509_paper_25091809_OnePiece_Bringing_Context_Engineering_and_Reasoning_to_Indu.md](../sources/2509_paper_25091809_OnePiece_Bringing_Context_Engineering_and_Reasoning_to_Indu.md)]

### 对齐范式对比：列表级 vs 业务级 vs 结果条件化 vs 渐进分层

| 维度 | HiGR（列表级对齐） | MBGR（业务级动态路由） | PinRec（结果条件化生成） | OnePiece（渐进分层对齐） |
|------|-------------------|------------------------|--------------------------|--------------------------|
| **优化粒度** | Slate/列表级联合打分 | Token/Step级业务条件路由 | Token/Step级概率分布重塑 | Chain/Stage级行为链分层 |
| **目标解耦方式** | 损失函数加权（α, β, γ） | 业务专属预测分支 + 门控激活 | 条件信号注入 + 动态概率调制 | 训练阶段动态权重调度 + 分层约束 |
| **标签/信号处理** | 隐式反馈直接建模 | 稀疏标签动态稠密化（LDR） | 业务权重作为生成先验条件 | 行为反馈链（曝光→点击→转化）递进注入 |
| **适用场景** | 单业务/垂直内容推荐 | 超级App多业务线统一生成 | 工业级大规模检索/召回 | 工业级级联排序（召回+精排） |
| **核心优势** | 列表多样性与用户体验平衡 | 缓解跷跷板效应，跨业务协同生成 | 免重训动态调权，多Token提效增样 | 缓解梯度冲突，稳定高阶稀疏目标收敛 |

### 对齐方法分类

| 方法 | 粒度 | 成本 | 效果 | 代表工作 |
|------|------|------|------|---------|
| 提示对齐 | Task | 低 | 中 | P5, InstructRec |
| 投影对齐 | Embedding | 中 | 中高 | QARM |
| CPT 对齐 | Token+Task | 高 | 高 | PLUM |
| 微调对齐 | 全部 | 最高 | 最高 | TALLRec |
| 列表级多目标对齐 | List+Task | 中高 | 高 | HiGR |
| 业务级动态路由对齐 | Business+Token | 中高 | 高(工业级) | MBGR |
| **结果条件化概率对齐** | **Outcome+Token** | **中** | **高(工业检索)** | **PinRec** |
| **渐进式分层对齐** | **Chain/Stage** | **中** | **高(工业排序)** | **OnePiece** |

### 技术实现

#### 隐式反馈与多业务信号建模
- 观看时长/播放次数 → 用户真实兴趣信号（比点击更可靠）
- 跳过行为 → 负反馈
- 分享/收藏/跨业务跳转 → 强正反馈与业务协同信号
- **稀疏标签稠密化（LDR）**：通过动态权重分配与对比学习，将离散稀疏的交互日志转化为连续监督梯度，稳定多业务联合训练。

#### 列表级/业务级/条件化/分层损失函数
传统多目标加权损失：
```
L_slate = α · L_preference + β · L_business + γ · L_diversity
```
MBGR 动态路由生成损失：
```
L_gen = Σ_{t=1}^T [ L_NTP(x_t | x_{<t}, b_t) + λ · L_LDR(y_t, ŷ_t) + μ · L_contrast ]
```
PinRec 结果条件化概率调制：
```
P(x_t | x_{<t}, w_obj) ∝ exp( log P_base(x_t | x_{<t}) + Σ_k w_k · φ_k(x_t) )
```
OnePiece 渐进式分层损失：
```
L_progressive(t) = Σ_{i=1}^{N} λ_i(t) · L_chain_i + η · L_consistency
```
- `w_obj`：业务目标权重向量（如 CTR, Save, Dwell Time）
- `φ_k(x_t)`：目标 k 对 Token $x_t$ 的条件偏好得分
- `λ_i(t)`：随训练步数动态调度的阶段权重，实现浅层到深层的平滑过渡
- `L_consistency`：跨阶段任务一致性正则项，防止高阶目标优化破坏已收敛的底层表征
- 通过直接修改 Softmax 前的 Logits 分布或动态调度损失权重，实现**免重训的动态多目标对齐**或**稳定渐进收敛**，彻底规避传统加权损失中的梯度冲突与超参敏感问题。

#### 多任务学习与动态路由框架
- **传统架构**：MMOE（Multi-gate Mixture of Experts）、PLE（Progressive Layered Extraction）
- **生成式路由架构**：业务条件门控（Business-Conditional Gating）、动态专家激活（Dynamic Expert Routing）、自回归解码中的业务上下文注入
- **条件化生成架构**：Outcome-Conditioned Logit Shaping、Multi-Token Parallel Decoding、动态权重热插拔（Hot-swappable Weights）
- **渐进式训练架构**：行为链分层监督注入、动态权重调度器（Dynamic Weight Scheduler）、跨阶段梯度裁剪与一致性正则
- **训练策略**：多业务混合采样 + 梯度裁剪 + 标签平滑稠密化 + 条件分布正则 + **分阶段损失权重退火**，保障 Scaling Law 下的训练稳定性。

### 评估

| 指标类别 | 具体指标 |
|---------|---------|
| 用户偏好 | CTR, CVR, 观看时长, 满意度评分, 跨业务跳转率, 保存率(Save Rate) |
| 多样性 | 类目覆盖率, 基尼系数, 新颖度, 业务分布熵, 长尾物品覆盖率 |
| 业务目标 | 留存率, 转化率, 收入/GMV, 跷跷板效应抑制率, 策略调权响应延迟, 训练收敛稳定性 |
| 公平性 | 物品曝光分布, 创作者/商户公平性, 长尾业务覆盖率 |
| 生成质量 | Recall@K, NDCG@K, 序列连贯性, 推理延迟(P99), 吞吐(TPS), 梯度冲突率 |

## Connections

- [HiGR](../models/HiGR.md) — 列表级多目标偏好对齐的实现
- [QARM V2](../models/QARM.md) — 定量多模态多目标对齐
- [MBGR](../models/MBGR.md) — 多业务预测路由与标签稠密化生成框架
- [PinRec](../models/PinRec.md) — 结果条件化生成与多Token检索范式
- [OnePiece](../models/OnePiece.md) — 渐进式多任务训练与上下文工程对齐
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
8. **条件化生成的分布稳定性**：Outcome-Conditioned Generation 在极端权重配置下是否会导致概率分布坍塌或模式退化？如何设计正则项保障生成空间的拓扑完整性？
9. **多Token解码的可控性边界**：并行预测多个Token时，如何保证跨步目标一致性（如避免前一个Token优化CTR而后续Token偏离核心意图）？
10. **渐进式训练的动态调度策略**：在 OnePiece 范式下，如何设计自适应的 $\lambda_i(t)$ 调度算法，使其能根据实时数据分布与业务优先级自动调整分层损失权重，避免人工经验依赖？

---

## 更新完成：2509_paper_25091809_OnePiece_Bringing_Context_Engineering_and_Reasoning_to_Indu.md
**更新时间**: 2026-04-16 03:56
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2509_paper_25091809_OnePiece_Bringing_Context_Engineering_and_Reasoning_to_Indu.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
