---
title: "Scaling Laws in Recommendation Systems — Predictable Performance Gains from Scaling"
category: "concepts"
tags: [scaling law, model scaling, data scaling, sequence length, compute efficiency, industrial recommendation]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../sources/2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md"]
related:
  - "../models/ULTRA_HSTU.md"
  - "../models/LONGER.md"
  - "../models/RankMixer.md"
  - "../concepts/model_flops_utilization_mfu.md"
  - "../synthesis/scaling_laws_comparison.md"
confidence: "high"
status: "stable"
---

# 推荐系统中的扩展定律

## 概述

推荐系统中的扩展定律描述了模型/数据/计算规模与推荐性能之间的**可预测关系**。受大语言模型中已建立的扩展定律（Kaplan 等，2020；Hoffmann 等，2022）启发，近期工业工作证明推荐系统在以下扩展时表现出类似的可预测提升：（1）**模型参数**（更深/更宽的架构），（2）**序列长度**（更长的用户行为历史），以及（3）**训练数据**（更多用户交互）。**Meta 的 HSTU 工作（2024）首次通过大规模实证确立了推荐领域的 Scaling Law**，将推荐任务重构为生成式序列转换问题，并在 1.5T 参数规模下验证了跨越三个数量级的严格幂律增长，证明“生成式范式+架构优化”是使推荐系统遵循缩放定律的核心前提。最新综述研究进一步确认，生成式推荐模型在知识融合、自然语言理解与推理生成等维度同样严格遵循扩展定律，但工业落地面临显著的**效率-准确性权衡**：生成式架构的端到端推理延迟通常比传统判别式模型高 2~5 倍。然而，推荐系统面临独特的挑战——严格的延迟约束、分布偏移和对高 GPU 利用率的需求——使得扩展曲线与 LLM 不同。ULTRA-HSTU 等近期工作证明，扩展定律曲线可以通过协同设计来**弯曲**，在每单位计算中实现更好的性能。此外，**GRAB（2026）在 CTR 预测任务中提供了序列长度扩展定律的工业级实证**，证明生成式架构能有效打破传统 DLRM 的长序列性能饱和瓶颈，实现业务指标的显著跃升。**HyFormer（2026）进一步在统一 CTR 架构下验证了 Scaling Law**，证明在参数量与 FLOPs 预算严格对齐时，模型性能仍随算力投入呈单调增长，为工业推荐系统的高效扩展提供了新范式。**与此同时，工业界逐渐认识到稀疏嵌入层（Sparse Embedding）的扩展与稠密网络扩展同等重要。OCP（2026）等工作首次系统验证了“稀疏-稠密协同扩展”范式，通过正交约束投影解决大规模 ID 词表扩展中的表征崩溃问题，补齐了 Scaling Law 在离散特征空间落地的关键一环。**

## 要点

- **可预测的性能增益**：更多参数、数据和序列长度产生单调提升
- **四个扩展维度**：模型规模、序列长度、训练数据量、**稀疏词表/嵌入层规模**
- **生成式范式奠基**：HSTU 首次确立推荐缩放定律，验证 1.5T 参数规模下的幂律增长
- **序列优先范式突破**：GRAB 在百度广告系统验证了序列长度扩展定律，打破传统 DLRM 长序列性能饱和瓶颈，实现收入 +3.05%、CTR +3.49% 的业务增益
- **统一架构扩展验证**：HyFormer 打破序列压缩与特征融合解耦范式，在参数量与 FLOPs 预算对齐时实现性能单调增长，进一步巩固工业级 Scaling Law 验证
- **稀疏-稠密协同扩展**：OCP 提出正交约束投影机制，解决超大规模 Item-ID 词表扩展时的表征崩溃与长尾过拟合，实现 UCXR +12.97%、GMV +8.9% 的工业级收益
- **生成式扩展验证**：最新综述证实生成式推荐严格遵循 Scaling Laws，在冷启动与复杂意图场景下指标提升 15%~30%
- **效率-准确性权衡**：生成式范式带来显著性能增益，但推理延迟通常增加 2~5 倍，长尾生成存在 5%~12% 幻觉率
- **工业验证**：LONGER、RankMixer、HSTU、ULTRA-HSTU、GRAB、HyFormer 与 OCP 都在生产中确认了扩展定律或其协同变体
- **弯曲曲线**：系统协同设计（线性注意力、统一词表、流式训练、交替优化、正交投影）实现每 FLOP 更好的性能与表征稳定性
- **独特挑战**：延迟约束、分布偏移、冷启动、可解释性弱、GPU 利用率、基准测试缺失、稀疏表征坍缩
- **业务影响**：扩展转化为可衡量的业务指标提升（CTR、CVR、参与度、核心转化 +12.4%、GMV +8.9%）

