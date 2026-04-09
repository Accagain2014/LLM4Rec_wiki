---
title: "Generative Recommendation for Large-Scale Advertising"
url: "https://arxiv.org/abs/2602.22732"
original_url: "https://arxiv.org/pdf/2602.22732"
fetched: "2026-04-09"
---

# Generative Recommendation for Large-Scale Advertising

> 来源：https://arxiv.org/abs/2602.22732

Computer Science > Information Retrieval
arXiv:2602.22732
(cs)
[Submitted on 26 Feb 2026 (
v1[^1]
), last revised 2 Apr 2026 (this version, v3)]
Title:
Generative Recommendation for Large-Scale Advertising
Authors:
Ben Xue[^2]
,
Dan Liu[^3]
,
Lixiang Wang[^4]
,
Mingjie Sun[^5]
,
Peng Wang[^6]
,
Pengfei Zhang[^7]
,
Shaoyun Shi[^8]
,
Tianyu Xu[^9]
,
Yunhao Sha[^10]
,
Zhiqiang Liu[^11]
,
Bo Kong[^12]
,
Bo Wang[^13]
,
Hang Yang[^14]
,
Jieting Xue[^15]
,
Junhao Wang[^16]
,
Shengyu Wang[^17]
,
Shuping Hui[^18]
,
Wencai Ye[^19]
,
Xiao Lin[^20]
,
Yongzhi Li[^21]
,
Yuhang Chen[^22]
,
Zhihui Yin[^23]
,
Quan Chen[^24]
,
Shiyang Wen[^25]
,
Wenjin Wu[^26]
,
Han Li[^27]
,
Guorui Zhou[^28]
,
Changcheng Li[^29]
,
Peng Jiang[^30]
,
Kun Gai[^31]
View a PDF of the paper titled Generative Recommendation for Large-Scale Advertising, by Ben Xue and 29 other authors
View PDF[^32]
HTML (experimental)[^33]
Abstract:
Generative recommendation has recently attracted widespread attention in industry due to its potential for scaling and stronger model capacity. However, deploying real-time generative recommendation in large-scale advertising requires designs beyond large-language-model (LLM)-style training and serving recipes. We present a production-oriented generative recommender co-designed across architecture, learning, and serving, named GR4AD (Generative Recommendation for ADdvertising). As for tokenization, GR4AD proposes UA-SID (Unified Advertisement Semantic ID) to capture complicated business information. Furthermore, GR4AD introduces LazyAR, a lazy autoregressive decoder that relaxes layer-wise dependencies for short, multi-candidate generation, preserving effectiveness while reducing inference cost, which facilitates scaling under fixed serving budgets. To align optimization with business value, GR4AD employs VSL (Value-Aware Supervised Learning) and proposes RSPO (Ranking-Guided Softmax Preference Optimization), a ranking-aware, list-wise reinforcement learning algorithm that optimizes value-based rewards under list-level metrics for continual online updates. For online inference, we further propose dynamic beam serving, which adapts beam width across generation levels and online load to control compute. Large-scale online A/B tests show up to 4.2% ad revenue improvement over an existing DLRM-based stack, with consistent gains from both model scaling and inference-time scaling. GR4AD has been fully deployed in Kuaishou advertising system with over 400 million users and achieves high-throughput real-time serving.
Comments:
13 pages, 6 figures, under review
Subjects:
Information Retrieval (cs.IR)
; Machine Learning (cs.LG)
Cite as:
arXiv:2602.22732[^34]
[cs.IR]
(or
arXiv:2602.22732v3[^35]
[cs.IR]
for this version)
https://doi.org/10.48550/arXiv.2602.22732[^36]
arXiv-issued DOI via DataCite
Submission history
From: Shaoyun Shi [
view email[^37]
]
[v1][^38]
Thu, 26 Feb 2026 08:15:26 UTC (1,018 KB)
[v2][^39]
Wed, 4 Mar 2026 09:28:17 UTC (1,017 KB)
[v3]
Thu, 2 Apr 2026 02:38:13 UTC (1,017 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Generative Recommendation for Large-Scale Advertising, by Ben Xue and 29 other authors
View PDF[^40]
HTML (experimental)[^41]
TeX Source[^42]
view license[^43]
Current browse context:
cs.IR
< prev[^44]
|
next >[^45]
new[^46]
|
recent[^47]
|
2026-02[^48]
Change to browse by:
cs[^49]
cs.LG[^50]
References & Citations
NASA ADS[^51]
Google Scholar[^52]
Semantic Scholar[^53]
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
What is the Explorer?[^56]
)
Connected Papers Toggle
Connected Papers
(
What is Connected Papers?[^57]
)
Litmaps Toggle
Litmaps
(
What is Litmaps?[^58]
)
scite.ai Toggle
scite Smart Citations
(
What are Smart Citations?[^59]
)
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv
(
What is alphaXiv?[^60]
)
Links to Code Toggle
CatalyzeX Code Finder for Papers
(
What is CatalyzeX?[^61]
)
DagsHub Toggle
DagsHub
(
What is DagsHub?[^62]
)
GotitPub Toggle
Gotit.pub
(
What is GotitPub?[^63]
)
Huggingface Toggle
Hugging Face
(
What is Huggingface?[^64]
)
ScienceCast Toggle
ScienceCast
(
What is ScienceCast?[^65]
)
Demos
Demos
Replicate Toggle
Replicate
(
What is Replicate?[^66]
)
Spaces Toggle
Hugging Face Spaces
(
What is Spaces?[^67]
)
Spaces Toggle
TXYZ.AI
(
What is TXYZ.AI?[^68]
)
Related Papers
Recommenders and Search Tools
Link to Influence Flower
Influence Flower
(
What are Influence Flowers?[^69]
)
Core recommender toggle
CORE Recommender
(
What is CORE?[^70]
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
Learn more about arXivLabs[^71]
.
Which authors of this paper are endorsers?[^72]
|
Disable MathJax[^73]
(
What is MathJax?[^74]
)

---
## 页面链接
[1] v1: https://arxiv.org/abs/2602.22732v1
[2] Ben Xue: https://arxiv.org/search/cs?searchtype=author&query=Xue,+B
[3] Dan Liu: https://arxiv.org/search/cs?searchtype=author&query=Liu,+D
[4] Lixiang Wang: https://arxiv.org/search/cs?searchtype=author&query=Wang,+L
[5] Mingjie Sun: https://arxiv.org/search/cs?searchtype=author&query=Sun,+M
[6] Peng Wang: https://arxiv.org/search/cs?searchtype=author&query=Wang,+P
[7] Pengfei Zhang: https://arxiv.org/search/cs?searchtype=author&query=Zhang,+P
[8] Shaoyun Shi: https://arxiv.org/search/cs?searchtype=author&query=Shi,+S
[9] Tianyu Xu: https://arxiv.org/search/cs?searchtype=author&query=Xu,+T
[10] Yunhao Sha: https://arxiv.org/search/cs?searchtype=author&query=Sha,+Y
[11] Zhiqiang Liu: https://arxiv.org/search/cs?searchtype=author&query=Liu,+Z
[12] Bo Kong: https://arxiv.org/search/cs?searchtype=author&query=Kong,+B
[13] Bo Wang: https://arxiv.org/search/cs?searchtype=author&query=Wang,+B
[14] Hang Yang: https://arxiv.org/search/cs?searchtype=author&query=Yang,+H
[15] Jieting Xue: https://arxiv.org/search/cs?searchtype=author&query=Xue,+J
[16] Junhao Wang: https://arxiv.org/search/cs?searchtype=author&query=Wang,+J
[17] Shengyu Wang: https://arxiv.org/search/cs?searchtype=author&query=Wang,+S
[18] Shuping Hui: https://arxiv.org/search/cs?searchtype=author&query=Hui,+S
[19] Wencai Ye: https://arxiv.org/search/cs?searchtype=author&query=Ye,+W
[20] Xiao Lin: https://arxiv.org/search/cs?searchtype=author&query=Lin,+X
[21] Yongzhi Li: https://arxiv.org/search/cs?searchtype=author&query=Li,+Y
[22] Yuhang Chen: https://arxiv.org/search/cs?searchtype=author&query=Chen,+Y
[23] Zhihui Yin: https://arxiv.org/search/cs?searchtype=author&query=Yin,+Z
[24] Quan Chen: https://arxiv.org/search/cs?searchtype=author&query=Chen,+Q
[25] Shiyang Wen: https://arxiv.org/search/cs?searchtype=author&query=Wen,+S
[26] Wenjin Wu: https://arxiv.org/search/cs?searchtype=author&query=Wu,+W
[27] Han Li: https://arxiv.org/search/cs?searchtype=author&query=Li,+H
[28] Guorui Zhou: https://arxiv.org/search/cs?searchtype=author&query=Zhou,+G
[29] Changcheng Li: https://arxiv.org/search/cs?searchtype=author&query=Li,+C
[30] Peng Jiang: https://arxiv.org/search/cs?searchtype=author&query=Jiang,+P
[31] Kun Gai: https://arxiv.org/search/cs?searchtype=author&query=Gai,+K
[32] View PDF: /pdf/2602.22732
[33] HTML (experimental): https://arxiv.org/html/2602.22732v3
[34] arXiv:2602.22732: https://arxiv.org/abs/2602.22732
[35] arXiv:2602.22732v3: https://arxiv.org/abs/2602.22732v3
[36] https://doi.org/10.48550/arXiv.2602.22732: https://doi.org/10.48550/arXiv.2602.22732
[37] view email: /show-email/a14e8e62/2602.22732
[38] [v1]: /abs/2602.22732v1
[39] [v2]: /abs/2602.22732v2
[40] View PDF: /pdf/2602.22732
[41] HTML (experimental): https://arxiv.org/html/2602.22732v3
[42] TeX Source: /src/2602.22732
[43] view license: http://arxiv.org/licenses/nonexclusive-distrib/1.0/
[44] < prev: /prevnext?id=2602.22732&function=prev&context=cs.IR
[45] next >: /prevnext?id=2602.22732&function=next&context=cs.IR
[46] new: /list/cs.IR/new
[47] recent: /list/cs.IR/recent
[48] 2026-02: /list/cs.IR/2026-02
[49] cs: /abs/2602.22732?context=cs
[50] cs.LG: /abs/2602.22732?context=cs.LG
[51] NASA ADS: https://ui.adsabs.harvard.edu/abs/arXiv:2602.22732
[52] Google Scholar: https://scholar.google.com/scholar_lookup?arxiv_id=2602.22732
[53] Semantic Scholar: https://api.semanticscholar.org/arXiv:2602.22732
[56] What is the Explorer?: https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer
[57] What is Connected Papers?: https://www.connectedpapers.com/about
[58] What is Litmaps?: https://www.litmaps.co/
[59] What are Smart Citations?: https://www.scite.ai/
[60] What is alphaXiv?: https://alphaxiv.org/
[61] What is CatalyzeX?: https://www.catalyzex.com
[62] What is DagsHub?: https://dagshub.com/
[63] What is GotitPub?: http://gotit.pub/faq
[64] What is Huggingface?: https://huggingface.co/huggingface
[65] What is ScienceCast?: https://sciencecast.org/welcome
[66] What is Replicate?: https://replicate.com/docs/arxiv/about
[67] What is Spaces?: https://huggingface.co/docs/hub/spaces
[68] What is TXYZ.AI?: https://txyz.ai
[69] What are Influence Flowers?: https://influencemap.cmlab.dev/
[70] What is CORE?: https://core.ac.uk/services/recommender
[71] Learn more about arXivLabs: https://info.arxiv.org/labs/index.html
[72] Which authors of this paper are endorsers?: /auth/show-endorsers/2602.22732
[73] Disable MathJax: javascript:setMathjaxCookie()
[74] What is MathJax?: https://info.arxiv.org/help/mathjax.html