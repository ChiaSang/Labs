print("输出乘法表")
i = 1
while i<=9:
    j = 1
    while j<=i:
        print("%d*%d=%d"%(i,j,i*j))
        j+=1
    print("\n")
    i = i+1
