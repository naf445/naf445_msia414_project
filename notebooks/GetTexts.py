# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from urllib.request import urlopen
from bs4 import BeautifulSoup

gita_html = urlopen("https://www.gutenberg.org/files/2388/2388-h/2388-h.htm").read()
gita_raw = BeautifulSoup(gita_html).get_text()

analects_html = urlopen("http://www.gutenberg.org/cache/epub/3330/pg3330.txt").read()
analects_raw = BeautifulSoup(analects_html).get_text()


