import requests

url = "http://www.baidu.com/s?"

header = {"User-Angent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/75.0.3770.142 Safari/537.36"}

wd = {"wd": "旅游"}

response = requests.get(url, params=wd, headers=header)

data = response.text  # test返回的是Unicode形式的数据

data2 = response.content  # content返回的是二进制格式的数据

print(data2.decode())



