---
title: "Paper 8Edbf8 Higr Efficient Generative Slate Recommendation Via Hierarch"
category: "sources"
tags: ["source", "2026-04-08"]
created: "2026-04-08"
updated: "2026-04-08"
sources: ["../../raw/sources/paper_8edbf8_HiGR_Efficient_Generative_Slate_Recommendation_via_Hierarch.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要

HiGR 是一个高效的生成式 Slate 推荐框架，通过层次化规划与多目标偏好对齐解决现有生成式推荐方法的三大限制：物品 tokenization 纠缠、低效顺序解码、缺乏整体 slate 规划。该框架设计了一个包含残差量化和对比约束的自编码器，将物品 token 化为语义结构化 ID 以实现可控生成。

HiGR 将生成过程解耦为两个阶段：列表级规划阶段捕捉全局 slate 意图，物品级解码阶段选择具体物品，有效减少搜索空间并实现高效生成。同时引入多目标和列表级偏好对齐机制，利用隐式用户反馈增强 slate 质量。

实验验证了 HiGR 的有效性：离线推荐质量超过 SOTA 基线 10%+，推理速度提升 5 倍。已在腾讯商业平台部署（服务数亿用户），在线 A/B 测试显示平均观看时间提升 1.22%，平均视频播放量提升 1.73%。

### 需要更新的页面

- **wiki/concepts/llm4rec_overview.md**：添加生成式 Slate 推荐作为 LLM4Rec 的重要应用范式，补充层次化规划概念
- **wiki/methods/llm_as_generator.md**：添加 HiGR 的层次化生成方法（列表级规划 + 物品级解码），补充多目标偏好对齐机制
- **wiki/methods/rag_for_recsys.md**：补充语义结构化 ID tokenization 作为检索增强的替代方案
- **wiki/entities/kuaishou.md**：在工业实践部分添加腾讯作为对比，说明不同公司的生成式推荐部署

### 需要创建的新页面

- **wiki/models/HiGR.md**：HiGR 模型架构、层次化规划机制、多目标对齐详情
- **wiki/concepts/slate_recommendation.md**：Slate 推荐的概念、挑战、与列表级推荐的区别
- **wiki/concepts/hierarchical_planning_rec.md**：层次化规划在推荐中的应用、两阶段生成架构
- **wiki/entities/tencent.md**：腾讯公司推荐系统团队和工业实践（包括 HiGR 部署）
- **wiki/methods/multi_objective_alignment.md**：多目标偏好对齐方法、列表级优化技术

### 矛盾/冲突

- **未发现直接冲突**。HiGR（腾讯）与 QARM（快手）都是生成式推荐框架，但来自不同公司，解决不同问题（HiGR 专注 Slate 推荐，QARM 专注多模态对齐），可共存于知识库中。
- **注意**：现有知识库中 `wiki/entities/kuaishou.md` 标题不规范（"快手公司推荐系统团队和工业实践如不存在则创建"），建议后续清理时修正为简洁标题。

### 提取的关键事实

- HiGR 解决生成式 Slate 推荐的三大限制：物品 tokenization 纠缠、低效顺序解码、缺乏整体 slate 规划
- HiGR 使用残差量化 + 对比约束的自编码器进行物品 tokenization
- HiGR 采用两阶段生成：列表级规划（全局意图）+ 物品级解码（具体选择）
- 离线推荐质量超过 SOTA 基线 10%+
- 推理速度提升 5 倍
- 在腾讯商业平台部署，服务数亿用户
- 在线 A/B 测试：平均观看时间 +1.22%，平均视频播放量 +1.73%
- 论文版本：arXiv:2512.24787v2（2026 年 2 月 23 日修订）
- 作者共 14 人，主要来自腾讯

### 建议的源页面内容

```markdown
---
title: "HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning"
category: "sources"
tags: [HiGR, generative, slate, hierarchical-planning, tencent, 2026]
created: "2026-04-08"
updated: "2026-04-08"
sources: []
related:
  - "../models/HiGR.md"
  - "../concepts/slate_recommendation.md"
  - "../concepts/hierarchical_planning_rec.md"
  - "../entities/tencent.md"
confidence: "high"
status: "stable"
---

# HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning and Multi-Objective Preference Alignment

## 摘要

HiGR 是腾讯提出的高效生成式 Slate 推荐框架，通过层次化规划与多目标偏好对齐解决现有生成式推荐方法的三大限制。该框架在腾讯商业平台部署，服务数亿用户，在线 A/B 测试显示显著的业务指标提升。

**来源**: arXiv:2512.24787v2 (2026-02-23)

## 关键信息

| 属性 | 值 |
|------|-----|
| **标题** | HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning and Multi-Objective Preference Alignment |
| **作者** | Yunsheng Pang, Zijian Liu, Yudong Li, et al. (14 人) |
| **机构** | 腾讯 (Tencent) |
| **发布日期** | v1: 2025-12-31, v2: 2026-02-23 |
| **领域** | Information Retrieval (cs.IR), Artificial Intelligence (cs.AI) |
| **DOI** | 10.48550/arXiv:2512.24787 |

## 核心问题

现有生成式 Slate 推荐方法存在三大关键限制：

1. **物品 Tokenization 纠缠**：物品 ID 表示缺乏语义结构，难以实现可控生成
2. **低效顺序解码**：自回归生成需要多次解码步骤，推理开销大
3. **缺乏整体 Slate 规划**：无法捕捉全局 slate 意图，难以对齐多样化用户偏好和业务需求

## 主要贡献

### 1. 语义结构化物品 Tokenization

- 设计自编码器 incorporating **残差量化 (Residual Quantization)** 和 **对比约束 (Contrastive Constraints)**
- 将物品 token 化为语义结构化 ID
- 支持可控生成和更好的物品表示

### 2. 层次化两阶段生成

| 阶段 | 功能 | 优势 |
|------|------|------|
| **列表级规划** | 捕捉全局 slate 意图 | 减少搜索空间，整体优化 |
| **物品级解码** | 选择具体物品 | 高效生成，保持多样性 |

### 3. 多目标列表级偏好对齐

- 利用隐式用户反馈增强 slate 质量
- 同时优化多个业务目标（观看时间、播放量等）
- 列表级而非物品级优化

## 性能结果

### 离线评估

- 推荐质量超过 SOTA 基线 **10%+**
- 推理速度提升 **5 倍**

### 在线 A/B 测试（腾讯商业平台）

| 指标 | 提升 |
|------|------|
| 平均观看时间 | +1.22% |
| 平均视频播放量 | +1.73% |

### 部署规模

- 平台：腾讯商业推荐平台
- 用户规模：数亿用户
- 状态：已生产部署

## 与现有工作的关系

- **对比 QARM**：QARM（快手）专注多模态对齐，HiGR 专注 Slate 推荐层次化规划
- **对比 P5/InstructRec**：HiGR 针对 Slate 场景优化，采用两阶段生成而非单阶段生成
- **对比 LLMRank**：HiGR 使用生成式方法，LLMRank 使用判别式排序

## 关键引用

```bibtex
@article{pang2025higr,
  title={HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning and Multi-Objective Preference Alignment},
  author={Pang, Yunsheng and Liu, Zijian and Li, Yudong and Zhu, Shaojie and Luo, Zijian and Yu, Chenyun and Wu, Sikai and Shen, Shichen and Xu, Cong and Wang, Bin and Jiang, Kai and Yu, Hongyong and Zhuo, Chengxiang and Li, Zang},
  journal={arXiv preprint arXiv:2512.24787},
  year={2025}
}
```

## 相关链接

- [arXiv 页面](https://arxiv.org/abs/2512.24787)
- [PDF 版本](https://arxiv.org/pdf/2512.24787)
- [HTML 版本 (实验性)](https://arxiv.org/html/2512.24787v2)

## 知识库关联

- [HiGR 模型](../models/HiGR.md) — 详细模型架构
- [Slate 推荐](../concepts/slate_recommendation.md) — 概念背景
- [层次化规划](../concepts/hierarchical_planning_rec.md) — 方法细节
- [腾讯](../entities/tencent.md) — 部署机构

## 更新日期

- **2026-04-08**: 初始摄入，创建源页面和相关模型/概念页面
```