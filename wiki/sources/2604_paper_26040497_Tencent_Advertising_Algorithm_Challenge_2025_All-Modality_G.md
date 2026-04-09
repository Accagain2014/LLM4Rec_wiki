---
title: "2604 Paper 26040497 Tencent Advertising Algorithm Challenge 2025 All-Modality G"
category: "sources"
tags: ["source", "2026-04-09"]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../../raw/sources/2604_paper_26040497_Tencent_Advertising_Algorithm_Challenge_2025_All-Modality_G.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要

本文档介绍了**腾讯广告算法挑战赛 2025**，这是一个面向全模态生成式推荐（All-Modality Generative Recommendation）的全球性竞赛。该竞赛基于两个从真实腾讯广告日志构建的数据集：**TencentGR-1M**（100 万用户序列）和**TencentGR-10M**（1000 万用户），填补了工业级全模态生成式推荐公共基准的空白。

数据集包含丰富的协同 ID 和使用最先进嵌入模型提取的多模态表示。初步赛道提供用户交互序列（曝光和点击信号），最终赛道进一步区分点击和转化事件，并在序列和目标级别进行标注。论文提供了任务定义、数据构建流程、特征模式、基线 GR 模型、评估协议以及获奖解决方案的关键发现。

该竞赛引入**加权评估**机制以突出高价值转化事件的重要性，数据集和基线实现已公开释放，旨在推动工业规模全模态生成式推荐的未来研究。

---

### 需要更新的页面

- **wiki/entities/tencent.md**：添加腾讯广告算法挑战赛 2025 信息，包括数据集发布、竞赛规模、与 HiGR 的关联
- **wiki/concepts/evaluation_llm4rec.md**：添加加权评估协议、转化事件评估方法
- **wiki/concepts/generative_retrieval.md**：更新工业级全模态 GR 基准信息
- **wiki/entities/amazon_reviews.md**：在对比部分添加 TencentGR 数据集作为工业广告场景的对比基准
- **wiki/synthesis/llm4rec_taxonomy.md**：在数据集分类中添加腾讯广告数据集类别

---

### 需要创建的新页面

- **wiki/entities/tencentgr_dataset.md**：TencentGR-1M 和 TencentGR-10M 数据集的详细页面，包括数据规模、特征 schema、获取方式
- **wiki/concepts/all_modality_gr.md**：全模态生成式推荐概念页面，解释多模态内容如何映射到离散 token 空间
- **wiki/methods/weighted_evaluation.md**：加权评估方法，用于高价值转化事件的评估协议
- **wiki/entities/taac.md**：腾讯广告算法挑战赛（Tencent Advertising Algorithm Challenge）实体页面

---

### 矛盾/冲突

- **未发现直接冲突**。但需注意：
  - 现有知识库中腾讯相关页面（tencent.md）主要基于 HiGR 论文，此源文档提供了更全面的腾讯推荐系统研究图景
  - 现有知识库中缺乏专门的工业广告推荐数据集页面，TencentGR 填补了这一空白
  - 需确认 Irwin King 是否已有实体页面，如无则需创建

---

### 提取的关键事实

- **数据集规模**：TencentGR-1M（100 万用户，每用户最多 100 个交互）、TencentGR-10M（1000 万用户）
- **数据来源**：真实去标识化的腾讯广告日志
- **信号类型**：曝光（exposure）、点击（click）、转化（conversion）
- **模态内容**：协同 ID + 多模态表示（使用 SOTA 嵌入模型提取）
- **评估特点**：加权评估协议，突出高价值转化事件
- **作者团队**：23 位作者，包括腾讯团队和 Irwin King（香港中文大学）等学术界合作者
- **提交日期**：2026 年 4 月 4 日
- **公开资源**：数据集（HuggingFace）、基线代码（GitHub）、竞赛官网（algo.qq.com/2025）
- **研究空白**：缺乏面向工业广告的大规模、真实、全模态生成式推荐公共基准

---

### 建议的源页面内容

