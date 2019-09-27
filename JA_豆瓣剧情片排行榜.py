import re
import requests
import xlsxwriter



header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=50"

response = requests.get(url, headers=header).text

pat1 = r'{"rating":\["(.*?)","\d+"\]'

pat2 = r'"title":"(.*?)"'

pattern1 = re.compile(pat1)

pattern2 = re.compile(pat2, re.I)

data1 = pattern1.findall(response)

data2 = pattern2.findall(response)

# print(data1, data2)

# result = []

# 创建表格
workbook = xlsxwriter.Workbook("demo1.xlsx")
worksheet = workbook.add_worksheet()

for i in range(len(data2)):
    print("排名:", "", str(i+1), "\t", "电影名:", str(data2[i]).ljust(30), "\t豆瓣评分:", "", str(data1[i]))
    # result.append("排名："+str(i+1)+"电影名："+data2[i] + "豆瓣评分："+data    1[i])

    # 写入数据
    worksheet.write("A"+str(i+1), "排名"+str(i+1))
    worksheet.write("B"+str(i+1), "电影名")
    worksheet.write("C"+str(i+1), data2[i])
    worksheet.write("D"+str(i+1), "豆瓣评分")
    worksheet.write("E"+str(i+1), data1[i])

# print(result)

workbook.close()







