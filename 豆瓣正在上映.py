import requests
from lxml import etree
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
           "Referer": "https://movie.douban.com/"}

url = "https://movie.douban.com/cinema/nowplaying/dongguan/"

response = requests.get(url, headers=headers)
text = response.text

html = etree.HTML(text)
ul = html.xpath('//ul[@class="lists"]')[0]
# print(etree.tostring(ul, encoding="utf-8").decode("utf-8"))
lis = ul.xpath('./li')

title = []
score = []
release = []
duration = []
region = []
director = []
actors = []

for li in lis:
    title.append(li.xpath('@data-title')[0])
    score.append(li.xpath('@data-score')[0])
    release.append(li.xpath('@data-release')[0])
    duration.append(li.xpath('@data-duration')[0])
    region.append(li.xpath('@data-region')[0])
    director.append(li.xpath('@data-director')[0])
    actors.append(li.xpath('@data-actors')[0])

    info_end = pd.DataFrame({
                    "title": title,
                    "score": score,
                    "release": release,
                    "duration": duration,
                    "region": region,
                    "director": director,
                    "actors": actors
    })
    info_end.to_csv("D:\douban1.csv")


