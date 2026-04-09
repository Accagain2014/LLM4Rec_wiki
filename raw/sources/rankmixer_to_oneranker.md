从 RankMixer 到 OneRanker：2025—2026 大厂搜推大模型技术路线
Leopold
Leopold
​关注他
tracholar、九河之间 等 371 人赞同了该文章
导语
如果将 2023 年视为推荐系统开始系统性讨论“大模型化”的起点，那么 2025—2026 年更像是这一技术方向真正进入产业深水区的阶段。

这一轮演进已经明显超出“参数规模扩张”的范畴，而是在四个层面同步发生：其一，排序主干正从传统 DLRM 式结构持续演化为更强的 token-based backbone；其二，超长用户行为序列开始从局部实验能力演进为可在线部署的工业能力；其三，item ID 正在被 semantic token、层次化索引与生成式表示体系重新定义；其四，推荐与广告系统中 retrieve、rank、rerank 的多阶段流水线，正在被端到端生成式 one-model 重新组织。

如果以字节跳动这一组工作作为观察窗口，那么从 RankMixer、OneTrans、TRM、MDL、MixFormer，到外部的 SORT、MTFM、OneRec、GPR、OneRanker、GR4AD、OxygenREC，行业内部事实上已经形成了一套相对清晰的技术分工与演进逻辑。

本文尝试回答三个问题：第一，这些工作分别位于哪一条主线上；第二，哪些论文属于同一脉络内的连续推进，哪些只是并行分支；第三，下一阶段推荐系统大模型化的真正分水岭究竟在哪里。

正文
一、总体判断：推荐系统大模型正在沿四条主线并行推进
近两年的工业论文如果仅按模型名称逐篇阅读，容易显得离散；如果按照问题域重新组织，则可以清楚看到四条相互耦合的主线。

第一条主线是大 ranking backbone 的可扩展化。 这一方向关注的核心问题是：工业排序模型如何像语言模型一样具备随参数、数据与算力共同扩展的能力。字节的 RankMixer、TokenMixer-Large、MSN、UG-Separation，阿里的 SORT，美团的 MTmixAtt，均属于这一问题域。

第二条主线是长序列建模的工业化。 这一方向关注的不是“是否能够建模长历史”，而是“如何在训练成本、在线时延、系统存储与效果收益之间建立可持续的平衡”。字节的 LONGER、STCA、LEMUR，小红书的 LASER，腾讯广告的长行为序列建模，LinkedIn 的 Feed-SR，均可归入此类。

第三条主线是统一 backbone。 过去的推荐系统通常将 sequence modeling、feature interaction、multi-scenario、multi-task 拆分为多个模块分别处理；而近两年的代表性工作正逐步将这些结构重新统一到更少但更强的主干之中。OneTrans、MixFormer、HoMer、MDL、MTFM 的核心命题，均可概括为“更大范围的统一建模”。

第四条主线是 semantic token 与生成式 one-model。 这一方向比前三条更具结构性变化。它不只改写排序器，而是尝试同时重构 item 表示、索引方式、召回与排序接口，甚至整个广告与推荐的多阶段流水线。字节的 TRM、MERGE，快手的 OneRec、OneLoc、OneMall、GR4AD、GRank，腾讯的 GPR、OneRanker，京东的 OxygenREC，均可置于这一脉络下理解。

更关键的事实在于，这四条主线并非彼此孤立。判别式大 ranking 模型正在吸收 semantic token、统一建模与更深的系统优化；生成式推荐则在吸收传统排序系统中的 value modeling、feature engineering 与 serving 约束。与此同时，线上系统优化已经不再是附属工程，而开始成为论文的主创新之一。

二、字节跳动的技术链条：为什么这一组工作值得单独分析
字节跳动这批论文的重要性，并不仅在于数量，而在于其内部形成了一条相对完整的工业技术链：从 dense backbone 的可扩展化，到长序列建模、多模态、统一主干、semantic token、多分布学习，再到 serving 与索引层改造，几乎覆盖了当前推荐系统大模型化的关键环节。

