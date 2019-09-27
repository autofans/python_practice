from selenium import webdriver
from lxml  import etree
import time
import requests
url = "http://www.htqyy.com/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                        " (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
# req = requests.get(url, headers=header).text
# print(req)

driver = webdriver.Chrome()

driver.get(url)

data = driver.page_source

driver.close()