def collatz(number):
    if (number % 2) == 0:
        print("这是偶数")
        print(number)
        return(number // 2)
    else:
        print("这是奇数")
        print(number)
        return((3 * number + 1))


number = int(input("请输入一个数字\n"))
collatz(number)
