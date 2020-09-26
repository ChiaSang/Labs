import datetime
import os
import sys

import pexpect


today = datetime.date.today().strftime('%Y%m%d')
path = "/mnt/d/Documents/DAI"+today
os.mkdir(path, 777)  # 创建目录

ip = 'vip.xiaomiqiu.com 35957'
passwd = 'ygwl@fh027'
name = 'Co-XCxuc-FH-S7803-1'


def Switch(name, ip, passwd):
    try:  # try except 防止有一个命令错误，导致程序不能进行，其实不加也可以，如果有命令没输出，下一个代码也会报错。
        more = "--More--"  # 模拟交换机出现的翻页提示
        child = pexpect.spawn('telnet %s' % ip)
        fout = open('/mnt/d/Documents/DAI'+today+'/' +
                    '%s.txt' % (name), 'wb+')
        child.logfile = fout
        child.expect('Username:')  # 提示用户登录，输入帐号，交换机不同，有所不同。
        child.sendline("admin")
        child.expect('(?i)ssword:')  # 提示输入密码
        child.sendline("%s" % passwd)
        child.expect('%s' % name)
        child.sendline("sho cpu")  # 查看cpu状态
        child.expect('%s' % name)
        child.sendline("sho temperature")  # 运行温度
        child.expect('%s' % name)
        child.sendline("sho fan")  # 风扇状态，一般输出都有2个
        child.expect('%s' % name)
        child.sendline("sho power")  # 电源状态
        child.expect('%s' % name)
        child.sendline("sho ver")  # 设备状态，为了看运行时间
        child.send('\003')
        child.expect('%s' % name)
        child.sendline("sho ip rout")  # 路由表
        while True:
            index = child.expect([more, '%s' % name])
            # child.logfile_read = sys.stdout
            if (index == 0):
                child.send(' ')
            else:
                child.sendline("sho ip interface")  # 端口状态
                break
        # while True:
        #     index = child.expect([more, '%s' % name])
        #     if (index == 0):
        #         child.send(' ')
        #     else:
        #         child.sendline("sho version")  # 版本信息
        #         break
        while True:
            index = child.expect([more, '%s' % name])
            if (index == 0):
                child.send(' ')
            else:
                child.sendline("sho logg hist")  # 历史日志
                break
        for i in range(10):
            index = child.expect([more, '%s' % name])
            child.send(' ')
            # child.send('\003')
            child.close()
            print("Check Finished!")
    except:
        Exception()
Switch(name, ip, passwd)
