#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
AUTHOR = 'F. Geng'
SITENAME = "Newflaw"
SITESUBTITLE = "Nature is never flawless"
SITE_TITLE = u"newflaw//破绽"

##Dev
SITEURL = ''
RELATIVE_URLS = True

##pub
SITEURL = 'http://www.newflaw.com/blog'
RELATIVE_URLS = False
# THEME = 'themes/karthur'
THEME = "/pelican-theme"
STATIC_PATHS = ['wp-content',  ]
PAGE_PATHS = ['./content/pages']
PLUGIN_PATHS= ['/pelican-plugins']

PLUGINS = [
#     'feed_summary', 
#     'related_posts', 
#     'sitemap',
#     'thumbnailer',
    'render_math',
#     'tag_cloud'
]

DISPLAY_PAGES_ON_MENU = True
MY_EMAIL_ADDR = 'feng.geng.14@ucl.ac.uk'
DISQUS = "newflaw"


PATH = '/app'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'



# ARTICLE_PATHS = ['blog']
# ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
# ARTICLE_URL = '{date:%Y}/{slug}.html'
# PAGE_PATHS = ['pages']

ARTICLE_ORDER_BY = 'reversed-date'
PAGE_ORDER_BY = 'basename'
DEFAULT_PAGINATION = 5


GITHUB_URL = 'http://github.com/shouldsee'
LINKS = SOCIAL = (
#           ('twitter', 'http://twitter.com/shouldsee'),
          #'linkedin', 'http://www.linkedin.com/in/danieldebie'),
          ('Stackoverflow','https://stackoverflow.com/users/8083313/shouldsee'),
          ('<img width="16" height="16" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"></img> Github', 'http://github.com/shouldsee'),
          
#         ('stackoverflow', 'http://stackoverflow.com/users/872397/dandydev', 'stack-overflow')
         )

# url and path settings
#CACHE_CONTENT = False
# article
ARTICLE_URL = u'articles/{category}/{slug}/'
ARTICLE_SAVE_AS = u'articles/{category}/{slug}/index.html'
# page
PAGE_URL = u'{slug}/'
PAGE_SAVE_AS = u'{slug}/index.html'
# author
AUTHOR_URL = u'author/{slug}/'
AUTHOR_SAVE_AS = u'author/{slug}/index.html'
# authors
AUTHORS_URL = u'authors/'
AUTHORS_SAVE_AS = u'authors/index.html'
# category
CATEGORY_URL = u'category/{slug}.html'
CATEGORY_SAVE_AS = u'category/{slug}.html'
# tag
TAG_URL = u'tag/{slug}/'
TAG_SAVE_AS = u'tag/{slug}/index.html'

DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (('Archive', '{SITEURL}/archives.html'.format(**locals())),)
USE_FOLDER_AS_CATEGORY = False

# PAGES = lambda: pages;


SUMMARY_MAX_LENGTH = 50
SUMMARY_MAX_LENGTH = 25
