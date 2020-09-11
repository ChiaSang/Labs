#!/usr/bin/env python

"""
This runs a command on a remote host using SSH. At the prompts enter hostname,
user, password and the command.
"""

import getpass
import os

import pexpect

user = 'admin'
host = 'vip.xiaomiqiu.com'
password = 'ygwl@fh027'
name = 'Co-XCxuc-FH-S7803-1'
command = 'sho version'


def ssh_command(user, host, password):
    """
    This runs a command on the remote host. This could also be done with the
    pxssh class, but this demonstrates what that class does at a simpler level.
    This returns a pexpect.spawn object. This handles the case when you try to
    connect to a new host and ssh asks you if you want to accept the public key
    fingerprint and continue connecting.
    """
    ssh_newkey = 'Are you sure you want to continue connecting'
    # 为 ssh 命令生成一个 spawn 类的子程序对象.
    child = pexpect.spawn('ssh %s@%s -p 37417' % (user, host))
    i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'password: '])
    # 如果登录超时，打印出错信息，并退出.
    if i == 0:  # Timeout
        print('ERROR!')
        print('SSH could not login. Here is what SSH said:')
        # print(child.before, child.after)
        return None
    # 如果 ssh 没有 public key，接受它.
    if i == 1:  # SSH does not have the public key. Just accept it.
        child.sendline('yes')
        child.expect('password: ')
        i = child.expect([pexpect.TIMEOUT, 'password: '])
        if i == 0:  # Timeout
            print('ERROR!')
            print('SSH could not login. Here is what SSH said:')
            # print(child.before, child.after)
            return None
    # 输入密码.
    child.sendline(password)
    fout = open('/mnt/d/Documents/a.txt', 'wb+')
    child.logfile = fout
    child.expect('Co-XCxuc-FH-S7803-1')
    child.sendline('show version')
    # print(child.before, child.after)
    child.send('chr(32)')
    child.expect('Co-XCxuc-FH-S7803-1')
    # print(child.before, child.after)
    # return child

ssh_command(user, host, password)