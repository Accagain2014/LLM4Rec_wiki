---
title: "从关联章节中检测到的页面"
category: "methods"
tags: ["new", "2026-04-15"]
created: "2026-04-15"
updated: "2026-04-15"
sources: ["../../raw/sources/2602_paper_26020186_GRAB_An_LLM-Inspired_Sequence-First_Click-Through_Rate_Pred.md"]
related: []
confidence: "medium"
status: "draft"
---

# GRAB：受大语言模型启发的序列优先CTR预测范式

## 摘要
GRAB（Generative Recommendation with Action-aware Browsing）是一种面向广告点击率（CTR）预测的端到端生成式建模范式。该模型突破传统深度学习推荐模型（DLRM）依赖人工特征交叉与多塔判别架构的局限，首次将大语言模型（LLM）的“序列优先”与“自回归生成”思想系统性地引入工业级推荐排序任务。通过引入因果动作感知多通道注意力机制（CamA），GRAB能够精准解耦用户行为序列中的时序动态与异构交互信号。在百度广告系统的全量部署中，GRAB不仅实现了显著的业务指标提升，更首次在工业场景实证了推荐系统的“缩放定律”（Scaling Law），为下一代生成式推荐架构的演进提供了关键范式参考。

## 核心要点
- **范式革新**：将CTR预测从“特征工程+判别式打分”重构为“历史序列输入+自回归概率生成”的端到端任务。
- **CamA机制**：设计因果动作感知多通道注意力，并行建模曝光、点击、转化等多源动作语义，严格保证时序因果性。
- **缩放定律实证**：验证了模型性能随用户行为序列长度增加呈单调近似线性增长，打破传统DLRM的长序列性能饱和瓶颈。
- **工业级落地**：在百度广告全量A/B测试中实现广告总收入提升3.05%，整体CTR提升3.49%。
- **工程挑战**：自回归推理带来延迟与显存压力，需结合知识蒸馏、并行解码与序列压缩技术优化。

## 详细说明

### 1. 架构设计：从判别式到生成式的范式迁移
传统DLRM（如DIN、DIEN、DCN等）通常采用“Embedding拼接→特征交叉层→独立排序塔”的流水线架构，严重依赖专家特征工程，且难以有效捕获超长序列中的细粒度兴趣演化。GRAB彻底摒弃该范式，采用纯生成式端到端架构。模型将用户离散ID特征、上下文特征与连续特征统一映射为连续的序列Token，以用户历史行为序列为核心上下文。预测过程被形式化为条件概率生成任务：$P(y_{next} | x_{1}, x_{2}, ..., x_{t})$，其中 $y_{next}$ 为目标广告的点击/转化概率分布。底层由多层Transformer块堆叠而成，通过序列到序列（Seq2Seq）或自回归（Autoregressive）方式直接输出预测结果，利用生成模型的上下文学习能力实现跨域兴趣的隐式对齐，大幅降低对显式特征交叉的依赖。

### 2. 关键技术：因果动作感知多通道注意力（CamA）
用户行为序列包含异构信号（如曝光未点击、点击、加购、转化等），不同动作蕴含的兴趣强度与时间衰减规律差异显著。GRAB提出CamA（Causal Action-aware Multi-channel Attention）模块以解决此问题：
- **多通道并行建模**：将标准自注意力头拆分为多个动作专属通道，每个通道独立学习特定交互类型（如Click通道、View通道）的语义空间与权重分布，避免信号混淆。
- **因果掩码与时间解耦**：严格引入下三角因果掩码（Causal Mask）防止未来信息泄露，确保在线推理的实时性与合规性。同时，结合可学习的时间位置编码（Temporal Positional Encoding），显式建模兴趣漂移与时间衰减效应，使模型能够区分“近期高频点击”与“历史偶然曝光”的语义差异。
- **细粒度动态捕捉**：通过通道间的交叉融合机制，CamA能够在保持计算效率的同时，精准捕捉用户兴趣的短期波动与长期偏好，为生成式输出提供高质量的上下文表征。

