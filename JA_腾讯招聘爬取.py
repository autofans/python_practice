from urllib import parse
from bs4 import BeautifulSoup
from selenium import webdriver
import time



# header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

# 每一页的URL
# https://careers.tencent.com/search.html?index=1
# https://careers.tencent.com/search.html?index=2
# https://careers.tencent.com/search.html?index=3

for i in range(1, 5):
    # index = i
    # index = {"index": index}
    # index = parse.urlencode(index)
    url = "https://careers.tencent.com/search.html?index="+str(i)
    # print(url)
    driver = webdriver.Chrome()
    driver.get(url)
    data = driver.page_source
    print(data)
    driver.close()








