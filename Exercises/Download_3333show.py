#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2018-02-04 13:08
"""
Created on Sun Feb  4 22:25:10 2018
@author: ChiaS
爬取3333show漫画网的某个漫画的某一章
"""

import requests
import os
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

pages = 0
pages_keys = '?p='


def get_html(url):
    global html
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    html = driver.page_source
    return html


def parse(html):
    global img_len
    soup = bs4.BeautifulSoup(html, 'lxml')
    # img_src = soup.find_all('table', id='qTcms_Pic_middle')[0].find_all('img')
    img_len = soup.find_all('select', id='k_pageSelect')[0].find_all('option')
    return img_len


# def get_img_req(imgurl):
#     html = requests.get(imgurl).text


if __name__ == '__main__':
    url = 'http://www.3333show.com/rexue/552/6822.html'
    os.makedirs('downloads', exist_ok=True)
    get_html(url)
    parse(html)
    for item in img_len:
        pages += 1
        img_url = url + pages_keys + str(pages)
        fname = str(pages) + '.jpg'
        print(img_url)
        get_html(img_url)
        soup_img = bs4.BeautifulSoup(html, 'lxml')
        sub_img_src = soup_img.find_all('table', id='qTcms_Pic_middle')[
            0].find_all('img')
        print(sub_img_src[0]['src'])
        req = requests.get(sub_img_src[0]['src'], stream=True)
        imageFile = open(
            os.path.join('downloads', os.path.basename(fname)), 'wb')
        for chunk in req.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
