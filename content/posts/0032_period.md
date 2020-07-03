---
title: Recent updates
tags: thoughts
category: thoughts
date: 2020-05-14T08:36:06Z
---

### Renovating my blogs with `github.com/gohugoio/hugo`: Not as easy as anticipated

- newflaw.com/blog has been broken since I moved the website under a reverse-proxy. BTW reverse-proxy is great fun!
- Using a new tool is never too easy, because of the Babylon tower: people just don’t write documentation in the way you want to query it!
- Stumbled on getting {{ .Site.BaseURL }} to work on image source but it just never render in content/posts/00foo.md!. Found out you need to use it in layout-template or layout-shortcode.
- I didn’t know these three types of documents are different. Retrospectively the hugo doc overview of Variables part does say it is the “template” that uses the variables, but worth to declare these types somewhere first.
- Hugo understand at least 3 types of documents
    - `content/**.md` markdown content, where you can only use shortcodes `{{\<rel posts/bar.md\>}}` (ignore slashes). and not variables`{{.Site.BaseURL}}`
    - `layouts/shortcodes/*.html` shortcodes html: you can use variables like `{{.Site.BaseURL}}`. You can use the defined shortcodes in markdown content.
    - `layouts/_defaults/*.html` template html: you can use variables like `{{.Site.BaseURL}}`. shortcodes avaliability can be uncertain.
- After understanding the templating machine, the rest is about modifying html, javascript and css here and there.
- Putting hugo behind a proxy is non-trivial: just set the BaseUrl in `config.yaml` or during static site generation, then use a simple server like `python3 -m http.server` with appropriate directory name.

### Shopping

   -  Xiaomi XMI 34-inch 2100RMB
   - LG gram 15-inch 8888RMB. It has a fan and I am planning to reconfigure it.
   - ASUS Vivobook 15 4100RMB. Way too heavy but you can’t return stuff easily in China offline stores. :(

### Learning C and Golang: reconfirmed some of my assumptions and gave me some questions.

- Trying to learn C99 following an excellent course Purdue ECE264 https://github.com/PurdueECE264/2019FallProblems
  - Learning C99 expands into
    - C99’s grammar/operator including `; & * (int*)`, for-loop, if statement, exit(1);
    - debug with gdb, common commands including:
      - break exit
      - catch sig
      - bt full
      - info args
      - info locals
      - step
      - next
      - x/x
      - print my_jumpy_pointer
      - `gdb --args` to supply arguments
    - memory leak is bad `valgrind --check-leak=full --error-exitcode=1`
    - compilation of small project is damn simple. But looking at `lh3/samtools` Makefile is scaring..
    - Makefile and luckmake: Since I am too lazy to write Makefile, I decided to write a Python alternative to gnu-make luckmake. As it rolls out I learned several messages:
      - Makefile has a very efficient syntax, thanks to the many operators defined and the strict syntax
      - Trying to mimic Makefile forced me to forge a simpler syntax for luckmake, which makes me rather comfortable when using it. Highly recommended for python users who struggles with the Makefile.
      - A pseudo-static graph for target dependencies is very useful. To write a such static graph, we can use leverage for-loop and suffix transformation. This graph is specified by a function and is pseudo-static, and may take inputs.
- Learning golang is harder because I could not find a systematic tutorial like for C99. It is much younger than C99 and is has much younger documentation… I am still looking for a good documentation for the built-in functions and types.
- Comparison:
  - C99 is simple, low-level. It does not have any types/objects definition. Struct is posible.
  - Golang is modern and has type inheritance? It is compiled thus faster than python.
  - I like using dependency injection to modularise my code. Struct and DI seems the two pillars for OOP and FOP. Maybe OOP is easier to document than FOP, but I found Golang’s documentation to be really hard to lookup (for now).

### [TBC]Learning nim maybe at some point.

## Thoughts

### The incompatibility 拮抗,不可兼得

The incompatitablity means the two underlying entities cannot coexist with each other, This can be thought to dervie some implicit conservation law. For example, the amount of your money is conserved, hence you can not buy a LG-gram-15 AND a Sufacebook 2, meaning these two choices are incompatible with each other. You cannot indulge and be disciplined at the same time because the two are incompatible. You cannot be a male and a female at the same time because most of humans only have one set of sex organs.

The incompatibility is often a useful entrypoint to dissect problems. Many many problems can be boiled down to the incompatibility due to time, space, money, placeholder of some underlying prototypes. On the immunology level, you cannot mix blood type A and blood type B or you will kill your patient. Examples are everywhere, and incompatibilty can be thought as a universal loss function to validate someone’s model. For example, if a picture is a cat, it must not be a dog, which means incompatibility is fundamental to categorical encoding. In academia, it is also useful to establish incompatibility classes, to create compartments and partitions.

### Exploration or exploitation

Exploration feels rather different from exploitation. When I was writing luckmake I was really delighted when the syntax became simpler. However when learning golang or hugo, I am very much doubting why a such ugly syntax would be used and why it would not work not for me. I can feel the internal reluctance to unfamiliar things/strangers as they are shouting in my brain.

Learning a language can be split into Grammar, Vocabulary, Reading and Writing, regarless of whether it is a programming language or a natural language. Learning a language with a good tutorial would be a great pain, but with a good intro the pain will be much less.

### Indulging or Discipline

Indulging is fun: sleep when you can, eat when you can. We humans have a nature to desire, and to fulfill our desire. However if the conscious never says NO to any desire request, then we call it indulging. If the conscious always says NO to any desire request, then we call it discipline.
Be Direct could be useful

Direct could mean different things in different context. In coding, this means to boil down the problem to its core, and selecting the simplest path to achieve it given the current situation. Note that trying to be direct sometime means to be exploitative and not explorative.

### Expedition

Expedition is not about exploiting the joystick that you are always playing, but expedition also needs a map. A good map would help you identify the landmarks and reorient yourself. If you dont have a map, at least use a compass, or some star or some clock. In this sense, modern human is no different from our ancient relatives when expediting. Sometimes you just dont have a good map, because that’s the result of the whole journey.

### The Unknown

Calling an function with None has some important usage in Python, and is used to invoke the default built-in route in many codes. The default reaction to unknown could be a universal attritbue to watch for for any entity that has a memory. Humans treat unknowns differently: we could sware, could panic, could explore, could be hostile, could be friendly. In different times, the Chinese authority has treated the unknown differently.

### Probing the (existence of) truth:

If you know str.upper would return a upper-cased string, then you know a such method exists. If you don’t know whether a method that transforms the lowercase string to uppercase string, you would have to lookup the documentation for it. In reality, you do not always have a documentation to read, and if something is not documented, you would have no way to detect the truth unless you try it yourself.

### github.com/shouldsee/html_to_yaml

  - designed a yaml-based data format that represent XML/HTML document. http://newflaw.com/blog/projects/0002_html-to-yaml/ I am not saying html is bad, I am just saying html does not have indentation, and I love indentation. Indentation helps human to identify structure and nice html should be indented anyway.
	```
	    head: T ## T for tag
	    _#c:
	      script: T
	      src: 
	```      

  -  Trying to patch a Loquat tree with some wall-repairing paint.
  -  Trying to play Fugue in C minor for 2 weeks without finishinig it…

### Plague

I dont know much about the plague because I am not within the healthcare system or the facemask producer company. All my knowledge is second-handed and transmitted through the internet. I know some good repositories exist but forced to deleted at some point. It makes me pounder, about how people forgot about wars and disasters over time. Is it because the human society only has a limited amount of memory? America seems to be suffering quite heavily, but who knows whats the real story.