---
title: "LLM-as-Generator"
category: "方法"
tags: [生成, 解释, 推荐文本, 创意]
created: "2026-04-08"
updated: "2026-04-08"
sources: []
related:
  - "../concepts/llm4rec_overview.md"
  - "../concepts/prompt_engineering_rec.md"
  - "../methods/llm_as_reasoner.md"
confidence: "高"
status: "稳定"
---

# LLM-as-Generator — 为推荐生成文本

## 摘要

LLM-as-Generator 范式利用大语言模型在推荐流程中**生成文本内容**。这包括**推荐解释**、**项目描述**、**面向用户的摘要**、**评论**，甚至**合成训练数据**。生成能力为传统推荐系统增加了一个维度：不仅*选择*内容，还能*创造*内容。

## 要点

- 主要用途：**可解释推荐**——"为什么我看到这个？"
- 可以生成**合成评论**、**项目描述**和**用户画像**用于数据增强
- 通过对话生成实现**对话式推荐**
- 质量取决于 LLM 对实际项目属性的**锚定**（存在幻觉风险）
- 评估具有挑战性——解释质量是主观的

## 详情

### 推荐系统中的生成任务

| 任务 | 描述 | 示例 |
|------|-------------|---------|
| **解释生成** | 证明为何推荐该项目 | "我们推荐《盗梦空间》，因为您喜欢《星际穿越》和《黑客帝国》这类烧脑科幻片" |
| **项目描述** | 根据属性生成项目摘要 | "一部由克里斯托弗·诺兰执导的 2 小时科幻惊悚片" |
| **评论综合** | 将多条评论整合为一条 | "评论者称赞摄影效果，但指出节奏较慢" |
| **用户画像生成** | 用自然语言描述用户偏好 | "该用户偏好叙事复杂的深度科幻片" |
| **合成数据生成** | 为其他模型创建训练数据 | 生成用户-项目交互描述 |
| **对话式回复** | 基于对话的推荐 | "根据您的描述，我认为您会喜欢……" |

### 解释生成

研究最多的生成任务。主要方法包括：

**基于模板（传统）：**
```
"您可能喜欢{项目}，因为您曾喜欢{相似项目}。"
```
- 僵化，表达能力有限

**基于 LLM：**
```
给定：
- 用户历史：[《盗梦空间》, 《星际穿越》, 《黑客帝国》]
- 推荐项目：《信条》
- 项目属性：科幻, 诺兰, 时间操控

生成一个令人信服的解释，说明为何推荐《信条》。
```
- 丰富、个性化、具有上下文感知能力
- 风险：可能捏造关联（幻觉）

### 生成文本的质量维度

1. **忠实性**：解释是否反映了真实的项目-用户关系？
2. **具体性**：是否针对该用户和该项目量身定制，还是泛泛而谈？
3. **连贯性**：是否文笔流畅、逻辑清晰？
4. **说服力**：能否促使用户尝试该项目？
5. **简洁性**：长度是否适当，详略是否得当？

### 通过生成进行数据增强

LLM 可以生成合成数据来训练更小的模型：

```
为电影《盗梦空间》生成 50 条合成用户评论。
变化情感倾向（30 条正面、15 条中性、5 条负面）。
包含对剧情、表演、视觉效果和节奏的具体评价。
```

这些合成数据可用于训练：
- 情感分类器
- 评论摘要模型
- 偏好推断模型

### 挑战

- **幻觉**：生成的解释可能引用不存在的项目属性
- **验证**：难以自动检查解释的忠实性
- **偏见**：LLM 生成的解释可能反映社会偏见
- **一致性**：同一用户-项目对在不同运行中可能获得不同解释
- **成本**：为百万级推荐生成解释成本高昂

## 关联

- [LLM-as-Reasoner](../methods/llm_as_reasoner.md) 提供推理来支撑生成
- [提示工程](../concepts/prompt_engineering_rec.md) 对生成质量至关重要
- [InstructRec](../models/InstructRec.md) 使用指令微调进行生成任务

## 开放问题

1. 如何可靠地检测幻觉解释？
2. 生成的解释能否切实提升用户参与度？
3. 解释的合适详细程度是什么？

## 参考文献

- Zhang, Y., et al. (2023). InstructRec: Instruction tuning for large language models in recommendation.
- Gao, C., et al. (2023). Generative recommendation with large language models.
- Rajagopal, A., et al. (2023). Explainable recommendation via large language models.


## 更新于 2026-04-08

**来源**: paper_8edbf8_HiGR_Efficient_Generative_Slate_Recommendation_via_Hierarch.md
：添加 HiGR 的层次化生成方法（列表级规划 + 物品级解码），补充多目标偏好对齐机制


## 更新于 2026-04-08

**来源**: paper_81ec38_PLUM_Adapting_Pre-trained_Language_Models_for_Industrial-sc.md
：更新生成式检索部分，添加 PLUM 的语义 ID 生成方法和工业规模部署经验


## 更新于 2026-04-08

**来源**: paper_4ddaf2_Recommender_Systems_with_Generative_Retrieval.md
：需要添加"生成式检索"作为 LLMasGenerator 的重要子类别。当前方法页面可能侧重于推荐文本生成，而此论文展示了物品 ID 生成。


## 更新于 2026-04-08

**来源**: paper_260110_Actions_Speak_Louder_than_Words_Trillion-Parameter_Sequenti.md
：添加 HSTU 方法作为 LLMasGenerator 的工业级实现案例，补充性能数据


## 更新于 2026-04-08

**来源**: 2510_paper_25101163_OneRec-Think_In-Text_Reasoning_for_Generative_Recommendatio.md
：新增“推理脚手架激活”与“多偏好对齐奖励函数”技术细节，更新生成式推荐的训练策略分类。


## 更新于 2026-04-09

**来源**: 2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md
：添加 LazyAR 解码器作为生成效率优化技术，补充动态束搜索服务策略


## 更新于 2026-04-09

**来源**: 2502_paper_25021896_OneRec_Unifying_Retrieve_and_Rank_with_Generative_Recommend.md
：添加会话级生成方法（sessionwise generation）作为新的生成范式
