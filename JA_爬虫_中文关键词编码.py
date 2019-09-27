from urllib import request
import urllib

url = "http://www.baidu.com/s?"

kw = {"wd": "北京"}

# 构造url编码
kww = urllib.parse.urlencode(kw)

url = url + kww

# 创建请求对象
req = request.Request(url)

# 发送请求
response = request.urlopen(req).read().decode()

print(response)
