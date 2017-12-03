#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/13/2017 3:47 PM
# @Author  : ChiaSang
# @Project : Python
# @File    : triangle


# def triangles(n):
#     i, l = 0, []
#     while i < n:
#         a = 0
#         k = []
#         for i in l:
#             k.append(a + i)
#             a = i
#             k.append(1)
#             yield k
#             l = k
#             n = n+1
# if __name__ == "__main__":
#     for t in triangles(5):
#         print(t)
def triangle(n):
    l = [1]  # 创建一个列表
    while True:
        yield l
        l = [l[x] + l[x + 1] for x in range(len(l) - 1)]  # 计算下一行中间的值
        l.insert(0, 1)  # 开头插入1
        l.append(1)  # 末尾的1
        if len(l) > 15:
            break  # 循环结束的条件


if __name__ == "__main__":
    for t in triangle(15):
        print(t)
