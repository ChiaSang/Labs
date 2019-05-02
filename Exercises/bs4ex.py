from bs4 import BeautifulSoup
import requests
r = requests.get('http://cn.bing.com')
soup = BeautifulSoup(r.text, 'lxml')
tag_a = soup.find_all('a')
for a in tag_a:
    print(a)
