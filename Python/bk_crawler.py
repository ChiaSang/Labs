import os
import re

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    chapter_url = 'http://www.biqukan.com/44_44297'
    chapter_req = requests.get(chapter_url)
    chapter_soup = BeautifulSoup(chapter_req.text, 'lxml')
    dlist = chapter_soup.select('div.listmain > dl > dd > a')
    chapters = chapter_soup.find_all('div', class_='listmain')
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    fname = re.search(r'我家二哈被附身了', str(download_soup)).group()
    os.makedirs(fname, exist_ok=True)
    begin_flag = False
    # 遍历dl标签下所有子节点
    for child in download_soup.dl.children:
        # 滤除回车
        if child != '\n':
            # 找到《一念永恒》正文卷,使能标志位
            if child.string == u"《我家二哈被附身了》正文卷":
                begin_flag = True
            # 爬取链接并下载链接内容
            if begin_flag == True and child.a != None:
                download_url = "http://www.biqukan.com" + child.a.get('href')
                download_name = child.string
                download_req = requests.get(download_url)
                download_req.encoding = 'gbk'
                soup_texts = BeautifulSoup(download_req.text, 'lxml')
                texts = soup_texts.find_all(id='content', class_='showtxt')
                raw_txt = BeautifulSoup(str(texts), 'lxml')
                retext = re.sub(
                    r'&1t;/p>|请记住本书首发域名：www.biqukan.com。笔趣阁手机版阅读网址：m.biqukan.com|(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', 
                    '', raw_txt.text)
                retext.replace('\xa0', '')
                print(retext)
                # with open(os.path.join(fname, os.path.basename(download_name)), 'a') as f:
                #     f.write(retext)
