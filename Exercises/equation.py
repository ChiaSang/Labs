#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError("bad operator")
    if not isinstance(b, (int, float)):
        raise TypeError("bad operator")
    if not isinstance(c, (int, float)):
        raise TypeError("bad operator")
    delta = b * b - 4 * a * c
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("方程的解：", x1, x2)
    else:
        print("方程没有解")


a = int(input("请输入a\n"))
b = int(input("请输入b\n"))
c = int(input("请输入c\n"))
quadratic(a, b, c)
