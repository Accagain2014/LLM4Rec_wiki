---
title: "2502 Paper 25021896 Onerec Unifying Retrieve And Rank With Generative Recommend"
category: "sources"
tags: ["source", "2026-04-09"]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../../raw/sources/2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要

OneRec 是首个端到端生成式推荐模型，统一了检索和排序阶段，替代了传统的级联学习框架。该模型采用编码器 - 解码器结构，使用稀疏混合专家（MoE）扩展模型容量而不显著增加计算开销，并提出会话级生成方法（session-wise generation）替代传统的逐点预测，使生成结果更加优雅和上下文连贯。

核心创新包括迭代偏好对齐模块，结合直接偏好优化（DPO）技术提升生成质量。针对推荐系统每次用户请求只能展示一次结果的限制（无法同时获取正负样本），OneRec 设计了奖励模型来模拟用户生成，并定制采样策略。实验表明，有限的 DPO 样本即可有效对齐用户兴趣偏好。

该模型已部署在快手主场景，实现观看时长提升 1.6%，显著超越当前复杂设计的推荐系统。这是生成式推荐在工业级大规模应用中的重要里程碑。

### 需要更新的页面

- **wiki/models/OneRec.md**：需要完整重写，当前索引显示为"从关联章节中检测到的页面"占位符，需补充完整架构、方法和部署信息
- **wiki/entities/kuaishou.md**：添加 OneRec 部署案例，补充 1.6% 观看时长提升指标，更新技术团队背景（Guorui Zhou 等）
- **wiki/entities/guorui_zhou.md**：添加 OneRec 作为其最新贡献（2025 年），补充其在统一生成式推荐框架中的领导角色
- **wiki/concepts/generative_retrieval.md**：更新统一检索排序范式，添加 OneRec 作为端到端生成式推荐的典型案例
- **wiki/methods/llm_as_generator.md**：添加会话级生成方法（session-wise generation）作为新的生成范式

### 需要创建的新页面

- **wiki/methods/iterative_preference_alignment.md**：迭代偏好对齐方法，涵盖推荐场景下 DPO 的适配挑战和解决方案
- **wiki/concepts/session_wise_generation.md**：会话级生成概念，解释与逐点生成的区别及优势
- **wiki/methods/reward_modeling_rec.md**：推荐系统中的奖励建模，涵盖模拟用户生成和定制采样策略

### 矛盾/冲突

- **未发现直接冲突**，但需注意以下区分：
  - OneRec (2502.18965) 与 OneRec-Think (2510.1163) 是同一团队的不同版本，后者增加了文本内推理能力
  - 当前知识库中 OneRec 页面为占位符，需确认是否与 OneRec-Think 内容混淆
  - 快手部署指标需与现有 kuaishou.md 中的 OneRec-Think 指标（+0.159% 停留时长）区分，OneRec 为 +1.6% 观看时长

### 提取的关键事实

- **论文标识**：arXiv:2502.18965，提交日期 2025 年 2 月 26 日
- **核心作者**：Guorui Zhou（周国瑞）为通讯作者之一，来自快手
- **模型架构**：编码器 - 解码器结构 + 稀疏 MoE
- **生成范式**：会话级生成（session-wise generation）替代逐点预测
- **对齐方法**：迭代偏好对齐 + DPO，针对推荐场景定制采样策略
- **部署场景**：快手主场景
- **业务指标**：观看时长提升 1.6%
- **创新地位**：首个显著超越传统复杂推荐系统的端到端生成式模型
- **技术挑战**：推荐系统每次请求只能展示一次结果，无法同时获取正负样本
- **解决方案**：设计奖励模型模拟用户生成，定制采样策略

### 建议的源页面内容

