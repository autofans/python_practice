
from urllib import request
from lxml import etree
from urllib import parse


class  Spider(object):

    def __init__(self):
        self.tie_ba_name = "美女"
        self.begin_page = 1
        self.end_page = 2
        self.url = "http://tieba.baidu.com/f?"
        self.header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.file_name = 1

    # 构造要爬取页面的URL
    def tie_ba_spider(self):
        for page in range(self.begin_page, self.end_page+1):
            pn = (page-1)*50
            wo = {"pn": pn, "kw": self.tie_ba_name}
            word = parse.urlencode(wo)
            url = self.url + word

            self.load_page(url)

    # 爬取页面
    def load_page(self, url):
        req = request.Request(url, headers=self.header)
        data = request.urlopen(req).read()
        html = etree.HTML(data)
        links = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')

        for link in links:
            link = "http://tieba.baidu.com" + link

            self.load_image(link)

    # 爬取每一页的a标签的子页面获得图片链接
    def load_image(self, link):
        req = request.Request(link, headers=self.header)
        data = request.urlopen(req).read()
        html = etree.HTML(data)
        links = html.xpath('//img[@class="BDE_Image"]/@src')
        for image_link in links:
            self.write_image(image_link)

    # 通过图片链接，爬取图片并保存到本地
    def write_image(self, image_link):
        print("正在爬取图片:", self.file_name)
        image = request.urlopen(image_link).read()

        file = open(r"C:\Users\autof\Desktop\img\\"+str(self.file_name)+".jpg", "wb")
        file.write(image)
        file.close()
        self.file_name += 1


if __name__ == "__main__":

    my_spider = Spider()

    my_spider.tie_ba_spider()


