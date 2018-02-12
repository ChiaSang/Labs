# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:54:26 2018

@author: ChiaS
"""

import tushare as ts
d600848 = ts.get_h_data('600848', start='2018-01-01', end='2018-01-31')
print(d600848)
