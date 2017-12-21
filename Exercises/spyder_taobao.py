# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 17:29:47 2017

@author: ChiaS
"""

import re
import time
import requests

t = time.localtime()


def store_file(filename, txt):
    # print"正在存储......"
    f = open(filename, 'w')
    f.write(txt)
    f.close()


# 参数
find_arg = {
    'q': 'python',
    'initiative_id': 'staobaoz_%s%02d%02d' % (t[0], t[1], t[2])
}


# 搜索页面
first_url = 'https://s.taobao.com/search?'
r = requests.get(first_url, params=find_arg)
print(r.url, r.content)
html = r.text

#html.encoding = 'utf-8'
print(html)

# 分析页面
# content = re.findall(r'', )
