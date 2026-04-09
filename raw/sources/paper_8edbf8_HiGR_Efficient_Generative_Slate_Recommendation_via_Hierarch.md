---
title: "HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning and Multi-Objective Preference Alignment"
url: "https://arxiv.org/abs/2512.24787"
original_url: "https://arxiv.org/pdf/2512.24787"
fetched: "2026-04-08"
---

# HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning and Multi-Objective Preference Alignment

> 来源：https://arxiv.org/abs/2512.24787

Computer Science > Information Retrieval
arXiv:2512.24787
(cs)
[Submitted on 31 Dec 2025 (
v1[^1]
), last revised 23 Feb 2026 (this version, v2)]
Title:
HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning and Multi-Objective Preference Alignment
Authors:
Yunsheng Pang[^2]
,
Zijian Liu[^3]
,
Yudong Li[^4]
,
Shaojie Zhu[^5]
,
Zijian Luo[^6]
,
Chenyun Yu[^7]
,
Sikai Wu[^8]
,
Shichen Shen[^9]
,
Cong Xu[^10]
,
Bin Wang[^11]
,
Kai Jiang[^12]
,
Hongyong Yu[^13]
,
Chengxiang Zhuo[^14]
,
Zang Li[^15]
View a PDF of the paper titled HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning and Multi-Objective Preference Alignment, by Yunsheng Pang and 13 other authors
View PDF[^16]
HTML (experimental)[^17]
Abstract:
Slate recommendation, which presents users with a ranked item list in a single display, is ubiquitous across mainstream online platforms. Recent advances in generative models have shown significant potential for this task via autoregressive modeling of discrete semantic ID sequences. However, existing methods suffer from three key limitations: entangled item tokenization, inefficient sequential decoding, and the absence of holistic slate planning. These issues often result in substantial inference overhead and inadequate alignment with diverse user preferences and practical business requirements, hindering the industrial deployment of generative slate recommendation systems. In this paper, we propose HiGR, an efficient generative slate recommendation framework that integrates hierarchical planning with listwise preference alignment. First, we design an auto-encoder incorporating residual quantization and contrastive constraints, which tokenizes items into semantically structured IDs to enable controllable generation. Second, HiGR decouples the generation process into two stages: a list-level planning stage to capture global slate intent, and an item-level decoding stage to select specific items, effectively reducing the search space and enabling efficient generation. Third, we introduce a multi-objective and listwise preference alignment mechanism that enhances slate quality by leveraging implicit user feedback. Extensive experiments have validated the effectiveness of our HiGR method. Notably, it outperforms state-of-the-art baselines by over 10\% in offline recommendation quality while achieving a $5\times$ inference speedup. Furthermore, we have deployed HiGR on a commercial platform under Tencent (serving hundreds of millions of users), and online A/B tests show that it increases average watch time and average video plays by 1.22\% and 1.73\%, respectively.
Subjects:
Information Retrieval (cs.IR)
; Artificial Intelligence (cs.AI)
Cite as:
arXiv:2512.24787[^18]
[cs.IR]
(or
arXiv:2512.24787v2[^19]
[cs.IR]
for this version)
https://doi.org/10.48550/arXiv.2512.24787[^20]
arXiv-issued DOI via DataCite
Submission history
From: Zijian Liu [
view email[^21]
]
[v1][^22]
Wed, 31 Dec 2025 11:16:24 UTC (416 KB)
[v2]
Mon, 23 Feb 2026 23:54:28 UTC (428 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning and Multi-Objective Preference Alignment, by Yunsheng Pang and 13 other authors
View PDF[^23]
HTML (experimental)[^24]
TeX Source[^25]
view license[^26]
Current browse context:
cs.IR
< prev[^27]
|
next >[^28]
new[^29]
|
recent[^30]
|
2025-12[^31]
Change to browse by:
cs[^32]
cs.AI[^33]
References & Citations
NASA ADS[^34]
Google Scholar[^35]
Semantic Scholar[^36]
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
What is the Explorer?[^39]
)
Connected Papers Toggle
Connected Papers
(
What is Connected Papers?[^40]
)
Litmaps Toggle
Litmaps
(
What is Litmaps?[^41]
)
scite.ai Toggle
scite Smart Citations
(
What are Smart Citations?[^42]
)
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv
(
What is alphaXiv?[^43]
)
Links to Code Toggle
CatalyzeX Code Finder for Papers
(
What is CatalyzeX?[^44]
)
DagsHub Toggle
DagsHub
(
What is DagsHub?[^45]
)
GotitPub Toggle
Gotit.pub
(
What is GotitPub?[^46]
)
Huggingface Toggle
Hugging Face
(
What is Huggingface?[^47]
)
Links to Code Toggle
Papers with Code
(
What is Papers with Code?[^48]
)
ScienceCast Toggle
ScienceCast
(
What is ScienceCast?[^49]
)
Demos
Demos
Replicate Toggle
Replicate
(
What is Replicate?[^50]
)
Spaces Toggle
Hugging Face Spaces
(
What is Spaces?[^51]
)
Spaces Toggle
TXYZ.AI
(
What is TXYZ.AI?[^52]
)
Related Papers
Recommenders and Search Tools
Link to Influence Flower
Influence Flower
(
What are Influence Flowers?[^53]
)
Core recommender toggle
CORE Recommender
(
What is CORE?[^54]
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
Learn more about arXivLabs[^55]
.
Which authors of this paper are endorsers?[^56]
|
Disable MathJax[^57]
(
What is MathJax?[^58]
)

---
## 页面链接
[1] v1: https://arxiv.org/abs/2512.24787v1
[2] Yunsheng Pang: https://arxiv.org/search/cs?searchtype=author&query=Pang,+Y
[3] Zijian Liu: https://arxiv.org/search/cs?searchtype=author&query=Liu,+Z
[4] Yudong Li: https://arxiv.org/search/cs?searchtype=author&query=Li,+Y
[5] Shaojie Zhu: https://arxiv.org/search/cs?searchtype=author&query=Zhu,+S
[6] Zijian Luo: https://arxiv.org/search/cs?searchtype=author&query=Luo,+Z
[7] Chenyun Yu: https://arxiv.org/search/cs?searchtype=author&query=Yu,+C
[8] Sikai Wu: https://arxiv.org/search/cs?searchtype=author&query=Wu,+S
[9] Shichen Shen: https://arxiv.org/search/cs?searchtype=author&query=Shen,+S
[10] Cong Xu: https://arxiv.org/search/cs?searchtype=author&query=Xu,+C
[11] Bin Wang: https://arxiv.org/search/cs?searchtype=author&query=Wang,+B
[12] Kai Jiang: https://arxiv.org/search/cs?searchtype=author&query=Jiang,+K
[13] Hongyong Yu: https://arxiv.org/search/cs?searchtype=author&query=Yu,+H
[14] Chengxiang Zhuo: https://arxiv.org/search/cs?searchtype=author&query=Zhuo,+C
[15] Zang Li: https://arxiv.org/search/cs?searchtype=author&query=Li,+Z
[16] View PDF: /pdf/2512.24787
[17] HTML (experimental): https://arxiv.org/html/2512.24787v2
[18] arXiv:2512.24787: https://arxiv.org/abs/2512.24787
[19] arXiv:2512.24787v2: https://arxiv.org/abs/2512.24787v2
[20] https://doi.org/10.48550/arXiv.2512.24787: https://doi.org/10.48550/arXiv.2512.24787
[21] view email: /show-email/0400624c/2512.24787
[22] [v1]: /abs/2512.24787v1
[23] View PDF: /pdf/2512.24787
[24] HTML (experimental): https://arxiv.org/html/2512.24787v2
[25] TeX Source: /src/2512.24787
[26] view license: http://creativecommons.org/licenses/by/4.0/
[27] < prev: /prevnext?id=2512.24787&function=prev&context=cs.IR
[28] next >: /prevnext?id=2512.24787&function=next&context=cs.IR
[29] new: /list/cs.IR/new
[30] recent: /list/cs.IR/recent
[31] 2025-12: /list/cs.IR/2025-12
[32] cs: /abs/2512.24787?context=cs
[33] cs.AI: /abs/2512.24787?context=cs.AI
[34] NASA ADS: https://ui.adsabs.harvard.edu/abs/arXiv:2512.24787
[35] Google Scholar: https://scholar.google.com/scholar_lookup?arxiv_id=2512.24787
[36] Semantic Scholar: https://api.semanticscholar.org/arXiv:2512.24787
[39] What is the Explorer?: https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer
[40] What is Connected Papers?: https://www.connectedpapers.com/about
[41] What is Litmaps?: https://www.litmaps.co/
[42] What are Smart Citations?: https://www.scite.ai/
[43] What is alphaXiv?: https://alphaxiv.org/
[44] What is CatalyzeX?: https://www.catalyzex.com
[45] What is DagsHub?: https://dagshub.com/
[46] What is GotitPub?: http://gotit.pub/faq
[47] What is Huggingface?: https://huggingface.co/huggingface
[48] What is Papers with Code?: https://paperswithcode.com/
[49] What is ScienceCast?: https://sciencecast.org/welcome
[50] What is Replicate?: https://replicate.com/docs/arxiv/about
[51] What is Spaces?: https://huggingface.co/docs/hub/spaces
[52] What is TXYZ.AI?: https://txyz.ai
[53] What are Influence Flowers?: https://influencemap.cmlab.dev/
[54] What is CORE?: https://core.ac.uk/services/recommender
[55] Learn more about arXivLabs: https://info.arxiv.org/labs/index.html
[56] Which authors of this paper are endorsers?: /auth/show-endorsers/2512.24787
[57] Disable MathJax: javascript:setMathjaxCookie()
[58] What is MathJax?: https://info.arxiv.org/help/mathjax.html