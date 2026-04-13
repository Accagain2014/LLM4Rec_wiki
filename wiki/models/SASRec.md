---
title: "从关联章节中检测到的页面"
category: "models"
tags: ["new", "2026-04-13"]
created: "2026-04-13"
updated: "2026-04-13"
sources: ["../../raw/sources/1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md"]
related: []
confidence: "medium"
status: "draft"
---

# Self-Attentive Sequential Recommendation (SASRec)

## 摘要
SASRec（Self-Attentive Sequential Recommendation）是序列推荐领域的里程碑式模型，由 Kang 与 McAuley 于 ICDM 2018 提出。该模型首次将 Transformer 中的自注意力机制引入推荐系统，通过因果掩码（Causal Mask）严格遵循用户行为的时间顺序，实现了对用户动态兴趣的精准建模。SASRec 有效平衡了马尔可夫链（MC）在稀疏数据上的参数简洁性与循环神经网络（RNN）在稠密数据上捕捉长期依赖的能力，凭借其并行计算架构与可解释的注意力权重分布，成为后续深度学习推荐模型及大语言模型推荐系统（LLM4Rec）的重要架构基石。[来源：[1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md](../sources/1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md)]

## 核心要点
- **首创自注意力序列建模**：将 Transformer 架构适配于推荐场景，利用多头自注意力机制动态捕捉用户历史交互中的关键依赖关系。
- **因果掩码保障时序性**：引入下三角掩码矩阵，确保预测第 $t$ 个物品时仅依赖 $1$ 至 $t-1$ 的历史行为，严格杜绝未来信息泄露。
- **动态适配数据密度**：注意力权重可随数据稀疏/稠密程度自适应调整，稀疏时聚焦近期行为（退化为类 MC 机制），稠密时聚合长程信号（发挥类 RNN 优势）。
- **计算效率与可解释性**：打破 RNN 串行计算瓶颈，训练与推理速度提升近一个数量级；注意力热力图直观揭示用户兴趣转移路径。
- **LLM4Rec 架构同源**：其“自注意力+因果掩码”范式直接启发了大语言模型在推荐任务中的上下文学习、自回归生成与意图推理机制。

## 详细说明

### 1. 模型架构与核心机制
SASRec 的核心是一个多层堆叠的自注意力编码器。输入层将用户历史交互序列映射为物品嵌入（Item Embedding），并与可学习的位置编码（Positional Embedding）逐元素相加，以保留序列的绝对顺序信息。网络主体由多头自注意力层（Multi-Head Self-Attention）与前馈神经网络（FFN）交替堆叠而成，每层均配备残差连接（Residual Connection）与层归一化（Layer Normalization）以稳定梯度传播。在预测阶段，模型提取序列末尾的隐藏状态向量，与全量候选物品的嵌入矩阵进行内积运算，输出下一项的预测得分分布。该架构摒弃了传统序列模型对固定滑动窗口或递归结构的依赖，实现了全局感受野下的动态特征交互。[来源：[1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md](../sources/1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md)]

### 2. 关键技术设计
- **因果掩码（Causal Masking）**：为保证推荐任务的自回归特性，SASRec 在注意力计算中引入下三角掩码矩阵，强制模型在计算第 $i$ 个位置的注意力分数时，仅能关注 $j \leq i$ 的位置。这一设计严格遵循时间因果律，是序列推荐模型避免数据穿越（Data Leakage）的核心保障。
- **可学习位置编码**：针对推荐场景中序列长度高度动态变化的特点，SASRec 采用参数化的位置嵌入替代 Transformer 原始的正弦/余弦固定编码，使模型能够更灵活地学习不同时间步的相对重要性及衰减规律。
- **优化目标与负采样**：模型采用逐点二元交叉熵损失（Point-wise BCE Loss）进行端到端优化。训练过程中，将用户未交互的物品随机采样为负样本，通过梯度下降拉近正负样本在表示空间中的距离，强化排序边界。结合 Dropout 与权重衰减策略，有效抑制了过拟合现象。[来源：[1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md](../sources/1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md)]

### 3. 实验表现与局限性
在 MovieLens-1M、Amazon（Beauty/Sports/Clothing）及 Steam 等 5 个真实数据集上的评估表明，SASRec 在 HR@10 与 NDCG@10 指标上全面超越 MC、CNN（如 Caser）及 RNN（如 GRU4Rec）基线。例如，在稀疏的 Amazon Beauty 数据集上 HR@10 达 0.148（较 Caser 提升 12.4%），在稠密的 Steam 数据集上 HR@10 达 0.285（较 GRU4Rec 提升 6.8%）。得益于并行化架构，其单轮训练耗时仅为 GRU4Rec 的 1/9，推理延迟降低约 85%。
然而，SASRec 仍存在一定局限：① 需预设固定最大序列长度 $L$，超长历史行为需截断处理，易丢失早期关键兴趣信号；② 依赖均匀随机负采样，缺乏难负样本挖掘（Hard Negative Mining），限制了细粒度排序任务的上限；③ 自注意力机制的 $O(L^2)$ 二次方复杂度在极长序列下面临显存与计算瓶颈。[来源：[1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md](../sources/1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md)]

### 4. 对 LLM4Rec 的启示与演进
SASRec 的架构思想与当前 LLM4Rec 高度同源。LLM 的 Decoder-only 架构本质上可视为 SASRec 在超大规模参数、海量多模态语料及指令微调下的泛化形态。SASRec 验证的“自注意力+因果掩码”序列建模能力，为 LLM4Rec 将用户行为序列转化为自然语言 Prompt 进行上下文学习提供了底层理论支撑。此外，SASRec 暴露的序列长度限制与负采样单一问题，正推动 LLM4Rec 探索长上下文窗口优化（如 RoPE、FlashAttention）、动态负采样策略以及基于指令微调（Instruction Tuning）的意图对齐技术，以在开放域推荐中实现更精准的语义理解与个性化生成。[来源：[1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md](../sources/1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md)]

## 关联页面
- [GRU4Rec — 基于循环神经网络的序列推荐](../models/gru4rec.md)
- [Caser — 基于CNN的序列推荐](../models/caser.md)
- [用于推荐系统的大语言模型 — 概述](../concepts/llm4rec_overview.md)
- [推荐系统中的提示词工程](../concepts/prompt_engineering_rec.md)
- [表示对齐](../concepts/representation_alignment.md)
- [Scaling Laws in Recommendation Systems](../concepts/scaling_laws_recsys.md)

## 开放问题
1. **超长序列建模优化**：如何结合线性注意力（Linear Attention）、状态空间模型（如 Mamba）或分块机制（Chunking），在保持 SASRec 因果特性的同时突破 $O(L^2)$ 复杂度瓶颈？
2. **动态负采样与对比学习**：如何将难负样本挖掘、课程学习（Curriculum Learning）或对比学习（Contrastive Learning）无缝集成至自注意力框架，以提升细粒度排序与泛化能力？
3. **多模态与跨域序列融合**：在 LLM4Rec 范式下，如何将 SASRec 的纯 ID 序列建模扩展至融合文本、图像、音频等多模态信号的统一序列表示学习？
4. **因果推理与去偏**：如何在自注意力机制中显式引入因果推断（Causal Inference）模块，以消除流行度偏差、选择偏差及位置偏差对序列兴趣建模的干扰？

## 参考文献
1. Kang, W. C., & McAuley, J. (2018). Self-Attentive Sequential Recommendation. *Proceedings of the 2018 IEEE International Conference on Data Mining (ICDM)*. [arXiv:1808.09781](https://arxiv.org/abs/1808.09781)
2. [来源：[1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md](../sources/1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md)]