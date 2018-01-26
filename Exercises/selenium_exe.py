# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:07:59 2018

@author: ChiaS
"""

from selenium import webdriver
BROWSER = webdriver.Chrome()
BROWSER.get("http://www.g.cn")
open_a = BROWSER.find_element_by_link_text('google.com.hk')
driver = open_a.click()
driver.
input_text = driver.find_element_by_id('lst-ib')