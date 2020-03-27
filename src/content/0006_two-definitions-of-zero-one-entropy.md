Title: 两种0/1序列的熵
Date: 2017-02-18 22:39
Tags: maths,short,chinese
Category: maths

两种定义方法

1.考虑 s=[0,1]^d  如果d位里有a位为1,则考虑p=a/d  H(S)=p*log(p)+(1-p)log(p).

2.考虑同样的s, 令 x=a/d, p=p(x), H(S)=sum(p*log(p), for all s).

受了张江老师的“<a href="http://www.swarmagents.cn/detail.php?id=10822">两种熵</a>”启发

## 毛毛毛球
<img class="alignnone size-full wp-image-314" src="{static}/wp-content/uploads/2017/03/fibre.png" alt="fibre" width="816" height="1000" />

思维跳跃如我，结合信息学最近上课学的多序列对齐（Multiple Sequence Alignment）猜想，能不能把CA的规则看成一条遗传信息，并且比较小的变异对其动力学性质的影响？ 一方面也希望能把MSA的想法应用进来，给出一个隐马尔可夫Profile，将会是一个非常漂亮的结果。随机变异过程倒是比较容易写，一两天就写完了，难在控制Alignment的深度，因为有些CA规则对变异一点都不敏感，18个比特你变掉三个它都无所谓，导致生成了巨大的团状Alignment，这个必须用算法进行控制。另一方面对这个树状图进行操作也需要一些新的编程技巧，以达到比较好的并行计算优化。 同时还花了三天帮室友修他的外星人，在EFI引导上栽了个大跟头，不过好在最后总算修好了Windows/Linux双系统。修系统无聊时就在琢磨把树状图显示出来，因为节点和连边一多起来Matlab的可视化就变得很慢，最后用vis.js做出了“毛毛毛球”。