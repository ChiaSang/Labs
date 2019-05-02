# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 20:19:43 2017

@author: ChiaChia
"""


def is_right(n):
    aNum = str(n)
    return aNum[::-1] == aNum
print(list(filter(is_right, range(1, 100))))
