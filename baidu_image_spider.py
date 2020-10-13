# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 1:42
# @Author  : Liu BO
# @FileName: baidu_image_spider.py
# @Software: PyCharm
import requests
import re
import time


class Spider(object):

    def __init__(self):
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                     " AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                                     "/86.0.4240.75 Safari/537.36"}
        self.file = 1
        self.keyword = str(input("请输入要爬取的关键词："))
        self.page = int(input("请输入要爬取的页数：（每一页包含30张图片）"))

    def url_spider(self):
        """百度是通过Ajax动态异步加载图片，必须找到JSON文件再构造URL"""
        page = self.page * 30 - 30

        url = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9851355535789237254" \
              "&ipn=rj&ct=201326592&is=&fp=result&queryWord=%s&cl=2&lm=-1&ie=utf-8" \
              "&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%s&s=&se=" \
              "&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=%d&rn=30&gsm=1e" \
              "&1602520554150=" % (self.keyword, self.keyword, page)

        response = requests.get(url, headers=self.header).text

        obj = re.compile(r'"objURL":"(.*?)"')
        obj_list = obj.findall(response)

        for url in obj_list:
            self.decode(url)

    def decode(self, url):
        """对加密的URL进行解密"""
        str_table = {
            '_z2C$q': ':',
            '_z&e3B': '.',
            'AzdH3F': '/'
        }

        char_table = {
            'w': 'a',
            'k': 'b',
            'v': 'c',
            '1': 'd',
            'j': 'e',
            'u': 'f',
            '2': 'g',
            'i': 'h',
            't': 'i',
            '3': 'j',
            'h': 'k',
            's': 'l',
            '4': 'm',
            'g': 'n',
            '5': 'o',
            'r': 'p',
            'q': 'q',
            '6': 'r',
            'f': 's',
            'p': 't',
            '7': 'u',
            'e': 'v',
            'o': 'w',
            '8': '1',
            'd': '2',
            'n': '3',
            '9': '4',
            'c': '5',
            'm': '6',
            '0': '7',
            'b': '8',
            'l': '9',
            'a': '0'
        }

        # str 的translate方法需要用单个字符的十进制unicode编码作为key
        # value 中的数字会被当成十进制unicode编码转换成字符
        # 也可以直接用字符串作为value
        char_table = {ord(key): ord(value) for key, value in char_table.items()}

        # 先替换字符串
        for key, value in str_table.items():
            url = url.replace(key, value)
        # 再替换剩下的字符
        real_url = url.translate(char_table)

        print(real_url)
        self.write_image(real_url)

    def write_image(self, real_url):
        """将爬取到的图片写入本地"""
        try:
            print("正在爬取第%d张图片......." % self.file)

            img = requests.get(real_url, headers=self.header).content

            with open(r'C:\Users\autof\Desktop\百度图片\\%s.jpg' % self.file, "wb") as fp:
                fp.write(img)
                self.file += 1
                time.sleep(0.5)
        except requests.exceptions.ConnectionError:
            print("requests.exceptions.ConnectionError:URL失效!!!")


def main():
    img_spider = Spider()
    img_spider.url_spider()


if __name__ == '__main__':
    # print("----------百度图片爬虫 Version 1.0----------")
    # print("Author:autofans2005")
    main()

