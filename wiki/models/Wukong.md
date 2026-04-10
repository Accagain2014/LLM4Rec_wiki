---
title: "Wukong — 迈向大规模推荐系统的缩放定律"
category: "models"
tags: ["scaling law", "factorization machines", "large-scale recommendation", "model architecture", "compute efficiency", "synergistic upscaling"]
status: "draft"
confidence: "medium"
source: "2403_paper_24030254_Wukong_Towards_a_Scaling_Law_for_Large-Scale_Recommendation.md"
---

# Wukong — 迈向大规模推荐系统的缩放定律

## 摘要
**Wukong** 是 2024 年提出的一种面向大规模推荐系统的新型模型架构与扩展范式。该工作首次在推荐领域成功建立并验证了**缩放定律（Scaling Laws）**，打破了传统推荐模型在参数量与计算量增加时性能易饱和或退化的长期瓶颈。Wukong 摒弃了复杂的显式交叉网络、注意力机制或手工特征工程，采用**纯分解机（Factorization Machines, FM）堆叠架构**，配合系统化的**协同扩展策略（Synergistic Upscaling）**，仅通过同步增加网络深度与宽度即可自适应捕获任意阶特征交互。实验表明，Wukong 在模型计算复杂度跨越两个数量级（突破 100 GFLOP/样本）时，推荐质量仍保持稳定的单调增长，为工业级大推荐模型的算力规划、架构选型与 LLM4Rec 范式演进提供了重要的理论依据与实践路径。

## 核心要点
- 📈 **首次确立推荐系统缩放定律**：证明推荐模型同样遵循“规模扩大 → 质量提升”的可预测幂律关系，填补了该领域长期缺乏 Scaling Law 的空白。
- 🧱 **极简纯 FM 堆叠架构**：以统一的 FM 块纵向堆叠替代 DCN、xDeepFM 等复杂交叉模块，通过深度累积自然涌现高阶特征交互，大幅降低架构设计复杂度与冗余计算。
- ⚖️ **协同扩展策略**：提出深度与宽度按比例同步扩展的系统化方案，结合特定初始化、层归一化与学习率调度，确保优化曲面平滑与梯度传播稳定。
- 🚀 **突破百 GFLOP 性能瓶颈**：在公开数据集与超大规模工业数据上，计算复杂度达 100+ GFLOP/样本时 AUC/LogLoss 仍单调上升，显著优于传统基线。
- 🔗 **与 LLM4Rec 高度同构**：揭示“特征交互能力随规模涌现”的本质规律，为构建轻量级大推荐模型、优化算力分配及探索统一基础模型（Foundation Model for RecSys）提供新范式。

## 详细说明

### 架构设计：纯 FM 堆叠范式
传统推荐模型（如 DeepFM、DCN、DIN、Transformer-based RecSys）通常依赖显式的高阶交叉模块或复杂的序列注意力机制来建模特征交互。这类设计虽在中小规模下表现优异，但在规模扩展时往往面临计算复杂度呈组合爆炸、梯度路径冗长、以及架构超参数敏感等问题。

Wukong 采用**极简的纯 FM 堆叠设计**。其核心思想是：每一层均独立执行标准的二阶特征交互计算（即隐向量内积与线性项求和），并通过残差连接与非线性激活函数进行层间信息传递。随着网络深度的增加，低阶交互信号在多层非线性变换与残差累积下，能够**隐式且自适应地逼近任意高阶特征组合**。该架构避免了硬编码特定交互阶数，消除了冗余的交叉网络参数，使模型具备更强的可扩展性与计算密度（Compute Density）。

### 协同扩展策略 (Synergistic Upscaling)
单纯增加模型规模往往会导致优化困难（如梯度消失/爆炸、损失曲面崎岖）。Wukong 提出了一套**协同扩展策略**，将“更深+更宽”的简单操作转化为可预测的性能增益函数：
1. **比例同步扩展**：在扩展过程中，网络层数（深度 $L$）与隐藏层维度（宽度 $D$）按预设比例协同增长，避免单一维度过度膨胀导致的表征冗余或优化不稳定。
2. **优化稳定性保障**：引入改进的参数初始化方案（适配 FM 结构的方差缩放）、逐层归一化（LayerNorm）以及带预热（Warmup）与余弦衰减的学习率调度，确保在参数量指数级增长时梯度范数保持平稳。
3. **幂律拟合特性**：通过控制扩展比例，模型性能与计算量（FLOPs）之间呈现出高度可拟合的幂律关系（$Performance \propto Compute^{-\alpha}$），使工业场景中的算力投入产出比（ROI）具备可量化预测性。

