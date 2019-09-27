import requests

url = "http://www.baidu.com"

response = requests.get(url).content.decode()

print(response)
