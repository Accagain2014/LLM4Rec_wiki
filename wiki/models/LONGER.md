---
title: "LONGER — Long-Sequence Optimized Transformer for Industrial Recommenders"
category: "models"
tags: [LONGER, long sequence, transformer, ByteDance, sparse attention, token merge, industrial deployment, scaling law]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md"]
related:
  - "../concepts/scaling_laws_recsys.md"
  - "../methods/sparse_attention_seq_rec.md"
  - "../methods/long_context_efficiency.md"
  - "../entities/bytedance.md"
confidence: "high"
status: "stable"
---

# LONGER — 面向 GPU 高效推荐器的长序列优化 Transformer

## 概述

LONGER（Long-sequence Optimized traNsformer for GPU-Efficient Recommenders）是字节跳动开发的工业级规模序列建模系统，解决了在生产推荐系统中建模**超长用户行为序列**的挑战。先前的解决方案依赖于两阶段检索或间接建模范式，遭受上下游不一致和计算效率低下的问题。LONGER 引入了完全同步的端到端 Transformer，具有三项关键创新：（1）**全局 token 机制**用于稳定长上下文上的注意力，（2）**token 合并模块**结合轻量级 InnerTransformers 和混合注意力以降低二次复杂度，（3）**GPU 优化工程**包括混合精度训练、激活重计算、KV 缓存服务及基于 IO 感知注意力范式的底层算力协同。LONGER 已部署于字节跳动 10+ 场景，服务数十亿用户。

## 要点

- **端到端长序列建模**：消除两阶段检索的不一致性
- **全局 token 机制**：稳定超长上下文上的注意力模式
- **Token 合并 + InnerTransformer**：降低二次注意力复杂度
- **全 GPU 优化**：混合精度、激活重计算、KV 缓存、IO 感知分块
- **工业级部署**：字节跳动 10+ 场景，数十亿用户
- **验证工业级扩展定律**：广告和电商中离线和在线的一致增益
- **底层算力协同**：基于 FlashAttention 范式构建生产级长序列推理与训练管线
- **架构演进基石**：为后续统一序列建模与特征交互的混合架构（如 HyFormer）提供算力底座与全局 Token 范式参考

## 详情

### 问题：超长序列建模

在工业推荐系统中，捕捉**长期和短期用户偏好**需要对非常长的行为序列建模。现有方法面临两个根本性局限：

1. **两阶段检索**：先检索候选，再排序——引入阶段间不一致
2. **间接建模**：通过摘要或池化近似长序列——丢失细粒度信息

两种方法都无法充分利用长用户历史中的信息，且传统自注意力机制在序列长度增加时面临 $O(N^2)$ 的显存墙与计算瓶颈，难以直接支撑数万步交互序列的端到端训练与低延迟推理。

### 核心创新

#### 1. 全局 Token 机制

- 引入特殊的**全局 token**，与序列中所有位置相互关注
- 作为稳定信号，防止在极长序列上的注意力退化
- 与 BERT 中的 [CLS] token 类似，但在训练期间动态学习
- 防止"中间丢失"问题，即中间序列物品获得的注意力不足

#### 2. 带 InnerTransformers 的 Token 合并模块

为了解决长序列上自注意力的**二次复杂度**：

- **Token 合并**：将相似 token 分组以减少有效序列长度
- **InnerTransformers**：轻量级 transformer 模块，处理合并后的 token 组
- **混合注意力策略**：在关键 token 上使用完整自注意力，在合并组上使用近似注意力
- 实现近线性扩展，同时保持表示能力

该方法可理解为：
```
Full sequence → Token merge → Grouped tokens → InnerTransformer → Hybrid attention → Output
```

### 工程优化

LONGER 包含全面的系统级优化，确保模型在理论合理的同时具备**生产就绪**能力：

| 优化 | 目的 |
|------|------|
| 混合精度训练 | 以最小精度损失实现更快训练与更低显存占用 |
| 激活重计算 | 避免存储中间激活矩阵，将显存复杂度从 $O(N^2)$ 降至 $O(N)$ |
| KV 缓存服务 | 通过缓存历史注意力状态加速在线推理，避免重复计算 |
| 完全同步训练/服务 | 统一的 GPU 稠密和稀疏参数更新，消除训练-推理偏差 |

