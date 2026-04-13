---
title: "Long Context Efficiency — Optimizing Transformer Inference for Long Sequences"
category: "methods"
tags: [long context, efficiency, KV cache, token merge, STCA, RLB, length extrapolation, industrial optimization]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md"]
related:
  - "../methods/sparse_attention_seq_rec.md"
  - "../models/LONGER.md"
  - "../concepts/scaling_laws_recsys.md"
  - "../models/ULTRA-HSTU.md"
confidence: "high"
status: "stable"
---

# 长上下文效率 — 优化 Transformer 长序列推理

## 概述

长上下文效率涵盖了一系列使基于 Transformer 的序列建模**在工业级规模上计算可行**的技术，其中用户行为历史跨越数千次交互。这些技术通过多种互补策略解决自注意力的二次复杂度瓶颈：**底层 IO 感知算子**突破显存墙、**token 合并**减少有效序列长度、**KV 缓存**避免冗余计算、**混合精度训练**提高内存效率，以及**长度外推训练**处理比训练期间所见更长的序列。LONGER（InnerTransformers、混合注意力、全局 token）和 10k 序列建模方法（STCA 线性复杂度交叉注意力、请求级批量共享、长度外推）中的方法代表了工业长上下文优化的最先进水平。

近年来，工业界进一步将优化视角从“单一算法降复杂度”扩展至**全栈工程协同**，强调**目标感知注意力（Target-Aware Attention）**、**请求级批处理与缓存复用（Request-Level Batching & Cache Reuse）**以及**I/O 与计算图优化**。小红书 LASER、LinkedIn Feed-SR、腾讯长行为序列建模等工作表明，长序列效率已不再是附属工程，而是决定模型能否在线落地的核心创新维度。同时，大语言模型领域成熟的上下文扩展技术（如 RoPE 线性插值、ALiBi 位置编码、KV Cache 压缩、参数高效微调与量化）正被快速引入推荐系统，与工业原生方案形成“算法近似-位置外推-状态压缩-推理加速”的立体技术对照。[来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)] [来源：[2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md](../sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md)] [来源：[2205_paper_22051413_FlashAttention_Fast_and_Memory-Efficient_Exact_Attention_wi.md](../sources/2205_paper_22051413_FlashAttention_Fast_and_Memory-Efficient_Exact_Attention_wi.md)]

## 要点

- **历史基石与瓶颈起点**：SASRec 首次将因果自注意力引入序列推荐，奠定并行建模范式，但其 $O(L^2)$ 复杂度与固定长度截断问题直接催生了后续长上下文优化技术
- **FlashAttention 与 IO 感知算子**：通过分块流式计算与在线 Softmax 突破显存墙，实现精确注意力的训练/推理加速
- **Token 合并**：通过分组相似 token 减少有效序列长度
- **KV 缓存与跨请求复用**：避免相同特征的冗余计算，支持用户/物品侧解耦复用
- **KV Cache 压缩**：通过量化、低秩近似与智能驱逐策略降低缓存显存占用
- **混合精度训练**：减少更长序列的内存占用
- **长度外推**：支持处理比训练长度更长的序列（RoPE 插值、ALiBi 等）
- **激活重计算**：用计算换内存以支持更长序列
- **目标感知注意力**：将历史内部自注意力改写为目标到历史的交叉注意力，降低复杂度并提升相关性
- **请求级批处理与 Serving 优化**：在批次内共享编码计算，结合连续批处理与投机解码优化 I/O 访问与在线推理预算
- **参数高效微调与模型压缩**：LoRA/Adapter 降低微调显存，INT4/INT8 量化与结构化剪枝支撑长序列部署
- **工业验证**：部署于字节跳动、小红书、LinkedIn、腾讯等工业级系统

## 详情

### 历史瓶颈与动机

序列推荐向深度学习范式的演进始于 **SASRec（Self-Attentive Sequential Recommendation, ICDM 2018）**。该工作首次将 Transformer 的因果自注意力机制引入推荐系统，通过下三角掩码严格遵循时间因果性，在统一框架下兼顾长期依赖建模与局部关键行为聚焦。SASRec 证明了自注意力在稀疏与稠密数据上的自适应能力，并凭借全序列并行计算将训练效率提升约一个数量级，为后续 LLM4Rec 的 Decoder 架构与 Prompt 上下文学习奠定了底层序列建模范式。[来源：[1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md](../sources/1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md)]

