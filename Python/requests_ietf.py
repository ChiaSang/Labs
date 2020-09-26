import requests

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        return 'False'


if __name__ == "__main__":
    url = 'http://www.ietf.org'
    getHTMLText(url)