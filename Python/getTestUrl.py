import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://touduyu.com'
markup = requests.get(url)
html = BeautifulSoup(markup.content, 'lxml')
# html.prettify()
net_info = {}
net_info1 = []
for item in html.find_all(class_="bg-hover"):
    for net_name in item.find_all("h4"):
               # print(net_name.text)
        net_info1.append(net_name.text)
        for net_intr in item.find_all("p"):
            print(net_intr.text)
            # net_info[net_name.text] = net_intr.text

            for net_add in item.find_all("a"):
                print(net_add['href'])
                net_info[net_name.text] = net_add['href']
                # print(net_add.get_text())
                # print(str(net_add).strip('\\'))

                with open('web_info.txt', 'a') as f:
                    f.write(net_add['href'] + '\n')
                    f.close()
    
print(net_info)



        # for item in html.find_all(class_="info"):