---
title: "[风子思传]修博客记"
date: 2020-05-15T05:16:09Z
---

二零二零年, 夏将炎, 疫将休, 余于轩中做得一二项目,有感. 然博客之废已久, 无以为记. 余闻异域有一静态建站新术,曰雨果[^hugo],以构兰格[^golang]写成, 遂阅其经试使之.

初试之,不甚解. 旧博客中有些许静态图片,以英美矩[^img]标签引用,然余所用云器已使反向代理,不可以斜杠求根目录,需在行术时以基准路径构建绝对路径,查阅雨果经,得之替换术曰`{{.Site.BaseURL}}` 余试之,无用.绝径于行术前后并无异,皆为

```html
<img src="{{.Site.BaseURL}/media/博客记.png"></img>
```

于是便览述雨果之经,未能解之.余怒甚,弃雨果替换术,而使派森之忍者替换术二,并以幸运美克施之.忍者术大约如下. 忍者之术既施,美积标签始得其效

```python
ctx = {"BaseURL": "http://newflaw.com/blog/"}
template = '<img src="{{ ctx["BaseURL"] }}media/博客记.png"></img>'
import jinja2
out = jinja2.Template(template).render(**locals())
```

次日朝,余退而思之,使雨果之术者五万人有余,构兰格之术更为当今异域所通行之语.异域之人岂不知此荒谬之误哉?度不然,必有异.乃又细读雨果经,得一术曰短码,试之而有效,复又阅短码之写作之术,而替换术终可用于短码之写作中矣.余喜甚,遂便读雨果之术而试行之云云. 呜呼,雨果之术疾如霹雳,然余初使之则慢如蝼蚁,岂其术实有误哉?岂吾之思实有误哉?似是而非也.虽能码矣,未能智.虽有智矣,未能学.虽能学矣,未能速. 夫阅经习术之途,非行常施之术也,所需智巧亦有不同, 切不可急功而近利, 而宜谨探而慎知. 前人所著之经, 常非习术者所愿读之经. 善习术者乃善读千万经卷而不怒,余尚不能为者也.

风子思二零二零年于沪上思码轩

[^hugo]:github.com/gohugoio/hugo
[^golang]:github.com/golang/go
[^img]:`<img></img>`