然而，随着工业场景对用户行为历史覆盖要求的不断提升，SASRec 架构暴露出两大核心瓶颈，直接成为长上下文效率优化的**历史起点与核心动机**：
1. **固定长度截断（Fixed-Length Truncation）**：模型需预设最大序列长度 $L$，超长历史必须硬性截断。这导致早期关键兴趣信号（如长期偏好、周期性复购模式）永久丢失，难以满足现代推荐系统对“全生命周期行为建模”的需求。
2. **二次方计算复杂度（$O(L^2)$ Complexity）**：标准自注意力的时间与空间复杂度随序列长度呈二次方增长。当 $L$ 从数百扩展至数千甚至上万时，显存占用与计算延迟呈指数级膨胀，严重违背工业在线服务 < 10ms 的延迟约束。

正是为突破 SASRec 遗留的复杂度与截断限制，工业界与学术界开启了长上下文效率的系统性探索：从**稀疏/线性注意力**（如 LONGER 的 Token 合并、ULTRAHSTU 的块稀疏掩码）降低理论计算上限，到**KV 缓存与跨请求复用**消除冗余编码，再到**目标感知交叉注意力（STCA/LASER）**将计算重心从“历史内部交互”转向“目标-历史对齐”。这些技术共同构成了从“固定截断近似”到“动态全量建模”的演进路径。[来源：[1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md](../sources/1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md)] [来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]

在工业推荐中，长上下文效率还必须与以下生产约束深度耦合：
- 用户行为历史跨越**数千次交互**，且持续增长
- 完整自注意力需要 $O(N^2)$ 计算和内存，I/O 访问成为新瓶颈
- 生产延迟约束（< 10ms）限制可行计算，要求计算图与存储访问模式高度可控
- 训练内存限制最大序列长度，且需兼顾增量更新与时效性衰减

### 底层算子优化：FlashAttention 与 IO 感知计算

传统自注意力实现将完整的 $N \times N$ 注意力矩阵写入 GPU 高带宽内存（HBM），导致显存占用呈二次方增长，并引发严重的 IO 延迟瓶颈。FlashAttention 首次将 **GPU 内存层级间的 IO 开销** 作为核心设计原则，通过硬件协同的流式计算架构，在保持数学精确性的前提下彻底打破“显存墙”。

**核心机制**：
- **IO 感知分块策略（Tiling）**：根据目标 GPU 的片上 SRAM 容量动态计算最优分块尺寸，将 Q、K、V 矩阵切分为子块逐块加载至 SRAM。在片上完成局部 QK 乘法、Softmax 归一化与 PV 乘法后，仅将最终输出写回 HBM，大幅削减 HBM 读写次数。
- **在线 Softmax 计算（Online Softmax）**：在分块迭代过程中动态维护 Softmax 的归一化因子与指数和，通过增量更新避免一次性加载全局注意力矩阵导致的显存溢出与数值不稳定。
- **反向传播重计算（Backward Recomputation）**：前向传播时不存储中间激活矩阵，反向传播时按需重新计算。该策略将显存复杂度从 $O(N^2)$ 降至 $O(N)$，以可控的额外 FLOPs 换取显存瓶颈的解除。

**在 LLM4Rec 中的价值**：
- **无损精确性**：与稀疏/线性近似注意力不同，FlashAttention 保证数学等价性，避免长序列推荐中细粒度交互信号的丢失。
- **训练与推理双加速**：在 BERT/GPT 类架构上实现 15%~300% 的端到端加速，直接赋能推荐模型在 16K~64K 超长行为序列上的预训练与微调。
- **算力底座协同**：作为底层算子，FlashAttention 与 KV Cache 压缩、PEFT 微调、连续批处理等上层优化无缝兼容，构成工业长序列推荐系统的标准计算图基座。

**局限性**：底层浮点计算复杂度仍为 $O(N^2)$，在极长序列下计算耗时依然呈二次方增长；性能高度依赖 GPU 架构与 SRAM 容量，需针对硬件调优分块参数。工业实践中常与块稀疏掩码或线性注意力结合，以进一步突破理论计算上限。[来源：[2205_paper_22051413_FlashAttention_Fast_and_Memory-Efficient_Exact_Attention_wi.md](../sources/2205_paper_22051413_FlashAttention_Fast_and_Memory-Efficient_Exact_Attention_wi.md)]

### Token 合并（LONGER）

**核心思路**：将相似 token 分组并作为单一单元处理。

```
Original: [t1, t2, t3, t4, t5, t6, t7, t8]  (8 tokens)
Merged:   [m1, m2, m3, m4]                   (4 tokens, each represents 2 originals)
```

过程：
1. **相似度计算**：识别具有相似表示的 token
2. **分组**：将相似 token 合并为代表 token
3. **InnerTransformer**：轻量级 transformer 处理合并后的 token 组
4. **混合注意力**：关键 token 上使用完整注意力，合并组上使用近似注意力

InnerTransformer 是一个轻量级模块：
- 高效处理合并的 token 组
- 与主 Transformer 相比使用缩减的隐藏维度
- 保持足够的容量来捕捉组级模式

