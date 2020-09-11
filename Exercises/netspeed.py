from io import BytesIO
from urllib.request import urlopen

import chardet
import pycurl

url = 'https://v.qq.com'

html = urlopen(url).read()
print(chardet.detect(html))


buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.VERBOSE, False)
c.setopt(c.URL, url)
c.setopt(c.WRITEDATA, buffer)
c.setopt(pycurl.USERAGENT,"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36")    #配置请求HTTP头的User-Agent
c.setopt(pycurl.DNS_CACHE_TIMEOUT,0) #设置保存DNS信息的时间，默认为120秒 
c.getinfo(pycurl.REDIRECT_TIME)     #重定向所消耗的时间
c.perform()
body = buffer.getvalue()

http_code = c.getinfo(pycurl.HTTP_CODE) #返回的HTTP状态码
dns_resolve = c.getinfo(pycurl.NAMELOOKUP_TIME) #DNS解析所消耗的时间
http_conn_time = c.getinfo(pycurl.CONNECT_TIME) #建立连接所消耗的时间
http_pre_trans = c.getinfo(pycurl.PRETRANSFER_TIME) #从建立连接到准备传输所消耗的时间
http_start_trans = c.getinfo(pycurl.STARTTRANSFER_TIME) #从建立连接到传输开始消耗的时间
http_total_time = c.getinfo(pycurl.TOTAL_TIME) #传输结束所消耗的总时间
http_size_download = c.getinfo(pycurl.SIZE_DOWNLOAD) #传输结束所消耗的总时间
http_header_size = c.getinfo(pycurl.HEADER_SIZE) #HTTP头大小
http_speed_downlaod = c.getinfo(pycurl.SPEED_DOWNLOAD) #平均下载速度
http_redirect = c.getinfo(pycurl.REDIRECT_TIME)     #重定向所消耗的时间
http_uplaod = c.getinfo(pycurl.SIZE_UPLOAD)       #上传数据包大小
http_speed_upload = c.getinfo(pycurl.SPEED_UPLOAD) #上传速度
c.close()


print ('HTTP响应状态：%-4d' %http_code)
print ('DNS解析时间： %-.2f ms' %(dns_resolve*1000))
print ('建立连接时间： %-.2f ms' %(http_conn_time*1000))
print ('准备传输时间： %-.2f ms' %(http_pre_trans*1000))
print ("传输开始时间： %-.2f ms" %(http_start_trans*1000))
print ("传输结束时间： %-.2f ms" %(http_total_time*1000))
print ("定向所消耗的时间： %-.2f ms" %(http_redirect*1000))
print ("下载数据包大小： %-4d bytes/s" %http_size_download)
print ("上传数据包大小： %-4d bytes/s" %http_uplaod)
print ("HTTP头大小： %d bytes/s" %http_header_size)
print ("平均下载速度： %d k/s" %(http_speed_downlaod/1024))
print ("平均上传速度： %d k/s" %(http_speed_upload/1024))


for i in range(0,100):
    url = 'https://v.qq.com'

    # html = urlopen(url).read()
    # print(chardet.detect(html))


    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.VERBOSE, False)
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(pycurl.USERAGENT,"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36")    #配置请求HTTP头的User-Agent
    # c.setopt(pycurl.DNS_CACHE_TIMEOUT,0) #设置保存DNS信息的时间，默认为120秒 
    # c.getinfo(pycurl.REDIRECT_TIME)     #重定向所消耗的时间
    c.perform()
    body = buffer.getvalue()
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME) #建立连接所消耗的时间
    print ('建立连接时间： %-.2f ms' %(http_conn_time*1000))

# print(body.decode('utf-8'))
