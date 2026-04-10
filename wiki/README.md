# LLM4Rec Wiki

> 一个持久的、不断增长的**大语言模型用于推荐系统(LLM4Rec)**知识库，基于 [karpathy/llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 模式构建，由Qwen Code调用qwen3.6-plus实现，使用阿里百炼Code Plan.

## 这是什么？

这不是一个每次查询都从头推导知识的RAG系统。相反，它维护一个**持久化的维基**，随着每次导入的源数据和每次提出的问题而不断丰富。知识会随时间积累。

- **原始来源**（`raw/sources/`）— 不可变的输入论文、文章、笔记
- **维基**（`wiki/`）— LLM生成的、相互链接的Markdown知识库
- **模式定义**（`AGENTS.md`）— 定义如何维护维基的指令

## 快速开始

```bash
# 设置百炼API密钥
export DASHSCOPE_API_KEY="your-api-key-here"

# 导入新来源（论文、文章、笔记）
python tools/llm_wiki.py ingest raw/sources/my_paper.pdf

# 提出问题
python tools/llm_wiki.py query "P5如何统一推荐任务？"

# 健康检查维基
python tools/llm_wiki.py lint
```

## 导航

| 章节 | 描述 |
|---------|-------------|
| [📇 索引](README.md) | 所有维基页面的完整目录 |
| [📝 日志](log.md) | 操作历史 |
| [💡 概念](concepts) | 核心理论和框架 |
| [🔧 方法](methods) | 算法和技术 |
| [🤖 模型](models) | 特定模型架构 |
| [👥 实体](entities) | 人物、数据集、平台 |
| [🔬 综合分析](synthesis) | 跨领域分析 |

## LLM后端

- **平台**：阿里云百炼（阿里云百炼）
- **主模型**：`qwen-max`
- **备选模型**：`qwen-plus`
- **SDK**：DashScope Python SDK

## 设计理念

> "维基是一个持久的、不断积累的产物。交叉引用已经存在。矛盾之处已经被标记。综合思考已经反映了你阅读的所有内容。" — Karpathy

本维基将这一理念应用于推荐系统中的大语言模型领域。