```markdown
---
title: "OneRec: Unifying Retrieve and Rank with Generative Recommender"
category: "sources"
tags: ["source", "2026-04-09", "generative-retrieval", "unified-model", "kuaishou"]
created: "2026-04-09"
updated: "2026-04-09"
sources: []
related:
  - "../models/OneRec.md"
  - "../entities/kuaishou.md"
  - "../entities/guorui_zhou.md"
  - "../methods/iterative_preference_alignment.md"
confidence: "high"
status: "stable"
---

# OneRec: Unifying Retrieve and Rank with Generative Recommender

## 元数据

| 字段 | 值 |
|------|-----|
| **arXiv ID** | 2502.18965 |
| **提交日期** | 2025-02-26 |
| **领域** | Information Retrieval (cs.IR) |
| **作者** | Jiaxin Deng, Shiyao Wang, Kuo Cai, Lejian Ren, Qigen Hu, Weifeng Ding, Qiang Luo, Guorui Zhou |
| **机构** | 快手 (Kuaishou) |
| **部署状态** | 已部署于快手主场景 |

## 核心贡献

1. **统一生成式框架**：首个端到端生成式模型，替代传统的检索 - 排序级联框架，显著超越当前复杂设计的推荐系统
2. **编码器 - 解码器架构**：编码用户历史行为序列，逐步解码用户可能感兴趣的视频，采用稀疏 MoE 扩展模型容量
3. **会话级生成**：提出 session-wise generation 方法，比逐点生成更优雅且上下文连贯
4. **迭代偏好对齐**：结合 DPO 的偏好对齐模块，针对推荐场景定制采样策略
5. **工业级验证**：快手主场景部署，观看时长提升 1.6%

## 方法概述

### 架构设计

```
用户历史行为序列 → 编码器 → 隐状态 → 解码器 → 生成视频序列
                        ↓
                   稀疏 MoE 扩展
```

- **编码器**：处理用户历史行为序列
- **解码器**：逐步生成用户可能感兴趣的视频
- **稀疏 MoE**：在不显著增加计算 FLOPs 的情况下扩展模型容量

### 会话级生成 (Session-wise Generation)

| 特性 | 传统逐点生成 | OneRec 会话级生成 |
|------|-------------|------------------|
| 生成单位 | 单个物品 | 整个会话/列表 |
| 上下文连贯性 | 依赖手工规则组合 | 自然上下文连贯 |
| 优雅性 | 较低 | 较高 |

### 迭代偏好对齐模块

**挑战**：推荐系统每次用户请求只能展示一次结果，无法同时获取正负样本（与 NLP 中的 DPO 不同）

**解决方案**：
- 设计奖励模型模拟用户生成
- 定制采样策略获取有效的偏好信号
- 实验表明有限的 DPO 样本即可有效对齐用户兴趣

## 关键发现

- 统一的生成式模型可以显著超越复杂的级联推荐系统
- 会话级生成比逐点生成更优雅且上下文连贯
- 稀疏 MoE 可有效扩展模型容量而不显著增加计算开销
- 有限的 DPO 样本即可实现有效的偏好对齐
- 工业级部署验证了生成式推荐的可行性

## 工业部署指标

| 指标 | 提升 |
|------|------|
| **观看时长** | +1.6% |
| **部署场景** | 快手主场景 |
| **模型状态** | 生产环境 |

## 与相关工作的关系

- **OneRec-Think** (arXiv:2510.1163)：同一团队的后续工作，增加了文本内推理能力
- **传统级联框架**：OneRec 替代了检索 - 排序分离的传统架构
- **NLP 中的 DPO**：针对推荐场景进行了适配和定制

## 开放问题

- 稀疏 MoE 的具体配置和专家数量未详细披露
- 奖励模型的具体架构和训练细节有限
- 与其他生成式推荐模型（如 P5、InstructRec）的系统对比有限
- 长序列用户行为的编码效率问题

## 参考文献

- Deng, J., Wang, S., Cai, K., Ren, L., Hu, Q., Ding, W., Luo, Q., & Zhou, G. (2025). OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment. arXiv:2502.18965.

## 关联页面

- [OneRec 模型](../models/OneRec.md)
- [快手](../entities/kuaishou.md)
- [周国瑞](../entities/guorui_zhou.md)
- [迭代偏好对齐](../methods/iterative_preference_alignment.md)
- [会话级生成](../concepts/session_wise_generation.md)
- [生成式检索](../concepts/generative_retrieval.md)
```