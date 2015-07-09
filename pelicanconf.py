#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ca5'
SITENAME = u'ca5blog'
SITEURL = ''
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'jp'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Ca5', 'http://ca5.me'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Ca5'),
          ('Facebook', 'https://www.facebook.com/ca54makske'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './themes/default'

#TOP_CATEGORY = []

STATIC_PATHS = ['images']
BANNER = 'images/banner.png'
FAVICON = 'images/favicon.ico'
SITE_LOGO = 'images/logo.png'
TWITTER_USERNAME = 'Ca5'
ORDERD_CATEGORIES = [
    'release',
    'event',
    'create',
    'other'
    ]


# Plugin
PLUGIN_PATHS = ["plugins", "./pelican/plugins"]

## Plugin-Sitemap
PLUGINS = ['sitemap',]
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
