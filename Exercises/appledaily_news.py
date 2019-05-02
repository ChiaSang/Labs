from bs4 import BeautifulSoup
import requests


res = requests.get('https://tw.entertainment.appledaily.com/realtime/20180913/1429593/')
soup = BeautifulSoup(res.text, 'lxml')
print(soup.select('.ndArticle_leftColumn  h1')[0].text)
print(soup.select('.ndArticle_contentBox p')[0].text)
print(soup.select('.ndArticle_creat')[0].text)