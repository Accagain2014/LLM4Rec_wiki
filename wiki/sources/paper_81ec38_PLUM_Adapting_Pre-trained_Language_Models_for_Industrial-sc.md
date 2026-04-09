---
title: "Paper 81Ec38 Plum Adapting Pre-Trained Language Models For Industrial-Sc"
category: "sources"
tags: ["source", "2026-04-08"]
created: "2026-04-08"
updated: "2026-04-08"
sources: ["../../raw/sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要

PLUM 是 Google/YouTube 团队提出的工业级生成式推荐框架，旨在将预训练大语言模型适配到大规模推荐任务。该框架包含三个核心组件：使用语义 ID（Semantic IDs）进行物品标记化、在领域特定数据上进行持续预训练（CPT）、以及针对推荐目标的特定任务微调。PLUM 专注于生成式检索范式，模型直接根据用户上下文生成推荐物品的语义 ID，而非传统的嵌入检索。

在 YouTube 内部大规模视频推荐数据集上的实验表明，PLUM 相比经过高度优化的生产模型（基于大型嵌入表）取得了显著提升。论文还提供了模型检索性能的扩展研究、CPT 的学习经验、语义 ID 的增强方法，以及支持该框架在 YouTube 数十亿用户中部署的训练和推理方法概述。这是 LLM4Rec 在工业界大规模应用的重要案例。

### 需要更新的页面

- **wiki/concepts/llm4rec_overview.md**：添加 PLUM 作为工业级生成式推荐的典型案例，补充生成式检索范式的工业应用信息
- **wiki/methods/llm_as_generator.md**：更新生成式检索部分，添加 PLUM 的语义 ID 生成方法和工业规模部署经验
- **wiki/entities/tencent.md**：添加 PLUM/YouTube 作为对比案例，说明不同公司的生成式推荐部署策略
- **wiki/synthesis/traditional_vs_llm.md**：添加 PLUM 与传统嵌入表方法的性能对比数据

### 需要创建的新页面

- **wiki/models/PLUM.md**：PLUM 模型架构、语义 ID 标记化、CPT 策略、YouTube 部署详情
- **wiki/concepts/semantic_id.md**：语义 ID 概念、标记化方法、在生成式推荐中的应用
- **wiki/concepts/continued_pretraining.md**：持续预训练（CPT）概念、在推荐领域的应用、与指令微调的区别
- **wiki/entities/google_youtube.md**：Google/YouTube 推荐系统团队和工业实践

### 矛盾/冲突

- **未发现直接冲突**：PLUM 的生成式检索方法与现有 HiGR、QARM 等生成式推荐模型方向一致
- **潜在差异需标注**：PLUM 使用语义 ID 而非传统物品 ID，与 P5 等基于 ID 的提示方法有所不同，需在相关页面标注此差异
- **工业规模声明**：PLUM 声称支持"数十亿用户"，这与现有知识库中工业案例的规模描述需保持一致性

### 提取的关键事实

- PLUM 由 Google/YouTube 团队开发，23 位作者
- 提交日期：2025 年 10 月 9 日
- 核心三组件：语义 ID 标记化、持续预训练（CPT）、任务特定微调
- 专注于生成式检索范式（直接生成物品语义 ID）
- 在 YouTube 内部大规模视频推荐数据集上验证
- 相比优化的生产嵌入表模型有显著提升
- 支持 YouTube 数十亿用户规模的部署
- 论文包含扩展研究、CPT 学习经验、语义 ID 增强方法
- 11 页，6 图
- arXiv:2510.07784

### 建议的源页面内容

```markdown
---
title: "PLUM: Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations"
category: "sources"
tags: ["source", "2026-04-08", "generative-retrieval", "industrial", "youtube", "semantic-id"]
created: "2026-04-08"
updated: "2026-04-08"
sources: ["../raw/sources/paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md"]
related:
  - "../models/PLUM.md"
  - "../concepts/semantic_id.md"
  - "../concepts/continued_pretraining.md"
  - "../entities/google_youtube.md"
confidence: "high"
status: "stable"
---

# PLUM: Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations

## 来源信息

- **arXiv**: 2510.07784
- **提交日期**: 2025-10-09
- **作者**: Ruining He 等 23 位（Google/YouTube 团队）
- **领域**: Information Retrieval (cs.IR), Machine Learning (cs.LG)
- **页数**: 11 页，6 图

## 核心贡献

1. **PLUM 框架**：将预训练 LLM 适配到工业级推荐任务的完整框架
2. **语义 ID 标记化**：使用 Semantic IDs 进行物品表示，支持生成式检索
3. **持续预训练（CPT）**：在领域特定数据上进行 CPT 以适配推荐场景
4. **生成式检索**：模型直接生成推荐物品的语义 ID，而非传统嵌入检索
5. **工业规模验证**：在 YouTube 内部大规模视频推荐数据集上验证
6. **部署方法**：支持数十亿用户规模的训练和推理方法

## 关键方法

### 三组件架构

```
┌─────────────────────────────────────────────────────────┐
│                      PLUM Framework                      │
├─────────────────────────────────────────────────────────┤
│  1. Item Tokenization (Semantic IDs)                    │
│  2. Continued Pre-Training (Domain-specific data)       │
│  3. Task-specific Fine-tuning (Generative retrieval)    │
└─────────────────────────────────────────────────────────┘
```

### 语义 ID 标记化

- 将物品映射到语义 ID 序列
- 支持 LLM 直接生成物品标识
- 相比传统 ID 具有语义信息

### 持续预训练（CPT）

- 在推荐领域数据上继续预训练
- 适配 LLM 到推荐任务分布
- 论文包含 CPT 学习经验总结

### 生成式检索

- 输入：用户上下文
- 输出：推荐物品的语义 ID 序列
- 端到端生成，无需独立检索器

## 实验结果

- **数据集**：YouTube 内部大规模视频推荐数据
- **基线**：高度优化的生产模型（大型嵌入表）
- **结果**：PLUM 取得显著提升
- **规模**：支持数十亿用户部署

## 附加内容

- 模型检索性能的扩展研究
- CPT 的学习经验和最佳实践
- 语义 ID 的增强方法
- 训练和推理方法概述

## 与现有研究的关联

| 相关研究 | 关系 |
|----------|------|
| [HiGR](../models/HiGR.md) | 同为生成式推荐，HiGR 侧重层次化规划 |
| [QARM](../models/QARM.md) | 同为工业级推荐，QARM 来自快手 |
| [P5](../models/P5.md) | P5 使用固定提示模板，PLUM 使用语义 ID 生成 |
| [TALLRec](../models/TALLRec.md) | TALLRec 侧重高效微调，PLUM 侧重工业部署 |

## 开放问题

1. 语义 ID 的具体编码方案是什么？
2. CPT 数据的具体规模和构成？
3. 与传统检索方法的详细对比指标？
4. 推理延迟和计算成本详情？

## 参考文献

- He, R., Heldt, L., Hong, L., et al. (2025). PLUM: Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations. arXiv:2510.07784
- 论文链接：https://arxiv.org/abs/2510.07784
- PDF: https://arxiv.org/pdf/2510.07784
```

---

**处理报告**：
- ✅ 源文档已分析
- ✅ 需要更新的页面：4 个
- ✅ 需要创建的新页面：4 个
- ✅ 矛盾检查：完成（无直接冲突）
- ✅ 关键事实提取：9 项
- ✅ 源页面内容：已生成