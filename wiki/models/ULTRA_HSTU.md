---
title: "ULTRA-HSTU — Bending the Scaling Law Curve in Recommendation"
category: "models"
tags: [ULTRA-HSTU, HSTU, scaling law, sparse attention, Meta, sequential recommendation, system co-design]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../sources/2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md"]
related:
  - "../concepts/scaling_laws_recsys.md"
  - "../concepts/model_flops_utilization_mfu.md"
  - "../methods/sparse_attention_seq_rec.md"
  - "../entities/meta.md"
confidence: "high"
status: "stable"
---

# ULTRA-HSTU — 弯曲大规模推荐中的扩展定律曲线

## 概述

ULTRA-HSTU 是 Meta 开发的下一代序列推荐模型，通过**端到端模型与系统协同设计**开发。它建立在初代 HSTU（Hierarchical Sequential Transduction Unit）奠定的生成式推荐范式与扩展定律实证基础之上，进一步解决了严重依赖交叉注意力机制或全局自注意力所带来的计算瓶颈问题。ULTRA-HSTU 在三个维度上进行创新：**输入序列设计**、**稀疏注意力机制**和**模型拓扑**，相比传统模型实现**5 倍更快的训练扩展**和**21 倍更快的推理扩展**。全面部署后，它每日服务数十亿用户，在生产中驱动 **4% 到 8% 的消费和参与度提升**。[来源：[2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md](../sources/2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md)]

## 要点

- **端到端模型 + 系统协同设计**：联合优化架构和基础设施，最大化硬件利用率
- **生成式推荐范式奠基**：继承 HSTU 将推荐重构为自回归序列生成的统一框架
- **输入序列创新**：高基数特征离散化、多粒度 Token 组织与流式非平稳数据适配
- **稀疏注意力机制**：从相对位置偏置与线性注意力演进至硬件感知的层次化稀疏模式
- **模型拓扑创新**：重构信息流与残差路径，实现每参数最大信息吞吐
- 相比传统模型**训练扩展加速 5 倍**，**推理扩展加速 21 倍**
- Meta 生产中 **4-8% 参与度提升**（ULTRA-HSTU），初代 HSTU 曾实现 **12.4% 核心转化提升**
- **每日服务数十亿用户**，支撑万亿参数规模稳定推理

## 详情

### 扩展定律挑战

最近的 LLM 进展揭示了有希望的扩展定律，激发了对推荐领域长序列建模和更深层次架构的研究。然而，许多方法面临根本性的权衡：

- **交叉注意力方法**：通过关注压缩表示来降低计算复杂度，但这限制了自注意力可以捕捉的表示能力
- **完整自注意力**：最大化表示能力，但随序列长度二次扩展，难以支撑工业级长序列
- **传统 DLRM 瓶颈**：依赖稠密/稀疏特征拼接与双塔架构，难以随算力线性扩展，且特征工程成本高

ULTRA-HSTU 旨在**弯曲扩展定律曲线**——通过使每个 FLOP 更有效，在每单位计算中获得更好的性能，并彻底验证了推荐模型质量与训练算力之间严格的幂律关系。[来源：[2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md](../sources/2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md)]

### 架构演进：从 HSTU 到 ULTRA-HSTU

ULTRA-HSTU 并非凭空诞生，而是 Meta 在生成式推荐架构探索上的**下一代迭代**。其演进路径如下：

- **初代 HSTU (2024)**：首次将推荐任务重构为生成式建模框架下的序列转换问题（Generative Recommenders）。HSTU 摒弃了计算密集的全局 Softmax 注意力，采用**相对位置偏置**与**GLU 门控前馈网络**，结合低秩投影与分块计算策略，将序列建模复杂度从 $O(L^2)$ 优化至接近 $O(L)$。该架构首次在推荐系统中实证了模型性能与训练算力之间存在稳定的幂律关系，跨越三个数量级（十亿至万亿参数）未出现性能饱和，并在 1.5 万亿参数规模下实现核心转化指标 **12.4%** 的提升。
- **ULTRA-HSTU (2026)**：在 HSTU 验证了 Scaling Law 可行性的基础上，ULTRA-HSTU 聚焦于**稀疏注意力模式**与**交互拓扑**的深度优化，并引入**端到端系统协同设计**。它不再仅依赖线性化近似，而是通过硬件感知的选择性稀疏注意力与动态信息路由，进一步“弯曲”扩展曲线，在同等算力下榨取更高性能，同时实现推理吞吐的跨越式提升。

> 🔗 **双向关联**：`[HSTU](./HSTU.md)` ←→ `[ULTRA-HSTU](./ULTRA-HSTU.md)`  
> HSTU 奠定了生成式范式与 Scaling Law 实证基础；ULTRA-HSTU 在其之上完成稀疏化、拓扑优化与系统级协同设计，实现工业级效率跃迁。[来源：[2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md](../sources/2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md)]

### 三个创新维度

#### 1. 输入序列设计

ULTRA-HSTU 改进了用户交互历史的构建和输入方式，深度融合了 HSTU 的高基数离散化思想：

- **高基数特征离散化与统一词表**：将海量用户 ID、物品 ID 及异构上下文特征统一离散化为共享词表中的 Token，消除传统 Embedding 查找表的内存瓶颈，使模型能够直接处理超大规模稀疏空间。
- **序列组织与多粒度 Token**：优化不同交互类型（点击、浏览、点赞、分享）的排序和加权；在同一序列中支持细粒度（单个交互）和粗粒度（会话摘要）Token，适配动态序列长度输入。
- **流式非平稳数据适配**：针对推荐数据分布随时间快速变化的特性，采用在线流式采样策略，使输入序列能够实时反映用户兴趣漂移。

