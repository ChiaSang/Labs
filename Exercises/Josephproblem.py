num = []
del_num = []

for i in range(1, 11):
    num.append(i)
    for j in range(len(num)):
        if (j%2==0):
            del_num.append(j)
print(del_num)