1. RankMixer：将排序主干改造为可扩展对象
RankMixer 的历史地位非常明确。它并非传统意义上的“又一个 CTR 模型”，而是第一次较系统地将工业 ranking backbone 改造成更适合大规模扩展的结构。其核心做法是以 token mixing 替代传统 attention 中并不适合异构推荐特征的相似度建模，再配合 per-token FFN 与 SparseMoE，将主干的表达能力、并行性与硬件利用率同时提升。

这一工作的关键贡献并不只是单点指标提升，而在于验证了一个更重要的命题：推荐排序模型也可以围绕统一的 token 交互主干形成自己的 scaling 路线。 在这一点被验证之后，TokenMixer-Large、MSN、UG-Separation 等后续工作才具有继续叠加的前提。

2. TokenMixer-Large、MSN、UG-Separation：围绕 RankMixer 的三种补强路径
在 RankMixer 之后，字节跳动并未立即切换技术路线，而是沿着三个方向持续深化。

TokenMixer-Large 解决的是“能够扩展之后，如何稳定扩展”的问题。该工作在 RankMixer 的基础上进一步引入 mixing-and-reverting、inter-layer residuals、auxiliary loss 以及 Sparse Per-token MoE，将模型规模推进到 7B 在线、15B 离线量级。它所代表的是 backbone 本体的结构升级。

MSN 解决的是“在严格算力预算下，如何继续扩大模型容量”的问题。它没有沿用标准 Sparse MoE 的扩容路线，而是引入 memory-based sparse activation，通过 Product-Key Memory 实现低成本稀疏检索，再将个性化记忆注入下游交互模块。其核心价值在于：将容量增长从‘激活更大 expert’转化为‘检索式注入个性化参数’。 它代表的是 容量扩张机制的升级。

UG-Separation 解决的是“如此之大的 dense 模型如何在线高效服务”的问题。该工作将 RankMixer 内部原本深度耦合的 user-side 与 item-side 信息流显式拆分，首次使 dense interaction 模型也具备了“用户侧只计算一次”的 serving 复用能力。它代表的是 部署与复用机制的升级。

将这三篇论文放在一起观察，可以发现其覆盖了大模型工业化最典型的三个问题：主干如何变大、容量如何继续扩展、系统如何在线承载。

3. STCA、LEMUR：另一条关键支柱是长序列与多模态
在同一组论文中，STCA 与 LEMUR 需要与 RankMixer 主干线区分理解。

STCA 解决的是超长行为序列的目标感知建模问题。其核心做法是将历史内部的 self-attention 改写为 stacked target-to-history cross attention，并通过 request-level batching 将序列计算的复用机制显式引入在线服务阶段。因此，STCA 的重点不在 dense 主干扩展，而在于以更低复杂度、更高复用性的方式提升序列侧建模上限。

LEMUR 则是在现有大推荐模型体系上，将多模态输入推进到端到端训练。其关键变化并非引入一个多模态 encoder，而是将多模态表示学习与 ranking objective 直接闭环，并通过 memory bank 控制长历史上的重复编码成本。因此，LEMUR 的价值在于：将多模态从“外部特征工程”提升为“主排序系统的内生组成部分”。

因此，STCA 与 LEMUR 更适合作为 sequence side 与 multimodal side 的工业化支柱理解，而非 RankMixer 的直接“下一版本”。这条线随后在 OneTrans、MixFormer 等统一 backbone 体系中与 dense 主干线完成汇合。

4. OneTrans、MixFormer、MDL：进入“统一化”阶段
如果说 RankMixer 解决的是“单个大 backbone 如何扩展”，那么 OneTrans、MixFormer、MDL 所回答的问题是：推荐系统中原本分散的模块是否应重新统一。

