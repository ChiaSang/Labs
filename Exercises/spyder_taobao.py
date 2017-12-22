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

t = time.localtime()
# 数据
DATA =[]

# def store_file(filename, txt):
#     # print"正在存储......"
#     f = open(filename, 'w')
#     f.write(txt)
#     f.close()


# 参数
find_arg = {
    'q': 'python',
    'initiative_id': 'staobaoz_%s%02d%02d' % (t[0], t[1], t[2]),
      '&ie': 'utf8'
}
search = 'go'
time_id = 'staobaoz_%s%02d%02d' % (t[0], t[1], t[2])
# print(time_id)

# 搜索页面
first_url = 'https://s.taobao.com/search?q=' + str(search)
second_url = '&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=' + str(time_id)
third_url = first_url + second_url + '&ie=utf8'
# print('third_url:\n', third_url)
r = requests.get(third_url)
print('third_url_r_url:\n{0}\n'.format(r.url))
html = r.text
# print(html)

# 分析页面
content = re.findall(r'g_page_config = (.*?)g_srp_loadCss', html, re.S)[0][:-6]


# 转换字典
content = json.loads(content)
print('{}'.format(content))
data_list = content['mods']['itemlist']['data']['auctions']

# 提取数据
for item in data_list:
    temp = {
    'title': item['title'],
    'view_price': item['view_price'],
    'view_sales': item['view_sales'],
    'view_fee': '否' if float(item['view_fee']) else '是',
    'isTmall': '是' if item['shopcard']['isTmall'] else '否',
    'name': item['nick'],
    'area': item['item_loc'],
    'detail_url': item['detail_url']
    }
    DATA.append(temp)

# 保存cookies
cookie_ = r.cookies

# 异步加载页面数据
ksts = str(int(time.time()*1000))
url = '''
https://s.taobao.com/api?_ksTS={}_208&callback=jsonp209&ajax=true&m=customized&stats_click=search_radio_all:1&q=%E5%AD%A3%E7%BE%A1%E6%9E%97&s=36&imgfile=&initiative_id=staobaoz_20171222&bcoffset=0&js=1&ie=utf8&rn={}
'''.format(ksts, md5(ksts.encode()).hexdigest())

r2 = requests.get(url, params=find_arg, cookies=cookie_)
html = r2.text
data_list = json.loads(re.findall(r'{.*}', html)[0])['API.CustomizedApi']['itemlist']['auctions']

# 提取数据
for item in data_list:
    temp = {
    'title': item['title'],
    'view_price': item['view_price'],
    'view_sales': item['view_sales'],
    'view_fee': '否' if float(item['view_fee']) else '是',
    'isTmall': '是' if item['shopcard']['isTmall'] else '否',
    'name': item['nick'],
    'area': item['item_loc'],
    'detail_url': item['detail_url']
    }
    DATA.append(temp)

# 更新cookies
cookie_ = r2.cookies
print(len(data_list))