#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-12 11:51:46
# @Author  : ChiaSang (ChiaSang@hotmail.com)
# @Link    : https://ChiaSang.Github.io

import datetime

Pi = 3.1415926535
R = 5
V = (3 / 4.0) * Pi * R**3
print(V)

BOOK_PRICE = 24.95
DISCOUNT = 0.6
FEE = 3
BOOKS_NUM = 60
prince = BOOK_PRICE * BOOKS_NUM * DISCOUNT + 3 + BOOKS_NUM * 0.75
print(prince)

base_str = str(datetime.date.today()) + '6:52:00'
base_time = datetime.datetime.strptime(base_str, '%Y-%m-%d%H:%M:%S')
t0 = datetime.timedelta(minutes=0, seconds=0)
while True:
    stamps = input('please enter your time\n')
    if stamps is not '.':
        t0 = datetime.timedelta(
            minutes=int(stamps[0]), seconds=int(stamps[-2:])) + t0
    else:
        break
print(t0 + base_time)
