
---
title: "Feng's Introduction to Python For Beginners"
date: 2020-05-16T16:01:03Z
---

## Overview

Learning a language can always be broadly split into 4 parts, including two concepts and two procedures, that is

    Grammar
    Vocabulary
    Reading
    Writing

I will try to cover a simplest path to learn Python language in this post.

### You will need to read

Reading is crucial to learner and to programmer. Read the instructions and documents carefully even if they look boring. A good tutorial is always worth a read, because it will save you many time debugging and trial-and-erroring later.

To start learning Python from scratch, I recommend you start with an online interactive course like the codeacacdemy python3 introduction https://www.codecademy.com/learn/learn-python-3. If you dont want to pay, you can try their Python2 course instead, but keep in mind that Python2 is deprecated as of 2020.

You will go through many concepts in an online course, enough to enable you writing your short python program. You will make mistakes and encounter confusing errors, which you should take time to understand. Consult an experienced python programmer if something is really weird.

One thing that does not get covered in the online course is the packaging and importing mechanisms. For real use-cases, you will need to find your package manager like `pip` and install new packages with it. Once installed, they should be importable in your script, but things could go wrong with beginners very easily. Using `conda` wont solve many of these problems, and `conda` is only useful for non-python packages AFAIK, so dont use `conda` if using pure python for simplicity.

### Writing reproducible codes

One good bad feature of Python is that you can import packages easily. This is bad in the sense that you create many dependencies as you write import statements, which can throw an error if the depended package is no longer there, because you changed to a new machine or changed to a new version of python. Non-reproducible code is not useful, because of its unreliability. If you are working on a small project, consider using a Makefile with gnu-make to manage your commands.

#### Edit your code

[TBC]

#### Run your code

[TBC]

### How to import a module?

[TBC]
 
### How to use git

Learn through a game called githug https://github.com/Gazler/githug.

### MISC

[TBC]