OneTrans 的关键突破在于首次较彻底地将 sequential features 与 non-sequential features 做统一 tokenization，并以单一 Transformer backbone 同时承担 sequence modeling 与 feature interaction。与通用 NLP Transformer 不同，它针对推荐系统中的异构 token 设计了 mixed parameterization，并结合 pyramid pruning 与 cross-request KV caching 处理真实部署约束。因此，OneTrans 的核心贡献是：在统一建模的前提下，仍然保持工业部署可行性。

MixFormer 更进一步。它并不只强调“统一”，而是明确提出 sequence module 与 dense module 之间存在 co-scaling 问题：如果两者始终分离，一侧的扩张将压制另一侧的容量。为此，MixFormer 用 Query Mixer、Cross Attention、Output Fusion 将序列建模与特征交互放入同一个 block，并通过 user-item decoupling 补偿统一模型的在线效率。因此，MixFormer 所推动的是统一主干下的协同扩展。

MDL 则将统一对象从“特征结构”扩展到了“分布结构”。它不仅统一 sequence 与 non-sequence 特征，还将 scenario 与 task 一并 token 化，形成可深入主干多层交互的 domain tokens。这一设计本质上是将 LLM 中 prompt token 的思想迁移到多场景、多任务推荐系统中：场景与任务不再只是浅层条件，而是主干内部真正参与计算的条件信息。它所回答的核心问题是：当 backbone 足够大时，多场景与多任务如何真正调动其参数潜力。

这三篇工作的共同指向非常清晰：推荐系统正在从“多模块拼接”转向“统一主干承载更多结构”，而统一对象也从特征逐步扩展到场景、任务乃至分布本身。

5. TRM、MERGE：输入表征与索引层的同步改写
如果仅关注 backbone，而忽视输入表征与索引层的重构，那么对这一轮推荐系统大模型演进的理解仍然是不完整的。

TRM（Farewell to Item IDs） 的关键意义在于，它提出当 ranking model 持续扩张时，item ID 这种“一物一符号”的输入表示会逐渐成为 scaling 的瓶颈。它的解决思路并不是简单地用现有 semantic token 替换 item ID，而是重新设计同时兼顾语义相似性、行为相关性与细粒度记忆能力的 tokenization 体系，并让 ranker 主干直接基于 semantic tokens 工作。由此，TRM 将“tokenization”从检索侧问题升级为大 ranking model 的输入语言问题。

MERGE 则位于更上游的索引层。它针对 streaming recommendation 中的 item indexing，放弃静态 VQ codebook 的固定形态，使 cluster 能够随流式数据动态生成、重置与合并，从而形成层次化动态索引。MERGE 虽不处于与 RankMixer 相同的层级，但两者共同说明：推荐系统的下一阶段变化，不仅是 backbone 的替换，更包括 item 表示与索引组织方式的系统性重写。

三、外部大厂的最新工作：分别对应哪些方向
如果不将字节跳动之外的大厂工作纳入考察，上述路线图仍然是不完整的。过去一年，外部工业界在若干关键方向上的进展已经非常明确。

1. 阿里：SORT 是判别式大 ranking backbone 的重要对照
阿里的 SORT 是 2026 年最值得关注的工业 ranking 论文之一。它并未走 token mixer 路线，而是将 Transformer 本体系统性地改造成适合电商 ranking 的形态：围绕 request-centric sample organization、local attention、query pruning、generative pre-training，以及 tokenization、MHA、FFN 的整套工程优化，同时解决训练稳定性、可扩展性与硬件效率问题。

SORT 的意义并不只在于线上指标和吞吐改善，更在于它验证了另一条成立的路线：在生成式 one-model 快速升温的背景下，判别式 ranking backbone 依然存在明确且可观的进化空间。 如果 RankMixer 代表“更适合推荐的 Transformer 变体”，那么 SORT 更接近“经过系统改造后仍可成立的 Transformer 本体”。

