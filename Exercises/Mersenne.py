P = int(input("请输入P\n"))
if P > 1:
    for i in range(2, P):
        if (P % 2) == 0:
            print("您输入的数字不是素数\n")
    else:
        M = 2**P - 1
        if (M % 2) == 0:
            print("不是梅尼森数字\n")
        else:
            print("是梅尼森数字\nP is {0}\nM is {1}".format(P, M))
else:
    print("输入有误")
