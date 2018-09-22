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


def get_html(url, args):
    '''获取页面信息'''
    # 发送请求
    web = requests.get(url, params=args)
    html = requests.get(url, params=args).text
    # 分析页面
    content = re.findall(r'g_page_config = (.*?)g_srp_loadCss', html, re.S)[0][:-6]
    # 转换字典
    content = json.loads(content)
    searchdata = content['mods']['itemlist']['data']['auctions']
    get_productioninfo(searchdata)
    COOKIES = web.cookies
    # 保存cookies


def get_productioninfo(search_list):
    '''提取数据'''
    for item_info in search_list:
        temp = {
            'title': item_info['raw_title'],
            'view_price': item_info['view_price'],
            'view_sales': item_info['view_sales'],
            'view_fee': '否' if float(item_info['view_fee']) else '是',
            'isTmall': '是' if item_info['shopcard']['isTmall'] else '否',
            'area': item_info['item_loc'],
            'name': item_info['nick'],
            'detail_url': item_info['detail_url'],
        }
        PRODUCTION_DATA.append(temp)
        COOKIES = r2.cookies


def get_more_productioninfo(pages, web_cookie):
    '''爬取剩下的页面'''
    for i in range(1, pages):
        ktsts = time.time()
        FIND_ARGS['_ksTS'] = '%s_%s' % (int(ktsts * 1000), str(ktsts)[-3:])
        FIND_ARGS['callback'] = 'jsonp%d' % (float(str(ktsts)[-3:]) + 1)
        FIND_ARGS['data-value'] = 44 * i
        url = "https://s.taobao.com/search?data-key=s&data-value=44&ajax=true&imgfile=&js=1&stats_click=search_radio_all%3A1&ie=utf8&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48".format(
            time.time())
        if i > 1:
            FIND_ARGS['s'] = 44 * (i - 1)
        r3 = requests.get(url, params=FIND_ARGS, cookies=web_cookie)
        HTML = r3.text
        SEARCH_DATA_LIST = json.loads(re.findall(
            r'{.*}', HTML)[0])['mods']['itemlist']['data']['auctions']
        get_productioninfo(SEARCH_DATA_LIST)
    COOKIES = r3.cookies


def write_into_excel(info):
    '''持久化'''
    book = xlwt.Workbook(encoding='utf-8')
    sheet01 = book.add_sheet(u'sheet1', cell_overwrite_ok=True)
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
    for i in range(len(info)):
        sheet01.write(i + 1, 0, info[i]['title'])
        sheet01.write(i + 1, 1, info[i]['view_price'])
        sheet01.write(i + 1, 2, info[i]['view_sales'])
        sheet01.write(i + 1, 3, info[i]['view_fee'])
        sheet01.write(i + 1, 4, info[i]['isTmall'])
        sheet01.write(i + 1, 5, info[i]['area'])
        sheet01.write(i + 1, 6, info[i]['name'])
        sheet01.write(i + 1, 7, info[i]['detail_url'])
    book.save(u'搜索商品{0}的结果.xls'.format(SEARCH_KEY))


if __name__ == '__main__':
    PRODUCTION_DATA = []
    COOKIES = ''
    # 构造时间串
    TIME_ARGS = time.localtime()
    # 搜索关键字
    SEARCH_KEY = 'java'
    # URL参数
    FIND_ARGS = {
        'q':
        SEARCH_KEY,
        'initiative_id':
        'staobaoz_%s%02d%02d' % (TIME_ARGS[0], TIME_ARGS[1], TIME_ARGS[2])
    }
    BASE_URL = "https://s.taobao.com/search?imgfile=&js=1&stats_click=search_radio_all%3A1&ie=utf8"
    get_html(BASE_URL, FIND_ARGS)
    ksts = str(int(time.time() * 1000))
    lurl = "https://s.taobao.com/api?_ksTS={}_208&callback=jsonp209&ajax=true&m=customized&stats_click=search_radio_all:1&q=&imgfile=&bcoffset=0&js=1&ie=utf8&rn={}".format(
        ksts,
        md5(ksts.encode()).hexdigest())
    r2 = requests.get(lurl, params=FIND_ARGS, cookies=COOKIES)
    HTML = r2.text
    SEARCH_DATA_LIST = json.loads(re.findall(r'{.*}', HTML)[0])['API.CustomizedApi']['itemlist']['auctions']
    # 异步加载页面数据
    get_productioninfo(SEARCH_DATA_LIST)
    # 更新cookies
    get_more_productioninfo(10, COOKIES)
    write_into_excel(PRODUCTION_DATA)
