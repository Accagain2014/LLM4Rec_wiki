---
title: "RankMixer: Scaling Up Ranking Models in Industrial Recommenders"
url: "https://arxiv.org/abs/2507.15551"
original_url: "https://arxiv.org/pdf/2507.15551"
fetched: "2026-04-09"
---

# RankMixer: Scaling Up Ranking Models in Industrial Recommenders

> 来源：https://arxiv.org/abs/2507.15551

Computer Science > Information Retrieval
arXiv:2507.15551
(cs)
[Submitted on 21 Jul 2025 (
v1[^1]
), last revised 26 Jul 2025 (this version, v3)]
Title:
RankMixer: Scaling Up Ranking Models in Industrial Recommenders
Authors:
Jie Zhu[^2]
,
Zhifang Fan[^3]
,
Xiaoxie Zhu[^4]
,
Yuchen Jiang[^5]
,
Hangyu Wang[^6]
,
Xintian Han[^7]
,
Haoran Ding[^8]
,
Xinmin Wang[^9]
,
Wenlin Zhao[^10]
,
Zhen Gong[^11]
,
Huizhi Yang[^12]
,
Zheng Chai[^13]
,
Zhe Chen[^14]
,
Yuchao Zheng[^15]
,
Qiwei Chen[^16]
,
Feng Zhang[^17]
,
Xun Zhou[^18]
,
Peng Xu[^19]
,
Xiao Yang[^20]
,
Di Wu[^21]
,
Zuotao Liu[^22]
View a PDF of the paper titled RankMixer: Scaling Up Ranking Models in Industrial Recommenders, by Jie Zhu and 20 other authors
View PDF[^23]
HTML (experimental)[^24]
Abstract:
Recent progress on large language models (LLMs) has spurred interest in scaling up recommendation systems, yet two practical obstacles remain. First, training and serving cost on industrial Recommenders must respect strict latency bounds and high QPS demands. Second, most human-designed feature-crossing modules in ranking models were inherited from the CPU era and fail to exploit modern GPUs, resulting in low Model Flops Utilization (MFU) and poor scalability. We introduce RankMixer, a hardware-aware model design tailored towards a unified and scalable feature-interaction architecture. RankMixer retains the transformer's high parallelism while replacing quadratic self-attention with multi-head token mixing module for higher efficiency. Besides, RankMixer maintains both the modeling for distinct feature subspaces and cross-feature-space interactions with Per-token FFNs. We further extend it to one billion parameters with a Sparse-MoE variant for higher ROI. A dynamic routing strategy is adapted to address the inadequacy and imbalance of experts training. Experiments show RankMixer's superior scaling abilities on a trillion-scale production dataset. By replacing previously diverse handcrafted low-MFU modules with RankMixer, we boost the model MFU from 4.5\% to 45\%, and scale our ranking model parameters by 100x while maintaining roughly the same inference latency. We verify RankMixer's universality with online A/B tests across two core application scenarios (Recommendation and Advertisement). Finally, we launch 1B Dense-Parameters RankMixer for full traffic serving without increasing the serving cost, which improves user active days by 0.3\% and total in-app usage duration by 1.08\%.
Subjects:
Information Retrieval (cs.IR)
Cite as:
arXiv:2507.15551[^25]
[cs.IR]
(or
arXiv:2507.15551v3[^26]
[cs.IR]
for this version)
https://doi.org/10.48550/arXiv.2507.15551[^27]
arXiv-issued DOI via DataCite
Submission history
From: Yuchen Jiang [
view email[^28]
]
[v1][^29]
Mon, 21 Jul 2025 12:28:55 UTC (607 KB)
[v2][^30]
Thu, 24 Jul 2025 16:19:32 UTC (607 KB)
[v3]
Sat, 26 Jul 2025 02:01:33 UTC (606 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled RankMixer: Scaling Up Ranking Models in Industrial Recommenders, by Jie Zhu and 20 other authors
View PDF[^31]
HTML (experimental)[^32]
TeX Source[^33]
view license[^34]
Current browse context:
cs.IR
< prev[^35]
|
next >[^36]
new[^37]
|
recent[^38]
|
2025-07[^39]
Change to browse by:
cs[^40]
References & Citations
NASA ADS[^41]
Google Scholar[^42]
Semantic Scholar[^43]
export BibTeX citation
Loading...
BibTeX formatted citation
×
loading...
Data provided by:
Bookmark
![BibSonomy logo](https://arxiv.org/static/browse/0.3.4/images/icons/social/bibsonomy.png)
![Reddit logo](https://arxiv.org/static/browse/0.3.4/images/icons/social/reddit.png)
Bibliographic Tools
Bibliographic and Citation Tools
Bibliographic Explorer Toggle
Bibliographic Explorer
(
What is the Explorer?[^46]
)
Connected Papers Toggle
Connected Papers
(
What is Connected Papers?[^47]
)
Litmaps Toggle
Litmaps
(
What is Litmaps?[^48]
)
scite.ai Toggle
scite Smart Citations
(
What are Smart Citations?[^49]
)
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv
(
What is alphaXiv?[^50]
)
Links to Code Toggle
CatalyzeX Code Finder for Papers
(
What is CatalyzeX?[^51]
)
DagsHub Toggle
DagsHub
(
What is DagsHub?[^52]
)
GotitPub Toggle
Gotit.pub
(
What is GotitPub?[^53]
)
Huggingface Toggle
Hugging Face
(
What is Huggingface?[^54]
)
Links to Code Toggle
Papers with Code
(
What is Papers with Code?[^55]
)
ScienceCast Toggle
ScienceCast
(
What is ScienceCast?[^56]
)
Demos
Demos
Replicate Toggle
Replicate
(
What is Replicate?[^57]
)
Spaces Toggle
Hugging Face Spaces
(
What is Spaces?[^58]
)
Spaces Toggle
TXYZ.AI
(
What is TXYZ.AI?[^59]
)
Related Papers
Recommenders and Search Tools
Link to Influence Flower
Influence Flower
(
What are Influence Flowers?[^60]
)
Core recommender toggle
CORE Recommender
(
What is CORE?[^61]
)
Author
Venue
Institution
Topic
About arXivLabs
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community?
Learn more about arXivLabs[^62]
.
Which authors of this paper are endorsers?[^63]
|
Disable MathJax[^64]
(
What is MathJax?[^65]
)

---
## 页面链接
[1] v1: https://arxiv.org/abs/2507.15551v1
[2] Jie Zhu: https://arxiv.org/search/cs?searchtype=author&query=Zhu,+J
[3] Zhifang Fan: https://arxiv.org/search/cs?searchtype=author&query=Fan,+Z
[4] Xiaoxie Zhu: https://arxiv.org/search/cs?searchtype=author&query=Zhu,+X
[5] Yuchen Jiang: https://arxiv.org/search/cs?searchtype=author&query=Jiang,+Y
[6] Hangyu Wang: https://arxiv.org/search/cs?searchtype=author&query=Wang,+H
[7] Xintian Han: https://arxiv.org/search/cs?searchtype=author&query=Han,+X
[8] Haoran Ding: https://arxiv.org/search/cs?searchtype=author&query=Ding,+H
[9] Xinmin Wang: https://arxiv.org/search/cs?searchtype=author&query=Wang,+X
[10] Wenlin Zhao: https://arxiv.org/search/cs?searchtype=author&query=Zhao,+W
[11] Zhen Gong: https://arxiv.org/search/cs?searchtype=author&query=Gong,+Z
[12] Huizhi Yang: https://arxiv.org/search/cs?searchtype=author&query=Yang,+H
[13] Zheng Chai: https://arxiv.org/search/cs?searchtype=author&query=Chai,+Z
[14] Zhe Chen: https://arxiv.org/search/cs?searchtype=author&query=Chen,+Z
[15] Yuchao Zheng: https://arxiv.org/search/cs?searchtype=author&query=Zheng,+Y
[16] Qiwei Chen: https://arxiv.org/search/cs?searchtype=author&query=Chen,+Q
[17] Feng Zhang: https://arxiv.org/search/cs?searchtype=author&query=Zhang,+F
[18] Xun Zhou: https://arxiv.org/search/cs?searchtype=author&query=Zhou,+X
[19] Peng Xu: https://arxiv.org/search/cs?searchtype=author&query=Xu,+P
[20] Xiao Yang: https://arxiv.org/search/cs?searchtype=author&query=Yang,+X
[21] Di Wu: https://arxiv.org/search/cs?searchtype=author&query=Wu,+D
[22] Zuotao Liu: https://arxiv.org/search/cs?searchtype=author&query=Liu,+Z
[23] View PDF: /pdf/2507.15551
[24] HTML (experimental): https://arxiv.org/html/2507.15551v3
[25] arXiv:2507.15551: https://arxiv.org/abs/2507.15551
[26] arXiv:2507.15551v3: https://arxiv.org/abs/2507.15551v3
[27] https://doi.org/10.48550/arXiv.2507.15551: https://doi.org/10.48550/arXiv.2507.15551
[28] view email: /show-email/66fe6c64/2507.15551
[29] [v1]: /abs/2507.15551v1
[30] [v2]: /abs/2507.15551v2
[31] View PDF: /pdf/2507.15551
[32] HTML (experimental): https://arxiv.org/html/2507.15551v3
[33] TeX Source: /src/2507.15551
[34] view license: http://arxiv.org/licenses/nonexclusive-distrib/1.0/
[35] < prev: /prevnext?id=2507.15551&function=prev&context=cs.IR
[36] next >: /prevnext?id=2507.15551&function=next&context=cs.IR
[37] new: /list/cs.IR/new
[38] recent: /list/cs.IR/recent
[39] 2025-07: /list/cs.IR/2025-07
[40] cs: /abs/2507.15551?context=cs
[41] NASA ADS: https://ui.adsabs.harvard.edu/abs/arXiv:2507.15551
[42] Google Scholar: https://scholar.google.com/scholar_lookup?arxiv_id=2507.15551
[43] Semantic Scholar: https://api.semanticscholar.org/arXiv:2507.15551
[46] What is the Explorer?: https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer
[47] What is Connected Papers?: https://www.connectedpapers.com/about
[48] What is Litmaps?: https://www.litmaps.co/
[49] What are Smart Citations?: https://www.scite.ai/
[50] What is alphaXiv?: https://alphaxiv.org/
[51] What is CatalyzeX?: https://www.catalyzex.com
[52] What is DagsHub?: https://dagshub.com/
[53] What is GotitPub?: http://gotit.pub/faq
[54] What is Huggingface?: https://huggingface.co/huggingface
[55] What is Papers with Code?: https://paperswithcode.com/
[56] What is ScienceCast?: https://sciencecast.org/welcome
[57] What is Replicate?: https://replicate.com/docs/arxiv/about
[58] What is Spaces?: https://huggingface.co/docs/hub/spaces
[59] What is TXYZ.AI?: https://txyz.ai
[60] What are Influence Flowers?: https://influencemap.cmlab.dev/
[61] What is CORE?: https://core.ac.uk/services/recommender
[62] Learn more about arXivLabs: https://info.arxiv.org/labs/index.html
[63] Which authors of this paper are endorsers?: /auth/show-endorsers/2507.15551
[64] Disable MathJax: javascript:setMathjaxCookie()
[65] What is MathJax?: https://info.arxiv.org/help/mathjax.html