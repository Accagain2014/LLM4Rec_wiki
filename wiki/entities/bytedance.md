---
title: "ByteDance — Recommendation Systems at Scale"
category: "entities"
tags: [ByteDance, TikTok, Douyin, industrial recommendation, LONGER, RankMixer, LEMUR, industrial deployment]
created: "2026-04-09"
updated: "2026-04-09"
sources: ["../sources/2505_paper_25050442_LONGER_Scaling_Up_Long_Sequence_Modeling_in_Industrial_Reco.md"]
related:
  - "../models/LONGER.md"
  - "../models/RankMixer.md"
  - "../models/LEMUR.md"
  - "../concepts/scaling_laws_recsys.md"
confidence: "high"
status: "stable"
---

# 字节跳动 — 大规模推荐系统

## 概述

字节跳动是一家运营着多个**数亿到数十亿用户**平台的全球科技公司，包括 TikTok/抖音、今日头条等内容平台。推荐系统是所有字节跳动产品的核心，驱动内容发现、参与度和变现。该公司一直是工业级规模推荐研究的领先贡献者，尤其在**长序列建模**、**硬件感知排序**和**多模态推荐**方面。他们的研究成果在前所未有的规模上验证了推荐扩展定律，并证明算法创新在服务于数十亿用户的生产环境中转化为显著的业务指标提升。

## 要点

- **规模**：十亿用户级平台（TikTok、抖音、今日头条）
- **研究成果**：LONGER、RankMixer、LEMUR 等有影响力的系统
- **部署范围**：推荐和广告中 10+ 场景
- **扩展定律验证**：可预测性能提升的经验证据
- **工业影响**：多个产品中一致的 A/B 测试提升
- **开放研究**：在 RecSys、KDD、WWW 等 venue 广泛发表

## 详情

### 字节跳动的推荐

字节跳动的推荐挑战由以下维度定义：

| 维度 | 规模 |
|------|------|
| **用户** | 数亿到数十亿 |
| **物品** | 数百万视频/文章/商品 |
| **交互** | 每日数万亿交互 |
| **延迟预算** | 每请求 < 10ms |
| **QPS** | 数千到数万 |
| **场景** | 推荐、广告、搜索 |

### 关键研究成果

#### LONGER（RecSys 2025）
- **问题**：超长用户行为序列建模
- **解决方案**：Token 合并、全局 token、混合注意力、GPU 优化
- **影响**：部署于字节跳动 10+ 场景
- **验证**：广告和电商中一致的离线和在线增益
- **作者**：Chai Zheng、Ren Qin、Xiao Xijun、Yang Huizhi、Han Bo 等

#### RankMixer（2025）
- **问题**：在延迟约束下扩展排序模型
- **解决方案**：硬件感知 token 混合，Sparse-MoE 到 1B 参数
- **影响**：用户活跃天数 +0.3%，应用内使用时长 +1.08%
- **验证**：推荐和广告场景
- **作者**：Zhu Jie、Fan Zhifang、Zhu Xiaoxie、Jiang Yuchen 等

#### LEMUR（2025）
- **问题**：大规模端到端多模态推荐
- **解决方案**：用于搜索和广告的统一多模态架构
- **影响**：查询变更率衰减降低 0.843%，QAUC 提升 0.81%
- **部署**：抖音搜索和广告
- **作者**：字节跳动推荐团队

### 技术哲学

字节跳动的推荐研究遵循以下原则：

1. **工业优先**：研究必须转化为生产部署
2. **硬件感知**：为 GPU 执行优化的设计，而不仅仅是算法优雅
3. **面向扩展**：验证改进随更多计算/数据可预测地扩展
4. **端到端**：偏好统一架构而非碎片化的多阶段流水线
5. **开放研究**：广泛发表，为更广泛的研究社区做出贡献

### 基础设施

字节跳动的推荐基础设施支持：
- **GPU 稠密训练**：在 GPU 集群上进行大规模模型训练
- **实时服务**：海量 QPS 下的低延迟推理
- **A/B 测试平台**：对算法变更进行严格的在线评估
- **特征仓库**：跨模型和场景的共享特征计算

### 与其他工业实验室对比

| 公司 | 关键贡献 | 规模 |
|------|---------|------|
| **字节跳动** | LONGER、RankMixer、LEMUR | 十亿用户 |
| **Meta** | HSTU、ULTRA-HSTU、DLRM | 十亿用户 |
| **快手** | OneRec 系列 | 数亿用户 |
| **腾讯** | HiGR、广告挑战赛 | 数亿用户 |
| **Google/YouTube** | PLUM、DLRM 变体 | 十亿用户 |

## 关联

- [LONGER](../models/LONGER.md) — 字节跳动的长序列建模系统
- [RankMixer](../models/RankMixer.md) — 字节跳动的硬件感知排序模型
- [LEMUR](../models/LEMUR.md) — 字节跳动的多模态推荐系统
- [扩展定律](../concepts/scaling_laws_recsys.md) — 在字节跳动规模下验证
- [Meta](./meta.md) — 另一个工业级规模推荐实验室

## 开放问题

1. 字节跳动的推荐方法在国内（抖音）和国际（TikTok）产品之间有何不同？
2. 生成式推荐在字节跳动未来路线图中的作用是什么？
3. 字节跳动如何平衡个性化与内容多样性和用户福祉？
4. 基于 LLM 的推荐在字节跳动生产系统中部署的时间线是什么？

## 参考文献

- Chai, Z., et al. (2025). LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders. RecSys 2025. arXiv:2505.04421.
- Zhu, J., et al. (2025). RankMixer: Scaling Up Ranking Models in Industrial Recommenders. arXiv:2507.15551.
- "Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling." arXiv:2511.06077.
- "LEMUR: Large-scale End-to-end Multimodal Recommendation." arXiv:2511.10966.
