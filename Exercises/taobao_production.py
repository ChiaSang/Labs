#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 17:29:47 2017

@author: ChiaS
"""

import re
import time
import json
from hashlib import md5
import requests
import xlwt

# 数据
PRODUCTION_DATA = []

TIME_ARGS = time.localtime()
# 搜索关键字
SEARCH_KEY = 'sony'
# 参数
FIND_ARGS = {
    'q':
    SEARCH_KEY,
    'initiative_id':
    'staobaoz_%s%02d%02d' % (TIME_ARGS[0], TIME_ARGS[1], TIME_ARGS[2])
}
# 搜索页面
BASE_URL = "https://s.taobao.com/search?imgfile=&js=1&stats_click=search_radio_all%3A1&ie=utf8"
# 发送请求
WEB = requests.get(BASE_URL, params=FIND_ARGS)
HTML = requests.get(BASE_URL, params=FIND_ARGS).text
# 分析页面
CONTENT = re.findall(r'g_page_config = (.*?)g_srp_loadCss', HTML, re.S)[0][:-6]
# 转换字典
CONTENT = json.loads(CONTENT)
SEARCH_DATA_LIST = CONTENT['mods']['itemlist']['data']['auctions']
def clean_spans(s):
    s = s.replace('<span class=H>', '')
    s = s.replace('</span>', '')
    return s
# 提取数据
for item in SEARCH_DATA_LIST:
    temp = {
        'title': clean_spans(item['title']),
        'view_price': item['view_price'],
        'view_sales': item['view_sales'],
        'view_fee': '否' if float(item['view_fee']) else '是',
        'isTmall': '是' if item['shopcard']['isTmall'] else '否',
        'area': item['item_loc'],
        'name': item['nick'],
        'detail_url': item['detail_url'],
    }
    PRODUCTION_DATA.append(temp)
# 保存cookies
COOKIE_ = WEB.cookies

# 异步加载页面数据
ksts = str(int(time.time() * 1000))
url = "https://s.taobao.com/api?_ksTS={}_208&callback=jsonp209&ajax=true&m=customized&stats_click=search_radio_all:1&q=&imgfile=&bcoffset=0&js=1&ie=utf8&rn={}".format(
    ksts, md5(ksts.encode()).hexdigest())

r2 = requests.get(url, params=FIND_ARGS, cookies=COOKIE_)
HTML = r2.text
SEARCH_DATA_LIST = json.loads(re.findall(
    r'{.*}', HTML)[0])['API.CustomizedApi']['itemlist']['auctions']

# 提取数据
for item in SEARCH_DATA_LIST:
    temp = {
        'title': clean_spans(item['title']),
        'view_price': item['view_price'],
        'view_sales': item['view_sales'],
        'view_fee': '否' if float(item['view_fee']) else '是',
        'isTmall': '是' if item['shopcard']['isTmall'] else '否',
        'area': item['item_loc'],
        'name': item['nick'],
        'detail_url': item['detail_url'],
    }
    PRODUCTION_DATA.append(temp)

# 更新cookies
COOKIE_ = r2.cookies
# 爬取剩下的页面
for i in range(1, 5):
    ktsts = time.time()
    FIND_ARGS['_ksTS'] = '%s_%s' % (int(ktsts * 1000), str(ktsts)[-3:])
    FIND_ARGS['callback'] = 'jsonp%d' % (float(str(ktsts)[-3:]) + 1)
    FIND_ARGS['data-value'] = 44 * i
    url = "https://s.taobao.com/search?data-key=s&data-value=44&ajax=true&imgfile=&js=1&stats_click=search_radio_all%3A1&ie=utf8&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48".format(
        time.time())
    print(url)
    if i > 1:
        FIND_ARGS['s'] = 44 * (i - 1)
    r3 = requests.get(url, params=FIND_ARGS, cookies=COOKIE_)
    HTML = r3.text
    SEARCH_DATA_LIST = json.loads(re.findall(
        r'{.*}', HTML)[0])['mods']['itemlist']['data']['auctions']

    # 数据
    for item in SEARCH_DATA_LIST:
        temp = {
            'title': clean_spans(item['title']),
            'view_price': item['view_price'],
            'view_sales': item['view_sales'],
            'view_fee': '否' if float(item['view_fee']) else '是',
            'isTmall': '是' if item['shopcard']['isTmall'] else '否',
            'area': item['item_loc'],
            'name': item['nick'],
            'detail_url': item['detail_url'],
        }
        PRODUCTION_DATA.append(temp)
COOKIE_ = r3.cookies
# 持久化
f = xlwt.Workbook(encoding='utf-8')
sheet01 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
# 写标题
sheet01.write(0, 0, '商品名')
sheet01.write(0, 1, '标价')
sheet01.write(0, 2, '购买人数')
sheet01.write(0, 3, '是否包邮')
sheet01.write(0, 4, '是否天猫')
sheet01.write(0, 5, '地区')
sheet01.write(0, 6, '店名')
sheet01.write(0, 7, 'url')
# 写内容
for i in range(len(PRODUCTION_DATA)):
    sheet01.write(i + 1, 0, PRODUCTION_DATA[i]['title'])
    sheet01.write(i + 1, 1, PRODUCTION_DATA[i]['view_price'])
    sheet01.write(i + 1, 2, PRODUCTION_DATA[i]['view_sales'])
    sheet01.write(i + 1, 3, PRODUCTION_DATA[i]['view_fee'])
    sheet01.write(i + 1, 4, PRODUCTION_DATA[i]['isTmall'])
    sheet01.write(i + 1, 5, PRODUCTION_DATA[i]['area'])
    sheet01.write(i + 1, 6, PRODUCTION_DATA[i]['name'])
    sheet01.write(i + 1, 7, PRODUCTION_DATA[i]['detail_url'])

f.save(u'搜索%s的结果.xls' % SEARCH_KEY)
