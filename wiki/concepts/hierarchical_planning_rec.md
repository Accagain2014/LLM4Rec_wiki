---
title: "Hierarchical Planning in Recommendation — 层次化规划"
category: "concepts"
tags: [hierarchical planning, two-stage generation, slate-level intent, HiGR, structured generation]
created: "2026-04-08"
updated: "2026-04-09"
sources: ["../sources/paper_8edbf8_HiGR_Efficient_Generative_Slate_Recommendation_via_Hierarch.md"]
related:
  - "../models/HiGR.md"
  - "../concepts/slate_recommendation.md"
  - "../concepts/generative_retrieval.md"
  - "../methods/llm_as_generator.md"
confidence: "high"
status: "stable"
---

# Hierarchical Planning in Recommendation — 层次化规划

## 摘要

Hierarchical planning（层次化规划）是一种**两阶段生成范式**，将推荐生成分解为：(1) **高层规划**——捕捉全局意图和 slate-level 约束，(2) **底层解码**——在高层规划的约束下生成具体物品。这种架构显著减少了搜索空间，实现了更高效和可控的生成式推荐。

## 要点

- **两阶段架构**：规划（意图）→ 解码（物品）
- **减少搜索空间**：高层约束大幅缩小候选范围
- **可控生成**：可以在规划层注入业务规则（多样性、公平性）
- **效率提升**：HiGR 实现 5× 推理加速
- 类比人类决策：先决定"看科幻片"，再选择具体电影

## 详情

### 动机

直接自回归生成物品序列存在以下问题：
1. **无全局规划**：每个 token 独立生成，缺乏 slate-level 意图
2. **搜索空间巨大**：|I|^K 组合（|I| 为物品数，K 为 slate 大小）
3. **无法注入约束**：难以在生成过程中控制多样性、类目分布等

层次化规划通过**解耦决策层级**来解决这些问题。

### 两阶段架构

#### Stage 1: List-Level Planning（列表级规划）
- **输入**：用户上下文、历史行为、业务目标
- **输出**：slate-level 的隐式表示（意图向量）
- **功能**：
  - 确定 slate 的主题分布（如 60% 科幻、30% 动作、10% 喜剧）
  - 设定多样性约束
  - 捕捉全局用户意图

#### Stage 2: Item-Level Decoding（物品级解码）
- **输入**：规划层的意图向量 + 已生成物品
- **输出**：单个物品的 Semantic ID
- **功能**：
  - 在规划约束下选择具体物品
  - 保证与 slate 意图的一致性
  - 逐步填充 slate

### 与 LLM Planning 的关系

LLM 在规划任务中表现出色：
- **Instruction following**：可以遵循"推荐多样化的物品"等指令
- **Reasoning**：能够推理为什么某些物品组合更优
- **Constraint satisfaction**：可以在规划阶段考虑多维度约束

### HiGR 中的层次化规划

HiGR 是该范式的代表性实现：
- 使用 **residual quantization autoencoder** 学习层次化物品表示
- 规划层输出 slate 的 **code prefix distribution**
- 解码层基于 prefix 逐步生成完整 Semantic ID
- 实现了 **controllable generation**：不同层级控制不同粒度

### 优势

| 优势 | 描述 |
|------|------|
| 效率 | 搜索空间从 |I|^K 减少到 |I| × K |
| 可控性 | 规划层可注入业务规则 |
| 质量 | 全局优化优于局部贪婪 |
| 可解释性 | 规划层输出可提供推荐解释 |

### 挑战

- 如何设计最优的规划-解码接口？
- 规划层的信息瓶颈问题
- 两阶段训练的稳定性
- 动态 slate size 下的规划适应性

## Connections

- [HiGR](../models/HiGR.md) — 层次化规划的代表性实现
- [Slate Recommendation](./slate_recommendation.md) — 主要应用场景
- [Generative Retrieval](./generative_retrieval.md) — 底层生成范式
- [LLM as Generator](../methods/llm_as_generator.md) — 生成式推荐方法

## Open Questions

1. 层次化规划是否可扩展到更多层级（如 category → subcategory → item）？
2. 如何实现规划层的可解释输出？
3. 规划-解码联合训练的最优策略是什么？
4. 该范式能否迁移到对话式/交互式推荐？

## References

- Pang, Y., et al. (2025). HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning. arXiv:2512.24787.
- Planning in LLMs: Hao, S., et al. (2023). Reasoning with language model is planning with world model. EMNLP 2023.