2. 美团：同时推进统一 foundation model 与生成式推荐
美团近一年的工作具有很强的代表性，因为其同时覆盖了判别式统一 backbone 与生成式推荐两个方向。

MTFM 更接近 foundation model 路线。它面向多场景推荐，不要求严格输入对齐，而是将跨场景数据统一转成 heterogeneous tokens，再用一个 alignment-free backbone 吸收不同业务分布的数据。该工作与字节的 MDL、OneTrans 形成了清晰对照：前者主要解决“不同场景的数据接口如何先统一为 token 接口”。

MTmixAtt 则可视作“受 RankMixer 启发但形成独立路线”的工作。它通过 AutoToken 自动完成 heterogeneous features 到 token 的聚合，再以共享 dense experts 与场景特定 sparse experts 结合的 Multi-Mix Attention block 完成交互。与 RankMixer 相比，它更强调自动 grouping 与多场景自适应。

MTGR 与 UniROM / EGA-V1 则代表美团在生成式推荐与广告 one-model 方向上的持续布局。前者尝试在 generative recommendation 中保留传统 DLRM 体系沉淀下来的 cross features；后者则更进一步，将广告排序重写为端到端生成问题。

美团这一组工作的共同特征在于：并未在“判别式”与“生成式”之间做单线押注，而是同时推进两条路线。

3. 腾讯：生成式广告 one-model 进入结构深融合阶段
腾讯在广告侧的推进速度很快，且技术链条相对完整。

GPR 可视作这一系列工作的起点。它将广告推荐重写为端到端生成问题，提出统一输入 schema、多级 semantic ID、Heterogeneous Hierarchical Decoder，以及由 MTP、VAFT、HEPO 组成的训练链路。其重点并不在于为广告任务简单引入 decoder，而在于系统性处理异构行为、超长序列、多目标价值建模与在线生成效率问题。

OneRanker 则是在 GPR 基础上的进一步推进。它识别出生成与排序之间的三类深层矛盾：兴趣目标与商业价值目标之间的张力、生成过程缺乏 target awareness，以及生成器与排序器之间的信息断裂。为此，OneRanker 引入 task tokens、fake item tokens、ranking decoder、Key/Value pass-through 与 Distribution Consistency loss，试图将 generation 与 ranking 从“阶段串联”推进为“架构级协同”。

这一点具有重要意义，因为广告 one-model 由此不再只是“将多个阶段压缩为一个模型”，而是开始处理兴趣、价值、候选感知与排序约束在同一生成系统中的深度融合。

此外，腾讯在长行为序列广告建模方面也有扎实推进，说明其并未完全放弃判别式路线，而是在广告场景中同时推进序列建模、生成式建模与价值优化。

4. 快手：生成式推荐向平台级体系扩展
快手较为系统地展示了生成式推荐如何从单场景能力演化为平台级技术体系。

OneRec 较早将 retrieve 与 rank 统一为端到端 generative recommender，并在短视频主场景上线后向行业释放出清晰信号：生成式 recommendation 并非只能停留在检索层，而可以进入主排序链路。

随后，这一路线快速向更多业务扩展。

OneLoc 将生成式推荐引入本地生活场景，通过 geo-aware semantic ID、geo-aware self-attention、neighbor-aware prompt 与强化学习的结合，处理兴趣、位置与商业目标的联合优化。

OneMall 则将电商中的商品卡片、短视频与直播分发统一到同一生成式家族框架中，表明 one-model 已不再是单一流量场景中的技巧，而开始向整个平台多分发入口扩张。

GR4AD 是广告侧最值得关注的工作之一。它不仅提出 UA-SID 处理广告内容与业务信号的统一 tokenization，还引入明显围绕在线推理预算设计的 LazyAR 解码结构，再结合价值感知监督与 ranking-guided 偏好优化，使生成式广告推荐成为 architecture、learning、serving 一体化协同设计。

