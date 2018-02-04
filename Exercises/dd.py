# 2018-02-04 13:08
import requests
import os
import bs4
url = 'http://www.3333show.com/rexue/552/6822.html'
os.makedirs('dd', exist_ok=True)
headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }
num = 1
args = {
    '?p': num
}
# while not url.endswith('#'):
print('Downloading pag %s...' % (url))
res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
comicElem = soup.find_all('table', id='qTcms_Pic_middle')[0].find_all('img')
comic_len = soup.find_all('select',id='k_pageSelect')
print(comic_len)
print(len(comic_len) - 1)
    # if comicElem == []:
    #     print('Can\'t find comic images')
    # else:
    #     comicUrl = comicElem[0].get('src')
    #     print('Downloading image %s...' % (comicUrl))
    #     res = requests.get(comicUrl)
    #     res.raise_for_status()
    #     imageFile = open(
    #         os.path.join('dd', os.path.basename(comicUrl)), 'wb')
    #     for chunk in res.iter_content(100000):
    #         imageFile.write(chunk)
    #     imageFile.close()
    # prevLink = soup.select('a[rel="prev"]')[0]
    # url = 'http://xkcd.com' + prevLink.get('href')
