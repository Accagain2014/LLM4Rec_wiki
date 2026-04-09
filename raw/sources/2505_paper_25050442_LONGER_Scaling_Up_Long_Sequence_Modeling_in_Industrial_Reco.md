---
title: "LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders"
url: "https://arxiv.org/abs/2505.04421"
original_url: "https://arxiv.org/pdf/2505.04421"
fetched: "2026-04-09"
---

# LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders

> 来源：https://arxiv.org/abs/2505.04421

Computer Science > Information Retrieval
arXiv:2505.04421
(cs)
[Submitted on 7 May 2025 (
v1[^1]
), last revised 18 Jul 2025 (this version, v2)]
Title:
LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders
Authors:
Zheng Chai[^2]
,
Qin Ren[^3]
,
Xijun Xiao[^4]
,
Huizhi Yang[^5]
,
Bo Han[^6]
,
Sijun Zhang[^7]
,
Di Chen[^8]
,
Hui Lu[^9]
,
Wenlin Zhao[^10]
,
Lele Yu[^11]
,
Xionghang Xie[^12]
,
Shiru Ren[^13]
,
Xiang Sun[^14]
,
Yaocheng Tan[^15]
,
Peng Xu[^16]
,
Yuchao Zheng[^17]
,
Di Wu[^18]
View a PDF of the paper titled LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders, by Zheng Chai and 16 other authors
View PDF[^19]
HTML (experimental)[^20]
Abstract:
Modeling ultra-long user behavior sequences is critical for capturing both long- and short-term preferences in industrial recommender systems. Existing solutions typically rely on two-stage retrieval or indirect modeling paradigms, incuring upstream-downstream inconsistency and computational inefficiency. In this paper, we present LONGER, a Long-sequence Optimized traNsformer for GPU-Efficient Recommenders. LONGER incorporates (i) a global token mechanism for stabilizing attention over long contexts, (ii) a token merge module with lightweight InnerTransformers and hybrid attention strategy to reduce quadratic complexity, and (iii) a series of engineering optimizations, including training with mixed-precision and activation recomputation, KV cache serving, and the fully synchronous model training and serving framework for unified GPU-based dense and sparse parameter updates. LONGER consistently outperforms strong baselines in both offline metrics and online A/B testing in both advertising and e-commerce services at ByteDance, validating its consistent effectiveness and industrial-level scaling laws. Currently, LONGER has been fully deployed at more than 10 influential scenarios at ByteDance, serving billion users.
Subjects:
Information Retrieval (cs.IR)
Cite as:
arXiv:2505.04421[^21]
[cs.IR]
(or
arXiv:2505.04421v2[^22]
[cs.IR]
for this version)
https://doi.org/10.48550/arXiv.2505.04421[^23]
arXiv-issued DOI via DataCite
Journal reference:
Proceedings of the Nineteenth ACM Conference on Recommender Systems (RecSys '25), September 22--26, 2025, Prague, Czech Republic
Submission history
From: Zheng Chai [
view email[^24]
]
[v1][^25]
Wed, 7 May 2025 13:54:26 UTC (2,242 KB)
[v2]
Fri, 18 Jul 2025 13:29:47 UTC (423 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders, by Zheng Chai and 16 other authors
View PDF[^26]
HTML (experimental)[^27]
TeX Source[^28]
view license[^29]
Current browse context:
cs.IR
< prev[^30]
|
next >[^31]
new[^32]
|
recent[^33]
|
2025-05[^34]
Change to browse by:
cs[^35]
References & Citations
NASA ADS[^36]
Google Scholar[^37]
Semantic Scholar[^38]
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
What is the Explorer?[^41]
)
Connected Papers Toggle
Connected Papers
(
What is Connected Papers?[^42]
)
Litmaps Toggle
Litmaps
(
What is Litmaps?[^43]
)
scite.ai Toggle
scite Smart Citations
(
What are Smart Citations?[^44]
)
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv
(
What is alphaXiv?[^45]
)
Links to Code Toggle
CatalyzeX Code Finder for Papers
(
What is CatalyzeX?[^46]
)
DagsHub Toggle
DagsHub
(
What is DagsHub?[^47]
)
GotitPub Toggle
Gotit.pub
(
What is GotitPub?[^48]
)
Huggingface Toggle
Hugging Face
(
What is Huggingface?[^49]
)
Links to Code Toggle
Papers with Code
(
What is Papers with Code?[^50]
)
ScienceCast Toggle
ScienceCast
(
What is ScienceCast?[^51]
)
Demos
Demos
Replicate Toggle
Replicate
(
What is Replicate?[^52]
)
Spaces Toggle
Hugging Face Spaces
(
What is Spaces?[^53]
)
Spaces Toggle
TXYZ.AI
(
What is TXYZ.AI?[^54]
)
Related Papers
Recommenders and Search Tools
Link to Influence Flower
Influence Flower
(
What are Influence Flowers?[^55]
)
Core recommender toggle
CORE Recommender
(
What is CORE?[^56]
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
Learn more about arXivLabs[^57]
.
Which authors of this paper are endorsers?[^58]
|
Disable MathJax[^59]
(
What is MathJax?[^60]
)

---
## 页面链接
[1] v1: https://arxiv.org/abs/2505.04421v1
[2] Zheng Chai: https://arxiv.org/search/cs?searchtype=author&query=Chai,+Z
[3] Qin Ren: https://arxiv.org/search/cs?searchtype=author&query=Ren,+Q
[4] Xijun Xiao: https://arxiv.org/search/cs?searchtype=author&query=Xiao,+X
[5] Huizhi Yang: https://arxiv.org/search/cs?searchtype=author&query=Yang,+H
[6] Bo Han: https://arxiv.org/search/cs?searchtype=author&query=Han,+B
[7] Sijun Zhang: https://arxiv.org/search/cs?searchtype=author&query=Zhang,+S
[8] Di Chen: https://arxiv.org/search/cs?searchtype=author&query=Chen,+D
[9] Hui Lu: https://arxiv.org/search/cs?searchtype=author&query=Lu,+H
[10] Wenlin Zhao: https://arxiv.org/search/cs?searchtype=author&query=Zhao,+W
[11] Lele Yu: https://arxiv.org/search/cs?searchtype=author&query=Yu,+L
[12] Xionghang Xie: https://arxiv.org/search/cs?searchtype=author&query=Xie,+X
[13] Shiru Ren: https://arxiv.org/search/cs?searchtype=author&query=Ren,+S
[14] Xiang Sun: https://arxiv.org/search/cs?searchtype=author&query=Sun,+X
[15] Yaocheng Tan: https://arxiv.org/search/cs?searchtype=author&query=Tan,+Y
[16] Peng Xu: https://arxiv.org/search/cs?searchtype=author&query=Xu,+P
[17] Yuchao Zheng: https://arxiv.org/search/cs?searchtype=author&query=Zheng,+Y
[18] Di Wu: https://arxiv.org/search/cs?searchtype=author&query=Wu,+D
[19] View PDF: /pdf/2505.04421
[20] HTML (experimental): https://arxiv.org/html/2505.04421v2
[21] arXiv:2505.04421: https://arxiv.org/abs/2505.04421
[22] arXiv:2505.04421v2: https://arxiv.org/abs/2505.04421v2
[23] https://doi.org/10.48550/arXiv.2505.04421: https://doi.org/10.48550/arXiv.2505.04421
[24] view email: /show-email/8372fee5/2505.04421
[25] [v1]: /abs/2505.04421v1
[26] View PDF: /pdf/2505.04421
[27] HTML (experimental): https://arxiv.org/html/2505.04421v2
[28] TeX Source: /src/2505.04421
[29] view license: http://arxiv.org/licenses/nonexclusive-distrib/1.0/
[30] < prev: /prevnext?id=2505.04421&function=prev&context=cs.IR
[31] next >: /prevnext?id=2505.04421&function=next&context=cs.IR
[32] new: /list/cs.IR/new
[33] recent: /list/cs.IR/recent
[34] 2025-05: /list/cs.IR/2025-05
[35] cs: /abs/2505.04421?context=cs
[36] NASA ADS: https://ui.adsabs.harvard.edu/abs/arXiv:2505.04421
[37] Google Scholar: https://scholar.google.com/scholar_lookup?arxiv_id=2505.04421
[38] Semantic Scholar: https://api.semanticscholar.org/arXiv:2505.04421
[41] What is the Explorer?: https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer
[42] What is Connected Papers?: https://www.connectedpapers.com/about
[43] What is Litmaps?: https://www.litmaps.co/
[44] What are Smart Citations?: https://www.scite.ai/
[45] What is alphaXiv?: https://alphaxiv.org/
[46] What is CatalyzeX?: https://www.catalyzex.com
[47] What is DagsHub?: https://dagshub.com/
[48] What is GotitPub?: http://gotit.pub/faq
[49] What is Huggingface?: https://huggingface.co/huggingface
[50] What is Papers with Code?: https://paperswithcode.com/
[51] What is ScienceCast?: https://sciencecast.org/welcome
[52] What is Replicate?: https://replicate.com/docs/arxiv/about
[53] What is Spaces?: https://huggingface.co/docs/hub/spaces
[54] What is TXYZ.AI?: https://txyz.ai
[55] What are Influence Flowers?: https://influencemap.cmlab.dev/
[56] What is CORE?: https://core.ac.uk/services/recommender
[57] Learn more about arXivLabs: https://info.arxiv.org/labs/index.html
[58] Which authors of this paper are endorsers?: /auth/show-endorsers/2505.04421
[59] Disable MathJax: javascript:setMathjaxCookie()
[60] What is MathJax?: https://info.arxiv.org/help/mathjax.html