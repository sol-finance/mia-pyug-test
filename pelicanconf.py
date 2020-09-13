#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Administrator'
SITENAME = 'MIA PyUG Test'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kuala_Lumpur'

DEFAULT_LANG = 'en'


ARTICLE_PATHS = ['articles',]
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEMES

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
PLUGIN_PATHS = ['pelican-plugins']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'
PLUGINS = [
    'i18n_subsites',
    'series',
    'render_math',
]

# for Tique Search Plugin

PLUGINS += ['tipue_search' ] 

TIPUE_SEARCH = True
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')

# pelicanconf.py Jupyter Notebooks plugin

MARKUP = ("md", "ipynb")
PLUGINS += ['pelican_jupyter.markup']
# this is the path to the module located inside 'pelican-ipynb' which should be part of the plugins installed earlier

IGNORE_FILES = [".ipynb_checkpoints"]