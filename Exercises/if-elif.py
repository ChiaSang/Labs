#!/usr/bin/env python
# -*- coding:utf-8 -*-
height = float(input("请输入小明的身高(单位：米)\n"))
weight = float(input("请输入小明的体重(单位：千克)\n"))
BMI = weight / (height**2)
print("小明的BMI为", BMI)
if BMI < 18.5:
    print("过轻")
elif 18.5 < BMI < 25:
    print("正常")
elif 25 < BMI < 28:
    print("过重")
elif 28 < BMI < 32:
    print("肥胖")
elif 32 < BMI:
    print("严重肥胖")
else:
    print("错误")
