---
title: "Recommender Systems with Generative Retrieval"
url: "https://arxiv.org/abs/2305.05065"
original_url: "https://arxiv.org/pdf/2305.05065"
fetched: "2026-04-08"
---

# Recommender Systems with Generative Retrieval

> 来源：https://arxiv.org/abs/2305.05065

Computer Science > Information Retrieval
arXiv:2305.05065
(cs)
[Submitted on 8 May 2023 (
v1[^1]
), last revised 3 Nov 2023 (this version, v3)]
Title:
Recommender Systems with Generative Retrieval
Authors:
Shashank Rajput[^2]
,
Nikhil Mehta[^3]
,
Anima Singh[^4]
,
Raghunandan H. Keshavan[^5]
,
Trung Vu[^6]
,
Lukasz Heldt[^7]
,
Lichan Hong[^8]
,
Yi Tay[^9]
,
Vinh Q. Tran[^10]
,
Jonah Samost[^11]
,
Maciej Kula[^12]
,
Ed H. Chi[^13]
,
Maheswaran Sathiamoorthy[^14]
View a PDF of the paper titled Recommender Systems with Generative Retrieval, by Shashank Rajput and 12 other authors
View PDF[^15]
Abstract:
Modern recommender systems perform large-scale retrieval by first embedding queries and item candidates in the same unified space, followed by approximate nearest neighbor search to select top candidates given a query embedding. In this paper, we propose a novel generative retrieval approach, where the retrieval model autoregressively decodes the identifiers of the target candidates. To that end, we create semantically meaningful tuple of codewords to serve as a Semantic ID for each item. Given Semantic IDs for items in a user session, a Transformer-based sequence-to-sequence model is trained to predict the Semantic ID of the next item that the user will interact with. To the best of our knowledge, this is the first Semantic ID-based generative model for recommendation tasks. We show that recommender systems trained with the proposed paradigm significantly outperform the current SOTA models on various datasets. In addition, we show that incorporating Semantic IDs into the sequence-to-sequence model enhances its ability to generalize, as evidenced by the improved retrieval performance observed for items with no prior interaction history.
Comments:
To appear in The 37th Conference on Neural Information Processing Systems (NeurIPS 2023)
Subjects:
Information Retrieval (cs.IR)
; Machine Learning (cs.LG)
Cite as:
arXiv:2305.05065[^16]
[cs.IR]
(or
arXiv:2305.05065v3[^17]
[cs.IR]
for this version)
https://doi.org/10.48550/arXiv.2305.05065[^18]
arXiv-issued DOI via DataCite
Submission history
From: Nikhil Mehta [
view email[^19]
]
[v1][^20]
Mon, 8 May 2023 21:48:17 UTC (3,413 KB)
[v2][^21]
Sat, 23 Sep 2023 20:27:21 UTC (1,884 KB)
[v3]
Fri, 3 Nov 2023 18:02:56 UTC (1,884 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Recommender Systems with Generative Retrieval, by Shashank Rajput and 12 other authors
View PDF[^22]
TeX Source[^23]
view license[^24]
Current browse context:
cs.IR
< prev[^25]
|
next >[^26]
new[^27]
|
recent[^28]
|
2023-05[^29]
Change to browse by:
cs[^30]
cs.LG[^31]
References & Citations
NASA ADS[^32]
Google Scholar[^33]
Semantic Scholar[^34]
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
What is the Explorer?[^37]
)
Connected Papers Toggle
Connected Papers
(
What is Connected Papers?[^38]
)
Litmaps Toggle
Litmaps
(
What is Litmaps?[^39]
)
scite.ai Toggle
scite Smart Citations
(
What are Smart Citations?[^40]
)
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv
(
What is alphaXiv?[^41]
)
Links to Code Toggle
CatalyzeX Code Finder for Papers
(
What is CatalyzeX?[^42]
)
DagsHub Toggle
DagsHub
(
What is DagsHub?[^43]
)
GotitPub Toggle
Gotit.pub
(
What is GotitPub?[^44]
)
Huggingface Toggle
Hugging Face
(
What is Huggingface?[^45]
)
Links to Code Toggle
Papers with Code
(
What is Papers with Code?[^46]
)
ScienceCast Toggle
ScienceCast
(
What is ScienceCast?[^47]
)
Demos
Demos
Replicate Toggle
Replicate
(
What is Replicate?[^48]
)
Spaces Toggle
Hugging Face Spaces
(
What is Spaces?[^49]
)
Spaces Toggle
TXYZ.AI
(
What is TXYZ.AI?[^50]
)
Related Papers
Recommenders and Search Tools
Link to Influence Flower
Influence Flower
(
What are Influence Flowers?[^51]
)
Core recommender toggle
CORE Recommender
(
What is CORE?[^52]
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
Learn more about arXivLabs[^53]
.
Which authors of this paper are endorsers?[^54]
|
Disable MathJax[^55]
(
What is MathJax?[^56]
)

---
## 页面链接
[1] v1: https://arxiv.org/abs/2305.05065v1
[2] Shashank Rajput: https://arxiv.org/search/cs?searchtype=author&query=Rajput,+S
[3] Nikhil Mehta: https://arxiv.org/search/cs?searchtype=author&query=Mehta,+N
[4] Anima Singh: https://arxiv.org/search/cs?searchtype=author&query=Singh,+A
[5] Raghunandan H. Keshavan: https://arxiv.org/search/cs?searchtype=author&query=Keshavan,+R+H
[6] Trung Vu: https://arxiv.org/search/cs?searchtype=author&query=Vu,+T
[7] Lukasz Heldt: https://arxiv.org/search/cs?searchtype=author&query=Heldt,+L
[8] Lichan Hong: https://arxiv.org/search/cs?searchtype=author&query=Hong,+L
[9] Yi Tay: https://arxiv.org/search/cs?searchtype=author&query=Tay,+Y
[10] Vinh Q. Tran: https://arxiv.org/search/cs?searchtype=author&query=Tran,+V+Q
[11] Jonah Samost: https://arxiv.org/search/cs?searchtype=author&query=Samost,+J
[12] Maciej Kula: https://arxiv.org/search/cs?searchtype=author&query=Kula,+M
[13] Ed H. Chi: https://arxiv.org/search/cs?searchtype=author&query=Chi,+E+H
[14] Maheswaran Sathiamoorthy: https://arxiv.org/search/cs?searchtype=author&query=Sathiamoorthy,+M
[15] View PDF: /pdf/2305.05065
[16] arXiv:2305.05065: https://arxiv.org/abs/2305.05065
[17] arXiv:2305.05065v3: https://arxiv.org/abs/2305.05065v3
[18] https://doi.org/10.48550/arXiv.2305.05065: https://doi.org/10.48550/arXiv.2305.05065
[19] view email: /show-email/2f9c8e97/2305.05065
[20] [v1]: /abs/2305.05065v1
[21] [v2]: /abs/2305.05065v2
[22] View PDF: /pdf/2305.05065
[23] TeX Source: /src/2305.05065
[24] view license: http://arxiv.org/licenses/nonexclusive-distrib/1.0/
[25] < prev: /prevnext?id=2305.05065&function=prev&context=cs.IR
[26] next >: /prevnext?id=2305.05065&function=next&context=cs.IR
[27] new: /list/cs.IR/new
[28] recent: /list/cs.IR/recent
[29] 2023-05: /list/cs.IR/2023-05
[30] cs: /abs/2305.05065?context=cs
[31] cs.LG: /abs/2305.05065?context=cs.LG
[32] NASA ADS: https://ui.adsabs.harvard.edu/abs/arXiv:2305.05065
[33] Google Scholar: https://scholar.google.com/scholar_lookup?arxiv_id=2305.05065
[34] Semantic Scholar: https://api.semanticscholar.org/arXiv:2305.05065
[37] What is the Explorer?: https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer
[38] What is Connected Papers?: https://www.connectedpapers.com/about
[39] What is Litmaps?: https://www.litmaps.co/
[40] What are Smart Citations?: https://www.scite.ai/
[41] What is alphaXiv?: https://alphaxiv.org/
[42] What is CatalyzeX?: https://www.catalyzex.com
[43] What is DagsHub?: https://dagshub.com/
[44] What is GotitPub?: http://gotit.pub/faq
[45] What is Huggingface?: https://huggingface.co/huggingface
[46] What is Papers with Code?: https://paperswithcode.com/
[47] What is ScienceCast?: https://sciencecast.org/welcome
[48] What is Replicate?: https://replicate.com/docs/arxiv/about
[49] What is Spaces?: https://huggingface.co/docs/hub/spaces
[50] What is TXYZ.AI?: https://txyz.ai
[51] What are Influence Flowers?: https://influencemap.cmlab.dev/
[52] What is CORE?: https://core.ac.uk/services/recommender
[53] Learn more about arXivLabs: https://info.arxiv.org/labs/index.html
[54] Which authors of this paper are endorsers?: /auth/show-endorsers/2305.05065
[55] Disable MathJax: javascript:setMathjaxCookie()
[56] What is MathJax?: https://info.arxiv.org/help/mathjax.html