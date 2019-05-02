# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 12:11:57 2018

@author: ChiaS
"""

import bs4
import requests
url = '''https://www.google.com.hk/search?
safe=strict&source=hp&ei=krxqWvO2G4v28gX08bf4CA&q=Google&oq=Google
&gs_l=psy-ab.3..0i131k1l3j0l7.1745.2727.0.3059.6.5.0.1.1.0.162.311.0j2.2.0....0...1c.1j4.64.psy-ab..3.3.317....0.16kC8bgX0Rs'''
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
sel_mark = soup.select('.r a')
print('=============================所选元素\n', sel_mark)
for i in range(len(sel_mark)):
    print('属性:', sel_mark[i].attrs)
    print('文本:', sel_mark[i].getText())
    print('链接:', sel_mark[i].get('href'))
    print('===============分割==============')
