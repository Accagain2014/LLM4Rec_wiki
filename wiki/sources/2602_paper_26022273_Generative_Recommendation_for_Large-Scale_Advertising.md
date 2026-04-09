---
title: "2602 Paper 26022273 Generative Recommendation For Large-Scale Advertising"
category: "sources"
tags: ["source", "2026-04-09"]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../../raw/sources/2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要

本文介绍了 **GR4AD**（Generative Recommendation for ADdvertising），这是一个面向大规模广告场景的生产级生成式推荐系统，由快手团队开发并部署。该系统针对工业级实时推荐的特殊需求，在架构、学习和服务三个层面进行了协同设计，超越了传统 LLM 风格的训练和服务方案。

核心技术创新包括：**UA-SID**（统一广告语义 ID）用于捕捉复杂的商业信息；**LazyAR**（懒自回归解码器）通过放松层间依赖来降低短序列、多候选生成的推理成本；**VSL**（价值感知监督学习）和 **RSPO**（排序引导的 Softmax 偏好优化）用于对齐业务价值优化；以及**动态束搜索服务**用于控制计算负载。

大规模在线 A/B 测试显示，相比现有 DLRM 基线，广告收入提升达 **4.2%**。该系统已在快手广告系统全面部署，服务超过 **4 亿用户**，实现了高吞吐实时服务。

### 需要更新的页面

- **wiki/entities/kuaishou.md**：添加 GR4AD 部署案例，补充 4 亿用户规模、4.2% 收入提升等工业指标，更新技术团队背景（Ben Xue、Guorui Zhou 等）
- **wiki/entities/guorui_zhou.md**：添加 GR4AD 作为其最新贡献（2026 年），补充其在生成式广告推荐领域的领导角色
- **wiki/concepts/semantic_id.md**：添加 UA-SID 作为语义 ID 在广告场景的变体，说明其如何捕捉商业信息
- **wiki/methods/llm_as_generator.md**：添加 LazyAR 解码器作为生成效率优化技术，补充动态束搜索服务策略
- **wiki/synthesis/traditional_vs_llm.md**：添加 GR4AD vs DLRM 的对比数据（4.2% 收入提升），强化 LLM 在工业广告场景的价值论证

### 需要创建的新页面

- **wiki/models/GR4AD.md**：GR4AD 模型架构页面，涵盖 UA-SID、LazyAR、VSL、RSPO 等核心组件
- **wiki/methods/ua_sid.md**：统一广告语义 ID 方法页面，解释广告场景下的语义 ID 设计
- **wiki/methods/lazy_ar.md**：懒自回归解码器方法页面，说明层间依赖放松机制
- **wiki/methods/rspo.md**：排序引导的 Softmax 偏好优化方法页面，涵盖列表级强化学习算法
- **wiki/sources/2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md**：本论文的源文档摘要页面

### 矛盾/冲突

- **未发现直接冲突**，但需注意：
  - 现有知识库中快手相关页面（kuaishou.md）主要引用 OneRec-Think，需明确 GR4AD 是独立的广告推荐系统
  - 语义 ID 相关页面提到 FORGE 的代理指标，GR4AD 的 UA-SID 是广告场景的特化版本，需标注适用场景差异
  - 现有 LLM-as-Generator 页面未涵盖 LazyAR 这类效率优化技术，需补充

### 提取的关键事实

- **模型名称**: GR4AD (Generative Recommendation for ADdvertising)
- **开发团队**: 快手广告系统团队（30 位作者）
- **核心作者**: Ben Xue、Guorui Zhou（周国瑞）、Kun Gai（盖坤）等
- **部署规模**: 4 亿 + 用户
- **业务效果**: A/B 测试广告收入提升 4.2%
- **UA-SID**: Unified Advertisement Semantic ID，捕捉复杂商业信息
- **LazyAR**: Lazy Autoregressive Decoder，放松层间依赖降低推理成本
- **VSL**: Value-Aware Supervised Learning，价值感知监督学习
- **RSPO**: Ranking-Guided Softmax Preference Optimization，列表级强化学习算法
- **动态束搜索**: 根据生成层级和在线负载自适应调整 beam width
- **基线对比**: 超越 DLRM-based stack
- **论文状态**: under review（2026 年 2 月提交，4 月修订 v3）
- **arXiv 编号**: 2602.22732

### 建议的源页面内容