## 详情

### 扩展定律基础

在 LLM 中，扩展定律描述了幂律关系：

```
Loss ∝ N^(-α) × D^(-β) × C^(-γ)
```

其中 N = 模型参数，D = 训练数据，C = 计算预算。

在推荐系统中，这种关系映射到业务指标。**HSTU 的实证研究首次明确：推荐模型质量随训练算力（FLOPs）增加呈现严格的幂律增长，跨越 3 个数量级（十亿至万亿参数）未出现性能饱和。** 这标志着推荐系统从“手工特征工程与双塔架构”正式迈入“基础模型缩放”时代。

```
Performance ∝ Compute^(-α) ∝ f(model_size, sequence_length, data_volume, sparse_vocab_size, compute_efficiency)
```

### 生成式范式与 HSTU 架构奠基

将推荐任务重构为生成式序列转换（Generative Recommenders）是验证缩放定律的关键前提。传统 DLRM 依赖稠密/稀疏特征拼接，难以随算力线性扩展；而生成式范式将用户历史交互序列直接视为离散 Token 序列，在自回归框架下统一建模召回、排序与重排任务。HSTU（Hierarchical Sequential Transduction Unit）作为该范式的核心骨干，通过以下设计突破扩展瓶颈：

- **统一离散化词表**：将海量用户 ID、物品 ID 及异构上下文特征统一映射为共享词表中的 Token，消除传统 Embedding 查找表的内存墙，使模型能够直接处理超大规模稀疏空间。
- **线性化注意力与相对位置偏置**：摒弃计算密集的全局 Softmax 注意力，采用可学习相对位置偏置与低秩投影/分块计算策略，将序列建模复杂度从 $O(L^2)$ 优化至接近 $O(L)$，显著提升长序列训练与推理效率。
- **流式非平稳数据训练**：针对推荐数据分布随时间快速变化的特性，采用在线流式采样、动态学习率调度与混合精度训练，保障万亿参数模型在工业级数据流上的稳定收敛。

[来源：[2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md](../sources/2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md)]

### 生成式扩展的优势与验证

最新系统性综述研究进一步从宏观视角验证了生成式推荐范式与扩展定律的深度绑定，并明确了其在工业场景中的优势与代价：

- **Scaling Laws 的普适性确认**：综述明确指出，生成式推荐模型在参数规模、数据量与序列长度扩展时，同样呈现严格的幂律性能增长。生成范式通过统一表征空间与自回归建模，有效释放了算力扩展带来的表征容量红利。
- **核心优势验证**：生成式架构在五大维度展现扩展红利：（1）世界知识集成（外部常识注入），（2）自然语言理解（复杂意图解析），（3）逻辑推理（CoT 动态意图捕捉），（4）缩放定律遵循（算力换性能），（5）创造性生成（个性化内容/对话输出）。在冷启动与复杂意图场景下，基于 LLM 的生成式方法相比传统协同过滤与深度判别模型，在 NDCG@10 与 Recall@20 指标上平均提升约 **15%~30%**；在可解释性与多轮对话任务中，用户满意度（CSAT）与任务完成率提升约 **20%~40%**。
- **效率-准确性权衡（Efficiency-Accuracy Trade-off）**：尽管扩展带来显著收益，但生成式模型的端到端推理延迟通常比传统判别式模型高 **2~5 倍**。此外，在长尾物品生成时存在 **5%~12% 的幻觉率**上升问题。这一工业现实表明，单纯堆砌算力会遭遇服务成本与延迟瓶颈，必须通过架构轻量化、缓存优化与系统协同设计（如 ULTRA-HSTU 的弯曲曲线策略）来平衡扩展收益与部署可行性。