GRank 与 PROMISE 则说明快手并未止步于“训练一个生成模型”，而是在进一步推进检索侧的 generate-rank 框架，以及 inference-time scaling、process reward model 等更靠近推理阶段优化的能力。

快手这一系列工作的共同特征在于：semantic token、生成式建模、强化学习、在线 serving 与多场景统一，已经形成连续演进的体系。

5. 小红书、LinkedIn、Meta、京东：几种不同的工业答案
小红书 给出的两种代表性回答分别是 RankGPT / Towards Large-scale Generative Ranking 与 LASER。前者直接讨论 ranking stage 的 generative ranking 是否成立以及收益来源；后者则将超长行为序列的 I/O 访问与 target-aware segmented attention 结合，代表长序列全栈优化路线。

LinkedIn 的 Feed-SR 说明海外大厂在 feed ranking 中依然高度重视判别式 sequential ranking 的工业落地。它没有急于以通用 LLM 替换现网 ranker，而是选择更稳健的 transformer-based sequential ranker 路线，并围绕 RoPE、incremental training、recency weighting、late fusion 完成工程化。

Meta 提出的 Foundation-Expert Paradigm 更接近一种平台级组织方式。其关注点不只是单模型结构，而是如何训练一个跨 surface、跨模态、长期流数据的中心 foundation model，再将知识高效迁移至 surface-specific experts。它代表的是“中心大模型 + 轻专家部署”的工业组织逻辑。

京东的 OxygenREC 则将 instruction-following 明确引入生成式电商推荐。它并不是在线调用通用大语言模型，而是通过近线 LLM 生成 Contextual Reasoning Instructions，再由线上高吞吐 encoder-decoder 实时解码，将“慢思考”与“快生成”拆分。对于未来电商 recommendation 的体系设计，这一路线具有较高参考价值。

四、综合观察：行业已出现五个明确趋势
趋势一：判别式大 ranking 并未结束，而是进入成熟阶段
一个常见误判是，随着生成式推荐兴起，判别式 ranker 将迅速失去演进空间。工业实践并未支持这一判断。

RankMixer、TokenMixer-Large、MSN、SORT、Feed-SR、MTFM 这一组工作表明，判别式大 ranking 依然存在明确且可持续的技术空间。尤其在强实时、高吞吐、严格时延约束的主链路场景中，判别式 backbone 仍然具备极强的工业竞争力。

真正发生变化的，并不是判别式路线被放弃，而是判别式模型正在越来越像 foundation model：更统一的 token 接口、更深的一体化主干、更明确的 scaling 目标，以及更系统的 serving 优化。

趋势二：生成式 one-model 正在广告、电商与多场景推荐中加速落地
另一条线同样清晰：生成式推荐已经走过仅在 retrieval 试水的阶段，开始进入主排序、广告与电商推荐链路。

OneRec、MTGR、RankGPT、GPR、OneRanker、GR4AD、OxygenREC、OneMall 这一批工作说明，生成式推荐的产业化推进已经不再是 academic prototype，而是在广告、电商与内容分发等高价值场景中形成体系化落地。 尤其广告领域推进更快，因为广告天然面临多目标优化、页面级生成、value alignment 与全局收益优化等问题，而这些问题与生成式框架的建模方式天然契合。

趋势三：semantic token 正在从“表示技巧”上升为“系统级接口”
TRM、MERGE、OneLoc、OneMall、GR4AD、GPR 这批工作实际上都在强调同一个事实：item 不再只是原子化 ID，而正在演化为可组合、可迁移、可生成、可索引的 token 序列。

一旦这一前提成立，许多传统问题都会被重新表述：检索不再只依赖 ANN 索引；排序不再只面对固定 item embedding；多场景推荐可以共享更高层级的 token 空间；推理阶段的 beam search、trie constraint、prefix constraint 也将逐渐成为推荐系统的一部分。

因此，semantic token 的意义已经远超“更有利于冷启动”这一局部优势，而正在成为推荐系统新的基础接口。

