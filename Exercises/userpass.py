# !usr/bin/env python
# *_coding:utf-8_*_
import sys
limit = 3
limit_count = 0
account_file = 'account.txt'
lock_file = 'lock.txt'
# ----------定义一个记录帐号的文件和记录锁定帐号的文件
while limit_count < limit:
    # 循环的次数小于3就执行循环
    username = input('please input your username\n')
    # 输入用户名
    lock_check = open(lock_file)
    # 打开一个文件赋值给lock_变量
    for line in lock_check.readlines():
        # 检查输入的username
        line = line.split()
        # 以空格为分隔，输出一个list
        if username == line:
            # 检查username是否等于文件中的值
            sys.exit("user %s" % username)
            # 条件符合执行下一步
    password = input('please input your password\n')
    # 输入密码
    f = open(account_file)
    match_flag = False
    # ----------打开账户文件进行检查，并把初始标识为置为0
    for line in f.readlines():
        user, passwd = line.strip('\n').split()
        if username == user and password == passwd:
            match_flag = True
            print('Match!', username)
            break
    f.close()
    # ----------读取文件中的账户和密码并复制给user和passwd变量
    # ----------并检查是否相等，相等标识位置为1，输出匹配，并
    # ----------关闭文件
    if match_flag is False:
        print('user unmatched!\n')
        limit_count += 1
    else:
        print('Welcome to the system!\n')
        break
    # 如果不匹配尝试次数累加1并打印不匹配，否则成功登入系统
else:
    print('your account is locked\n')
    f = open(lock_file, 'a+')
    # 注意文件的写入模式都有哪几种？
    f.write(username + '\n')
    f.close()
# 如果锁定文件存在锁定的账号就打印账号被锁定，并记录进文件
