#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:47:07 2018
@author: ChiaSang
"""
import re
import sqlite3

import requests
from bs4 import BeautifulSoup


def insert_sql(fname, tname):
    sql1 = 'CREATE TABLE IF NOT EXISTS ' + tname + ' (id integer primary key, name TEXT, flag char(2))'
    sql2 = 'INSERT INTO ' + tname + ' (id, name, flag) VALUES(?,?,0)'
    cu.execute(sql1)
    with open(fname, 'r') as xssf:
        i = 0
        for line in xssf.readlines():
            coon.execute(sql2, (i, line))
            i += 1
        coon.commit()
    return tname


# 创建测试用例数据库并返回表名


def detect_xss(url, xss, id):
    html = requests.get(url)
    html.encoding = 'gbk'
    web = html.text
    # print('detect--------', html.text, type(web))
    # pattern = re.compile(r'%s'%(xss))
    # regex = pattern.search(web)
    # print(regex)
    if xss in web:
        print('XSS漏洞存在\n', xss)
        coon.execute(
            'UPDATE XSS_CheatSheets SET flag = 1 where id = %s' % str(id))
        coon.commit()
    else:
        print('XSS漏洞不存在')


def get_flzxurl(flzx_url):
    response = requests.get(flzx_url)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find(name='td', class_='hui')
    get_pages = pages.find(name='p').text[27:28]  #获取页面数量
    for page in range(1, int(get_pages) + 1):
        print('第{0}页,共{1}页'.format(page, int(get_pages)))
        pages_url = next_url + str(page)
        response = requests.get(pages_url)
        response.encoding = 'gbk'
        soup = BeautifulSoup(response.text, 'lxml')
        a_tag = soup.find(name='div', class_='r_d_c_c_n')  #获取a的父级div标签
        for ele_li in a_tag.find_all(name='li'):  #获取a（包含在li中）的数量
            href_li = ele_li.find(name='a').get('href')  # 找到a并打印
            xss_url = base_url + href_li
            print('返回地址', xss_url)
            return xss_url


if __name__ == '__main__':
    base_url = 'http://192.168.6.173/'
    url = 'http://192.168.6.173/online_pass.asp'
    flzx_url = 'http://192.168.6.173/flzx.asp'
    next_url = 'http://192.168.6.173/flzx.asp?Page='
    lyinfo = {
        'title': 'title'.encode('gbk'),
        'name': 'XSS测试'.encode('gbk'),
        'sh': '0',
        'qq': '12345678',
        'mail': 'example@example.com',
        'tel': '13012345678',
        'body': 'Python自动化xss测试!'.encode('gbk'),
        'VerifyCode': '0',
    }
    coon = sqlite3.connect("xss.db")
    cu = coon.cursor()
    insert_sql('D:/Documents/Python/Exercises/xxsfilterbypass.txt',
               'XSS_CheatSheets')
    cu.execute("select * from XSS_CheatSheets")
    values = cu.fetchall()
    j = 0
    for i in values:
        lyinfo['body'] = i[1]
        response = requests.post(url, data=lyinfo, allow_redirects=True)
        response.encoding = 'gbk'
        print('输入XSS', i[1])
        xss_url = get_flzxurl(flzx_url)
        detect_xss(xss_url, str(i[1]), j)
        j = j + 1
        print(j)
    coon.close()
