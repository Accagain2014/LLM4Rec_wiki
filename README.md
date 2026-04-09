# LLM4Rec Wiki

> 一个持久化、持续累积的知识库，专注于**推荐系统中的大语言模型**，基于 Karpathy LLM Wiki 模式构建，并由阿里云百炼（Bailian）提供驱动。

## 概述

本项目实现了一个由 LLM 维护的领域知识库，聚焦于**推荐系统中的大语言模型（LLM4Rec）**。与传统的 RAG（每次查询都重新推导知识）不同，该 wiki **逐步构建并维护**一个结构化的、相互链接的知识库，随着时间推移不断累积。

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API 密钥

```bash
# 获取你的密钥：https://bailian.console.aliyun.com/
export DASHSCOPE_API_KEY="sk-your-api-key-here"
```

### 3. 使用 CLI

```bash
# 导入新的源文档
python tools/llm_wiki.py ingest raw/sources/my_source.md

# 从 URL 抓取网页并自动分析（推荐）
python tools/llm_wiki.py fetch "https://arxiv.org/abs/2307.06435"

# 仅保存网页内容，不自动分析
python tools/llm_wiki.py fetch "https://example.com/article" --no-ingest

# 查询 wiki
python tools/llm_wiki.py query "P5 是如何统一推荐任务的？"

# 健康检查 wiki
python tools/llm_wiki.py lint

# 汇总当前 wiki 状态
python tools/llm_wiki.py summarize
```

## 项目结构

```
LLM4REC_wiki/
├── AGENTS.md              # Schema：规范与工作流
├── wiki/
│   ├── README.md          # Wiki 概览
│   ├── index.md           # 内容目录
│   ├── log.md             # 操作日志
│   ├── concepts/          # 核心理论（6 页）
│   ├── methods/           # 算法（5 页）
│   ├── models/            # 模型架构（5 页）
│   ├── entities/          # 人物、数据集、平台（3 页）
│   ├── synthesis/         # 跨主题分析（2 页）
│   └── sources/           # 每个来源的摘要
├── raw/
│   ├── sources/           # 不可变的源文档
│   └── assets/            # 本地图片、图表
├── tools/
│   └── llm_wiki.py        # 集成百炼的 CLI 工具
├── scripts/               # 实用脚本
└── requirements.txt       # Python 依赖
```

## 当前内容

该 wiki 目前包含 **21 个种子页面**，涵盖：

### Concepts（6 页）
- [LLM4Rec 概述](wiki/concepts/llm4rec_overview.md)
- [协同过滤](wiki/concepts/collaborative_filtering.md)
- [序列推荐](wiki/concepts/sequential_recommendation.md)
- [面向推荐系统的提示工程](wiki/concepts/prompt_engineering_rec.md)
- [知识增强推荐](wiki/concepts/knowledge_enhanced_rec.md)
- [LLM4Rec 中的评估](wiki/concepts/evaluation_llm4rec.md)

### Methods（5 页）
- [LLM 作为排序器](wiki/methods/llm_as_ranker.md)
- [LLM 作为生成器](wiki/methods/llm_as_generator.md)
- [LLM 作为推理器](wiki/methods/llm_as_reasoner.md)
- [基于提示的微调](wiki/methods/prompt_finetuning.md)
- [面向推荐系统的 RAG](wiki/methods/rag_for_recsys.md)

### Models（5 页）
- [P5](wiki/models/P5.md)
- [InstructRec](wiki/models/InstructRec.md)
- [TALLRec](wiki/models/TALLRec.md)
- [LLMRank](wiki/models/LLMRank.md)
- [Qwen 系列](wiki/models/qwen_series.md)

### Entities（3 页）
- [Amazon Reviews 数据集](wiki/entities/amazon_reviews.md)
- [MovieLens 数据集](wiki/entities/movielens.md)
- [阿里云百炼平台](wiki/entities/bailian_platform.md)

### Synthesis（2 页）
- [LLM4Rec 分类体系](wiki/synthesis/llm4rec_taxonomy.md)
- [传统 vs 基于 LLM 的推荐系统](wiki/synthesis/traditional_vs_llm.md)

## 设计理念

基于 [Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)：

> "Wiki 是一个持久化、持续累积的产物。交叉引用已经存在。矛盾之处已经被标记。综合内容已经反映了你阅读过的所有内容。"

### 三个层次
1. **源文档（Raw Sources）** — 不可变的输入文档
2. **Wiki** — LLM 生成的、相互链接的 Markdown 文件
3. **Schema** — 给 LLM 的指令（AGENTS.md）

### 三项操作
1. **Ingest（导入）** — 添加源文档 → LLM 更新 wiki
2. **Query（查询）** — 提出问题 → LLM 从 wiki 中综合生成答案
3. **Lint（检查）** — 健康检查 → LLM 发现矛盾、空白和孤立页面

## LLM 后端

- **平台**：阿里云百炼（Alibaba Cloud Bailian）
- **API 类型**：OpenAI 兼容 SDK（同时支持标准密钥和 Coding Plan 密钥）
- **Coding Plan 密钥**（`sk-sp-*`）：`qwen3.5-plus`（默认）、`qwen3-coder-plus`、`kimi-k2.5`、`glm-5`
- **标准密钥**（`sk-*`）：`qwen-max`（默认）、`qwen-plus`、`qwen-turbo`
- **自动检测**：CLI 会自动检测你的密钥类型并配置正确的端点

## 添加新源文档

### 方式 A：从 URL 抓取（推荐）
```bash
# 自动：抓取 → 保存 → 分析 → 更新知识库
python tools/llm_wiki.py fetch "https://arxiv.org/abs/2307.06435"

# 仅保存源文件，不自动分析
python tools/llm_wiki.py fetch "https://example.com/article" --no-ingest
```

### 方式 B：手动添加本地文件
1. 将源文件放置于 `raw/sources/`
2. 运行：`python tools/llm_wiki.py ingest raw/sources/your_file.md`
3. 审查建议的 wiki 变更
4. 确认应用变更

## 环境变量

| 变量 | 说明 | 默认值 |
|----------|-------------|---------|
| `DASHSCOPE_API_KEY` | 你的百炼 API 密钥 | （必填） |
| `BAILIAN_MODEL` | 主模型名称 | `qwen-max` |
| `WIKI_AUTO_CONFIRM` | 自动应用 wiki 变更 | `false` |

## 许可证

本知识库用于研究和教育目的。

## 致谢

- Karpathy 提出的 LLM Wiki 模式
- 阿里云百炼提供的 LLM 基础设施
- LLM4Rec 研究社区
