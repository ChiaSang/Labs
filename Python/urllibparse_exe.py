# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 21:26:11 2018

@author: ChiaS
"""

from urllib.parse import urlparse
o = urlparse('https://www.google.com.hk/search?q=fiddler+xss&newwindow=1&safe=strict&dcr=0&tbs=qdr:y&ei=_RpwWr-eJYOv0gSL_5DYCw&start=30&sa=N&biw=1920&bih=959')
print(o)
