---
title: "MovieLens 数据集"
category: "entities"
tags: [dataset, movielens, movies, benchmark, ratings]
created: "2026-04-08"
updated: "2026-04-08"
sources: []
related:
  - "./amazon_reviews.md"
  - "../concepts/evaluation_llm4rec.md"
confidence: "high"
status: "stable"
---

# MovieLens 数据集

## 摘要

MovieLens 是推荐研究中使用最广泛的**电影评分数据集**，由明尼苏达大学 GroupLens Research 团队维护。它包含用户对电影的评分数据，以及电影元数据（类型、标签）和某些版本中的用户人口统计信息。其清晰的结构和广泛的采用使其成为比较推荐算法的**标准基准**。

## 要点

- **维护方**：明尼苏达大学 GroupLens Research 团队
- **版本**：MovieLens-100K、1M、10M、25M、最新版（2700 万+）
- **核心数据**：用户 ID、电影 ID、评分（1-5）、时间戳
- **元数据**：电影类型、标题、标签、TMDB/IMDb 链接
- **常见用途**：通用推荐基准、冷启动研究

## 详情

### 数据集版本

| 版本 | 评分数 | 用户数 | 电影数 | 年份 |
|---------|---------|-------|--------|------|
| **100K** | 100,000 | 943 | 1,682 | 1997 |
| **1M** | 1,000,209 | 6,040 | 3,952 | 2000 |
| **10M** | 10,000,054 | 69,878 | 10,681 | 2009 |
| **25M** | 25,000,095 | 162,541 | 62,423 | 2020 |
| **最新版** | 2700 万+ | 28 万+ | 5.8 万+ | 持续更新 |

### 数据格式

**评分文件：**
```
userId, movieId, rating, timestamp
1, 1, 4.0, 964982703
1, 3, 4.0, 964981247
```

**电影文件：**
```
movieId, title, genres
1, Toy Story (1995), Adventure|Animation|Children|Comedy|Fantasy
```

**标签文件（25M+）：**
```
userId, movieId, tag, timestamp
```

### 电影类型

Action, Adventure, Animation, Children, Comedy, Crime, Documentary, Drama, Fantasy, Film-Noir, Horror, IMAX, Musical, Mystery, Romance, Sci-Fi, Thriller, War, Western

### 在 LLM4Rec 研究中的应用

- **基线对比**：大多数 LLM4Rec 论文在 MovieLens 上与协同过滤基线进行对比
- **冷启动研究**：电影元数据有助于评估 LLM 的语义理解能力
- **类型分析**：电影类型提供自然的评估分层依据
- **标签理解**：LLM 可以从语义角度理解用户打出的标签

### 优势

- 数据干净、结构清晰
- 广泛采用，便于与已有研究直接对比
- 电影元数据丰富（标题、类型、年份）
- 用户人口统计信息（1M 版本：年龄、性别、职业、邮编）
- 时间数据支持序列分析

### 局限性

- 没有评论文本（与 Amazon 不同）
- 交互类型单一（仅有评分，无隐式反馈）
- 老电影占比偏高
- 用户人口统计信息仅存在于 1M 版本
- 没有社交网络信息

### 获取方式

- 下载：https://grouplens.org/datasets/movielens/
- 许可证：CC BY-SA
- 通常通过 `surprise` 或 `recbole` 库使用

## 关联

- [Amazon 评论](./amazon_reviews.md) 提供更丰富的文本数据
- [评估](../concepts/evaluation_llm4rec.md) 将 MovieLens 用作基准数据集

## 参考文献

- Harper, F. M., & Konstan, J. A. (2015). The MovieLens datasets: History and context. ACM Transactions on Interactive Intelligent Systems.
- GroupLens Research: https://grouplens.org/
