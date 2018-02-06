# -*- encoding: utf-8 -*-
# 2018-02-04 09:34

import requests
import os
from bs4 import BeautifulSoup
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
chapter_address = {}
tag_a = []
tag_p = []
base_url = 'http://www.3333show.com/rexue/552/'
os.makedirs('zhiranchenghun', exist_ok=True)
base_response = requests.get(base_url, headers=headers)
base_response.encoding = 'utf-8'
# print(base_response.text,'\n=============================')
base_response.raise_for_status()
soup = BeautifulSoup(base_response.text, 'lxml')
a_body = soup.find_all('ul', id='mh-chapter-list-ol-0')[0].find_all('a')
p_body = soup.find_all('ul', id='mh-chapter-list-ol-0')[0].find_all('p')


def clean_a(a):
    a = a.replace('<a>', '')
    a = a.replace('</a>', '')
    return a


def clean_p(p):
    p = p.replace('<p>', '')
    p = p.replace('</p>', '')
    return p
# for i, j in zip(a_body, p_body):
#     tag_a.append(clean_a(i))
#     tag_p.append(clean_p(j))
# print(tag_a, tag_p)
