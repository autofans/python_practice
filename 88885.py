import requests

from lxml import etree


class Spider(object):

    def __init__(self):

        self.begin = begin

        self.end = end

        self.c = []

        self.t = []

        self.f = []

        self.a = []

        self.en = []
        self.zhi=[]
        self.zhi_2=[]

        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

    def web_spider(self):
        """构建每一页的URL"""

        for i in range(self.begin, self.end+1):

            url = "https://airport.supfree.net/index.asp?page=%d" % i

            response = requests.get(url, headers=self.header)

            response.encoding = "gb18030"

            html = response.text

            print(html)

            data = etree.HTML(html)

            # 城市名
            citys = data.xpath('//div/table/tr')[1:]
            for x in citys:
                citys_l=x.xpath(".//td[1]//text()")[0]
                citys_2 = x.xpath(".//td[2]//text()")[0] if (len(x.xpath(".//td[2]//text()"))>0) else None
                print(citys)


                self.zhi.append(citys_l)
                self.zhi_2.append(citys_2)

        print(self.zhi)
        print(self.zhi_2)

if __name__ == "__main__":

    begin = int(input("请输入要爬取的起始页："))

    end = int(input("请输入要爬取的结束页："))

    my_spider = Spider()

    my_spider.web_spider()