[来源：[2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md](../sources/2510_paper_25102715_A_Survey_on_Generative_Recommendation_Data,_Model,_and_Task.md)]

### RecSys 中的核心扩展维度

#### 1. 模型参数扩展
- **HSTU (Meta)**：首次验证推荐模型质量随训练算力呈幂律增长，跨越 **3 个数量级**（1B 至 1.5T 参数）未出现性能饱和，确立缩放定律在推荐领域的普适性。
- **RankMixer**：在相似延迟下从 ~10M 扩展到 1B 参数（100 倍）
- **OneRec-V2**：通过计算效率扩展到 8B 参数
- **OneRec-Foundation**：1.7B 和 8B 变体显示可预测的提升
- **HyFormer**：在统一 CTR 架构下，当参数量与 FLOPs 预算严格对齐时，性能仍随规模扩大呈单调增长，且扩展曲线斜率优于传统解耦基线，验证了统一骨干网络在算力投入上的更高边际收益。
- 每个维度的增加都产生可衡量的业务指标增益

#### 2. 序列长度扩展
- **LONGER**：证明超长序列（数千次交互）提供一致的增益
- **HSTU**：在处理长度为 **8192** 的超长交互序列时，推理吞吐量达到基于 FlashAttention2 的 Transformer 的 **5.3 倍至 15.2 倍**，显存占用大幅降低，满足工业场景毫秒级延迟要求。
- **GRAB (百度)**：提出“序列优先”的生成式 CTR 预测范式，彻底摒弃传统 DLRM 的特征拼接与多塔判别架构。其核心引入**因果动作感知多通道注意力机制（CamA）**，通过因果掩码与多通道并行计算，精准解耦时间衰减效应与异构动作信号（曝光、点击、转化等），实现对动态兴趣演化的细粒度捕捉。大规模离线与线上实验实证表明，GRAB 的表征能力随输入序列长度增加呈现**单调且近似线性的提升**，直接打破了传统 DLRM 在长序列场景下的性能饱和瓶颈。在百度广告系统全量部署中，序列扩展直接转化为业务收益：广告总收入提升 **3.05%**，整体 CTR 提升 **3.49%**。
- 更长序列同时捕捉长期偏好和短期意图
- 序列长度与性能之间的关系是**可预测且单调的**
- 注意力效率技术（token 合并、稀疏/线性注意力、IO感知分块、CamA 多通道解耦）支持更长序列
- **部署挑战**：GRAB 也指出，自回归生成在超大规模高并发排序中可能引入额外延迟，极端长序列受限于 GPU 显存与实时 SLA，需结合知识蒸馏、并行解码或序列压缩技术进行工程优化；同时生成式范式对高质量连续行为序列依赖较强，冷启动场景仍需进一步探索。

[来源：[2602_paper_26020186_GRAB_An_LLM-Inspired_Sequence-First_Click-Through_Rate_Pred.md](../sources/2602_paper_26020186_GRAB_An_LLM-Inspired_Sequence-First_Click-Through_Rate_Pred.md)]

#### 3. 数据量扩展
- 更多用户交互 → 更好的模式学习
- OpenOneRec 使用来自 16 万用户的 9600 万交互
- **流式数据扩展**：HSTU 采用在线流式采样策略应对推荐数据分布随时间快速变化的特性，证明在动态非平稳数据流上持续扩展数据量仍能带来稳定收益。
- Meta、字节跳动和快手的工业系统都确认了数据扩展的益处