### 底层依赖与相关技术

LONGER 的高效长序列建模能力深度依赖于现代 GPU 注意力算子的底层范式演进，其中 **FlashAttention** 构成了其核心算力底座。工业级推荐模型在该 IO 优化范式之上，进一步引入了面向生产环境的系统级扩展：

- **IO 感知分块范式**：FlashAttention 首次将 GPU 内存层级间的 IO 开销作为核心设计原则，通过分块（Tiling）流式计算策略，将输入序列划分为子块并逐块加载至片上 SRAM 进行局部 QK 与 PV 计算，仅将最终结果写回 HBM。该设计在保持数学精确性的前提下，彻底消除了传统实现中将完整 $N \times N$ 注意力矩阵写入高带宽内存的显存墙瓶颈 `[来源：[2205_paper_22051413_FlashAttention_Fast_and_Memory-Efficient_Exact_Attention_wi.md](../sources/2205_paper_22051413_FlashAttention_Fast_and_Memory-Efficient_Exact_Attention_wi.md)]`。
- **KV Cache 服务集成**：在 FlashAttention 训练期显存优化的基础上，LONGER 在推理阶段引入动态 KV Cache 服务。通过持久化缓存历史交互的 Key-Value 状态，系统在服务新用户请求时仅需计算新增 token 的注意力，将在线推理延迟从线性/二次级压缩至常数级，完美适配推荐系统高并发、低延迟的 SLA 要求。
- **动态稀疏掩码与 Token 合并协同**：FlashAttention 原生支持块稀疏注意力扩展，而 LONGER 将其思想进一步适配至推荐场景的**动态稀疏掩码**机制。结合 Token 合并模块，系统能够根据用户行为序列的语义密度与时间衰减特性，动态生成稀疏计算掩码，跳过无效或低信息量交互块的 IO 与 FLOPs，实现“计算资源向高价值行为倾斜”的硬件协同设计。
- **硬件协同与算子调优**：LONGER 的 GPU 优化管线根据目标硬件的 SRAM 容量与带宽特性，动态计算最优分块尺寸（Block Size），并与混合精度训练、激活重计算策略深度耦合。这种软硬件协同设计使得 LONGER 能够在单卡上稳定支撑 16K~64K 长度的用户序列建模，为工业推荐系统的长上下文扩展提供了可复用的工程范式。

### 部署与结果

LONGER 已在字节跳动的**广告和电商服务**中部署：

- **10+ 重要场景**，涵盖 diverse 推荐任务
- 每日服务**数十亿用户**
- 在离线指标和在线 A/B 测试中**持续超越强基线**
- **验证工业级扩展定律**：更长序列和更大模型产生可预测、单调的 CTR、CVR 和停留时间提升

### 与扩展定律的关联

LONGER 为推荐系统中的扩展定律提供了经验证据：
- 增加序列长度 → 更好的偏好捕捉 → 提升指标
- 增加模型容量 → 更好的模式学习 → 提升指标
- 这种关系是**可预测且单调的**，类似于 LLM 扩展定律

这验证了在工业推荐中投入更大、更长序列模型的投资。同时，底层 IO 感知注意力与 KV 缓存技术的成熟，使得扩展定律在推荐场景中的“算力-收益”曲线更加平滑，降低了长序列模型规模化落地的边际成本。

### 后续演进与相关模型

作为 LONGER 在工业长序列建模领域的自然演进，**HyFormer (2026)** 进一步打破了传统推荐系统中“序列建模”与“特征交互”解耦的范式。LONGER 专注于高效压缩与表征超长用户行为序列，而工业界另一主流方向（如 [RankMixer](../models/rankmixer.md)）则侧重于异构非序列特征的高阶交互。HyFormer 将两者的核心能力统一至单一 Transformer 骨干网络中，通过**交替优化机制**实现端到端的联合建模，并在对齐算力下实现性能超越 `[来源：[2601_paper_26011268_HyFormer_Revisiting_the_Roles_of_Sequence_Modeling_and_Feat.md](../sources/2601_paper_26011268_HyFormer_Revisiting_the_Roles_of_Sequence_Modeling_and_Feat.md)]`。

