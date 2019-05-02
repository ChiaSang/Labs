# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 20:10:07 2017

@author: ChiaChia
"""


def is_odd(n):
    return n % 2 == 1
list(filter(is_odd, range(1, 100)))
print(list)
