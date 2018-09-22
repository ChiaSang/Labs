# /usr/bin/env python3
# !-*-coding:utf-8-*-
# A first Python script
import sys
print(sys.platform)
print(2**10)
x = 'Spam!'
print(x * 8)
# 打印一个数字
for i in range(0, 110, 10):
    print("this is a number", i)
# 这是一个猜数字的程序
Number = 515
while True:
    Score = int(input("Please type a integer \n"))
    if Score == Number:
        print("Your score is right")
    elif Score > Number:
        print("Your score is older than number")
    else:
        print("Your score is less than number")
