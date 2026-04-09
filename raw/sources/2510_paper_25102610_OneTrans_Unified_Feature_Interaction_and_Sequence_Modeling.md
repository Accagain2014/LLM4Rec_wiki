---
title: "OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender"
url: "https://arxiv.org/abs/2510.26104"
original_url: "https://arxiv.org/pdf/2510.26104"
fetched: "2026-04-09"
---

# OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender

> 来源：https://arxiv.org/abs/2510.26104

Computer Science > Information Retrieval
arXiv:2510.26104
(cs)
[Submitted on 30 Oct 2025 (
v1[^1]
), last revised 2 Feb 2026 (this version, v3)]
Title:
OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender
Authors:
Zhaoqi Zhang[^2]
,
Haolei Pei[^3]
,
Jun Guo[^4]
,
Tianyu Wang[^5]
,
Yufei Feng[^6]
,
Hui Sun[^7]
,
Shaowei Liu[^8]
,
Aixin Sun[^9]
View a PDF of the paper titled OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender, by Zhaoqi Zhang and 7 other authors
View PDF[^10]
HTML (experimental)[^11]
Abstract:
In recommendation systems, scaling up feature-interaction modules (e.g., Wukong, RankMixer) or user-behavior sequence modules (e.g., LONGER) has achieved notable success. However, these efforts typically proceed on separate tracks, which not only hinders bidirectional information exchange but also prevents unified optimization and scaling. In this paper, we propose OneTrans, a unified Transformer backbone that simultaneously performs user-behavior sequence modeling and feature interaction. OneTrans employs a unified tokenizer to convert both sequential and non-sequential attributes into a single token sequence. The stacked OneTrans blocks share parameters across similar sequential tokens while assigning token-specific parameters to non-sequential tokens. Through causal attention and cross-request KV caching, OneTrans enables precomputation and caching of intermediate representations, significantly reducing computational costs during both training and inference. Experimental results on industrial-scale datasets demonstrate that OneTrans scales efficiently with increasing parameters, consistently outperforms strong baselines, and yields a 5.68% lift in per-user GMV in online A/B tests.
Comments:
Accepted at The Web Conference 2026 (WWW 2026). Camera-ready version forthcoming
Subjects:
Information Retrieval (cs.IR)
Cite as:
arXiv:2510.26104[^12]
[cs.IR]
(or
arXiv:2510.26104v3[^13]
[cs.IR]
for this version)
https://doi.org/10.48550/arXiv.2510.26104[^14]
arXiv-issued DOI via DataCite
Submission history
From: Zhaoqi Zhang [
view email[^15]
]
[v1][^16]
Thu, 30 Oct 2025 03:30:12 UTC (252 KB)
[v2][^17]
Fri, 30 Jan 2026 07:30:45 UTC (249 KB)
[v3]
Mon, 2 Feb 2026 06:48:36 UTC (267 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender, by Zhaoqi Zhang and 7 other authors
View PDF[^18]
HTML (experimental)[^19]
TeX Source[^20]
view license[^21]
Current browse context:
cs.IR
< prev[^22]
|
next >[^23]
new[^24]
|
recent[^25]
|
2025-10[^26]
Change to browse by:
cs[^27]
References & Citations
NASA ADS[^28]
Google Scholar[^29]
Semantic Scholar[^30]
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
What is the Explorer?[^33]
)
Connected Papers Toggle
Connected Papers
(
What is Connected Papers?[^34]
)
Litmaps Toggle
Litmaps
(
What is Litmaps?[^35]
)
scite.ai Toggle
scite Smart Citations
(
What are Smart Citations?[^36]
)
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv
(
What is alphaXiv?[^37]
)
Links to Code Toggle
CatalyzeX Code Finder for Papers
(
What is CatalyzeX?[^38]
)
DagsHub Toggle
DagsHub
(
What is DagsHub?[^39]
)
GotitPub Toggle
Gotit.pub
(
What is GotitPub?[^40]
)
Huggingface Toggle
Hugging Face
(
What is Huggingface?[^41]
)
Links to Code Toggle
Papers with Code
(
What is Papers with Code?[^42]
)
ScienceCast Toggle
ScienceCast
(
What is ScienceCast?[^43]
)
Demos
Demos
Replicate Toggle
Replicate
(
What is Replicate?[^44]
)
Spaces Toggle
Hugging Face Spaces
(
What is Spaces?[^45]
)
Spaces Toggle
TXYZ.AI
(
What is TXYZ.AI?[^46]
)
Related Papers
Recommenders and Search Tools
Link to Influence Flower
Influence Flower
(
What are Influence Flowers?[^47]
)
Core recommender toggle
CORE Recommender
(
What is CORE?[^48]
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
Learn more about arXivLabs[^49]
.
Which authors of this paper are endorsers?[^50]
|
Disable MathJax[^51]
(
What is MathJax?[^52]
)

---
## 页面链接
[1] v1: https://arxiv.org/abs/2510.26104v1
[2] Zhaoqi Zhang: https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Z
[3] Haolei Pei: https://arxiv.org/search/cs?searchtype=author&query=Pei,+H
[4] Jun Guo: https://arxiv.org/search/cs?searchtype=author&query=Guo,+J
[5] Tianyu Wang: https://arxiv.org/search/cs?searchtype=author&query=Wang,+T
[6] Yufei Feng: https://arxiv.org/search/cs?searchtype=author&query=Feng,+Y
[7] Hui Sun: https://arxiv.org/search/cs?searchtype=author&query=Sun,+H
[8] Shaowei Liu: https://arxiv.org/search/cs?searchtype=author&query=Liu,+S
[9] Aixin Sun: https://arxiv.org/search/cs?searchtype=author&query=Sun,+A
[10] View PDF: /pdf/2510.26104
[11] HTML (experimental): https://arxiv.org/html/2510.26104v3
[12] arXiv:2510.26104: https://arxiv.org/abs/2510.26104
[13] arXiv:2510.26104v3: https://arxiv.org/abs/2510.26104v3
[14] https://doi.org/10.48550/arXiv.2510.26104: https://doi.org/10.48550/arXiv.2510.26104
[15] view email: /show-email/c26fe9bb/2510.26104
[16] [v1]: /abs/2510.26104v1
[17] [v2]: /abs/2510.26104v2
[18] View PDF: /pdf/2510.26104
[19] HTML (experimental): https://arxiv.org/html/2510.26104v3
[20] TeX Source: /src/2510.26104
[21] view license: http://arxiv.org/licenses/nonexclusive-distrib/1.0/
[22] < prev: /prevnext?id=2510.26104&function=prev&context=cs.IR
[23] next >: /prevnext?id=2510.26104&function=next&context=cs.IR
[24] new: /list/cs.IR/new
[25] recent: /list/cs.IR/recent
[26] 2025-10: /list/cs.IR/2025-10
[27] cs: /abs/2510.26104?context=cs
[28] NASA ADS: https://ui.adsabs.harvard.edu/abs/arXiv:2510.26104
[29] Google Scholar: https://scholar.google.com/scholar_lookup?arxiv_id=2510.26104
[30] Semantic Scholar: https://api.semanticscholar.org/arXiv:2510.26104
[33] What is the Explorer?: https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer
[34] What is Connected Papers?: https://www.connectedpapers.com/about
[35] What is Litmaps?: https://www.litmaps.co/
[36] What are Smart Citations?: https://www.scite.ai/
[37] What is alphaXiv?: https://alphaxiv.org/
[38] What is CatalyzeX?: https://www.catalyzex.com
[39] What is DagsHub?: https://dagshub.com/
[40] What is GotitPub?: http://gotit.pub/faq
[41] What is Huggingface?: https://huggingface.co/huggingface
[42] What is Papers with Code?: https://paperswithcode.com/
[43] What is ScienceCast?: https://sciencecast.org/welcome
[44] What is Replicate?: https://replicate.com/docs/arxiv/about
[45] What is Spaces?: https://huggingface.co/docs/hub/spaces
[46] What is TXYZ.AI?: https://txyz.ai
[47] What are Influence Flowers?: https://influencemap.cmlab.dev/
[48] What is CORE?: https://core.ac.uk/services/recommender
[49] Learn more about arXivLabs: https://info.arxiv.org/labs/index.html
[50] Which authors of this paper are endorsers?: /auth/show-endorsers/2510.26104
[51] Disable MathJax: javascript:setMathjaxCookie()
[52] What is MathJax?: https://info.arxiv.org/help/mathjax.html