---
title: "Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations"
url: "https://arxiv.org/abs/2402.17152"
original_url: "https://arxiv.org/pdf/2402.17152"
fetched: "2026-04-08"
---

# Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations

> 来源：https://arxiv.org/abs/2402.17152

Computer Science > Machine Learning
arXiv:2402.17152
(cs)
[Submitted on 27 Feb 2024 (
v1[^1]
), last revised 6 May 2024 (this version, v3)]
Title:
Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations
Authors:
Jiaqi Zhai[^2]
,
Lucy Liao[^3]
,
Xing Liu[^4]
,
Yueming Wang[^5]
,
Rui Li[^6]
,
Xuan Cao[^7]
,
Leon Gao[^8]
,
Zhaojie Gong[^9]
,
Fangda Gu[^10]
,
Michael He[^11]
,
Yinghai Lu[^12]
,
Yu Shi[^13]
View a PDF of the paper titled Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations, by Jiaqi Zhai and 11 other authors
View PDF[^14]
HTML (experimental)[^15]
Abstract:
Large-scale recommendation systems are characterized by their reliance on high cardinality, heterogeneous features and the need to handle tens of billions of user actions on a daily basis. Despite being trained on huge volume of data with thousands of features, most Deep Learning Recommendation Models (DLRMs) in industry fail to scale with compute.
Inspired by success achieved by Transformers in language and vision domains, we revisit fundamental design choices in recommendation systems. We reformulate recommendation problems as sequential transduction tasks within a generative modeling framework ("Generative Recommenders"), and propose a new architecture, HSTU, designed for high cardinality, non-stationary streaming recommendation data.
HSTU outperforms baselines over synthetic and public datasets by up to 65.8% in NDCG, and is 5.3x to 15.2x faster than FlashAttention2-based Transformers on 8192 length sequences. HSTU-based Generative Recommenders, with 1.5 trillion parameters, improve metrics in online A/B tests by 12.4% and have been deployed on multiple surfaces of a large internet platform with billions of users. More importantly, the model quality of Generative Recommenders empirically scales as a power-law of training compute across three orders of magnitude, up to GPT-3/LLaMa-2 scale, which reduces carbon footprint needed for future model developments, and further paves the way for the first foundational models in recommendations.
Comments:
26 pages, 13 figures. ICML'24. Code available at
this https URL[^16]
Subjects:
Machine Learning (cs.LG)
; Information Retrieval (cs.IR)
Cite as:
arXiv:2402.17152[^17]
[cs.LG]
(or
arXiv:2402.17152v3[^18]
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.2402.17152[^19]
arXiv-issued DOI via DataCite
Submission history
From: Jiaqi Zhai [
view email[^20]
]
[v1][^21]
Tue, 27 Feb 2024 02:37:37 UTC (1,966 KB)
[v2][^22]
Thu, 18 Apr 2024 03:38:55 UTC (1,768 KB)
[v3]
Mon, 6 May 2024 02:05:45 UTC (1,765 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations, by Jiaqi Zhai and 11 other authors
View PDF[^23]
HTML (experimental)[^24]
TeX Source[^25]
view license[^26]
Current browse context:
cs.LG
< prev[^27]
|
next >[^28]
new[^29]
|
recent[^30]
|
2024-02[^31]
Change to browse by:
cs[^32]
cs.IR[^33]
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
IArxiv recommender toggle
IArxiv Recommender
(
What is IArxiv?[^55]
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
Learn more about arXivLabs[^56]
.
Which authors of this paper are endorsers?[^57]
|
Disable MathJax[^58]
(
What is MathJax?[^59]
)

---
## 页面链接
[1] v1: https://arxiv.org/abs/2402.17152v1
[2] Jiaqi Zhai: https://arxiv.org/search/cs?searchtype=author&query=Zhai,+J
[3] Lucy Liao: https://arxiv.org/search/cs?searchtype=author&query=Liao,+L
[4] Xing Liu: https://arxiv.org/search/cs?searchtype=author&query=Liu,+X
[5] Yueming Wang: https://arxiv.org/search/cs?searchtype=author&query=Wang,+Y
[6] Rui Li: https://arxiv.org/search/cs?searchtype=author&query=Li,+R
[7] Xuan Cao: https://arxiv.org/search/cs?searchtype=author&query=Cao,+X
[8] Leon Gao: https://arxiv.org/search/cs?searchtype=author&query=Gao,+L
[9] Zhaojie Gong: https://arxiv.org/search/cs?searchtype=author&query=Gong,+Z
[10] Fangda Gu: https://arxiv.org/search/cs?searchtype=author&query=Gu,+F
[11] Michael He: https://arxiv.org/search/cs?searchtype=author&query=He,+M
[12] Yinghai Lu: https://arxiv.org/search/cs?searchtype=author&query=Lu,+Y
[13] Yu Shi: https://arxiv.org/search/cs?searchtype=author&query=Shi,+Y
[14] View PDF: /pdf/2402.17152
[15] HTML (experimental): https://arxiv.org/html/2402.17152v3
[16] this https URL: https://github.com/facebookresearch/generative-recommenders
[17] arXiv:2402.17152: https://arxiv.org/abs/2402.17152
[18] arXiv:2402.17152v3: https://arxiv.org/abs/2402.17152v3
[19] https://doi.org/10.48550/arXiv.2402.17152: https://doi.org/10.48550/arXiv.2402.17152
[20] view email: /show-email/1e55524d/2402.17152
[21] [v1]: /abs/2402.17152v1
[22] [v2]: /abs/2402.17152v2
[23] View PDF: /pdf/2402.17152
[24] HTML (experimental): https://arxiv.org/html/2402.17152v3
[25] TeX Source: /src/2402.17152
[26] view license: http://creativecommons.org/licenses/by-nc-sa/4.0/
[27] < prev: /prevnext?id=2402.17152&function=prev&context=cs.LG
[28] next >: /prevnext?id=2402.17152&function=next&context=cs.LG
[29] new: /list/cs.LG/new
[30] recent: /list/cs.LG/recent
[31] 2024-02: /list/cs.LG/2024-02
[32] cs: /abs/2402.17152?context=cs
[33] cs.IR: /abs/2402.17152?context=cs.IR
[34] NASA ADS: https://ui.adsabs.harvard.edu/abs/arXiv:2402.17152
[35] Google Scholar: https://scholar.google.com/scholar_lookup?arxiv_id=2402.17152
[36] Semantic Scholar: https://api.semanticscholar.org/arXiv:2402.17152
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
[55] What is IArxiv?: https://iarxiv.org/about
[56] Learn more about arXivLabs: https://info.arxiv.org/labs/index.html
[57] Which authors of this paper are endorsers?: /auth/show-endorsers/2402.17152
[58] Disable MathJax: javascript:setMathjaxCookie()
[59] What is MathJax?: https://info.arxiv.org/help/mathjax.html