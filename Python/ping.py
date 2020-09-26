#!/usr/bin/env python
#_*_ coding:utf8 _*_

import datetime
import re
import subprocess
import time
from datetime import datetime


def check_alive(ip,count=1,timeout=1):
        '''
        ping网络测试,通过调用ping命令,发送一个icmp包，从结果中通过正则匹配是否有100%关键字，有则表示丢包，无则表示正常.
        '''
        cmd = 'ping -c %d -w %d %s' % (count,timeout,ip)

        p = subprocess.Popen(cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True
        )

        result = p.stdout.read()
        text = '@@@@@' + str(run_time) + '@@@@@' + '-----------------------' + str(sequence) + '\n' + result + '***********************************************************\n'
        # with open('recording.txt', 'a') as f:
        #     f.write(text)
        regex = re.findall('100% packet loss',result)
        if len(regex) == 0:
                # run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                t1 = datetime.datetime.now()
                t1 = t1.strftime("%Y-%m-%d %H:%M:%S")
                # text = '@@@@@' + str(run_time) + '@@@@@' + '-----------------------' + str(sequence) + '\n' + result + '***********************************************************\n'
                with open('recording.txt', 'a') as f:
                    f.write(text)
                print "\033[31m%s UP\033[0m" % (ip)
        else:
                errors_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                t2 = datetime.datetime.now()
                t2 = t2.strftime("%Y-%m-%d %H:%M:%S")
                # offset = subtime(t2, t1)
                # flag = '------------------OFFSET------------------' + str(offset) + '\n'
                print "\033[32m%s DOWN\033[0m" % (ip)
                with open('recording_errors.txt', 'a') as f:
                    f.write(text)
                    # f.write(flag)


if __name__ == "__main__":
    sequence = 0
    while True:
        run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # t1 = datetime.datetime.now()
        # t1 = t1.strftime("%Y-%m-%d %H:%M:%S")
        # localtime = time.asctime( time.localtime(time.time()) )
        # format_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sequence = sequence + 1
        check_alive('8.8.8.8')
        time.sleep(0.5)
        # with file('ip.txt','r') as f:
                # while True:
                    # for line in f.readlines():
                    #     ip = line.strip()
                    #     check_alive(ip)         #执行函数功能调用
                    #     time.sleep(1)
