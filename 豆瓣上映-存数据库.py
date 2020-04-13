import requests
from lxml import etree
import pandas
import pymysql


class Spider(object):

    def __init__(self):
        # 初始化数据库连接
        self.db = pymysql.Connect(host="localhost", port=3306, user="root", password="root", database="db3", charset="utf8")
        self.cursor = self.db.cursor()
        self.sql = "delete from douban"
        self.cursor.execute(self.sql)
        self.db.commit()
        # 初始化空列表
        self.title = []
        self.score = []
        self.release = []
        self.duration = []
        self.region = []
        self.director = []
        self.actors = []

        self.url = "https://movie.douban.com/cinema/nowplaying/dongguan/"

        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
           "Referer": "https://movie.douban.com/"}

    # 先爬取所有ul标签里面的正在上映电影列表
    def ul_spider(self):

        response = requests.get(self.url, headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        ul = html.xpath('//ul[@class="lists"]')[0]
        # ul_str = etree.tostring(ul, encoding="utf-8").decode()
        # print(ul_str)
        self.li_spider(ul)

    # 然后从ul里面提取所有li标签
    def li_spider(self, ul):

        lists = ul.xpath('./li')
        # print(etree.tostring(lists[0], encoding="utf-8").decode())
        for li in lists:  # 将遍历出来的数据写入到空列表

            title = li.xpath('@data-title')
            self.title.append(title[0])

            score = li.xpath('@data-score')
            self.score.append(score[0])

            release = li.xpath('@data-release')
            self.release.append(release[0])

            duration = li.xpath('@data-duration')
            self.duration.append(duration[0])

            region = li.xpath('@data-region')
            self.region.append(region[0])

            director = li.xpath('@data-director')
            self.director.append(director[0])

            actors = li.xpath('@data-actors')
            self.actors.append(actors[0])

            # 数据写入MySQL数据库
            sql = """
            insert into douban(title,score,releases,duration,region,director,actors)values(%s,%s,%s,%s,%s,%s,%s)
            
            """
            self.cursor.execute(sql, (title, score, release, duration, region, director, actors))

        self.db.commit()
        self.db.close()

        self.data_csv()

    # 将提取的数据写入csv
    def data_csv(self):

        info_end = pandas.DataFrame({
            "电影名": self.title,
            "评分": self.score,
            "上映时间": self.release,
            "片长": self.duration,
            "制片国家/地区": self.region,
            "导演": self.director,
            "演员": self.actors
        })
        info_end.to_csv("D:\douban2.csv")


if __name__ == "__main__":

    my_spider = Spider()
    my_spider.ul_spider()

