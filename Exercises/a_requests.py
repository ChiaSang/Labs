import requests


#----------------------------------------------------------------------
def getHTMLtext(url):
    """"""
    try:
        response = requests.get(url)
        a = response.raise_for_status()
        b = response.status_code
        response.encoding = r.apparent_encoding
        return response.text
    except:
        return "错误"

if __name__ == "__main__":
    url = 'http://www.baidu.com'
    getHTMLtext(url)