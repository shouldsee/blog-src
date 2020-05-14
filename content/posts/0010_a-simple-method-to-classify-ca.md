---
title: A simple method to classify CA // 一个简单的CA分类方法
date: 2017-03-18T15:42:00
category: maths
tags: maths, automata, english
---


<style type="text/css">
	code.has-jax {font: inherit;
              font-size: 100%;
              background: inherit;
              border: inherit;
              color: #515151;}
</style>
<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    displayMath: [['$$','$$'] ],
    processEscapes: true,
    processEnvironments: true,
    skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
    TeX: { equationNumbers: { autoNumber: "AMS" },
         extensions: ["AMSmath.js", "AMSsymbols.js"] }
  }
});

  MathJax.Hub.Queue(function() {
    // Fix <code> tags after MathJax finishes running. This is a
    // hack to overcome a shortcoming of Markdown. Discussion at
    // https://github.com/mojombo/jekyll/issues/199
    var all = MathJax.Hub.getAllJax(), i;
    for(i = 0; i < all.length; i += 1) {
        all[i].SourceElement().parentNode.className += ' has-jax';
    }
});
</script>



- Recall a CA rule $rule$ project a circular-boundary state space $S$ back to it self, that is
- $rule: S\rightarrow$
- aka $x_{t+1}=rule(x_t), x_t \in S, x_{t+1} \in S $

<!--more-->


where $S = \\{ 0, 1 \\}^n$, and more strictly $x_t: [1,2,...,n] \rightarrow \\{0,1\\}$, for simplicity we let $\phi = [1,2,...,n]$, thus $x = x(\phi) $

In practical, we take n=20^2=400;

<!--more-->
Consider $x_S(\phi_S)$ where $\phi_S=[1, 2, ..., n] \times [1, 2, ..., card(S)], x_S:\phi_S \rightarrow \\{0,1\\}$

In practical, we sought a big enough representative subset, $S_r$ from $S$, so that

$x_S(\phi_S)\approx x_{S_r}(\phi_{S_r})$

Denote $rule(rule(x))=rule^2(x)$, we have

$rule(rule^t(x))=rule^{n+1}(x)$,

We then define a profile $\lambda: [0, 1, 2, 3, ......] \rightarrow [0, 1]$ with Pearson correlation so that

$\lambda(t) =( \rho[x_S,y^t_S]) ^2= ({Cov[x_S, \ y^t_S]\over\sigma[x_S] \cdot \sigma[y^t_S]})^2$,
where $y^t_S=rule^n(x_S)$, $\sigma[X]$ denotes standard deviation of X and $Cov[X,Y]$ denotes covariance between X and Y.

We assert that $\lambda(t)$ classify the dynamics of the CA rule by capturing the periodic behavior in the underlying dynamics.

Importantly, we can find a good $S_r$ by taking a random $S_{r0}$ and obtain

$S_r = rule^T(S_{r0})$ where T is a variable parameter.