Title: 风城纪事·渣渣
Tags: chinese, thoughts
Category: thoughts
Date: 2017-09-27 22:39
Summary: “我到底是不是一个渣渣？”

“我到底是不是一个渣渣？”

[caption id="attachment_1021" align="alignnone" width="548"]<img src="{static}/wp-content/uploads/2017/09/set2-1024x768.jpg" alt="" width="548" class="size-large wp-image-1021" /> 简单的交集操作："我 & 你"[/caption]

<!--more-->


<h1>
前言：
</h1>

通过比较来下定义是一个通用的办法，想象我们有两个集合，“我”集和“你”集。可以抽象的认为，“我”集包含了个体“我”具有的所有品质，相应地可以定义“你”集。接下来我们讨论几个逻辑上存疑的推断，以支持论点”不要因为别人的看似强大而自卑，也不要因为自己的看似渊博而自负。“：
<li>
自卑推断</li>
<li>
自负推断</li>
<li>
联合自卑推断</li>

[caption id="attachment_1019" align="alignnone" width="584"]<img src="{static}/wp-content/uploads/2017/09/set1-1024x768.jpg" alt="" width="584" height="438" class="alignnone size-large wp-image-1019" /> 初始韦恩图[/caption]

[caption id="attachment_1021" align="alignnone" width="548"]<img src="{static}/wp-content/uploads/2017/09/set2-1024x768.jpg" alt="" width="548" class="size-large wp-image-1021" /> 简单的交集操作："我 & 你"[/caption]

<h2>
1.自负推断：“你看，我有的这些，他都没有！（看我多厉害！）”
</h2>

<h3>
注： "&"指交集操作，“|x|”指“x”的度量/大小。"+"指并集操作， ”-“ 指差集操作
</h3>


在“我”被清楚定义而“你”的定义不明时，我们通过“我”和"你"的交集来估算“你”的大小，也就是通俗意义上的“攀比”。

也就是说基于假设： |你| 正比于 |我 & 你|，我们可以实现推断： f:|我 & 你| --> |你|， 

[caption id="attachment_1025" align="alignnone" width="584"]<img src="{static}/wp-content/uploads/2017/09/set7-1024x768.jpg" alt="" width="584" height="438" class="size-large wp-image-1025" /> 通过交集逆推”你“集[/caption]

又因为 |我 & 你| = |我| - |我 - 你|， 所以实际操作中我们常常直接从 |我 - 你| 出发，实现对 |你| 的估算。

[caption id="attachment_1028" align="alignnone" width="584"]<img src="{static}/wp-content/uploads/2017/09/set10-1024x768.jpg" alt="" width="584" height="438" class="size-large wp-image-1028" /> | 我 - 你 | 可以导出 | 我 & 你 |[/caption]

但是事实上，这个估算不一定成立。因为我们的假设是没有任何保证的（一厢情愿），实际情况中 |我 & 你| 和 |你| 不一定有相关性。

[caption id="attachment_1026" align="alignnone" width="584"]<img src="{static}/wp-content/uploads/2017/09/set8-1024x768.jpg" alt="" width="584" height="438" class="size-large wp-image-1026" /> 情景一： ”你“集的确很小<br />[/caption]

[caption id="attachment_1027" align="alignnone" width="584"]<img src="{static}/wp-content/uploads/2017/09/set9-1024x768.jpg" alt="" width="584" height="438" class="size-large wp-image-1027" /> 情景二： 尽管交集很小，但”你“集其实很大[/caption]

<h2>
2.自卑推断:“你看，你有的这些，我都没有！（看我多渣！）”
</h2>

<h3>
注：“正比”是一个可逆关系
</h3>

自卑推断基本上是自负推断的对偶，可以表示为 g:|你 - 我| -> |我|。换句话说，是对“我”的度量不确定的情况下，用“交集”来估算自身的大小。
[caption id="attachment_1030" align="alignnone" width="584"]<img src="{static}/wp-content/uploads/2017/09/set11-1024x768.jpg" alt="" width="584" height="438" class="size-large wp-image-1030" /> 既可以用交集估算[/caption]

[caption id="attachment_1031" align="alignnone" width="584"]<img src="{static}/wp-content/uploads/2017/09/set12-1024x768.jpg" alt="" width="584" height="438" class="size-large wp-image-1031" /> 也可以用差集估算[/caption]

由于同样的原因，自卑推断也受限于假设 |我 & 你| 正比于 |我|。

<h2>
3.联合自卑推断：“你看，这些东西，我们都没有！（在座的各位都是渣渣！）”
</h2>

这个时候我们的注意力在 “(我 + 你)” 的补集上，亦即"全集 - (我 + 你)"，此时我们对”全集“，”我“，”你“三者的大小都没有准确的信息(”全集“包含了所有已知)，但是我们知道”我 + 你“ 所不具备的那些元素。

可以把该推断写成 u: | 全集 - （我 + 你) | --> ( | 我 | ， | 你 | )

这个推断利用了以下等式： |全集| = | 全集 - （我 + 你) |  +  |我 + 你|

[caption id="attachment_1032" align="alignnone" width="584"]<img src="{static}/wp-content/uploads/2017/09/set13-1024x768.jpg" alt="" width="584" height="438" class="size-large wp-image-1032" /> 差集常常是我们认识世界的直觉[/caption]

按理说没有地方可以出问题了，但是如果|全集|和 |我 + 你| 同时变大或者变小， 中间的差集大小是可以不变的。也就是说， | 全集 - （我 + 你) | 无法对 |我 + 你| 的大小作出任何保证。

<h2>
总结： 基于单一指标的观察，尤其是差集的大小(如： |我 - 你| )，常常会导出不可靠的结论。时刻警惕从相对度量”差距“中导出绝对度量的推断。
</h2>

<h2>
说人话： 不要因为别人的看似强大而自卑，也不要因为自己的看似渊博而自负。只有将注意力合理分配在多个个体上，才能做出可靠的判断。
</h2>

这篇文章的灵感是来自于ISS项目中对交集运算的使用，更一般说是来自于对 "Sensitivity" 和 "Specificity" 两个指标的理解。通俗的讲，就是基于”攀比/对比“生成的”长处“和”短处“进行的一些常见推断，和常见潜在假设（Implicit Assumption）的梳理。

<h2>
后记 (胡言乱语)：
</h2>
有时候会碰上很奇怪的谈话，言语间分明感到“我不想和你说话，你个渣渣”，但是对方又没有主动停下的意思。。。这个时候就很尴尬了。考虑发送者(sender)和接收者(receiver)

这种情况呢，一般伴随着接收者的莫名其妙。也就是说，接收者完全不相信发送者的“渣渣声明”，但是又不愿意花太多力气去停止这个“渣渣声明”，毕竟如果不是渣渣，谁会在乎是否被声明成了渣渣。换句话说，接收者相信“渣渣声明”与自己是无关的，尽管在表面这个声明是指向自己的。...

2017年9月26日
剑桥

