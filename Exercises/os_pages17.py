#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/22 18:36
# @Author  : ChiaSang
# @Project : Python
# @File    : os_pages17
import sys
import os
if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print('[-]'+filename + 'does not exist')
        exit(0)
    if not os.access(filename, os.R_OK):
        print('[-]'+filename+'access denied')
        exit(0)
    print('[+]Reading Vulnerabilities From:'+filename)
print("这是Python绝技的第17页的练习题")


