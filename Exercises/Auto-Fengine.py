#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
import datetime
import os
import sys

today = datetime.date.today().strftime('%Y%m%d')
path = "/mnt/d/Documents/DeviceAutoCheck/"
# os.mkdir(path, 777)  # 创建目录


JIANAN_FENGINE_S7800 = {
    "host": "vip.xiaomiqiu.com",
    "port": 37417,
    "username": "admin",
    "password": "ygwl@fh027",
    "device_type": "cisco_ios",
}


net_connect = Netmiko(**cisco1)
commands = ["show cpu", "show temperat", "sho fan", "sho power", "sho ip rout", "show cloc",
           "ls", "sho ip interface", "show mem pool",  "sho devic", "show versi", "sho ip int", "sho run inc sub 8908"]
print(net_connect.find_prompt())
with open(path + '/' + today + '.txt', 'w') as f:
    for command in commands:
        info = net_connect.send_command(command)
        print("Finished!\n")
        f.write(str(info) + '\n==============================================================\n')
net_connect.disconnect()
