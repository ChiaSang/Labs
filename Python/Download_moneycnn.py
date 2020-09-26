# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 23:02:11 2018

@author: ChiaS
"""

import re

import requests


def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile(
        'class="wsod_symbol">(.*)<\/a>.*<span.*">(.*)<\/span>.*\n.*class="wsod_stream">(.*)<\/span>'
    )
    dji_list_in_text = re.findall(search_pattern, r.text)
    return dji_list_in_text


dji_list = retrieve_dji_list()
for item in dji_list:
    print(item)
