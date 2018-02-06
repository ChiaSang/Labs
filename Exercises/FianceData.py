# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 18:42:01 2018

@author: ChiaS
"""

import requests
import re
import json
import pandas as pd
from datetime import date
import time

#from pylab import *
#from scipy.cluster.vq import *


def retrieve_quotes_historical(stock_code):
    '''Get the Fiance Data and find the historical price.'''
    quotes = []
    url = 'http://finance.yahoo.com/quote/{0}/history?p={1}'.format(
        stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return [item for item in quotes if 'type' not in item]


def create_df(stock_code):
    '''Create a DataFrame.'''
    quotes = retrieve_quotes_historical(stock_code)
    list1 = []
    for i in range(len(quotes)):
        x = date.fromtimestamp(quotes[i]['date'])
        y = date.strftime(x, '%Y-%m-%d')
        list1.append(y)
    quotesdf_ori = pd.DataFrame(quotes, index=list1)
    listtemp = []
    for i in range(len(quotesdf_ori)):
        temp = time.strptime(quotesdf_ori.index[i], "%Y-%m-%d")
        listtemp.append(temp.tm_mon)
    tempdf = quotesdf_ori.copy()
    tempdf['month'] = listtemp
    totalclose = tempdf.groupby('month').close.mean()
    df_totalclose = pd.DataFrame(totalclose)
    df_totalclose['code'] = stock_code
    return df_totalclose


dfAXP_totalclose = create_df('AXP')
dfKO_totalclose = create_df('KO')
AKdf = dfAXP_totalclose.append(dfKO_totalclose)
AKdf['month'] = AKdf.index
print(AKdf)
