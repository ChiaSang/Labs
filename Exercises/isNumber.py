str1 = input("please type a str\n")
num = '0123456789'
flag = False
for c in str1:
    if c in num:
        flag = True
if flag:
    print('this str included a num\n')
else:
    print('this str excluded a num\n')
