# -*- coding: utf-8 -*-

import sys
import os
import datetime
sys.path.append(os.path.abspath('.'))

project = 'JUTSU-srg'
copyright = '2023, scillidan'
author = 'scillidan'
extensions = [
    'sphinx_rtd_theme',
    'sphinx_rtd_dark_mode',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'JUTSU-srg'
copyright = u'2023-{}, scillidan'.format(datetime.date.today().year)
exclude_patterns = []
pygments_style = 'default'
html_theme = 'sphinx_rtd_theme'
html_theme_options = { }
html_title = "cheat sheet"
html_logo = ""
# html_baseurl = ""
html_static_path = ['_static']
html_use_smartypants = False
html_css_files = [
    'custom.css',
]
html_context = {
  'display_github': True,
  'github_user': 'scillidan',
  'github_repo': 'JUTSU-srg',
  'github_version': 'main/',
}
html_show_sourcelink = False
html_show_copyright = False
html_permalinks = True
html_permalinks_icon = " link"
# locale_dirs = ["locale/"]
# latex_documents = [
#     ('index', 'all.tex', u'Ren\'Py Visual Novel Engine Reference Manual', u'', 'manual'),
# ]
# latex_logo = "logo.png"
# epub_title = u''
# epub_author = u''
# epub_publisher = u''
# epub_copyright = copyright
default_dark_mode = False