import requests
from lxml import etree

url = "https://www.qiushibaike.com/text/"

header = {"User-Angent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/75.0.3770.142 Safari/537.36"}

response = requests.get(url, headers=header).text

html = etree.HTML(response)

list_1 = html.xpath('//div')

# print(list_1)

# print(list_1[0].text)

for i in list_1:
    with open("D:\qiu.txt", "a") as f:
        f.write(str(i.text))
        f.write("\n")
        f.write("-----------------------------------------------------------------------------------------------")









