import requests
import bs4
from urllib.request import urlopen
downloadPath = []
downloadName = []
downloadDir = []
url = 'http://data.caida.org/datasets/2013-asrank-data-supplement/'
#url = 'http://data.caida.org/datasets/2013-asrank-data-supplement/data/'
#url = 'http://data.caida.org/datasets/2013-asrank-data-supplement/extra/'
html = requests.get(url)
html.raise_for_status()
file_size = int(urlopen(url).info().get('Content-Length', -1))
soup = bs4.BeautifulSoup(html.text, 'lxml')
print(soup.pre.text.encode('utf-8', 'ignore').decode('utf-8'))
a_address = soup.find_all(name='a')
for item in a_address[5:]:
    downloadPath.append(url + item.get('href'))
    downloadName.append(item.get('href'))
for filename in downloadName:
    if '/' not in filename:
        for downloadAddress in downloadPath:
            req = requests.get(downloadAddress, stream=False)
            with(open(filename, 'ab')) as f:
                for chunk in req.iter_content(chunk_size=512):
                    if chunk:
                        f.write(chunk)
            print(filename)
    else:
        downloadDir.append(filename)
