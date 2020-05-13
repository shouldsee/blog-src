---
title: 应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展
tags: chinese, maths
category: maths
date: 2017-02-15T11:35:00+08:00
---

以相关性(correlation)为度量的回归图忠实地反映了基础元胞自动机(ECA)的动力学性质，可以很好地区分稳态和混沌态。

我对Logistic Mapping做了简单的耦合推广，并应用回归图找到了处在混沌边界的参数，有趣的是这种推广系统也处在混沌边界。

<img class="alignnone size-full wp-image-253" src="{{static}}/wp-content/uploads/2017/02/demo_log_torus.jpg" alt="demo_log_torus" width="2409" height="436" />

<img class="alignnone size-full wp-image-304" src="{{static}}/wp-content/uploads/2017/02/logistic__3-811_corrprofile.jpg" alt="logistic__3-811_corrprofile" width="1000" height="563" />

讨论：二维元胞自动机是一个幻象，它并不比一维元胞高明到哪里去，对于Glider和Pattern的分类看起来没有发展壮大的希望。CA和物理学的联系目前还是太弱了，需要一些契机把CA爱好者引导到更有建设性的道路上。Wolfram对Rule110的阐释是很有insight的，但是他本人最后也认识到CA有一些内在的缺陷使其不能模拟神经网络。我希望Derrida Plot的复兴可以改变这一情况，这一工具允许人们更加系统地对自动机的动力学性质进行分类，而且和微扰论有很深的联系，希望有更多的人参与到这个研究里来。

这里用一个二维BS元胞自动机为例子(B013468/S23,生命游戏是B3/S23),大致介绍一下Covariance Profile的具体操作办法，用一个常值分布随机取两个初始状态，计算它们的距离H(0),接下来用CA规则将两个初态分别迭代T次，并记录它们的轨迹。这样我们可以得到H(1),H(2),H(3)....H(T). 然后把上述操作重复N次。想象[H(1),H(2)]在平面内确定一个点，由于有N个样本，我们可以确定N个点，这时候我们可以计算H(1),H(2)的统计学关系(一开始我用的是相关性(Pearson Correlation),后面发现不够灵敏，于是换成了协方差(Covariance)

<img class="alignnone size-full wp-image-306" src="{{static}}/wp-content/uploads/2017/02/expanded6491tca.jpg" alt="expanded6491tca" width="735" height="661" />

对于任选的H(t_a),H(t_b),我们都可以确定一个分布并且抽象成一个单值。将这些单值集合起来之后，我们就的到了刚刚看到的热相图。

<img class="alignnone size-full wp-image-308" src="{{static}}/wp-content/uploads/2017/02/collected6491tca.jpg" alt="collected6491tca" width="497" height="416" />

(这里的单值用的都是协方差。)

我的观察是，热相图的凹凸性可以很好地刻画原系统的动力学性质。可以看到这个热相图的对角线有一个凹扩散，这一般对应复杂的动力学（complex,相对于混沌 chaotic，稳定 stable而言）

待续

Comments: 

1. Yanbo Zhang zhangyb1"AT"mail.ustc.edu.cn: Logistic Mapping 的想法非常有意思，似乎只用一个参数k就出现了Wolfram的四个基本类型。我在想，是否可以对离散元胞自动机做逆向的工作，从时空图直接反推到k，从而得到一个意义非常明确的序参量。

1. shouldsee: 我现在的想法是完全用密度涨落来描述动力学性质，而不是用DerridaPlot。 把密度涨落抽象成几个Scalar的序参量应该是可行的，但是我还没有仔细考虑什么样的抽取办法是推广性最好的，因为目前这个抽取办法挺初等的，还缺少很多形式上的工作，只是从实用的角度发现还挺有用。