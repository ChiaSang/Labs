# _*_coding:utf-8_*_

import random

print("这个程序是一个猜数字的小游戏\n你有6次的机会\n")

secret = random.randint(0, 100)

print("请输入你要猜的数字\n")

score = 0

i = 0

while score != secret and i < 6:

    score = int(input())

    if score < secret:

        print("你输入的数字小了")

    elif score > secret:

        print("你输入的数字大了")

    i = i + 1

    if i == 6:
        print('''
		---------------
		6次机会已用完
		---------------
		   游戏结束
		---------------
		''');

if score == secret:
    print("恭喜你答对了！")
