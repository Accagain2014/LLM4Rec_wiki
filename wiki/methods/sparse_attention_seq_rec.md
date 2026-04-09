---
title: "Sparse Attention for Sequential Recommendation — Efficient Long-Sequence Modeling"
category: "methods"
tags: [sparse attention, sequential recommendation, long sequence, efficiency, ULTRA-HSTU, LONGER]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../sources/2602_paper_26021698_Bending_the_Scaling_Law_Curve_in_Large-Scale_Recommendation.md"]
related:
  - "../methods/long_context_efficiency.md"
  - "../models/ULTRA_HSTU.md"
  - "../models/LONGER.md"
  - "../concepts/scaling_laws_recsys.md"
confidence: "high"
status: "stable"
---

# 面向序列推荐的稀疏注意力 — 高效长序列建模

## 概述

面向序列推荐的稀疏注意力指一类**降低自注意力二次计算复杂度**的技术，通过限制哪些 token 对可以相互关注。在序列推荐中，用户行为历史可跨越数千次交互，完整自注意力变得计算上不可行。稀疏注意力方法通过仅在精心选择的 token 对上计算注意力来解决这一问题，在保留使自注意力有效的表示能力的同时实现近线性扩展。这种方法是 ULTRA-HSTU（实现 5 倍训练和 21 倍推理扩展加速）等系统的核心，并补充了 LONGER 中 token 合并等其他效率方法。

## 要点

- **二次瓶颈**：完整自注意力随序列长度 N 按 O(N^2) 扩展
- **选择性计算**：仅为重要的 token 对计算注意力
- **保留自注意力能力**：与交叉注意力不同，保持完整的表示容量
- **硬件感知模式**：为高效 GPU 执行而设计
- **ULTRA-HSTU 验证**：训练 5 倍、推理 21 倍扩展加速
- **多种稀疏模式**：滑动窗口、空洞、学习型和层次化模式

## 详情

### 二次瓶颈

在标准自注意力中：

```
Attention(Q, K, V) = softmax(QK^T / sqrt(d)) V
```

QK^T 乘法创建 N x N 注意力矩阵，需要 O(N^2) 计算和内存。对于长度 N = 10,000 的用户行为序列：
- 完整注意力：1 亿次成对计算
- 内存：每层 10K x 10K 注意力矩阵

这在以下场景中成为瓶颈：
- **训练**：内存限制序列长度
- **推理**：生产中的延迟约束

### 稀疏注意力方法

#### 1. 固定稀疏模式

**滑动窗口注意力**：
- 每个 token 仅关注固定窗口内的 token
- 复杂度：O(N * window_size)——N 的线性
- 高效捕捉局部模式
- 错过长程依赖

**空洞注意力**：
- 以固定间隔关注 token（类似空洞卷积）
- 在多个时间尺度上捕捉模式
- 可与滑动窗口结合以实现覆盖

**跨步注意力**：
- 将序列分为段，在段内和段间关注
- 平衡局部细节与全局上下文

#### 2. 学习型稀疏模式

**ULTRA-HSTU 的方法**：
- 不同的注意力头使用不同的稀疏模式
- 模式在训练期间学习，而非固定
- 层次化：某些头关注局部模式，其他头关注全局趋势
- 硬件感知：模式设计为高效 GPU 执行

#### 3. 混合方法

**LONGER 的方法**（token 合并 + 混合注意力）：
- 合并相似 token 以减少有效序列长度
- 关键 token 上使用完整注意力，合并组上使用近似注意力
- 结合两种方法的最佳之处

### 为什么不使用交叉注意力？

许多方法使用交叉注意力来降低复杂度：
- 将序列压缩为少量摘要向量
- 关注摘要而非单个 token

然而，这**限制了表示能力**：
- 摘要丢失细粒度信息
- 自注意力可以捕捉任意成对关系；交叉注意力不能
- 压缩步骤是瓶颈

稀疏注意力在减少计算的同时保留了自注意力的完整表达能力。

### ULTRA-HSTU 中的稀疏注意力

ULTRA-HSTU 的稀疏注意力设计：

1. **选择性注意力模式**：并非所有 token 对都需要相互关注；模式将计算集中在最重要的地方
2. **层次化稀疏**：不同的头使用不同的模式
   - 局部头：用于最近行为的滑动窗口
   - 全局头：用于长程趋势的空洞模式
   - 意图头：关注关键事件（购买、长时间观看）
3. **硬件感知模式**：尽管访问模式不规则，仍设计为最大化 GPU 利用率

这实现了：
- **训练扩展加速 5 倍**：每训练 FLOP 更多序列长度
- **推理扩展加速 21 倍**：每推理 FLOP 更多序列长度
- **更优的推荐质量**：优于交叉注意力基线

### 与其他效率方法对比

| 方法 | 复杂度 | 表示能力 | GPU 效率 |
|------|-------|---------|---------|
| **完整注意力** | O(N^2) | 最大 | 好（规则的） |
| **稀疏注意力** | O(N * k) | 高（选择性） | 可变（取决于模式） |
| **Token 合并（LONGER）** | O(M^2), M << N | 高（带合并损失） | 好 |
| **交叉注意力** | O(N * m), m << N | 有限（有瓶颈） | 好 |
| **线性注意力** | O(N * d) | 中等 | 好 |

### 实际考量

1. **模式选择**：最优稀疏模式取决于推荐领域
2. **超参数调优**：窗口大小、空洞因子、模式数量需要仔细调优
3. **实现**：高效的稀疏注意力需要自定义 GPU 内核
4. **与其他优化的交互**：与 KV 缓存、混合精度训练结合良好

## 关联

- [ULTRA-HSTU](../models/ULTRA_HSTU.md) — 使用稀疏注意力作为核心效率机制
- [LONGER](../models/LONGER.md) — 互补方法（token 合并）
- [长上下文效率](./long_context_efficiency.md) — 更广泛的优化类别
- [扩展定律](../concepts/scaling_laws_recsys.md) — 稀疏注意力使能更长序列扩展

## 开放问题

1. 不同推荐领域（视频、电商、新闻）的最优稀疏模式是什么？
2. 稀疏模式能否通过神经架构搜索自动发现？
3. 稀疏注意力如何与位置编码方案交互？
4. 在推荐质量下降之前的最小稀疏度（最大剪枝）是多少？
5. 稀疏注意力模式能否根据输入序列特征动态适应？

## 参考文献

- Ding, Q., Course, K., Ma, L., et al. (2026). Bending the Scaling Law Curve in Large-Scale Recommendation Systems. arXiv:2602.16986.
- Chai, Z., et al. (2025). LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders. RecSys 2025. arXiv:2505.04421.
