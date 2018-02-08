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

# import random

# print("这个程序是一个猜数字的小游戏\n你有6次的机会\n")

# secret = random.randint(0, 100)

# print("请输入你要猜的数字\n")

# score = 0

# i = 0

# while score != secret and i < 6:

#     score = int(input())

#     if score < secret:

#         print("你输入的数字小了")

#     elif score > secret:

#         print("你输入的数字大了")

#     i = i + 1

#     if i == 6:
#         print('''
# 		---------------
# 		6次机会已用完
# 		---------------
# 		   游戏结束
# 		---------------
# 		''')

# if score == secret:
#     print("恭喜你答对了！")
