#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChiaSang on 2018/2/5


import requests
import re
from bs4 import BeautifulSoup
pages = 109
se_num = re.compile(r'\d+')
for page in range(1, pages):
    url = 'https://www.sto.cc/book-112356-{0}.html'.format(str(page))
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    now_page = soup.select('div.bookbox > h1')
    num = se_num.search(str(now_page[0].get_text()))
    print(num)
    body = soup.select('#BookContent')
    raw_novel = ''.join(body[0].get_text()).replace("\n", "")
    with open('何为贤妻.txt', 'a', encoding='utf-8') as f:
        f.write(raw_novel)
