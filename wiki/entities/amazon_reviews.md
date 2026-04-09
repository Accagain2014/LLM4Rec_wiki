---
title: "Amazon 评论数据集"
category: "entities"
tags: [dataset, amazon, e-commerce, reviews, benchmark]
created: "2026-04-08"
updated: "2026-04-08"
sources: []
related:
  - "./movielens.md"
  - "../concepts/evaluation_llm4rec.md"
confidence: "high"
status: "stable"
---

# Amazon 评论数据集

## 摘要

Amazon 评论数据集（Amazon Reviews Dataset）是来自 Amazon.com 的大规模产品评论集合，广泛用作推荐系统研究中的**基准数据集**。它包含用户-物品交互（评分）、评论文本、时间戳以及产品元数据，使其对**传统协同过滤**和**基于大语言模型的推荐**研究都具有价值。

## 要点

- **规模**：涵盖 36 年（1996-2023）的 2.33 亿条评论
- **丰富的元数据**：产品类别、描述、价格、图片
- **文本数据**：评论正文、标题、有用性投票
- **多个版本**：2014、2018、2023 年发布，规模逐步增长
- **常见用途**：评分预测、序列推荐、评论生成

## 详情

### 数据统计

| 版本 | 评论数 | 用户数 | 产品数 | 时间跨度 |
|---------|---------|-------|----------|-----------|
| **2014** | 1.428 亿 | 3970 万 | 2310 万 | 1996-2014 |
| **2018** | 2.047 亿 | 4160 万 | 3250 万 | 1996-2018 |
| **2023** | 2.33 亿+ | 5000 万+ | 4000 万+ | 1996-2023 |

### 数据格式

每条评论包含以下字段：
- `reviewerID`：用户标识符
- `asin`：产品标识符（Amazon Standard Identification Number）
- `overall`：评分（1-5 星）
- `reviewText`：评论正文
- `summary`：评论标题/摘要
- `unixReviewTime`：时间戳
- `reviewerName`：用户显示名称

产品元数据包括：
- `title`：产品名称
- `description`：产品描述
- `price`：爬取时的价格
- `imUrl`：产品图片 URL
- `categories`：类别层级
- `brand`：品牌名称
- `salesRank`：类别中的销售排名

### 常见子集

研究人员通常使用特定类别的子集：

| 类别 | 评论数 | 用途 |
|----------|---------|----------|
| **Beauty（美妆）** | 320 万 | 小规模实验 |
| **Sports（运动）** | 290 万 | 序列推荐 |
| **Movies & TV（影视）** | 1670 万 | 跨领域研究 |
| **Books（图书）** | 2250 万 | 文本密集型推荐 |

### 在 LLM4Rec 研究中的应用

- **P5**：在 Amazon 子集（Beauty、Sports、Toys）上进行训练和评估
- **InstructRec**：使用 Amazon 数据进行指令微调
- **TALLRec**：在 Amazon 类别上评估 LoRA 微调效果
- **评论生成**：利用评论文本训练解释性模型

### 优势

- 大规模数据支持稳健的评估
- 丰富的文本数据适用于基于 LLM 的方法
- 时间信息支持序列推荐系统
- 多类别支持跨领域研究

### 局限性

- 需要进行隐式负采样（未观测到的视为负样本）
- 流行度偏差（热门产品评论更多）
- 评论文本质量差异较大
- 没有用户的人口统计信息

## 关联

- [MovieLens](./movielens.md) 是另一个常见的基准数据集
- [评估](../concepts/evaluation_llm4rec.md) 涵盖了基准数据集的使用方法

## 参考文献

- Ni, J., Li, J., & McAuley, J. (2019). Justifying recommendations using distantly-labeled reviews and fine-grained aspects. EMNLP.
- Amazon Reviews Dataset: https://nijianmo.github.io/amazon/index.html


## 更新于 2026-04-08

**来源**: paper_ad0dff_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md
：在相关数据集中补充多模态数据集的对比（QARM 使用快手内部数据）


## 更新于 2026-04-08

**来源**: paper_ad0dff_QARM_Quantitative_Alignment_Multi-Modal_Recommendation_at_K.md
：在相关数据集中补充多模态数据集的对比说明（QARM 使用快手内部视频数据）


## 更新于 2026-04-09

**来源**: 2604_paper_26040497_Tencent_Advertising_Algorithm_Challenge_2025_All-Modality_G.md
：在对比部分添加 TencentGR 数据集作为工业广告场景的对比基准