#### 4. 稀疏嵌入与词表扩展 (Sparse Embedding & Vocabulary Scaling)
工业推荐系统的核心瓶颈之一在于海量离散 ID（Item-ID/User-ID）构成的超大规模稀疏词表。传统扩展策略在盲目扩大词表规模时，极易引入低频长尾噪声，导致嵌入空间发生**表征共线性坍缩（Representation Collapse）**与泛化能力断崖式下降。**OCP（2026）** 首次系统性地提出了面向稀疏扩展的底层优化范式，补齐了 Scaling Law 在离散特征空间的验证拼图：
- **正交约束投影（Orthogonal Constrained Projection）**：在反向传播路径中嵌入梯度投影算子，将参数更新动态限制在正交子空间内。该机制有效阻断了低频物品对主流表征空间的梯度污染，防止训练后期嵌入向量发生维度坍缩。
- **奇异值谱对齐与高熵保持**：从谱分析角度证明，OCP 可强制嵌入矩阵的奇异值分布逼近正交基，最大化奇异熵（Singular Entropy）。高奇异熵确保了不同 Item-ID 在隐空间中保持均匀分布与各向同性，显著提升模型对未见物品的零样本泛化能力。
- **稀疏-稠密协同扩展**：OCP 与稠密网络层（Dense Layers）的扩展深度解耦。在持续扩大词表规模的同时，支持深层网络参数的稳定增长，避免传统缩放策略中常见的梯度爆炸或表征退化现象，实现“稀疏扩展不降效、稠密扩展可叠加”。
- **工业级收益**：在京东真实商品推荐场景全量上线后，OCP 使 UCXR（用户交叉转化率）提升 **12.97%**，GMV（商品交易总额）提升 **8.9%**，训练损失收敛速度提升约 30%，显著降低了工业场景下的算力成本。
- **LLM4Rec 关联价值**：OCP 为 LLM 驱动的推荐系统提供了稳定的 ID-Text 对齐基础。其生成的高熵、正交化嵌入可直接用于 LLM Token Embedding 初始化或 Adapter/LoRA 微调，有效缓解大模型在推荐场景下的长尾幻觉与语义漂移问题。

[来源：[2603_paper_26031869_OCP_Orthogonal_Constrained_Projection_for_Sparse_Scaling_in.md](../sources/2603_paper_26031869_OCP_Orthogonal_Constrained_Projection_for_Sparse_Scaling_in.md)]

### 统一架构下的扩展验证：HyFormer

传统工业推荐系统通常采用“序列压缩 + 特征融合”的两阶段解耦流水线（如先使用 LONGER 压缩序列，再用 RankMixer 融合特征），这种范式在算力扩展时容易遭遇表征容量瓶颈与信息交互损失。**HyFormer（2026）** 提出了一种统一的混合 Transformer 骨干架构，将长序列建模与异构非序列特征深度融合于单一网络中，为 Scaling Law 在 CTR 预测中的验证提供了全新视角：

- **Query Decoding（Query解码机制）**：将非序列稠密特征动态扩展为全局 Token（Global Tokens），并利用长行为序列的逐层 Key-Value 表示进行交叉注意力解码。该机制以 Query 为锚点高效检索历史行为关键信号，避免传统序列压缩带来的信息瓶颈。
- **Query Boosting（Query增强机制）**：引入高效的 Token Mixing 模块，专门用于增强跨 Query 与跨序列的异构特征交互，通过轻量级混合操作捕获高阶组合特征，弥补传统注意力在稠密特征交互上的计算冗余。
- **交替优化策略（Alternating Optimization）**：上述两种互补机制在 Transformer 的每一层中严格交替执行，形成“解码-增强-精炼”的迭代闭环。该策略在严格控制前向计算开销（FLOPs）的同时，最大化了信息流动效率。
- **Scaling Law 实证**：在十亿级工业数据集上，当参数量与 FLOPs 预算完全对齐时，HyFormer 展现出显著优于 LONGER 与 RankMixer 的扩展行为，性能提升曲线更为陡峭。大规模线上 A/B 测试证实其在低延迟与高吞吐约束下，CTR 与 GAUC 均实现显著正向增长，进一步巩固了“统一架构+交替优化”范式在工业级 Scaling Law 中的有效性。

