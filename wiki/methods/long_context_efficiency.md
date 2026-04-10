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

长上下文效率涵盖了一系列使基于 Transformer 的序列建模**在工业级规模上计算可行**的技术，其中用户行为历史跨越数千次交互。这些技术通过多种互补策略解决自注意力的二次复杂度瓶颈：**token 合并**减少有效序列长度、**KV 缓存**避免冗余计算、**混合精度训练**提高内存效率，以及**长度外推训练**处理比训练期间所见更长的序列。LONGER（InnerTransformers、混合注意力、全局 token）和 10k 序列建模方法（STCA 线性复杂度交叉注意力、请求级批量共享、长度外推）中的方法代表了工业长上下文优化的最先进水平。

近年来，工业界进一步将优化视角从“单一算法降复杂度”扩展至**全栈工程协同**，强调**目标感知注意力（Target-Aware Attention）**、**请求级批处理与缓存复用（Request-Level Batching & Cache Reuse）**以及**I/O 与计算图优化**。小红书 LASER、LinkedIn Feed-SR、腾讯长行为序列建模等工作表明，长序列效率已不再是附属工程，而是决定模型能否在线落地的核心创新维度。[来源：[rankmixer_to_oneranker.md](wiki/sources/rankmixer_to_oneranker.md)]

## 要点

- **Token 合并**：通过分组相似 token 减少有效序列长度
- **KV 缓存与跨请求复用**：避免相同特征的冗余计算，支持用户/物品侧解耦复用
- **混合精度训练**：减少更长序列的内存占用
- **长度外推**：支持处理比训练长度更长的序列
- **激活重计算**：用计算换内存以支持更长序列
- **目标感知注意力**：将历史内部自注意力改写为目标到历史的交叉注意力，降低复杂度并提升相关性
- **请求级批处理与 Serving 优化**：在批次内共享编码计算，优化 I/O 访问与在线推理预算
- **工业验证**：部署于字节跳动、小红书、LinkedIn、腾讯等工业级系统

## 详情

### 长上下文挑战

在工业推荐中：
- 用户行为历史跨越**数千次交互**，且持续增长
- 完整自注意力需要 O(N^2) 计算和内存，I/O 访问成为新瓶颈
- 生产延迟约束（< 10ms）限制可行计算，要求计算图与存储访问模式高度可控
- 训练内存限制最大序列长度，且需兼顾增量更新与时效性衰减

长上下文效率技术使超长序列建模成为实际可行，且必须与在线 Serving 约束深度耦合。[来源：[rankmixer_to_oneranker.md](wiki/sources/rankmixer_to_oneranker.md)]

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

益处：
- 避免相同特征的冗余计算
- 减少每请求延迟与显存峰值
- 在高 QPS 场景中特别有效，使长序列模型具备工业级吞吐能力 [来源：[rankmixer_to_oneranker.md](wiki/sources/rankmixer_to_oneranker.md)]

### 目标感知注意力与分段机制（工业新范式）

传统长序列自注意力计算所有历史 token 间的交互，存在大量与当前目标无关的冗余计算。工业界转向**目标感知（Target-Aware）**与**分段（Segmented）**设计：

- **STCA（稀疏 Token 交叉注意力）**：将历史内部的 self-attention 改写为 stacked target-to-history cross attention。通过线性复杂度的交叉注意力取代二次自注意力，仅计算目标 token 与历史摘要 token 的交互，显著降低计算上限。
- **LASER（小红书）**：结合超长行为序列的 I/O 访问优化与 target-aware segmented attention。将长序列按时间或语义分段，仅对与当前目标高度相关的分段进行精细注意力计算，其余分段采用轻量级聚合，实现全栈长序列优化。
- **Feed-SR（LinkedIn）**：在判别式序列排序器中引入 RoPE 位置编码、增量训练（Incremental Training）与时效性加权（Recency Weighting），并通过 Late Fusion 平衡长短期兴趣，确保长序列在真实 Feed 流中的稳定推理。

这些方案表明，长序列效率的核心已从“单纯压缩序列”转向“按需计算与目标对齐”。[来源：[rankmixer_to_oneranker.md](wiki/sources/rankmixer_to_oneranker.md)]

### 请求级批处理与 Serving 优化

**请求级批量共享（Request-Level Batching, RLB）**：
- 在批次内的请求间共享编码计算
- 减少常见特征的冗余计算
- 对共享的用户/物品特征特别有效
- 与 STCA 结合后，可在在线服务阶段显式引入序列计算的复用机制，提升吞吐并稳定延迟

**Serving 与推理预算控制**：
- 训练阶段的模型创新必须转化为在线可控的计算图、存储访问模式与推理策略
- 引入 LazyAR 解码、动态 Beam Serving、近线 Reasoning Distillation 等推理期优化手段
- 长序列模型的竞争已延伸至推理阶段（Inference-Time Scaling），要求系统级协同设计 [来源：[rankmixer_to_oneranker.md](wiki/sources/rankmixer_to_oneranker.md)]

### 训练优化

