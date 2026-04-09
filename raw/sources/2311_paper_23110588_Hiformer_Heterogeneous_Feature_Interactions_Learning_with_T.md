---
title: "Hiformer: Heterogeneous Feature Interactions Learning with Transformers for Recommender Systems"
url: "https://arxiv.org/abs/2311.05884"
original_url: "https://arxiv.org/pdf/2311.05884"
fetched: "2026-04-09"
---

# Hiformer: Heterogeneous Feature Interactions Learning with Transformers for Recommender Systems (Hiformer：基于 Transformer 的推荐系统异构特征交互学习)

**来源类型**：论文摘要
**作者**：Huan Gui, Ruoxi Wang, Ke Yin, Long Jin, Maciej Kula, Taibai Xu, Lichan Hong, Ed H. Chi
**年份**：2023
**会议/期刊**：arXiv
**arXiv**：2311.05884

## 摘要

本文针对网络规模推荐系统中特征交互学习的挑战，提出了一种基于 Transformer 架构的 Hiformer 模型。该模型通过异构自注意力层自动捕捉特征交互，并利用低秩近似和模型剪枝技术优化推理延迟。实验表明，Hiformer 已在 Google Play 应用排名模型中成功部署，关键参与度指标提升高达 2.66%。

## 主要贡献

1. **异构自注意力层设计**：针对标准 Transformer 无法有效捕捉推荐系统中异构特征交互的问题，提出了一种简单而有效的异构自注意力层修改方案，显著增强了模型对不同类型特征交互的感知能力。
2. **Hiformer 模型架构**：引入了 Hiformer（Heterogeneous Interaction Transformer）架构，旨在进一步提高了模型的表达能力，填补了 Transformer 架构在工业界特征交互建模中的应用空白。
3. **高效在线部署优化**：通过低秩近似和模型剪枝技术，解决了 Transformer 架构在服务延迟上的瓶颈，使其能够适用于网络规模的推荐系统在线部署，兼顾了效果与效率。

## 方法

### 架构
Hiformer 的核心架构基于 Transformer，但针对推荐系统的特性进行了定制化改造。传统的 Transformer 架构在自然语言处理和计算机视觉领域取得了巨大成功，但在工业界推荐系统的特征交互建模中 adoption 较少。Hiformer 旨在缩小这一差距，其架构设计重点在于利用注意力层自动捕捉特征交互，而非依赖人工 crafted 的特征组合，从而应对指数级的解决方案空间挑战。

### 关键技术
1. **异构特征交互处理**：模型识别出将 vanilla Transformer 应用于网络规模推荐系统的两大挑战之一是自注意力层无法捕捉异构特征交互。为此，作者修改了自注意力层，使其能够考虑到特征交互的异构性。
2. **推理加速技术**：针对第二大挑战即服务延迟过高的问题，模型采用了低秩近似（low-rank approximation）和模型剪枝（model pruning）技术。这些技术使得 Hiformer 在保持模型表达能力的同时，享受快速推理能力，满足在线部署的严格延迟要求。
3. **自动化特征学习**：方法的核心在于利用 Transformer 的注意力机制自动学习特征交互，避免了在稀疏且巨大的输入特征空间中手动构建有效特征交互的不可行性。

## 实验结果

论文进行了广泛的离线实验，结果证实了 Hiformer 模型的有效性和效率。更重要的是，该模型已成功部署到 Google Play 的真实世界大规模应用排名模型中。在线 A/B 测试结果显示，Hiformer 带来了显著的关键参与度指标提升，最高增幅达到 **+2.66%**。这一具体数字证明了该模型在处理网络规模稀疏特征空间时的优越性能，以及其在实际工业场景中的落地价值。离线实验也 corroborates 了模型在效率方面的优势，表明优化后的 Transformer 架构可以满足在线服务的延迟约束。

## 局限性

虽然论文摘要未明确列出具体的局限性，但从其解决的问题中可以推断：标准的 Transformer 架构原本存在服务延迟过高的问题，必须依赖低秩近似和剪枝才能部署，这意味着模型复杂度和计算资源消耗仍然高于传统的浅层深度学习模型。此外，针对异构特征交互的修改虽然有效，但可能增加了模型结构的复杂性，对工程实现和维护提出了更高要求。在极端稀疏的特征空间下，注意力机制的有效性可能仍受限于数据质量。

## 与 LLM4Rec 的相关性

这篇论文与 LLM 推荐系统（LLM4Rec）领域具有高度的相关性和重要的启示意义。首先，Hiformer 验证了 Transformer 架构在推荐系统特征交互建模中的有效性，这是将大语言模型（本质上也是 Transformer 架构）引入推荐系统的基础前提。其次，论文中提到的解决 Transformer 服务延迟过高问题的技术（如低秩近似、模型剪枝），正是当前 LLM4Rec 领域面临的核心挑战之一，即如何在资源受限的推荐场景中高效部署大模型。最后，该工作展示了自动化特征交互学习的能力，这与 LLM 利用语义理解能力自动生成特征交互的思路不谋而合，为未来结合 LLM 语义能力与 Hiformer 结构效率提供了可行的技术路径参考。