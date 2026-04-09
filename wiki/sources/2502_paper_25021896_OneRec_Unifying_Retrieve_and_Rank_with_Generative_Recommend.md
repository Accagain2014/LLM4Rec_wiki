---
title: "OneRec: Unifying Retrieve and Rank with Generative Recommender"
category: "sources"
tags: ["source", "2026-04-09", "generative-retrieval", "unified-model", "kuaishou", "preference-alignment"]
created: "2026-04-09"
updated: "2026-04-09"
sources: []
related:
  - "../models/OneRec.md"
  - "../entities/kuaishou.md"
  - "../entities/guorui_zhou.md"
  - "../methods/iterative_preference_alignment.md"
  - "../concepts/session_wise_generation.md"
confidence: "high"
status: "stable"
---

# OneRec：用生成式推荐器统一检索与排序

## 元数据

| 字段 | 值 |
|------|------|
| **arXiv ID** | 2502.18965 |
| **提交日期** | 2025-02-26 |
| **领域** | 信息检索（cs.IR） |
| **作者** | Jiaxin Deng、Shiyao Wang、Kuo Cai、Lejian Ren、Qigen Hu、Weifeng Ding、Qiang Luo、Guorui Zhou |
| **机构** | 快手 |
| **部署状态** | 已部署于快手主场景 |

## 核心贡献

1. **统一生成框架**：首个端到端生成式模型，取代传统的检索-排序级联流水线，显著超越当前复杂设计的推荐系统
2. **编码器-解码器架构**：编码用户行为历史并逐步解码用户可能感兴趣的视频，使用稀疏 MoE 扩展模型容量
3. **会话级生成**：提出会话级生成方法而非逐点预测，使生成更优雅且上下文连贯
4. **迭代偏好对齐**：结合 DPO 的偏好对齐模块，具有为推荐场景定制的采样策略
5. **工业验证**：部署于快手主场景，观看时长提升 +1.6%

## 方法概述

### 架构设计

```
User behavior history → Encoder → Hidden states → Decoder → Generated video sequence
                                ↓
                          Sparse MoE expansion
```

- **编码器**：处理用户行为历史序列
- **解码器**：逐步生成用户可能感兴趣的物品
- **稀疏 MoE**：在不显著增加计算 FLOPs 的情况下扩展模型容量

### 会话级生成

| 特征 | 传统逐点 | OneRec 会话级 |
|------|---------|--------------|
| 生成单元 | 单个物品 | 整个会话/列表 |
| 上下文连贯性 | 依赖手工规则组合 | 自然上下文连贯 |
| 优雅度 | 较低 | 较高 |

### 迭代偏好对齐模块

**挑战**：推荐系统每次用户请求只能展示一个结果，无法同时获取正负样本（与 NLP 中的 DPO 不同）

**解决方案**：
- 设计奖励模型模拟用户生成
- 定制化采样策略获取有效的偏好信号
- 实验表明有限的 DPO 样本能有效对齐用户兴趣偏好

## 关键发现

- 统一生成式模型可以显著超越复杂级联推荐系统
- 会话级生成比逐点生成更优雅且上下文连贯
- 稀疏 MoE 可以在不显著增加计算开销的情况下有效扩展模型容量
- 有限的 DPO 样本实现有效的偏好对齐
- 工业部署验证了生成式推荐的可行性

## 工业部署指标

| 指标 | 提升 |
|------|------|
| **观看时长** | +1.6% |
| **部署场景** | 快手主场景 |
| **模型状态** | 生产环境 |

## 与相关工作的关系

- **OneRec-Think**（arXiv:2510.1163）：同一团队的后续工作，添加文内推理能力
- **OneRec-V2**（arXiv:2508.2090）：同一团队的效率优化变体，采用纯解码器架构
- **传统级联流水线**：OneRec 取代了检索-排序分离范式
- **NLP 中的 DPO**：为推荐场景适配和定制

## 开放问题

- 稀疏 MoE 中专家的具体配置和数量未详细说明
- 奖励模型架构和训练细节有限
- 与其他生成式推荐模型（P5、InstructRec）的系统比较有限
- 长用户行为序列的编码效率

## 参考文献

- Deng, J., Wang, S., Cai, K., Ren, L., Hu, Q., Ding, W., Luo, Q., & Zhou, G. (2025). OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment. arXiv:2502.18965.
- arXiv: https://arxiv.org/abs/2502.18965