```markdown
---
title: "2604 Paper 26040497 Tencent Advertising Algorithm Challenge 2025 All-Modality Generative Recommendation"
category: "sources"
tags: ["source", "2026-04-09", "tencent", "dataset", "competition", "all-modality", "generative-recommendation"]
created: "2026-04-09"
updated: "2026-04-09"
sources: []
related:
  - "../entities/tencent.md"
  - "../entities/tencentgr_dataset.md"
  - "../concepts/all_modality_gr.md"
  - "../methods/weighted_evaluation.md"
confidence: "high"
status: "stable"
---

# 2604 Paper 26040497: Tencent Advertising Algorithm Challenge 2025

## 摘要

本文档介绍了**腾讯广告算法挑战赛 2025（TAAC 2025）**，这是一个面向**全模态生成式推荐**的全球性竞赛。竞赛基于两个从真实腾讯广告日志构建的数据集（TencentGR-1M 和 TencentGR-10M），填补了工业级全模态生成式推荐公共基准的空白。

## 要点

- **数据集**：TencentGR-1M（100 万用户）、TencentGR-10M（1000 万用户）
- **数据来源**：真实去标识化的腾讯广告日志
- **信号类型**：曝光、点击、转化（最终赛道区分点击和转化事件）
- **模态内容**：协同 ID + 多模态表示（SOTA 嵌入模型提取）
- **评估协议**：加权评估，突出高价值转化事件
- **公开资源**：数据集、基线代码、竞赛官网全部开放

## 详情

### 论文元数据

| 字段 | 值 |
|------|-----|
| **arXiv ID** | 2604.04976 |
| **提交日期** | 2026 年 4 月 4 日 |
| **领域** | Information Retrieval (cs.IR) |
| **作者数** | 23 位 |
| **主要机构** | 腾讯广告、香港中文大学等 |

### 核心作者

- Junwei Pan（腾讯）
- Wei Xue（腾讯）
- Chao Zhou（腾讯）
- Irwin King（香港中文大学）
- 等 23 位作者

### 数据集规格

#### TencentGR-1M（初步赛道）

| 指标 | 数值 |
|------|------|
| 用户序列数 | 100 万 |
| 每用户最大交互数 | 100 |
| 信号类型 | 曝光、点击 |
| 用途 | 初步筛选、基线验证 |

#### TencentGR-10M（最终赛道）

| 指标 | 数值 |
|------|------|
| 用户序列数 | 1000 万 |
| 信号类型 | 曝光、点击、转化 |
| 事件区分 | 序列级别 + 目标级别 |
| 用途 | 最终排名、工业验证 |

### 数据特征 Schema

- **协同 ID**：用户和物品的离散标识符
- **多模态表示**：
  - 文本嵌入（标题、描述）
  - 图像嵌入（商品图片）
  - 视频嵌入（广告视频内容）
  - 使用 SOTA 嵌入模型提取
- **行为序列**：用户历史交互的自回归序列
- **时间戳**：交互发生时间

### 评估协议

#### 加权评估机制

- **核心思想**：高价值转化事件获得更高权重
- **动机**：广告场景中转化（conversion）比点击（click）具有更高商业价值
- **实现**：在标准指标（NDCG、HR@K）基础上引入事件权重

#### 评估指标

- 序列级别指标
- 目标级别指标
- 点击率（CTR）预测
- 转化率（CVR）预测
- 加权 NDCG@K
- 加权 HR@K

### 基线模型

- **模型类型**：生成式推荐（GR）基线
- **架构**：自回归序列模型
- **输入**：用户行为序列 + 多模态物品表示
- **输出**：离散 token 空间中的物品预测
- **代码公开**：GitHub 仓库提供完整实现

### 关键发现

1. **工业基准缺乏**：现有公共数据集缺乏面向工业广告的大规模全模态 GR 基准
2. **多模态重要性**：多模态内容映射到离散 token 空间是 GR 的核心挑战
3. **转化事件价值**：加权评估能更好反映广告场景的商业目标
4. **规模效应**：10M 级别数据集能更好验证模型的工业适用性

### 公开资源

| 资源类型 | 链接 |
|----------|------|
| **数据集** | https://huggingface.co/datasets/TAAC2025 |
| **基线代码** | https://github.com/TencentAdvertisingAlgorithmCompetition/baseline_2025 |
| **竞赛官网** | https://algo.qq.com/2025 |
| **论文 PDF** | https://arxiv.org/pdf/2604.04976 |

### 与现有研究的关联

- **HiGR**：同属腾讯团队的生成式推荐研究，HiGR 聚焦 Slate 推荐，本竞赛聚焦全模态 GR 基准
- **FORGE**：FORGE 聚焦语义 ID 形成，本竞赛提供完整的工业级评估框架
- **PLUM**：Google/YouTube 的工业 GR 部署，本竞赛提供可公开获取的工业基准

## 关联

- [腾讯公司](../entities/tencent.md) — 竞赛主办方
- [TencentGR 数据集](../entities/tencentgr_dataset.md) — 竞赛数据集详情
- [全模态生成式推荐](../concepts/all_modality_gr.md) — 核心概念
- [加权评估](../methods/weighted_evaluation.md) — 评估方法

## 参考文献

- Pan, J., Xue, W., Zhou, C., et al. (2026). Tencent Advertising Algorithm Challenge 2025: All-Modality Generative Recommendation. arXiv:2604.04976.
```

---

### 操作日志条目建议

```markdown
## [2026-04-09] ingest | 处理腾讯广告算法挑战赛 2025 论文

- 源文件：raw/sources/2604_paper_26040497_Tencent_Advertising_Algorithm_Challenge_2025.md
- 创建源摘要页面：wiki/sources/2604_paper_26040497_Tencent_Advertising_Algorithm_Challenge_2025_All-Modality_G.md
- 待创建页面：
  - wiki/entities/tencentgr_dataset.md
  - wiki/concepts/all_modality_gr.md
  - wiki/methods/weighted_evaluation.md
  - wiki/entities/taac.md
- 待更新页面：
  - wiki/entities/tencent.md
  - wiki/concepts/evaluation_llm4rec.md
  - wiki/concepts/generative_retrieval.md
- 矛盾检查：未发现直接冲突
- 可信度：high（官方竞赛论文，arXiv 发布）
```