#### 混合精度训练
- 对激活和梯度使用 FP16/BF16
- 对主权重和优化器状态使用 FP32
- 内存减少约 2 倍，支持更长序列

#### 激活重计算
- 在前向传播期间丢弃中间激活
- 在反向传播期间重新计算
- 用计算（更便宜）换内存（更稀缺）
- 在相同 GPU 内存下支持约 2 倍更长序列

#### 增量训练与时效性建模
- 采用增量训练策略持续吸收新行为数据，避免全量重训
- 结合 Recency Weighting 与 Late Fusion 缓解长序列中的“近期偏好淹没”问题
- 配合 Memory Bank 控制长历史上的重复编码成本（如 LEMUR 多模态长序列方案）[来源：[rankmixer_to_oneranker.md](wiki/sources/rankmixer_to_oneranker.md)]

### 长度外推训练

一个关键挑战：在长度 N 的序列上训练的模型必须在推理时处理长度 M > N 的序列。

长度外推的技术：
- **位置编码插值**：缩放位置编码以适应更长序列
- **RoPE 缩放**：带缩放因子的旋转位置嵌入
- **课程训练**：在 progressively 更长的序列上训练
- **注意力模式泛化**：设计泛化到任意长度的注意力模式

### 综合优化栈

生产就绪的长上下文系统结合多种技术，形成从算法到 Serving 的全栈优化：

| 优化 | 益处 | 成本/约束 |
|------|------|------|
| Token 合并 | 减少序列长度 | 近似误差 |
| KV 缓存与跨请求复用 | 减少每请求计算，支持用户/物品解耦 | 缓存内存与一致性维护 |
| 目标感知注意力 (STCA/LASER) | 线性/分段复杂度，按需计算 | 目标对齐设计复杂度 |
| 请求级批处理 (RLB) | 批次内共享编码，提升吞吐 | 请求调度与对齐开销 |
| 混合精度 | 2 倍内存减少 | 微小精度损失 |
| 激活重计算 | 2 倍序列长度 | 反向传播 2 倍计算 |
| 全局 token | 稳定的长序列注意力 | 最小开销 |
| 长度外推 | 处理未见长度 | 训练复杂度与位置编码设计 |
| I/O 与计算图优化 | 降低存储访问延迟，适配 Serving 约束 | 系统级工程改造 |

## 关联

- [LONGER](../models/LONGER.md) — 实现这些技术的主要系统
- [STCA 与 10k 序列建模](./stca_10k_sequence.md) — 线性交叉注意力与请求级批处理
- [LASER](../models/LASER.md) — 小红书目标感知分段注意力与 I/O 优化
- [Feed-SR](../models/FeedSR.md) — LinkedIn 判别式长序列排序器工程实践
- [UG-Separation](../models/UG_Separation.md) — 用户/物品侧解耦与 Serving 复用
- [稀疏注意力](./sparse_attention_seq_rec.md) — 互补的效率方法
- [扩展定律](../concepts/scaling_laws_recsys.md) — 效率使能序列长度扩展
- [ULTRA-HSTU](../models/ULTRA_HSTU.md) — 通过稀疏注意力的替代效率方法

## 开放问题

1. 在满足生产延迟约束的同时，可以处理的最大序列长度是多少？
2. Token 合并质量在不同推荐领域之间如何变化？
3. 长度外推能否对极长序列（100K+ token）更可靠？
4. 当 KV 缓存满时，缓存驱逐策略应如何工作？
5. 不同效率技术之间的交互是什么——它们是相加的还是协同的？
6. 目标感知注意力在生成式 One-Model 架构中如何与 Beam Search/Prefix Constraint 协同？
7. 长序列 I/O 优化与近线 Reasoning Distillation 能否进一步解耦训练与推理预算？[来源：[rankmixer_to_oneranker.md](wiki/sources/rankmixer_to_oneranker.md)]

## 参考文献

- Chai, Z., Ren, Q., Xiao, X., Yang, H., Han, B., Zhang, S., Chen, D., Lu, H., Zhao, W., Yu, L., Xie, X., Ren, S., Sun, X., Tan, Y., Xu, P., Zheng, Y., & Wu, D. (2025). LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders. RecSys 2025. arXiv:2505.04421.
- "Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling." arXiv:2511.06077.
- Leopold. (2025). 从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线. [来源：[rankmixer_to_oneranker.md](wiki/sources/rankmixer_to_oneranker.md)]

## 更新于 2026-04-09

**来源**: 2311_paper_23110588_Hiformer_Heterogeneous_Feature_Interactions_Learning_with_T.md
：添加低秩近似和模型剪枝作为 Transformer 推理加速的具体技术示例

**来源**: rankmixer_to_oneranker.md
：补充 STCA、LASER、FeedSR 等工业长序列方案，强调“目标感知注意力”与“请求级批处理/缓存复用”的工程价值；新增跨请求 KV 缓存、UG-Separation 解耦复用、I/O 与计算图优化、增量训练与时效性建模等内容；更新综合优化栈与开放问题。

---

## 更新完成：rankmixer_to_oneranker.md
**更新时间**: 2026-04-09 12:38
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 rankmixer_to_oneranker.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
