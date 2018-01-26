# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:49:48 2018

@author: ChiaS
"""

import requests
import bs4
DOWNLOADPATH = []
DIRPATH = []
FILENAME = []
DIRNAME = []
URL = 'http://data.caida.org/datasets/2013-asrank-data-supplement/'
# URL = 'http://data.caida.org/datasets/2013-asrank-data-supplement/data/'
# URL = 'http://data.caida.org/datasets/2013-asrank-data-supplement/extra/'
#URL = 'http://data.caida.org/datasets/topology/ark/'


def regularize_html(url):
    '''regularize_html'''
    html = requests.get(url)
    html.raise_for_status()
    soup = bs4.BeautifulSoup(html.text, 'lxml')
    print(soup.pre.text.encode('utf-8', 'ignore').decode('utf-8'))
    src_a = soup.find_all(name='a')
    return(src_a)


def is_file(src_a):
    '''getFile and judge the file'''
    for item in src_a[5:]:
        if '/' not in item.get('href'):
            DOWNLOADPATH.append(URL + item.get('href'))
            FILENAME.append(item.get('href'))
        else:
            DIRPATH.append(URL + item.get('href'))
            DIRNAME.append(item.get('href'))


def download_file(filename, downloadpath):
    '''download the files'''
    for (i, j) in zip(filename, downloadpath):
        req = requests.get(j, stream=True)
        with(open(i, 'ab')) as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()


def traversal_subdir(dirpath):
    '''sub_dir'''
    for address in dirpath:
        html = regularize_html(address)
        is_file(html)


if __name__ == '__main__':
    a_html = regularize_html(URL)
    is_file(a_html)
    traversal_subdir(DIRPATH)
    while DOWNLOADPATH:
        download_file(FILENAME, DOWNLOADPATH)
