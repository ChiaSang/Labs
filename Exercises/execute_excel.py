# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 16:16:51 2018

@author: ChiaS
"""

import openpyxl
wb = openpyxl.load_workbook(r'E:\Google 云端硬盘\Doc\2#宿舍楼ip地址分配表2016.xlsx')
sheet1 = wb.sheetnames
info_sheet1 = wb['Sheet1']
for i in info_sheet1['B']:
    print(i.value)