### 3. 训练策略与缩放定律（Scaling Law）验证
GRAB采用序列生成损失函数（如交叉熵或序列级对比损失）进行端到端优化，并结合海量在线日志进行持续预训练（Continued Pretraining）。训练过程中引入**序列长度动态采样策略**，使模型自适应学习不同长度行为序列的表征规律。
离线与在线实验首次系统验证了推荐领域的缩放定律：当用户行为序列长度从基准值逐步扩展时，GRAB的AUC、GAUC等核心排序指标呈现单调且近似线性的增长趋势（序列长度每翻倍，性能增益保持稳定）。这一发现直接证明了生成式架构在长序列场景下未出现传统模型常见的表征饱和或梯度消失问题，确立了“更长序列即更强性能”的扩展路径，为推荐系统算力与数据投入提供了可预期的收益模型。

### 4. 工业部署与工程优化
尽管生成式范式在精度上优势显著，但自回归解码在超大规模高并发广告排序场景中面临推理延迟与显存瓶颈。GRAB在百度广告系统的落地过程中，采用了多项工程优化策略：
- **推理加速**：结合KV Cache复用、投机解码（Speculative Decoding）与算子融合技术，将首字延迟（TTFT）与吞吐率优化至工业SLA要求范围内。
- **显存管理**：针对极端长序列，引入动态序列截断与检索增强（Retrieval-Augmented）机制，仅保留高信息密度的核心行为Token，平衡精度与资源消耗。
- **持续迭代**：建立在线日志回流与增量微调（Incremental Fine-tuning）管道，确保模型能够实时捕捉广告生态与用户兴趣的分布偏移（Distribution Shift）。

## 关联页面
- [Scaling Laws in Recommendation Systems — Predictable Performance Gains from Scaling](../concepts/scaling_laws_recsys.md)
- [用于推荐系统的大语言模型 — 概述](../concepts/llm4rec_overview.md)
- [Continued Pretraining — Domain Adaptation for LLM-based Recommendation](../concepts/continued_pretraining.md)
- [Generative Retrieval — 生成式检索](../concepts/generative_retrieval.md)
- [Model FLOPs Utilization (MFU) — Measuring Hardware Efficiency in Recommendation Models](../concepts/model_flops_utilization_mfu.md)

## 开放问题
1. **推理延迟与吞吐的极致优化**：在千亿级广告库与毫秒级响应要求下，如何进一步结合非自回归生成（Non-autoregressive Generation）或状态空间模型（SSM/Mamba）替代Transformer，以突破生成式推荐的延迟瓶颈？
2. **冷启动与稀疏序列泛化**：生成式范式高度依赖连续高质量行为序列。针对新用户（Cold-start）或行为稀疏场景，如何设计混合判别-生成架构或引入跨模态先验知识以保障基线性能？
3. **多目标与多任务统一建模**：当前GRAB主要聚焦CTR预测。如何将CVR、停留时长、GMV等多目标优化无缝融入同一生成式框架，并解决目标间的梯度冲突与负迁移问题？
4. **缩放定律的理论边界**：序列长度与模型性能的线性增长是否存在理论上限？数据质量下降、噪声累积或分布外（OOD）泛化是否会打破当前的缩放规律？

## 参考文献
- [来源：[2602_paper_26020186_GRAB_An_LLM-Inspired_Sequence-First_Click-Through_Rate_Pred.md](../sources/2602_paper_26020186_GRAB_An_LLM-Inspired_Sequence-First_Click-Through_Rate_Pred.md)]
- Vaswani, A., et al. "Attention Is All You Need." *NeurIPS*, 2017. (Transformer架构基础)
- Zhou, G., et al. "Deep Interest Network for Click-Through Rate Prediction." *KDD*, 2018. (传统序列推荐模型代表)
- Kaplan, J., et al. "Scaling Laws for Neural Language Models." *arXiv*, 2020. (LLM缩放定律原始文献)
- Li, Y., et al. "Generative Recommendation: A New Paradigm for Next-Item Prediction." *SIGIR*, 2024. (生成式推荐相关综述)