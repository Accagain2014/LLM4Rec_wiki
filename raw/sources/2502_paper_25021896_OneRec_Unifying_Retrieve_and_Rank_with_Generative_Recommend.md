---
title: "OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment"
url: "https://arxiv.org/abs/2502.18965"
original_url: "https://arxiv.org/pdf/2502.18965"
fetched: "2026-04-09"
---

# OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment

> 来源：https://arxiv.org/abs/2502.18965

Computer Science > Information Retrieval
arXiv:2502.18965
(cs)
[Submitted on 26 Feb 2025]
Title:
OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment
Authors:
Jiaxin Deng[^1]
,
Shiyao Wang[^2]
,
Kuo Cai[^3]
,
Lejian Ren[^4]
,
Qigen Hu[^5]
,
Weifeng Ding[^6]
,
Qiang Luo[^7]
,
Guorui Zhou[^8]
View a PDF of the paper titled OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment, by Jiaxin Deng and 7 other authors
View PDF[^9]
HTML (experimental)[^10]
Abstract:
Recently, generative retrieval-based recommendation systems have emerged as a promising paradigm. However, most modern recommender systems adopt a retrieve-and-rank strategy, where the generative model functions only as a selector during the retrieval stage. In this paper, we propose OneRec, which replaces the cascaded learning framework with a unified generative model. To the best of our knowledge, this is the first end-to-end generative model that significantly surpasses current complex and well-designed recommender systems in real-world scenarios. Specifically, OneRec includes: 1) an encoder-decoder structure, which encodes the user's historical behavior sequences and gradually decodes the videos that the user may be interested in. We adopt sparse Mixture-of-Experts (MoE) to scale model capacity without proportionally increasing computational FLOPs. 2) a session-wise generation approach. In contrast to traditional next-item prediction, we propose a session-wise generation, which is more elegant and contextually coherent than point-by-point generation that relies on hand-crafted rules to properly combine the generated results. 3) an Iterative Preference Alignment module combined with Direct Preference Optimization (DPO) to enhance the quality of the generated results. Unlike DPO in NLP, a recommendation system typically has only one opportunity to display results for each user's browsing request, making it impossible to obtain positive and negative samples simultaneously. To address this limitation, We design a reward model to simulate user generation and customize the sampling strategy. Extensive experiments have demonstrated that a limited number of DPO samples can align user interest preferences and significantly improve the quality of generated results. We deployed OneRec in the main scene of Kuaishou, achieving a 1.6\% increase in watch-time, which is a substantial improvement.
Subjects:
Information Retrieval (cs.IR)
Cite as:
arXiv:2502.18965[^11]
[cs.IR]
(or
arXiv:2502.18965v1[^12]
[cs.IR]
for this version)
https://doi.org/10.48550/arXiv.2502.18965[^13]
arXiv-issued DOI via DataCite
Submission history
From: Shiyao Wang [
view email[^14]
]
[v1]
Wed, 26 Feb 2025 09:25:10 UTC (17,475 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment, by Jiaxin Deng and 7 other authors
View PDF[^15]
HTML (experimental)[^16]
TeX Source[^17]
view license[^18]
Current browse context:
cs.IR
< prev[^19]
|
next >[^20]
new[^21]
|
recent[^22]
|
2025-02[^23]
Change to browse by:
cs[^24]
References & Citations
NASA ADS[^25]
Google Scholar[^26]
Semantic Scholar[^27]
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
What is the Explorer?[^30]
)
Connected Papers Toggle
Connected Papers
(
What is Connected Papers?[^31]
)
Litmaps Toggle
Litmaps
(
What is Litmaps?[^32]
)
scite.ai Toggle
scite Smart Citations
(
What are Smart Citations?[^33]
)
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv
(
What is alphaXiv?[^34]
)
Links to Code Toggle
CatalyzeX Code Finder for Papers
(
What is CatalyzeX?[^35]
)
DagsHub Toggle
DagsHub
(
What is DagsHub?[^36]
)
GotitPub Toggle
Gotit.pub
(
What is GotitPub?[^37]
)
Huggingface Toggle
Hugging Face
(
What is Huggingface?[^38]
)
Links to Code Toggle
Papers with Code
(
What is Papers with Code?[^39]
)
ScienceCast Toggle
ScienceCast
(
What is ScienceCast?[^40]
)
Demos
Demos
Replicate Toggle
Replicate
(
What is Replicate?[^41]
)
Spaces Toggle
Hugging Face Spaces
(
What is Spaces?[^42]
)
Spaces Toggle
TXYZ.AI
(
What is TXYZ.AI?[^43]
)
Related Papers
Recommenders and Search Tools
Link to Influence Flower
Influence Flower
(
What are Influence Flowers?[^44]
)
Core recommender toggle
CORE Recommender
(
What is CORE?[^45]
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
Learn more about arXivLabs[^46]
.
Which authors of this paper are endorsers?[^47]
|
Disable MathJax[^48]
(
What is MathJax?[^49]
)

---
## 页面链接
[1] Jiaxin Deng: https://arxiv.org/search/cs?searchtype=author&query=Deng,+J
[2] Shiyao Wang: https://arxiv.org/search/cs?searchtype=author&query=Wang,+S
[3] Kuo Cai: https://arxiv.org/search/cs?searchtype=author&query=Cai,+K
[4] Lejian Ren: https://arxiv.org/search/cs?searchtype=author&query=Ren,+L
[5] Qigen Hu: https://arxiv.org/search/cs?searchtype=author&query=Hu,+Q
[6] Weifeng Ding: https://arxiv.org/search/cs?searchtype=author&query=Ding,+W
[7] Qiang Luo: https://arxiv.org/search/cs?searchtype=author&query=Luo,+Q
[8] Guorui Zhou: https://arxiv.org/search/cs?searchtype=author&query=Zhou,+G
[9] View PDF: /pdf/2502.18965
[10] HTML (experimental): https://arxiv.org/html/2502.18965v1
[11] arXiv:2502.18965: https://arxiv.org/abs/2502.18965
[12] arXiv:2502.18965v1: https://arxiv.org/abs/2502.18965v1
[13] https://doi.org/10.48550/arXiv.2502.18965: https://doi.org/10.48550/arXiv.2502.18965
[14] view email: /show-email/bafd8092/2502.18965
[15] View PDF: /pdf/2502.18965
[16] HTML (experimental): https://arxiv.org/html/2502.18965v1
[17] TeX Source: /src/2502.18965
[18] view license: http://creativecommons.org/licenses/by/4.0/
[19] < prev: /prevnext?id=2502.18965&function=prev&context=cs.IR
[20] next >: /prevnext?id=2502.18965&function=next&context=cs.IR
[21] new: /list/cs.IR/new
[22] recent: /list/cs.IR/recent
[23] 2025-02: /list/cs.IR/2025-02
[24] cs: /abs/2502.18965?context=cs
[25] NASA ADS: https://ui.adsabs.harvard.edu/abs/arXiv:2502.18965
[26] Google Scholar: https://scholar.google.com/scholar_lookup?arxiv_id=2502.18965
[27] Semantic Scholar: https://api.semanticscholar.org/arXiv:2502.18965
[30] What is the Explorer?: https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer
[31] What is Connected Papers?: https://www.connectedpapers.com/about
[32] What is Litmaps?: https://www.litmaps.co/
[33] What are Smart Citations?: https://www.scite.ai/
[34] What is alphaXiv?: https://alphaxiv.org/
[35] What is CatalyzeX?: https://www.catalyzex.com
[36] What is DagsHub?: https://dagshub.com/
[37] What is GotitPub?: http://gotit.pub/faq
[38] What is Huggingface?: https://huggingface.co/huggingface
[39] What is Papers with Code?: https://paperswithcode.com/
[40] What is ScienceCast?: https://sciencecast.org/welcome
[41] What is Replicate?: https://replicate.com/docs/arxiv/about
[42] What is Spaces?: https://huggingface.co/docs/hub/spaces
[43] What is TXYZ.AI?: https://txyz.ai
[44] What are Influence Flowers?: https://influencemap.cmlab.dev/
[45] What is CORE?: https://core.ac.uk/services/recommender
[46] Learn more about arXivLabs: https://info.arxiv.org/labs/index.html
[47] Which authors of this paper are endorsers?: /auth/show-endorsers/2502.18965
[48] Disable MathJax: javascript:setMathjaxCookie()
[49] What is MathJax?: https://info.arxiv.org/help/mathjax.html