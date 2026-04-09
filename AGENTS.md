# LLM4Rec Wiki — Agent Schema & Conventions

本文档定义了 LLM agent 应如何维护此知识库。它是**模式层（schema layer）**，使 wiki 成为一个纪律严明、不断积累的知识产物，而非零散笔记的集合。

## Domain Scope

本 wiki 专注于**大语言模型用于推荐系统（LLM4Rec）**。核心主题包括：

- 传统推荐范式（协同过滤、基于内容、序列推荐）
- 与推荐系统相关的 LLM 能力（推理、生成、理解、个性化）
- 集成模式（LLM-as-ranker、LLM-as-generator、LLM-as-reasoner）
- 关键架构与训练策略
- 评估方法与基准测试
- 工业界应用与案例研究
- 开放问题与研究前沿

## Directory Structure

```
LLM4REC_wiki/
├── AGENTS.md              # This file — schema and conventions
├── raw/
│   ├── sources/           # Immutable source documents (papers, articles, notes)
│   └── assets/            # Local images, diagrams, figures
├── wiki/
│   ├── index.md           # Content catalog — all pages listed with summaries
│   ├── log.md             # Append-only chronological operation log
│   ├── entities/          # People, organizations, datasets, platforms
│   ├── concepts/          # Core concepts, theories, frameworks
│   ├── methods/           # Specific methods, algorithms, techniques
│   ├── models/            # Specific model architectures and implementations
│   ├── synthesis/         # Cross-cutting analyses, comparisons, surveys
│   └── sources/           # Per-source summary pages
│   └── README.md          # Wiki overview and navigation guide
├── scripts/               # Utility scripts
└── tools/                 # CLI tools (llm_wiki.py, etc.)
```

## Page Conventions

### Frontmatter

每个 wiki 页面必须包含 YAML frontmatter：

```yaml
---
title: "Page Title"
category: "concepts|methods|models|entities|synthesis|sources"
tags: [tag1, tag2, tag3]
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
sources: ["relative/path/to/source.md"]
related: ["../related/page.md"]
confidence: "high|medium|low"
status: "draft|stable|deprecated"
---
```

### Page Structure

1. **Overview** — 2-3 句话摘要
2. **Key Points** — 核心洞察的要点列表
3. **Details** — 正文内容，使用标题合理组织
4. **Connections** — 与其他 wiki 页面的关联
5. **Open Questions** — 未解决的问题、研究空白
6. **References** — 对源材料的引用

### Writing Style

- 简洁、技术性、精确
- 使用要点列表提升可读性
- 大量使用相对链接进行交叉引用
- 明确标注来源之间的矛盾
- 对声明标注可信度等级

## Workflows

### 1. Ingest（添加新源）

```
Input: New source file in raw/sources/
Steps:
  1. Read and analyze the source document
  2. Create/update summary in wiki/sources/
  3. Update relevant entity pages (wiki/entities/)
  4. Update relevant concept pages (wiki/concepts/)
  5. Update relevant method pages (wiki/methods/)
  6. Create new pages if new entities/concepts/methods are introduced
  7. Update wiki/index.md with new entries
  8. Append entry to wiki/log.md
  9. Report: pages created, pages updated, contradictions found
```

### 2. Query（回答问题）

```
Input: User question
Steps:
  1. Read wiki/index.md to find relevant pages
  2. Read and synthesize relevant wiki pages
  3. Generate answer with citations to specific wiki pages
  4. If the synthesis is substantial, save as new wiki page in wiki/synthesis/
  5. Log the query in wiki/log.md
```

### 3. Lint（健康检查）

```
Trigger: Periodic or on request
Steps:
  1. Scan for contradictions between pages
  2. Identify stale claims superseded by newer sources
  3. Find orphan pages with no inbound links
  4. Detect missing cross-references
  5. Identify concepts mentioned but lacking dedicated pages
  6. Report findings and suggest fixes
```

## Index & Log Format

### index.md

按类别组织。每个条目包含：
- 链接（相对路径）
- 一句话摘要
- 关键标签
- 最后更新日期

### log.md

仅追加模式。每个条目以统一前缀开头：
```
## [YYYY-MM-DD] operation_type | Brief description
- Details...
- Pages affected: ...
```

操作类型：`ingest`、`query`、`lint`、`init`、`update`

## Tooling

### Primary LLM Backend

本 wiki 使用**阿里云百炼（Bailian）**模型。配置如下：

- **Model**: `qwen-max`（主）、`qwen-plus`（备用）
- **API**: DashScope SDK
- **Environment variables**:
  - `DASHSCOPE_API_KEY`: 你的百炼 API 密钥
  - `BAILIAN_MODEL`: 主模型名称（默认：qwen-max）

### CLI Tool

`tools/llm_wiki.py` 脚本提供以下功能：

- `ingest <source_file>` — 处理新源
- `query "<question>"` — 对 wiki 提出问题
- `lint` — 对 wiki 进行健康检查
- `summarize` — 生成当前 wiki 状态的摘要

## LLM Behavior Guidelines

1. **对事实保持保守** — 如不确定，标记为低可信度
2. **始终引用来源** — 每个声明都应追溯到源
3. **标注矛盾** — 当来源冲突时，同时记录两种观点
4. **保留历史** — 永不删除页面，标记为 deprecated
5. **增量更新** — 更新现有页面而非重新创建
6. **积极交叉引用** — 双向链接相关概念
7. **标注知识空白** — 指出缺失或未充分探索的内容

## Quality Standards

- 不允许无支持的声明
- 每个页面都有入站链接
- 索引保持最新
- 日志记录所有操作
- 矛盾明确标注，不隐藏
- 可信度等级准确
