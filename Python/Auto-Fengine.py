#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
import datetime
import os
import sys

today = datetime.date.today().strftime('%Y%m%d')
path = "/mnt/d/net/" + today + ".log"
# os.mkdir(path, 777)  # 创建目录


JIANAN_FENGINE_S7800 = {
    "host": "10.178.144.1",
    "port": 22,
    "username": "admin",
    "password": "ygwl@fh027",
    "device_type": "cisco_ios",
}

CHANGGE_FENGINE_S7800 = {
    "host": "10.178.140.1",
    "port": 22,
    "username": "admin",
    "password": "ygwl@fh027",
    "device_type": "cisco_ios",
}

LINYING_FENGINE_S7800 = {
    "host": "10.185.176.1",
    "port": 22,
    "username": "admin",
    "password": "ygwl@fh027",
    "device_type": "cisco_ios",
}

XIANGCHENG_FENGINE_S7800 = {
    "host": "10.178.136.1",
    "port": 22,
    "username": "admin",
    "password": "ygwl@fh027",
    "device_type": "cisco_ios",
}

WUGANG_FENGINE_S7800 = {
    "host": "10.113.255.1",
    "port": 22,
    "username": "admin",
    "password": "ygwl@fh027",
    "device_type": "cisco_ios",
}

YEXIAN_FENGINE_S7800 = {
    "host": "10.112.160.1",
    "port": 22,
    "username": "admin",
    "password": "ygwl@fh027",
    "device_type": "cisco_ios",
}

YUZHOU_FENGINE_S7800 = {
    "host": "10.178.123.1",
    "port": 22,
    "username": "admin",
    "password": "ygwl@fh027",
    "device_type": "cisco_ios",
}



DEVICES_LIST = [
    JIANAN_FENGINE_S7800,
    CHANGGE_FENGINE_S7800,
    LINYING_FENGINE_S7800,
    XIANGCHENG_FENGINE_S7800,
    # WUGANG_FENGINE_S7800,
    # YEXIAN_FENGINE_S7800,
    # JIAXIAN_FENGINE_S7800,
    # YUZHOU_FENGINE_S7800,
    # WUYANG_FENGINE_S7800,
]

print(path)


def detect(device):
    net_connect = Netmiko(**device)
    commands = ["show cpu", "show temperat", "sho fan", "sho power", "sho ip rout", "show cloc",
            "ls", "sho ip interface", "show mem pool",  "sho devic", "show versi", "sho ip int", "sho run inc sub 8908"]
    # print(net_connect.find_prompt())
    with open(path, 'a+') as f:
        for command in commands:
            info = net_connect.send_command(command)
            print("Finished!\n", net_connect.find_prompt())
            f.write(str(info) + '\n===========' + net_connect.find_prompt() + '===========\n')
    net_connect.disconnect()

for device in DEVICES_LIST:
    detect(device)

