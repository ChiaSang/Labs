# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:49:48 2018

@author: ChiaS
"""

import requests
import bs4
downloadPath = []
dirPath = []
fileName = []
dirName = []
subdirName = []
subhtml = []
url = 'http://data.caida.org/datasets/2013-asrank-data-supplement/'
# url = 'http://data.caida.org/datasets/2013-asrank-data-supplement/data/'
# url = 'http://data.caida.org/datasets/2013-asrank-data-supplement/extra/'


def regularizeHTML(url):
    '''RegularizeHTML'''
    html = requests.get(url)
    html.raise_for_status()
    soup = bs4.BeautifulSoup(html.text, 'lxml')
    print(soup.pre.text.encode('utf-8', 'ignore').decode('utf-8'))
    src_a = soup.find_all(name='a')
    return(src_a)


def isFile(src_a):
    '''getFile and judge the file'''
    for item in src_a[5:]:
        if '/' not in item.get('href'):
            downloadPath.append(url + item.get('href'))
            fileName.append(item.get('href'))
        else:
            dirPath.append(url + item.get('href'))
            dirName.append(item.get('href'))


def downloadFile(fileName, downloadPath):
    '''download the files'''
    for (i, j) in zip(fileName, downloadPath):
        req = requests.get(j, stream=False)
        with(open(i, 'wb')) as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)


if __name__ == '__main__':
    gethtml = regularizeHTML(url)
    isFile(gethtml)
    downloadFile(fileName, downloadPath)
    for subi in dirPath:
        subhtml = regularizeHTML(subi)
        isFile(subhtml)
        downloadFile(fileName, downloadPath)
