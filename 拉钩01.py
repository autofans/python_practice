import requests
import time
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Accept': 'application/json, text/javascript, */*; q=0.01'
}
url_start = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
url_parse = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

data = {
    ' first': 'true',
    'pn': 1,
    'kd': 'python'
}
session = requests.Session()  #会话维持
session.get(url_start, headers=headers, timeout=3)
cookie = session.cookies
res = requests.post(url_parse, headers=headers, cookies=cookie, data=data, timeout=3)
# print(res.text)
time.sleep(5)
res.encoding = res.apparent_encoding #apparent_endoding可以根据网页内容分析出编码方式，比encoding更加准确
result = json.loads(res.text)
info = result["content"]["positionResult"]["result"]
print(info)