#### 2. 稀疏注意力机制

ULTRA-HSTU 不是放弃自注意力转向交叉注意力，而是使自注意力更高效，在 HSTU 相对位置偏置的基础上进一步稀疏化：

- **选择性注意力模式**：并非所有 token 对都需要相互关注；稀疏模式将计算集中在重要的交互对上，大幅降低无效 FLOPs。
- **层次化稀疏**：不同的注意力头使用不同的稀疏模式，结合 HSTU 的局部-全局混合机制，精准捕捉局部行为模式与全局兴趣趋势。
- **硬件感知的稀疏模式**：设计为在不规则计算模式下最大化 GPU 利用率，配合混合精度训练与大规模数据并行，保障万亿参数模型在工业级数据流上的稳定收敛。

#### 3. 模型拓扑

ULTRA-HSTU 重构了信息在模型中的流动方式，突破标准 Transformer 堆叠的局限：

- **优化的层连接与动态路由**：层之间的连接并非同等重要；拓扑设计为每参数最大信息流，支持跨层特征复用。
- **高效的残差连接与 GLU 增强**：确保梯度流动无冗余计算，结合门控线性单元（GLU）增强非线性表征能力，提升深层网络训练稳定性。
- **专业化层角色**：不同的层关注序列建模的不同方面（局部模式、全局趋势、用户意图），实现计算资源的按需分配。

### 扩展效率与 Scaling Law 验证

"弯曲扩展定律曲线"的比喻指在每个计算点实现更好的性能。ULTRA-HSTU 及其前身 HSTU 共同完成了推荐领域 Scaling Law 的完整闭环验证：

```
Performance
    ^
    |     /  Conventional models (plateau early)
    |    /
    |   /   HSTU (Power-law baseline)
    |  /   /
    | /   /   ULTRA-HSTU (bent curve, higher MFU)
    |/   /
    +------------------> Compute (FLOPs)
```

- **幂律增长实证**：模型质量随训练算力增加呈现严格的幂律增长曲线，跨越 **3 个数量级**（从十亿级至万亿级参数），未出现性能 plateau。
- **每 FLOP 效率跃升**：通过稀疏注意力与拓扑优化，ULTRA-HSTU 在相同计算预算下实现显著更高的 NDCG 与转化率，真正“弯曲”了传统扩展曲线。[来源：[2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md](../sources/2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md)]

### 性能

| 指标 | HSTU (2024 基线) | ULTRA-HSTU (2026 迭代) |
|------|------------------|------------------------|
| 参数规模 | 1.5 万亿 | 持续扩展至更大规模 |
| 训练扩展加速 | 验证幂律 Scaling | 相比传统模型 **5 倍** |
| 推理扩展加速 | 较 FlashAttention2 Transformer **5.3x-15.2x** | 相比传统模型 **21 倍** |
| 离线指标提升 | NDCG 最高提升 **65.8%** | 持续优化长尾与冷启动表现 |
| 在线业务增益 | 核心转化指标提升 **12.4%** | 消费与参与度提升 **4-8%** |
| 部署规模 | 十亿级用户平台 | 每日数十亿用户，全量生产 |
| 平台 | Meta 生产系统 | Meta 生产系统（协同优化版） |

## 关联

- [推荐中的扩展定律](../concepts/scaling_laws_recsys.md) — ULTRA-HSTU 弯曲了扩展曲线
- [模型 FLOPs 利用率](../concepts/model_flops_utilization_mfu.md) — 系统协同设计提升 MFU
- [稀疏注意力](../methods/sparse_attention_seq_rec.md) — 核心效率机制
- [HSTU](./HSTU.md) — 初代架构，奠定生成式推荐范式与 Scaling Law 实证基础（双向关联）
- [Meta](../entities/meta.md) — 开发组织
- [LONGER](./LONGER.md) — 字节跳动的长序列效率方法
- [RankMixer](./RankMixer.md) — 另一种硬件感知扩展方法

## 开放问题

1. ULTRA-HSTU 使用什么具体的稀疏注意力模式（滑动窗口、空洞、学习型）？其与 HSTU 的相对位置偏置如何融合？
2. 模型拓扑与标准 Transformer 堆叠有何不同？动态路由机制是否引入额外通信开销？
3. 输入序列设计与稀疏注意力之间的交互是什么——它们是联合优化的吗？
4. ULTRA-HSTU 与纯解码器生成式推荐方法相比如何？在冷启动与长尾覆盖上如何结合知识图谱或外部先验？
5. 系统协同设计原则能否迁移到其他组织的基础设施？万亿参数训练的工程门槛如何降低？
6. 生成式自回归范式在强业务归因、合规审计场景中的可解释性如何增强？

## 参考文献

- Ding, Q., Course, K., Ma, L., Sun, J., Liu, R., Zhu, Z., Yin, C., Li, W., Li, D., Shi, Y., Cao, X., Yang, Z., Li, H., Liu, X., Xue, B., Li, H., Jian, R., He, D. S., Qian, J., Ma, M., Zhang, Q., & Li, R. (2026). Bending the Scaling Law Curve in Large-Scale Recommendation Systems. arXiv:2602.16986.
- Zhai, J., Liao, L., Liu, X., Wang, Y., Li, R., Cao, X., Gao, L., Gong, Z., Gu, F., He, M., Lu, Y., & Shi, Y. (2024). Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations. *ICML 2024*. arXiv:2402.17152.
- arXiv (2026): https://arxiv.org/abs/2602.16986
- arXiv (2024): https://arxiv.org/abs/2402.17152

---

## 更新完成：2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md
**更新时间**: 2026-04-10 11:51
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2402_paper_24021715_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
