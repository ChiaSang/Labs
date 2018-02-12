#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 13:57
# @Author  : ChiaSang
# @Project : Python
# @File    : is_palindrome


def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return n
    else:
        pass


def is_right(n):
    aNum = str(n)
    return aNum[::-1] == aNum


output = filter(is_palindrome, range(1, 1000))
print(list(output))
print(list(filter(is_right, range(1, 100))))
