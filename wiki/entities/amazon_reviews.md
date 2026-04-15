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

Amazon 评论数据集（Amazon Reviews Dataset）是来自 Amazon.com 的大规模产品评论集合，广泛用作推荐系统研究中的**基准数据集**。它包含用户-物品交互（评分）、评论文本、时间戳以及产品元数据，使其对**传统协同过滤**、**生成式推荐**和**基于大语言模型的推荐**研究都具有核心价值。

## 要点

- **规模**：涵盖 36 年（1996-2023）的 2.33 亿条评论
- **丰富的元数据**：产品类别、描述、价格、图片、品牌与销售排名
- **文本数据**：评论正文、标题、有用性投票
- **多个版本**：2014、2018、2023 年发布，规模逐步增长
- **常见用途**：评分预测、序列推荐、评论生成、生成式推荐分词验证
- **跨品类泛化**：在美妆、运动、玩具等多个垂直品类上表现稳定，支持细粒度语义建模研究

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

研究人员通常使用特定类别的子集进行实验：

| 类别 | 评论数 | 用途 |
|----------|---------|----------|
| **Beauty（美妆）** | 320 万 | 小规模实验、生成式推荐分词验证 |
| **Sports（运动）** | 290 万 | 序列推荐、上下文感知建模 |
| **Movies & TV（影视）** | 1670 万 | 跨领域研究、长文本理解 |
| **Books（图书）** | 2250 万 | 文本密集型推荐、指令微调 |
| **Toys（玩具）** | ~1500 万 | 生成式推荐泛化评估、多模态/属性对齐 |

### 在 LLM4Rec 研究中的应用

- **P5**：在 Amazon 子集（Beauty、Sports、Toys）上进行训练和评估
- **InstructRec**：使用 Amazon 数据进行指令微调，构建推荐任务指令集
- **TALLRec**：在 Amazon 类别上评估 LoRA 微调效果与参数效率
- **评论生成**：利用评论文本训练解释性模型与可控文本生成器

### 近期研究应用

- **ActionPiece（ICML 2025 Spotlight）**：该工作利用 Amazon 的 Beauty、Sports 和 Toys 子集验证了**上下文感知序列分词**的有效性。传统生成式推荐模型通常对单一动作独立分配固定 Token，割裂了序列上下文；ActionPiece 将用户交互动作解构为物品元数据特征集合，通过统计特征在集合内部及相邻序列间的共现频率构建动态词表，并引入集合排列正则化消除无序特征线性化带来的偏差。实验表明，该方法在三个品类上均展现出优异的泛化表现：在 Beauty 上 Recall@10 达 18.72%（较最优基线 TIGER 提升 +2.41%），Sports 上 Recall@10 达 14.56%（+2.15%），Toys 上 Recall@10 与 NDCG@10 分别提升 +2.03% 与 +1.65%。该研究证明了 Amazon 数据集丰富的元数据与序列结构能够有效支撑 LLM4Rec 从“浅层 ID 映射”向“深度上下文语义理解”演进，为生成式推荐的前置分词模块提供了可插拔的标准化验证基准。[来源：[2502_paper_25021358_ActionPiece_Contextually_Tokenizing_Action_Sequences_for_Ge.md](../sources/2502_paper_25021358_ActionPiece_Contextually_Tokenizing_Action_Sequences_for_Ge.md)]

### 优势

- 大规模数据支持稳健的评估与统计显著性检验
- 丰富的文本与元数据适用于基于 LLM 的语义对齐与指令微调
- 精确的时间戳支持序列推荐与动态兴趣建模
- 多类别划分支持跨领域迁移、冷启动与长尾分布研究
- 公开且持续更新，便于学术界复现与横向对比

### 局限性

- 需要进行隐式负采样（未观测到的交互通常视为负样本）
- 流行度偏差显著（热门产品评论更多，长尾物品覆盖不足）
- 评论文本质量差异较大，存在噪声、刷评或无关内容
- 缺乏用户的人口统计学信息（年龄、性别、地理位置等）
- 元数据完整性依赖爬取质量，在特征稀疏场景下可能影响上下文分词或属性对齐效果

## 关联

- [MovieLens](./movielens.md) 是另一个常见的基准数据集，侧重显式评分与电影领域
- [评估](../concepts/evaluation_llm4rec.md) 涵盖了基准数据集在 LLM4Rec 中的使用方法与指标体系
- [生成式推荐](../concepts/generative_recommendation.md) 探讨了基于序列分词与自回归生成的推荐范式

## 参考文献

- Ni, J., Li, J., & McAuley, J. (2019). Justifying recommendations using distantly-labeled reviews and fine-grained aspects. EMNLP.
- Hou, Y., Ni, J., He, Z., Sachdeva, N., Kang, W. C., Chi, E. H., McAuley, J., & Cheng, D. Z. (2025). ActionPiece: Contextually Tokenizing Action Sequences for Generative Recommendation. *ICML 2025 (Spotlight)*. arXiv:2502.13581.
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

## 更新于 2026-04-14

**来源**: 2502_paper_25021358_ActionPiece_Contextually_Tokenizing_Action_Sequences_for_Ge.md
：新增“近期研究应用”小节，记录 ActionPiece 利用该数据集验证上下文感知分词有效性，补充其在 Beauty/Sports/Toys 多品类上的泛化表现与性能指标

---

## 更新完成：2502_paper_25021358_ActionPiece_Contextually_Tokenizing_Action_Sequences_for_Ge.md
**更新时间**: 2026-04-14 16:05
**更新摘要**: 已使用 LLM 对页面进行内容充实，基于 2502_paper_25021358_ActionPiece_Contextually_Tokenizing_Action_Sequences_for_Ge.md

*该页面的此次更新已完成。下次 ingest 其他源文档时将跳过此页面。*
