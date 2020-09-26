
# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 11:34
# @Author  : ChiaSang
# @Project : Python
# @File    : funmapreduce

name = ['adam', 'LISA', 'barT']
a = []

# def isFormat(name):
#     return name[0].upper() + name[1:].lower()
# print(list(map(isFormat, name)))

# 使用map函数来实现功能

for i in name:
    forname = i[0].upper() + i[1:].lower()
    print(list(forname))
    a.append(forname)  # 把生成的字符串插入列表中
print(a)
