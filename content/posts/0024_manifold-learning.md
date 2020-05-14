---
title: 流型学习还是流行学习?
tag: chinese, thoughts
category: thoughts
date: 2020-03-31T22:39:00
---

tsne由于有谷歌的支持一路吃香喝辣地入侵了单细胞RNA测序领域scRNA-Seq, 
造成的后果呢就是Nividia开心地卖显卡,Illumina开心地卖测序耗材,微流体开心地卖耗材
tSNE作为流型学习的一种算法实际上在单核系统上运行的速度是很让人望而却步的. 比较快的非线性替代品有 isomap 和 umap, 两者都是
基于用k近邻对测地线长度的估算. 线性替代品自然是古老的pca了,但是pca的线性假设实在是跟不上时代了.

<!--more-->

tSNE的是随着神经网络+大数据的浪潮兴起的,这个浪潮信奉的哲学是:数据就是资本,算力就是权力.
但实际上这个信条在生物领域是有点举步维艰: 数据资本是受到生物伦理管制的,算力在没有合适算法的情况下
也不能转化成权力. 因此大家最后就只好测一测单细胞RNA和FACS然后做tSNE标一标细胞亚型就完事了. 但问题是,
这样真的能推动生物学的发展吗?

生物信息的另一条脉络是沿着基因组测序发展的.这个流派专注于研究基因组在各种情况下的演化,因此
衍生出了很多专注于测序领域专精(Domain-specific)的程序和理念,包括samtools,bwa,bowtie等一系列
跟图模型联系紧密的概念.这一流派是有自己的学术主权而很难被机器学习的浪潮所殖民的.

![](https://umap-learn.readthedocs.io/en/latest/_images/performance_14_1.png)

(From: umap-learn docs)

![tsne_isomap_diffmap](https://www.researchgate.net/profile/Hao_Chen91/publication/308546668/figure/fig2/AS:410491240370184@1474880147183/Assessing-ISOMAP-diffusion-map-and-t-SNE-for-inference-of-subset-relationship-Three.png)

(From: https://www.researchgate.net/profile/Hao_Chen91/publication/308546668/figure/fig2/AS:410491240370184@1474880147183/Assessing-ISOMAP-diffusion-map-and-t-SNE-for-inference-of-subset-relationship-Three.png)

See also:

- https://www.sciencedirect.com/science/article/pii/S0098299717300493

<!--more-->


转化劳动成果提高科研(生产)效率