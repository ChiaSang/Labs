
from urllib.parse import urlencode
import requests

headers = {
    'Cookie': 'JSESSIONID=0f0a8d3e-d119-4ba8-8288-3c0dab38ea1e; rememberMe=up3JdTCIrafHVurgp/KJ+sLpXlgi15n0tPn/OY6MT9jDtYVXibbRV+uAE3tkPQ2oNuQmDMQVZ7575VX458+LoeQ+rYEm7eDXPPOp4aVDM5qBHjlRhm+0UIR8ZWR8NaY59NAGIzSJ3PsS9oEHwN6OhnpyQ9BJWSShe5sY7rqXLs2B6jOj1GBwfbiDL9n19oREDVg1r5ob1a65AYXl7lA5gG6lQUT9V2oFSXxV4IMQwZArdMVjLTGKydIlGusqdqohUKvUtat4RVYxRrVwwzHRQM4M3KCbMCwL3FUGd0X4TCH5uJq3fTMuAZA2vKSvRLBWJ8mY07RYS7akZ+7a/Le6VIRHITsgIg8moTEAeKjmA2EQ2DYCQqdDg0MzHsY41cBTzuvSLT2bEG+tREhPUOMM5arrVqSeaFWRxZJdIi1A8ti8/vGt35ImuttLyPfyfKCJ5fpVb3hSbD7btMXGcz36cNXdUhD5mfzSFioHq7YYyc/bge4t3trBMZEd5zmoAqJW',
    'Host': '10.179.148.2:8080',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.45 Safari/537.36 Edg/84.0.522.20',
}


def get_searchpage(key):
    data = {
        sEcho: 2
        iColumns: 14
        sColumns: , , , , , , , , , , , , ,
        iDisplayStart: 0
        iDisplayLength: 10
        'mDataProp_0': 0
        'bSortable_0': false
        'mDataProp_1': 1
        'bSortable_1': true
        'mDataProp_2': 2
        'bSortable_2': true
        'mDataProp_3': 3
        'bSortable_3': true
        'mDataProp_4': 4
        'bSortable_4': true
        'mDataProp_5': 5
        'bSortable_5': true
        'mDataProp_6': 6
        'bSortable_6': true
        'mDataProp_7': 7
        'bSortable_7': false
        'mDataProp_8': 8
        'bSortable_8': false
        'mDataProp_9': 9
        'bSortable_9': false
        mDataProp_10: 10
        bSortable_10: false
        mDataProp_11: 11
        bSortable_11: false
        mDataProp_12: 12
        bSortable_12: false
        mDataProp_13: 13
        bSortable_13: false
        iSortCol_0: 0
        sSortDir_0: asc
        iSortingCols: 1
        selectarea: 0
        selectOperation: 0
        searchkey: key
    }
    url = 'http://10.179.148.2:8080/loadOnuList?' + urlencode(data)
    r = requests.get(url, headers=headers)
    return r.text


def main():
    html = get_searchpage('44 C6 9B 00 25 E6')
    print(html)