### 缩放定律的验证与实验表现
研究在 6 个公开基准数据集（如 Criteo、Avazu 等）及内部超大规模工业数据集上进行了系统性评估。实验结果表明：
- **全面超越 SOTA**：在 AUC、LogLoss、NDCG 等核心指标上，Wukong 一致优于当前主流推荐模型。
- **单调缩放能力**：当模型计算复杂度从基础规模逐步提升至 **100+ GFLOP/样本**（跨越两个数量级）时，推荐质量保持稳定的单调上升趋势。相比之下，传统基线模型在复杂度达到阈值后迅速饱和甚至出现性能退化。
- **计算效率优势**：由于摒弃了复杂的注意力与交叉计算，Wukong 在同等 FLOPs 预算下具备更高的有效计算利用率（MFU），更适配现代 GPU/TPU 的并行计算架构。

### 与 LLM4Rec 的范式关联
Wukong 的成功对 LLM4Rec（大语言模型用于推荐系统）的发展具有三重启示：
1. **轻量级大推荐模型路径**：证明推荐系统无需盲目引入庞大的 Transformer 结构。通过合理的架构简化与协同扩展，传统判别式模型同样可逼近大模型规模下的性能上限，为资源受限场景提供高性价比方案。
2. **算力规划与数据配比依据**：Wukong 的缩放曲线为 LLM4Rec 的算力分配、训练数据规模设定与模型选型提供了可量化的决策框架，有助于避免工业场景中的“无效算力堆砌”与“数据-算力不匹配”问题。
3. **涌现机制的同构性**：Wukong 揭示的“特征交互能力随深度堆叠自然涌现”规律，与 LLM 中“上下文学习/复杂推理能力随规模增长”的涌现机制高度同构。这为构建统一的大语言-推荐基础模型（Foundation Model for RecSys）奠定了架构与理论桥梁，提示未来可探索 FM 堆叠塔与 LLM 语义塔的深度融合。

## 关联页面
- [Scaling Laws in Recommendation Systems — Predictable Performance Gains from Scaling](../concepts/scaling_laws_recsys.md)
- [Model FLOPs Utilization (MFU) — Measuring Hardware Efficiency in Recommendation Models](../concepts/model_flops_utilization_mfu.md)
- [用于推荐系统的大语言模型 — 概述](../concepts/llm4rec_overview.md)
- [Representation Alignment — 表示对齐](../methods/representation_alignment.md)

## 开放问题
尽管 Wukong 在架构设计与缩放规律验证上取得突破，但面向工业级落地与 LLM4Rec 融合仍存在以下挑战：
1. **分布式训练工程瓶颈**：超大规模 FM 堆叠在数据并行与模型并行下的通信开销、显存碎片化及激活检查点（Activation Checkpointing）策略仍需优化。
2. **在线推理延迟控制**：百 GFLOP 级别模型的实时推理（<10ms）对动态批处理、算子融合与硬件感知编译（如 TensorRT、TVM）提出极高要求。
3. **长尾稀疏特征与动态兴趣**：纯 FM 结构在应对极度稀疏的长尾 ID 特征、用户兴趣快速漂移（Concept Drift）时的泛化与遗忘机制尚待验证。
4. **多模态与跨域扩展**：如何将 Wukong 的协同扩展范式迁移至图文/视频多模态推荐、跨域迁移学习场景，仍需探索特征对齐与模态路由机制。
5. **与 LLM 的协同范式**：未来可研究将 Wukong 作为高效“推荐计算塔”，与 LLM 的“语义理解塔”进行混合专家（MoE）式路由或表示对齐，实现精度与效率的帕累托最优。

## 参考文献
1. Zhang, B., Luo, L., Chen, Y., et al. (2024). *Wukong: Towards a Scaling Law for Large-Scale Recommendation*. arXiv preprint arXiv:2403.02545.
2. Kaplan, J., McCandlish, S., Henighan, T., et al. (2020). *Scaling Laws for Neural Language Models*. arXiv:2001.08361.
3. Guo, H., Tang, R., Ye, Y., Li, Z., & He, X. (2017). *DeepFM: A Factorization-Machine based Neural Network for CTR Prediction*. IJCAI.
4. Wang, R., Fu, B., Fu, G., & Wang, M. (2017). *Deep & Cross Network for Ad Click Predictions*. ADKDD.
5. Hoffmann, J., Borgeaud, S., Mensch, A., et al. (2022). *Training Compute-Optimal Large Language Models (Chinchilla)*. arXiv:2203.15556.