---
title: "2411 Paper 24111881 Unifying Generative And Dense Retrieval For Sequential Recom"
category: "sources"
tags: ["source", "2026-04-15"]
created: "2026-04-15"
updated: "2026-04-15"
sources: ["../../raw/sources/2411_paper_24111881_Unifying_Generative_and_Dense_Retrieval_for_Sequential_Recom.md"]
related: []
confidence: "high"
status: "stable"
---

### 源文档摘要
本文系统性地对比了序列推荐中**稠密检索（Dense Retrieval）**与**生成式检索（Generative Retrieval）**两大主流范式，揭示了两者在推荐精度、内存开销与推理延迟上的核心工程权衡。针对单一范式的局限性，作者提出 **LIGER** 混合架构，通过“稠密表征+语义生成”双路协同机制，将稠密向量的细粒度匹配能力与生成式语义 ID 的高效索引/泛化能力深度融合。

实验表明，LIGER 在学术基准上相比纯生成式基线在 Recall@10 与 NDCG@10 上平均提升 12%-18%，在冷启动与长尾场景增益超 20%；同时相比传统稠密检索，全量物品向量存储开销降低 70%-80%，推理延迟优化约 15%。该工作为 LLM4Rec 在工业级序列推荐中平衡精度、存储与泛化能力提供了可落地的混合范式蓝图。

### 需要更新的页面
- **`wiki/concepts/generative_retrieval.md`**：补充生成式检索与稠密检索的实证对比结论，明确其在存储效率与冷启动泛化上的优势，以及在细粒度匹配精度上的相对短板；增加“混合检索范式”作为演进方向。
- **`wiki/concepts/sequential_recommendation.md`**：在检索/召回模块更新中引入 LIGER 的双路协同架构，说明序列推荐正从单一检索范式向“稠密+生成”混合架构演进。
- **`wiki/methods/hybrid_generative_recommendation.md`**：将 LIGER 作为核心案例补充，详细说明其跨空间表征对齐、门控融合层与多目标联合优化策略，丰富混合生成的具体实现路径。
- **`wiki/concepts/semantic_id.md`**：在“构建依赖与局限性”章节补充说明：SID 质量高度依赖预训练语义模型与物品元数据，噪声或稀疏元数据会直接影响生成路径稳定性，需结合稠密信号进行鲁棒性补偿。

### 需要创建的新页面
- **`wiki/models/LIGER.md`**：LIGER 混合检索模型专页，涵盖双通道架构设计、跨空间对齐机制、联合优化目标、实验结果及在序列推荐中的定位。

### 矛盾/冲突
- **未发现直接矛盾**。本文结论与现有知识库中关于“纯生成式检索在冷启动/长尾场景具优势但细粒度匹配不足”、“混合架构是工业落地重要方向”的论述高度一致，属于实证补充与架构细化。

### 提取的关键事实
- 论文发表于 arXiv (2411.18814)，2024 年 11 月。
- 提出 **LIGER** 模型，采用“生成式自回归解码 + 序列稠密内积匹配”双通道架构，通过门控层动态融合。
- 引入**跨空间表征对齐**（对比学习+投影映射），确保稠密向量空间与生成式语义 ID 空间隐层特征一致。
- 训练采用**多目标联合优化**：生成交叉熵损失 + 稠密匹配排序损失，端到端共享梯度。
- 实验结果：较纯生成式基线 Recall@10/NDCG@10 提升 12%-18%；冷启动/长尾场景增益 >20%；较稠密检索存储降低 70%-80%，延迟优化 ~15%。
- 局限性：目前仅在学术数据集验证；SID 构建强依赖元数据质量，数据噪声可能影响生成稳定性；缺乏亿级工业分布式扩展验证。

### 建议的源页面内容