趋势四：serving、复用与 inference-time scaling 已成为一等公民
过去的工业论文往往将线上部署放在最后一节作为工程实现说明；当前的情况已经发生变化。

UG-Separation、LASER、GR4AD、PROMISE、OxygenREC 这类工作共同表明：训练阶段的模型创新，如果不能转化为在线可控的计算图、存储访问模式与推理策略，就很难构成真正意义上的工业创新。

进一步看，inference-time scaling 也不再是通用大语言模型独有的话题。beam 设计、path-level reward、dynamic beam serving、用户侧复用、近线 reasoning distillation 等手段，正在将推荐系统的竞争拉向推理阶段。

趋势五：统一化正在从“统一特征”走向“统一分布、统一目标、统一平台”
OneTrans、MixFormer、MDL、MTFM、OneMall、OxygenREC 等工作具有一个高度一致的方向：它们都不再满足于只统一 sequence 与 non-sequence 特征。

当前更激进的目标已经变成：统一特征类型，统一场景分布，统一任务目标，统一训练与部署接口，乃至统一推荐、搜索、广告之间的基础表达。

从这一角度观察，推荐系统的大模型化并不是简单照搬 NLP，而是在形成一套自身特有的 foundation model 逻辑：tokenization、long context、multi-distribution、value alignment、serving co-design、one-model deployment。

五、结论：下一阶段的分水岭，不是参数规模本身，而是“统一接口”的形成速度
未来一到两年内，真正拉开差距的因素，大概率不会只是参数规模本身，而会是三类“统一接口”谁先成形。

第一，是 统一的 token 接口。也即 item、广告、内容、地理、场景、任务等对象，是否能够被映射到更稳定、更可扩展的语义空间中。

第二，是 统一的 backbone 接口。无论是判别式统一 backbone 还是生成式 one-model，核心竞争都在于：究竟由谁来承接 sequence、feature、scenario、task 与 value 这些异质信息。

第三，是 统一的在线推理接口。训练、蒸馏、缓存、复用、beam search、近线 reasoning 之间能否形成闭环，将决定“论文中的大模型”能否转化为“线上可持续迭代的平台能力”。

从这一角度看，RankMixer 之后这批工作的真正价值，并不只是贡献了一组新的模型名词，而是逐步揭示出一个更深层的事实：推荐系统的大模型化，已经从“模型更大”演进到“接口重写”。

结语
近两年的推荐系统论文，如果仅按公司或模型名称阅读，容易显得碎片化；但如果按照“主干扩展、长序列、统一 backbone、semantic token / 生成式 one-model”四条主线重新组织，技术演进脉络实际上相当连贯。

字节跳动这条线的价值在于，它将判别式大 ranking、长序列、多模态、semantic token、多场景学习与 serving 优化串联成了一套相对完整的工业方法论；外部大厂则分别在统一 Transformer、foundation-expert、生成式广告、指令式电商推荐与平台级 generative family 上继续推进这一方法论。

因此，当前真正值得讨论的问题已经不再是“是否应该做推荐系统大模型”，而是：哪一层会最先完成 token 化，哪一段会最先完成统一，哪一块会最先完成生成式重写，以及现有在线系统能否承接这些变化。

参考文献
[1] Zhu, J. et al. RankMixer: A Scalable and Reliable Ranking Model Serving 1 Billion Parameters. arXiv:2507.15551, 2025.

[2] Zhang, Z. et al. OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender. arXiv:2510.26104, 2025.

[3] Jiang, Y. et al. TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders. arXiv:2602.06563, 2026.

[4] Chai, Z. et al. Make It Long, Keep It Fast: Making Ranking Models See More History with Targeted Cross Attention and Request-Level Batching. arXiv:2511.06077, 2025.

[5] Zhou, J. et al. LEMUR: Learning Multi-Modal End-to-End Recommendation with LLMs and Unified Ranking. arXiv:2511.10962, 2025.

