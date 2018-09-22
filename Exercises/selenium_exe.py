# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:07:59 2018

@author: ChiaS
"""

from selenium import webdriver
BROWSER = webdriver.Firefox()
BROWSER.get("http://www.g.cn")
OPEN_A = BROWSER.find_element_by_link_text('google.com.hk')
DRIVER = OPEN_A.click()