> **技术对照**：Token 合并属于**输入侧近似压缩**，通过牺牲细粒度交互换取计算量下降；而 RoPE/ALiBi 属于**位置编码外推**，KV Cache 压缩属于**状态存储优化**，FlashAttention 属于**底层算子 IO 优化**。四者分别作用于序列构建、位置泛化、显存管理与硬件协同，形成互补栈。[来源：[2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md](../sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md)]

### 全局 Token 机制（LONGER）

特殊 token 与所有位置相互关注并被所有位置关注：
- 稳定长序列上的注意力模式
- 防止"中间丢失"问题
- 充当全局上下文聚合器

### KV 缓存与跨请求复用

**关键洞察**：许多特征在请求间高度共享，且用户侧与物品侧计算可解耦。

- **用户画像特征**：变化不频繁，按用户缓存 KV 状态
- **物品特征**：在多个请求同一物品的用户间共享
- **上下文特征**：经常重复（一天中的时间、设备类型）
- **跨请求 KV 缓存（Cross-Request KV Caching）**：在统一主干（如 OneTrans）中显式引入跨请求缓存机制，避免重复编码
- **用户/物品侧解耦（UG-Separation 范式）**：将 dense interaction 模型中的 user-side 与 item-side 信息流显式拆分，实现“用户侧只计算一次”的 Serving 复用能力

**KV Cache 压缩机制**：
随着序列长度突破 10k+，KV 状态显存占用呈线性增长，成为 Serving 瓶颈。工业界引入以下压缩策略：
- **低秩近似（Low-Rank Approximation）**：对 KV 矩阵进行 SVD 或随机投影，保留主成分方向，显著降低存储维度
- **量化压缩（INT8/FP8 KV）**：对缓存的 Key/Value 进行动态或静态量化，配合反量化算子实现无损/微损恢复
- **智能驱逐策略（Eviction Policy）**：基于注意力权重、时间衰减或语义重要性动态淘汰低价值 KV 块，结合滑动窗口与全局摘要 token 维持上下文连贯性

益处：
- 避免相同特征的冗余计算
- 减少每请求延迟与显存峰值
- 在高 QPS 场景中特别有效，使长序列模型具备工业级吞吐能力 [来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)] [来源：[2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md](../sources/2307_paper_23070643_A_Comprehensive_Overview_of_Large_Language_Models.md)]

### 目标感知注意力与分段机制（工业新范式）

传统长序列自注意力计算所有历史 token 间的交互，存在大量与当前目标无关的冗余计算。工业界转向**目标感知（Target-Aware）**与**分段（Segmented）**设计：

- **STCA（稀疏 Token 交叉注意力）**：将历史内部的 self-attention 改写为 stacked target-to-history cross attention。通过线性复杂度的交叉注意力取代二次自注意力，仅计算目标 token 与历史摘要 token 的交互，显著降低计算上限。
- **LASER（小红书）**：结合超长行为序列的 I/O 访问优化与 target-aware segmented attention。将长序列按时间或语义分段，仅对与当前目标高度相关的分段进行精细注意力计算，其余分段采用轻量级聚合，实现全栈长序列优化。
- **Feed-SR（LinkedIn）**：在判别式序列排序器中引入 RoPE 位置编码、增量训练（Incremental Training）与时效性加权（Recency Weighting），并通过 Late Fusion 平衡长短期兴趣，确保长序列在真实 Feed 流中的稳定推理。

这些方案表明，长序列效率的核心已从“单纯压缩序列”转向“按需计算与目标对齐”。[来源：[rankmixer_to_oneranker.md](../sources/rankmixer_to_oneranker.md)]

### 请求级批处理与 Serving 优化

**请求级批量共享（Request-Level Batching, RLB）**：
- 在批次内的请求间共享编码计算
- 减少常见特征的冗余计算
- 对共享的用户/物品特征特别有效
- 与 STCA 结合后，可在在线服务阶段显式引入序列计算的复用机制，提升吞吐并稳定延迟

**连续批处理与推理加速（Continuous Batching & Speculative Decoding）**：
- **连续批处理**：打破传统静态 batch 边界，允许请求动态进出计算队列，最大化 GPU 利用率，显著降低长尾延迟
- **投机解码（Speculative Decoding）**：利用轻量级草稿模型（或历史缓存摘要）预生成多个 token/特征，主模型并行验证，在推荐生成式排序或序列补全场景中可提升 1.5~2.5 倍吞吐
- 训练阶段的模型创新必须转化为在线可控的计算图、存储访问模式与推理策略
- 长序列模型的竞争已延伸至推理阶段（Inference-Time Scaling），要求 Serving 框架具备动态资源调度与计算图融合能力

---

## 更新完成：1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md
**更新时间**: 2026-04-13 06:56
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 1808_paper_18080978_Self-Attentive_Sequential_Recommendation.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