[6] Zhou, Y. et al. Farewell to Item IDs: Unlocking the Scaling Potential of Large Ranking Models via Semantic Tokens. arXiv:2601.22694, 2026.

[7] Guo, J. et al. MDL: A Unified Multi-Distribution Learner in Large-scale Industrial Recommendation through Tokenization. arXiv:2602.07520, 2026.

[8] Zhang, H. et al. MixFormer: A Unified Transformer Backbone for Sequence Modeling and Feature Interaction in Industrial Recommendation. arXiv:2602.14110, 2026.

[9] Lu, H. et al. Compute Only Once: UG-Separation for Efficient Large Recommendation Models. arXiv:2602.10455, 2026.

[10] Bai, S. et al. MSN: A Memory-based Sparse Activation Scaling Framework for Large-scale Industrial Recommendation. arXiv:2602.07526, 2026.

[11] Chen, Y. et al. MERGE: Next-Generation Item Indexing Paradigm for Large-Scale Streaming Recommendation. arXiv:2601.20199, 2026.

[12] Wang, C. et al. SORT: A Systematically Optimized Ranking Transformer for Industrial-scale Recommenders. arXiv:2603.03988, 2026.

[13] Song, X. et al. MTFM: A Scalable and Alignment-free Foundation Model for Industrial Recommendation in Meituan. arXiv:2602.11235, 2026.

[14] Qiu, J. et al. One Model to Rank Them All: Unifying Online Advertising with End-to-End Learning. arXiv:2505.19755, 2025.

[15] Han, R. et al. MTGR: Industrial-Scale Generative Recommendation Framework in Meituan. arXiv:2505.18654, 2025.

[16] Zhang, J. et al. GPR: Towards a Generative Pre-trained One-Model Paradigm for Large-Scale Advertising Recommendation. arXiv:2511.10138, 2025.

[17] Sun, D. et al. OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation. arXiv:2603.02999, 2026.

[18] Deng, J. et al. OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment. arXiv:2502.18965, 2025.

[19] Xue, B. et al. Generative Recommendation for Large-Scale Advertising. arXiv:2602.22732, 2026.

[20] Zhang, K. et al. OneMall: One Model, More Scenarios – End-to-End Generative Recommender Family at Kuaishou E-Commerce. arXiv:2601.21770, 2026.

[21] Wei, Z. et al. OneLoc: Geo-Aware Generative Recommender Systems for Local Life Service. arXiv:2508.14646, 2025.

[22] Guo, C. et al. PROMISE: Process Reward Models Unlock Test-Time Scaling Laws in Generative Recommendations. arXiv:2601.04674, 2026.

[23] Sun, Y. et al. GRank: Towards Target-Aware and Streamlined Industrial Retrieval with a Generate-Rank Framework. arXiv:2510.15299, 2025.

[24] Huang, Y. et al. Towards Large-scale Generative Ranking. arXiv:2505.04180, 2025.

[25] Yu, J. et al. LASER: An Efficient Target-Aware Segmented Attention Framework for End-to-End Long Sequence Modeling. arXiv:2602.11562, 2026.

[26] Hertel, L. et al. An Industrial-Scale Sequential Recommender for LinkedIn Feed Ranking. arXiv:2602.12354, 2026.

[27] Li, D. et al. Realizing Scaling Laws in Recommender Systems: A Foundation-Expert Paradigm for Hyperscale Model Deployment. arXiv:2508.02929, 2025.

[28] Hao, X. et al. OxygenREC: An Instruction-Following Generative Framework for E-commerce Recommendation. arXiv:2512.22386, 2025.

[29] Song, J. et al. HoMer: Addressing Heterogeneities by Modeling Sequential and Set-wise Contexts for CTR Prediction. arXiv:2510.11100, 2025.

[30] Wang, Z. et al. MTmixAtt: Integrating Mixture-of-Experts with Multi-Mix Attention for Large-Scale Recommendation. arXiv:2510.15286, 2025.