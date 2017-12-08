mylist = range(1, 11)
del_num = []
x = 0
i = 0
while len(del_num) < 11:
    if x > 10:
        x = 0
    if (mylist[i] not in del_num):
        i = i + 1
        if (i % 2 == 0):
            print(mylist[x])
            del_num.append(mylist[x])
            i = 0
    x = x + 1
