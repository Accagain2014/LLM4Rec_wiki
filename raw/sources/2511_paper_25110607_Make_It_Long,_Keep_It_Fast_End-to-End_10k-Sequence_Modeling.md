---
title: "Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling at Billion Scale on Douyin"
url: "https://arxiv.org/abs/2511.06077"
original_url: "https://arxiv.org/pdf/2511.06077"
fetched: "2026-04-09"
---

# Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling at Billion Scale on Douyin

> 来源：https://arxiv.org/abs/2511.06077

Computer Science > Machine Learning
arXiv:2511.06077
(cs)
[Submitted on 8 Nov 2025]
Title:
Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling at Billion Scale on Douyin
Authors:
Lin Guan[^1]
,
Jia-Qi Yang[^2]
,
Zhishan Zhao[^3]
,
Beichuan Zhang[^4]
,
Bo Sun[^5]
,
Xuanyuan Luo[^6]
,
Jinan Ni[^7]
,
Xiaowen Li[^8]
,
Yuhang Qi[^9]
,
Zhifang Fan[^10]
,
Hangyu Wang[^11]
,
Qiwei Chen[^12]
,
Yi Cheng[^13]
,
Feng Zhang[^14]
,
Xiao Yang[^15]
View a PDF of the paper titled Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling at Billion Scale on Douyin, by Lin Guan and 14 other authors
View PDF[^16]
HTML (experimental)[^17]
Abstract:
Short-video recommenders such as Douyin must exploit extremely long user histories without breaking latency or cost budgets. We present an end-to-end system that scales long-sequence modeling to 10k-length histories in production. First, we introduce Stacked Target-to-History Cross Attention (STCA), which replaces history self-attention with stacked cross-attention from the target to the history, reducing complexity from quadratic to linear in sequence length and enabling efficient end-to-end training. Second, we propose Request Level Batching (RLB), a user-centric batching scheme that aggregates multiple targets for the same user/request to share the user-side encoding, substantially lowering sequence-related storage, communication, and compute without changing the learning objective. Third, we design a length-extrapolative training strategy -- train on shorter windows, infer on much longer ones -- so the model generalizes to 10k histories without additional training cost. Across offline and online experiments, we observe predictable, monotonic gains as we scale history length and model capacity, mirroring the scaling law behavior observed in large language models. Deployed at full traffic on Douyin, our system delivers significant improvements on key engagement metrics while meeting production latency, demonstrating a practical path to scaling end-to-end long-sequence recommendation to the 10k regime.
Subjects:
Machine Learning (cs.LG)
; Information Retrieval (cs.IR)
Cite as:
arXiv:2511.06077[^18]
[cs.LG]
(or
arXiv:2511.06077v1[^19]
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.2511.06077[^20]
arXiv-issued DOI via DataCite
Submission history
From: Jia-Qi Yang [
view email[^21]
]
[v1]
Sat, 8 Nov 2025 17:22:54 UTC (499 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling at Billion Scale on Douyin, by Lin Guan and 14 other authors
View PDF[^22]
HTML (experimental)[^23]
TeX Source[^24]
view license[^25]
Current browse context:
cs.LG
< prev[^26]
|
next >[^27]
new[^28]
|
recent[^29]
|
2025-11[^30]
Change to browse by:
cs[^31]
cs.IR[^32]
References & Citations
NASA ADS[^33]
Google Scholar[^34]
Semantic Scholar[^35]
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
What is the Explorer?[^38]
)
Connected Papers Toggle
Connected Papers
(
What is Connected Papers?[^39]
)
Litmaps Toggle
Litmaps
(
What is Litmaps?[^40]
)
scite.ai Toggle
scite Smart Citations
(
What are Smart Citations?[^41]
)
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv
(
What is alphaXiv?[^42]
)
Links to Code Toggle
CatalyzeX Code Finder for Papers
(
What is CatalyzeX?[^43]
)
DagsHub Toggle
DagsHub
(
What is DagsHub?[^44]
)
GotitPub Toggle
Gotit.pub
(
What is GotitPub?[^45]
)
Huggingface Toggle
Hugging Face
(
What is Huggingface?[^46]
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
IArxiv recommender toggle
IArxiv Recommender
(
What is IArxiv?[^53]
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
Learn more about arXivLabs[^54]
.
Which authors of this paper are endorsers?[^55]
|
Disable MathJax[^56]
(
What is MathJax?[^57]
)

---
## 页面链接
[1] Lin Guan: https://arxiv.org/search/cs?searchtype=author&query=Guan,+L
[2] Jia-Qi Yang: https://arxiv.org/search/cs?searchtype=author&query=Yang,+J
[3] Zhishan Zhao: https://arxiv.org/search/cs?searchtype=author&query=Zhao,+Z
[4] Beichuan Zhang: https://arxiv.org/search/cs?searchtype=author&query=Zhang,+B
[5] Bo Sun: https://arxiv.org/search/cs?searchtype=author&query=Sun,+B
[6] Xuanyuan Luo: https://arxiv.org/search/cs?searchtype=author&query=Luo,+X
[7] Jinan Ni: https://arxiv.org/search/cs?searchtype=author&query=Ni,+J
[8] Xiaowen Li: https://arxiv.org/search/cs?searchtype=author&query=Li,+X
[9] Yuhang Qi: https://arxiv.org/search/cs?searchtype=author&query=Qi,+Y
[10] Zhifang Fan: https://arxiv.org/search/cs?searchtype=author&query=Fan,+Z
[11] Hangyu Wang: https://arxiv.org/search/cs?searchtype=author&query=Wang,+H
[12] Qiwei Chen: https://arxiv.org/search/cs?searchtype=author&query=Chen,+Q
[13] Yi Cheng: https://arxiv.org/search/cs?searchtype=author&query=Cheng,+Y
[14] Feng Zhang: https://arxiv.org/search/cs?searchtype=author&query=Zhang,+F
[15] Xiao Yang: https://arxiv.org/search/cs?searchtype=author&query=Yang,+X
[16] View PDF: /pdf/2511.06077
[17] HTML (experimental): https://arxiv.org/html/2511.06077v1
[18] arXiv:2511.06077: https://arxiv.org/abs/2511.06077
[19] arXiv:2511.06077v1: https://arxiv.org/abs/2511.06077v1
[20] https://doi.org/10.48550/arXiv.2511.06077: https://doi.org/10.48550/arXiv.2511.06077
[21] view email: /show-email/7a6c52aa/2511.06077
[22] View PDF: /pdf/2511.06077
[23] HTML (experimental): https://arxiv.org/html/2511.06077v1
[24] TeX Source: /src/2511.06077
[25] view license: http://creativecommons.org/licenses/by-sa/4.0/
[26] < prev: /prevnext?id=2511.06077&function=prev&context=cs.LG
[27] next >: /prevnext?id=2511.06077&function=next&context=cs.LG
[28] new: /list/cs.LG/new
[29] recent: /list/cs.LG/recent
[30] 2025-11: /list/cs.LG/2025-11
[31] cs: /abs/2511.06077?context=cs
[32] cs.IR: /abs/2511.06077?context=cs.IR
[33] NASA ADS: https://ui.adsabs.harvard.edu/abs/arXiv:2511.06077
[34] Google Scholar: https://scholar.google.com/scholar_lookup?arxiv_id=2511.06077
[35] Semantic Scholar: https://api.semanticscholar.org/arXiv:2511.06077
[38] What is the Explorer?: https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer
[39] What is Connected Papers?: https://www.connectedpapers.com/about
[40] What is Litmaps?: https://www.litmaps.co/
[41] What are Smart Citations?: https://www.scite.ai/
[42] What is alphaXiv?: https://alphaxiv.org/
[43] What is CatalyzeX?: https://www.catalyzex.com
[44] What is DagsHub?: https://dagshub.com/
[45] What is GotitPub?: http://gotit.pub/faq
[46] What is Huggingface?: https://huggingface.co/huggingface
[47] What is ScienceCast?: https://sciencecast.org/welcome
[48] What is Replicate?: https://replicate.com/docs/arxiv/about
[49] What is Spaces?: https://huggingface.co/docs/hub/spaces
[50] What is TXYZ.AI?: https://txyz.ai
[51] What are Influence Flowers?: https://influencemap.cmlab.dev/
[52] What is CORE?: https://core.ac.uk/services/recommender
[53] What is IArxiv?: https://iarxiv.org/about
[54] Learn more about arXivLabs: https://info.arxiv.org/labs/index.html
[55] Which authors of this paper are endorsers?: /auth/show-endorsers/2511.06077
[56] Disable MathJax: javascript:setMathjaxCookie()
[57] What is MathJax?: https://info.arxiv.org/help/mathjax.html