[来源：[2601_paper_26011268_HyFormer_Revisiting_the_Roles_of_Sequence_Modeling_and_Feat.md](../sources/2601_paper_26011268_HyFormer_Revisiting_the_Roles_of_Sequence_Modeling_and_Feat.md)]

### 弯曲扩展定律曲线

ULTRA-HSTU、GRAB、HyFormer 与 OCP 的架构演进共同引入了**弯曲扩展定律曲线（Bending the Scaling Curve）**的概念：通过算法-系统协同设计，打破传统幂律的固定斜率，在相同 FLOPs 预算下获得更高的性能上限或更低的延迟开销。

```
Performance
    ^
    |     /  Conventional models (baseline scaling)
    |    /
    |   /   ULTRA-HSTU / HSTU / GRAB / HyFormer (bent curve — better per-FLOP efficiency)
    |  /
    | /    OCP + Dense Co-Scaling (stabilized curve — prevents collapse during sparse expansion)
    |/
    +----------------------------------> Compute / Scale
```

- **计算效率弯曲**：线性注意力、流式训练、IO 感知分块与交替优化策略降低了有效 FLOPs，使曲线向左上方移动。
- **表征稳定性弯曲**：OCP 的正交约束投影机制从底层几何结构上阻断了稀疏扩展过程中的表征坍缩，使扩展曲线在词表规模急剧扩大时仍保持单调增长，避免了传统 Scaling Law 在离散空间中的“断崖式饱和”。
- **稀疏-稠密协同**：未来工业系统的扩展将不再局限于单一维度的堆叠，而是走向“序列长度 × 稠密参数 × 稀疏词表 × 数据流”的多维正交扩展，通过联合优化实现每单位算力的边际收益最大化。

### 挑战与未来方向

尽管扩展定律在推荐系统中展现出巨大潜力，但工业落地仍面临多重挑战：
- **效率-准确性权衡**：生成式范式与超长序列建模带来 2~5 倍延迟增长，需结合知识蒸馏、KV Cache 优化与硬件感知编译进行系统级加速。
- **稀疏表征的几何稳定性**：超大规模 ID 词表扩展易引发共线性坍缩，OCP 等正交约束方法为底层优化提供了新方向，但十亿级词表下的实时投影开销仍需轻量化近似算法（如随机正交投影、低秩分解）进一步突破。
- **分布偏移与冷启动**：流式数据扩展虽能提升长期收益，但动态分布偏移要求模型具备在线自适应能力；生成式范式对高质量连续行为序列依赖较强，冷启动场景仍需探索多模态先验注入与跨域迁移策略。
- **基准测试与可解释性**：缺乏统一的 Scaling Law 评测基准（涵盖不同延迟 SLA、不同稀疏度、不同业务目标），且生成式推荐的可解释性弱于传统判别模型，需结合因果推断与归因分析建立可信评估体系。

## 相关页面
- [生成式推荐系统 (Generative Recommendation)](./generative_recommendation.md)
- [序列建模与长行为序列 (Sequence Modeling & Long-term Behavior)](./sequence_modeling.md)
- [推荐系统基础模型 (Foundation Models for RecSys)](./foundation_models_rec.md)
- [稀疏特征与嵌入优化 (Sparse Features & Embedding Optimization)](./sparse_embedding.md)

---

## 更新完成：2603_paper_26031869_OCP_Orthogonal_Constrained_Projection_for_Sparse_Scaling_in.md
**更新时间**: 2026-04-23 05:19
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2603_paper_26031869_OCP_Orthogonal_Constrained_Projection_for_Sparse_Scaling_in.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