```markdown
---
title: "2411 Paper 24111881 Unifying Generative and Dense Retrieval for Sequential Recommendation"
category: "sources"
tags: ["source", "2026-04-15", "LIGER", "hybrid retrieval", "dense retrieval", "generative retrieval", "sequential recommendation", "cold-start", "storage optimization"]
created: "2026-04-15"
updated: "2026-04-15"
sources: ["../../raw/sources/2411_paper_24111881_Unifying_Generative_and_Dense_Retrieval_for_Sequential_Recom.md"]
related:
  - "../concepts/generative_retrieval.md"
  - "../concepts/sequential_recommendation.md"
  - "../methods/hybrid_generative_recommendation.md"
  - "../models/LIGER.md"
confidence: "high"
status: "stable"
---

# 2411 Paper 24111881 Unifying Generative and Dense Retrieval for Sequential Recommendation

## 源文档摘要
本文针对序列推荐中稠密检索与生成式检索的性能与计算权衡展开系统研究。在公平受控实验条件下，作者首次深度对比了两大范式的核心差异，并提出 **LIGER** 混合架构。该架构通过“稠密表征+语义生成”双路协同机制，有效弥合了单一范式的性能差距，显著缓解冷启动瓶颈，并在学术基准上验证了其在推荐精度、存储效率与推理延迟上的综合优势。

## 核心贡献
1. **首次公平对比两大检索范式**：明确揭示稠密检索（高精度、高存储）与生成式检索（低存储、强泛化）的工程权衡边界。
2. **提出 LIGER 混合架构**：设计双路融合机制，底层保留生成式自回归解码，上层并行引入序列稠密检索，通过门控层动态加权输出。
3. **突破冷启动与存储瓶颈**：在保持高推荐准确率的同时，大幅降低全量物品向量存储需求（-70%~80%），为中小规模及冷启动场景提供高效范式。

## 方法与技术细节
### 架构设计
- **双通道协同**：生成路径直接预测语义 ID 序列；稠密路径利用序列编码器提取用户历史稠密表征，与物品向量进行内积匹配。
- **门控融合层**：根据上下文动态分配两路信号权重，生成统一排序列表，支持灵活切换或并行推理。

### 关键技术
- **语义 ID 层次化编码**：将多模态/文本语义压缩为树状或序列化 ID，供生成模型学习物品语义拓扑。
- **跨空间表征对齐**：通过对比学习与投影映射，使稠密向量空间与生成式语义 ID 空间在隐层对齐，避免信号冲突。
- **多目标联合优化**：构建生成交叉熵损失 + 稠密匹配排序损失的复合目标，实现端到端梯度共享。
- **内存感知推理**：利用生成路径免维护全量 Embedding 的特性，结合稠密路径局部缓存，动态压缩显存/内存占用。

## 实验结果
- **精度提升**：较纯生成式基线 Recall@10 与 NDCG@10 平均相对提升 12%-18%。
- **冷启动/长尾增益**：在稀疏交互场景下性能提升超 20%。
- **效率优化**：较传统稠密检索全量向量存储降低 70%-80%，推理延迟优化约 15%。

## 局限性
- 评估集中于中小规模学术数据集，尚未验证千万/亿级工业分布式扩展能力。
- 生成式语义 ID 质量高度依赖预训练语义模型与物品元数据，数据稀疏或噪声可能影响生成路径稳定性。
- 需进一步探索更鲁棒的 ID 自动构建算法及大规模分布式推理优化方案。

## 与 LLM4Rec 的相关性
本文紧密契合 LLM4Rec 的核心演进方向。生成式检索本质上是 LLM 在推荐系统中的典型落地范式，LIGER 提出的“生成+稠密”融合思路为 LLM 推荐系统提供了兼顾细粒度匹配与低存储开销的工程蓝图。其架构设计可直接迁移至基于大语言模型的序列推荐、对话推荐及多模态推荐场景，对推动 LLM 在工业级推荐系统中的高效部署具有重要指导意义。

## 需要更新的页面
- `wiki/concepts/generative_retrieval.md`：补充生成式 vs 稠密检索的实证对比与混合范式演进。
- `wiki/concepts/sequential_recommendation.md`：更新检索模块，纳入双路协同架构。
- `wiki/methods/hybrid_generative_recommendation.md`：补充 LIGER 作为混合生成的核心实现案例。
- `wiki/concepts/semantic_id.md`：补充 SID 构建对元数据质量的依赖性及混合架构的补偿作用。

## 参考文献
- Yang, L., Paischer, F., Hassani, K., et al. (2024). *Unifying Generative and Dense Retrieval for Sequential Recommendation*. arXiv:2411.18814.
```