```markdown
---
title: "2602 Paper 26022273 Generative Recommendation for Large-Scale Advertising"
category: "sources"
tags: ["source", "2026-04-09", "kuaishou", "advertising", "GR4AD"]
created: "2026-04-09"
updated: "2026-04-09"
sources: []
related:
  - "../models/GR4AD.md"
  - "../entities/kuaishou.md"
  - "../entities/guorui_zhou.md"
  - "../methods/ua_sid.md"
  - "../methods/lazy_ar.md"
  - "../methods/rspo.md"
confidence: "high"
status: "stable"
---

# 2602 Paper 26022273 Generative Recommendation for Large-Scale Advertising

## 元数据

| 字段 | 值 |
|------|-----|
| **arXiv ID** | 2602.22732 |
| **标题** | Generative Recommendation for Large-Scale Advertising |
| **作者** | Ben Xue, Dan Liu, Lixiang Wang, Mingjie Sun, Peng Wang, Pengfei Zhang, Shaoyun Shi, Tianyu Xu, Yunhao Sha, Zhiqiang Liu, Bo Kong, Bo Wang, Hang Yang, Jieting Xue, Junhao Wang, Shengyu Wang, Shuping Hui, Wencai Ye, Xiao Lin, Yongzhi Li, Yuhang Chen, Zhihui Yin, Quan Chen, Shiyang Wen, Wenjin Wu, Han Li, **Guorui Zhou**, Changcheng Li, Peng Jiang, **Kun Gai** |
| **机构** | 快手（Kuaishou）广告系统 |
| **提交日期** | 2026-02-26 (v1), 2026-04-02 (v3) |
| **状态** | under review |
| **领域** | Information Retrieval (cs.IR), Machine Learning (cs.LG) |

## 摘要

生成式推荐因其可扩展性和更强的模型容量，在工业界受到广泛关注。然而，在大规模广告中部署实时生成式推荐需要超越 LLM 风格训练和服务方案的设计。本文提出 **GR4AD**（Generative Recommendation for ADdvertising），一个在架构、学习和服务层面协同设计的生产级生成式推荐系统。

## 核心贡献

### 1. UA-SID（Unified Advertisement Semantic ID）

- **目的**: 捕捉广告场景中复杂的商业信息
- **设计**: 统一广告语义 ID 编码方案
- **优势**: 相比传统 Item ID，能更好地表达广告的多维特征（广告主、创意、定向条件等）

### 2. LazyAR（Lazy Autoregressive Decoder）

- **机制**: 放松层间依赖（relaxes layer-wise dependencies）
- **适用场景**: 短序列、多候选生成
- **效果**: 保持有效性的同时降低推理成本
- **价值**: 在固定服务预算下支持模型扩展

### 3. VSL（Value-Aware Supervised Learning）

- **目标**: 使优化与业务价值对齐
- **方法**: 价值感知监督学习
- **应用**: 将广告收入等商业指标纳入训练目标

### 4. RSPO（Ranking-Guided Softmax Preference Optimization）

- **类型**: 排序感知的列表级强化学习算法
- **优化目标**: 基于列表级指标的价值奖励
- **用途**: 支持持续在线更新（continual online updates）

### 5. Dynamic Beam Serving

- **功能**: 动态调整束搜索宽度
- **自适应维度**: 生成层级（generation levels）和在线负载（online load）
- **目的**: 控制计算资源消耗

## 实验结果

| 指标 | 数值 |
|------|------|
| **广告收入提升** | +4.2%（vs DLRM-based stack） |
| **服务用户规模** | 4 亿 + |
| **部署状态** | 全面上线（fully deployed） |
| **服务类型** | 高吞吐实时服务 |

## 关键发现

1. **模型扩展收益**: 广告收入提升来自模型扩展和推理时扩展的一致增益
2. **工业可行性**: 生成式推荐可在大规模广告场景中实现实时服务
3. **架构协同设计**: 架构、学习、服务三层面需协同优化，不能仅套用 LLM 训练范式

## 与现有研究的关联

- **与 OneRec-Think 的关系**: 同为快手团队工作，但 GR4AD 专注于广告场景，OneRec-Think 专注于通用推荐推理
- **与 HiGR 的关系**: HiGR 关注 Slate 推荐的层次化生成，GR4AD 关注广告场景的价值优化
- **与 FORGE 的关系**: FORGE 提出语义 ID 的免训练评估，GR4AD 的 UA-SID 是广告场景的特化实现

## 局限性

- 论文状态为 under review，尚未经过同行评审
- 未公开 UA-SID 的具体编码细节
- LazyAR 的技术细节描述有限
- 未提供与其他生成式推荐系统（如 PLUM、OneRec）的直接对比

## 开放问题

1. UA-SID 如何具体编码广告的多维商业特征？
2. LazyAR 放松层间依赖的具体机制是什么？
3. RSPO 与现有偏好优化方法（如 DPO、PPO）的差异？
4. 动态束搜索的自适应策略如何设计？

## 参考文献

- arXiv:2602.22732 - https://arxiv.org/abs/2602.22732
- DOI: https://doi.org/10.48550/arXiv.2602.22732

---

*本页面由 LLM 自动生成，内容基于源文档摘要，可能需要人工审查和补充。*
```

## 更新于 2026-04-09

**来源**: 2602_paper_26022273_Generative_Recommendation_for_Large-Scale_Advertising.md
：本论文的源文档摘要页面