- **架构统一**：摒弃“先序列压缩（如 LONGER）后特征融合（如 RankMixer）”的两阶段流水线，将长行为序列与稠密非序列特征置于同一高维空间进行联合表征。
- **交替优化范式**：引入 **Query Decoding**（将非序列特征动态扩展为全局 Token，利用序列逐层 KV 进行交叉注意力解码）与 **Query Boosting**（轻量级 Token 混合模块增强跨特征交互），在 Transformer 各层严格交替执行，形成“解码-增强-精炼”闭环。
- **算力对齐下的性能超越**：在参数量与 FLOPs 预算严格对齐的设定下，HyFormer 在十亿级工业数据集上持续优于 LONGER 与 RankMixer 等强基线，并展现出更陡峭的 Scaling 曲线。大规模线上 A/B 测试证实其在低延迟约束下带来显著的 CTR/GAUC 提升。
- **对 LONGER 的启示**：HyFormer 验证了 LONGER 所奠定的长序列建模与 IO 感知算力底座具备向统一表征架构平滑迁移的潜力。其全局 Token 扩展与逐层 KV 解码思想，直接继承并拓展了 LONGER 的全局 Token 机制与 KV Cache 服务，为 LLM4Rec 时代的“推荐专用基础模型”提供了轻量化、高效化的工程路径。

## 关联

- [推荐中的扩展定律](../concepts/scaling_laws_recsys.md) — LONGER 提供经验验证
- [FlashAttention](../methods/flash_attention.md) — LONGER 底层 IO 感知注意力与显存优化基石
- [稀疏注意力](../methods/sparse_attention_seq_rec.md) — 相关效率技术，与动态稀疏掩码协同
- [长上下文效率](../methods/long_context_efficiency.md) — LONGER 的优化方法
- [字节跳动](../entities/bytedance.md) — 部署组织
- [HyFormer](../models/hyformer.md) — 后续演进：统一长序列建模与特征交互的混合 Transformer
- [RankMixer](../models/rankmixer.md) — 相关模型：专注于异构特征交互的工业级排序架构

## 开放问题

1. 在收益递减之前的最大有效序列长度是多少？受限于 SRAM 容量与 KV Cache 内存带宽，是否存在硬件感知的理论上限？
2. Token 合并质量在不同推荐领域（视频、电商、新闻）之间如何变化？动态稀疏掩码的自适应阈值是否需要领域特定调优？
3. LONGER 在生产规模下的确切延迟概况是什么？KV Cache 命中率与冷启动序列的推理开销如何平衡？
4. 全局 token 机制能否扩展到跨用户协同建模？结合 IO 感知分块，能否实现多用户序列的联合注意力计算？
5. **解耦 vs 统一架构的边界**：在极端高并发与严格延迟约束下，LONGER 的“序列压缩+独立排序”范式与 HyFormer 的“统一交替优化”范式，其算力-收益拐点如何随业务场景（如搜索 vs 信息流）动态变化？

## 参考文献

- Chai, Z., Ren, Q., Xiao, X., Yang, H., Han, B., Zhang, S., Chen, D., Lu, H., Zhao, W., Yu, L., Xie, X., Ren, S., Sun, X., Tan, Y., Xu, P., Zheng, Y., & Wu, D. (2025). LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders. RecSys 2025. arXiv:2505.04421.
- arXiv: https://arxiv.org/abs/2505.04421
- Huang, Y., Hong, S., Xiao, X., Jin, J., Luo, X., Wang, Z., Chai, Z., Wu, S., Zheng, Y., & Lin, J. (2026). HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction in CTR Prediction. arXiv:2601.12681.
- arXiv: https://arxiv.org/abs/2601.12681
- Dao, T., Fu, D. Y., Ermon, S., Rudra, A., & Ré, C. (2022). FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness. *NeurIPS 2022*. arXiv:2205.14135.
- arXiv: https://arxiv.org/abs/2205.14135

---

## 更新完成：2601_paper_26011268_HyFormer_Revisiting_the_Roles_of_Sequence_Modeling_and_Feat.md
**更新时间**: 2026-04-17 06:40
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2601_paper_26011268_HyFormer_Revisiting_the_Roles_of_Sequence_Modeling_and_Feat.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
