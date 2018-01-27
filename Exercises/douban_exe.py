# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 22:51:56 2018

@author: ChiaS
"""

import requests
from bs4 import BeautifulSoup
import re

sum = 0
r = requests.get('https://book.douban.com/subject/27108971/comments/')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('p', 'comment-content')
for item in pattern:
    print(item.string)
pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
p = re.findall(pattern_s, r.text)
for i in p:
    sum += int(str(i))
    print(i)
print(sum)
