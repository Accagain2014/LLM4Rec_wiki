---
title: "InstructRec"
category: "models"
tags: [InstructRec, instruction-tuning, LLM, conversational]
created: "2026-04-08"
updated: "2026-04-08"
sources: []
related:
  - "../models/P5.md"
  - "../models/TALLRec.md"
  - "../methods/prompt_finetuning.md"
  - "../methods/llm_as_generator.md"
confidence: "high"
status: "stable"
---

# InstructRec — 面向推荐的指令调优

## 摘要

InstructRec 将**指令调优**（在指令-回复对上训练 LLM）应用于推荐任务。与使用固定提示模板的 P5 不同，InstructRec 将推荐任务格式化为**自然语言指令**并微调 LLM 来遵循这些指令。这实现了更灵活的对话式推荐，并对未见过的任务具有更好的泛化能力。

## 要点

- 使用**指令-回复对**而非固定模板
- 在推荐系统指令上微调 LLM（Flan-T5、Alpaca 风格）
- 通过多轮对话支持**对话式推荐**
- 与基于模板的方法相比具有更好的**泛化能力**
- 展现出强大的**零样本**和**少样本**能力

## 详情

### 指令格式

InstructRec 将推荐数据转换为指令-回复格式：

```
Instruction: Based on the user's history, recommend a movie they would enjoy.
Input: The user has watched and enjoyed: Inception, Interstellar, The Prestige
Response: I recommend "Tenet" — it's another Christopher Nolan film with mind-bending
sci-fi elements similar to what you've enjoyed before.
```

### 数据构建

指令-回复对的来源：
1. **评分数据**："该用户会给出什么评分？" → "4 星"
2. **序列数据**："该用户接下来应该看什么？" → "物品 X"
3. **评论数据**："总结该用户的评论风格" → "详细，注重情节"
4. **解释数据**："为什么推荐这个？" → "因为他们喜欢类似的物品"
5. **合成数据**：LLM 生成的指令用于数据增强

### 训练流程

1. **指令模板设计**：为每个任务定义指令格式
2. **数据转换**：将推荐系统数据集转换为指令-回复对
3. **微调**：使用标准指令调优更新 LLM 权重
4. **评估**：在保留任务和零样本泛化上进行测试

### 相较于 P5 的主要优势

| 方面 | P5 | InstructRec |
|--------|----|-------------|
| **格式** | 固定模板 | 自然语言指令 |
| **灵活性** | 模板受限 | 开放式指令 |
| **泛化能力** | 局限于见过的模板 | 更好的零样本迁移 |
| **对话能力** | 单轮 | 多轮对话 |
| **可解释性** | 结构化输出 | 自然语言解释 |

### 能力

- **直接推荐**："推荐一部科幻电影"
- **约束推荐**："推荐一部 90 分钟以内的喜剧片"
- **负反馈**："我不喜欢那个，推荐别的"
- **比较**："约会之夜选 X 还是 Y 更好？"
- **解释**："我为什么会喜欢这部电影？"

### 局限性

- 需要指令调优数据（无法从基础 LLM 直接零样本使用）
- 指令质量对性能影响显著
- 仍可能虚构物品属性
- 实时部署计算成本较高

## 关联

- [P5](./P5.md) 是基于模板的前身
- [TALLRec](./TALLRec.md) 专注于调优效率
- [LLM 作为生成器](../methods/llm_as_generator.md) 涵盖解释生成

## 开放问题

1. 指令训练数据需要多高的多样性？
2. InstructRec 能否处理领域特定的术语？
3. 最优的指令长度是多少？

## 参考文献

- Zhang, Y., et al. (2023). InstructRec: Instruction tuning for large language models in recommendation.
- 官方仓库：https://github.com/RUCAIBox/InstructRec
