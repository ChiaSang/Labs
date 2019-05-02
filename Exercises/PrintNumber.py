#!/usr/bin/env python3
# _*_Coding:utf-8_*_
import sys

count = 0
while True:
    PrintNumber = int(
        input("please input the number which you want to printed\n"))
    while count < 10000:
        if PrintNumber <= count:
            if PrintNumber == count:
                print("Now {0} lines was printed in\n".format(PrintNumber))
                Choice = input("Would you want to continue the loop?(y/n)\n")
                if Choice == 'n':
                    sys.exit()
                else:
                    break
            else:
                if PrintNumber <= count:
                    print("This number has been printed in\n")
            break
        else:
            count += 1
            print(count)
