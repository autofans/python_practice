import requests

url = "http://dashen123.com"

header = {"User-Angent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/75.0.3770.142 Safari/537.36"}



response = requests.get(url,headers=header)

data = response.text  # test返回的是Unicode形式的数据

data2 = response.content  # content返回的是二进制格式的数据

with open("D:\dashen123.html", "wb") as f:
    f.write(data2)
print(data)

