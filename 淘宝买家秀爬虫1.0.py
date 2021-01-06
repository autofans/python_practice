# -*- coding: utf-8 -*-
# @Time    : 2021/1/1 1:22
# @Author  : Liu BO
# @FileName: 淘宝买家秀爬虫1.0.py
# @Software: PyCharm
import parsel
import requests
import re
import time


class Spider(object):

    def __init__(self):

        self.good_id = int(input("请输入商品ID:"))

        self.userNumId = int(input("请输入userNumId（网页按F12，在Parameters里找到）:"))

        self.page_num = int(input("请输入页码:"))

        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                     " AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                                     "/86.0.4240.75 Safari/537.36",
                      "cookie": "cna=We4EGGVxNTsCAXQSpSGf1qJ8; lgc=autofans2005; tracknick=autofans2005; enc=kuVsm98AkQyOi3ALKfjXra2VP9zOli0zWP9w9vbJVTpFhvWYBGEP6%2BN9J3W8sX3gDn46HjwRbwT16XduoWCFiQ%3D%3D; thw=cn; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; hng=CN%7Czh-CN%7CCNY%7C156; t=d3cbe1637a85268faefc3330892ebb96; mt=ci=0_1; _m_h5_tk=2c948f8e8aab8140533e23c96c163a6b_1609695916393; _m_h5_tk_enc=f3de748fb8701704b0434ca8c3a64236; v=0; _tb_token_=fe65e0a97310e; xlly_s=1; _samesite_flag_=true; cookie2=1100c5874562a4636367201135110e42; sgcookie=E100RlMmSPR6ogW%2FIScOUk7zirkBxhPc82D%2BljXekMMc%2BIv7U%2F%2BdmiJ5jXGUmQvrTxL%2B8LPgjsN2uYYE2lxdAJUQrw%3D%3D; unb=1597522064; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&cookie14=Uoe0ZNCwUR6NmQ%3D%3D&existShop=true&cookie21=Vq8l%2BKCLivbdjeuVIQ%2Fdkg%3D%3D&pas=0; uc3=id2=UoTV6yz7bz6d2Q%3D%3D&nk2=AmRw0xWdTnwaB%2B8U&lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dCuAAn5j0fgkeFurc%3D; csg=497bfbc0; cookie17=UoTV6yz7bz6d2Q%3D%3D; dnk=autofans2005; skt=883885a3899669ba; existShop=MTYwOTY4NzY0Mw%3D%3D; uc4=nk4=0%40AI%2FDpERfvcMjSWY0G9W%2BJLt1ozaq41Y%3D&id4=0%40UOx%2FUw0B1cNwGxLXdi%2ByrMBrNgWg; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=541; _nk_=autofans2005; cookie1=AQCeSTGbC8gUluz3WTrVFe4vp0RLDI%2BWMhsSE%2FBCM20%3D; x5sec=7b22726174656d616e616765723b32223a223436323031396434323163373937343939633063616537623563353465343130434c7a4d782f3846454a434f6e2f6a657834474e6f774561444445314f5463314d6a49774e6a51374d513d3d227d; tfstk=c-IdB_qYq5Vn99pO3wUiPxuafXTdaFNJ1vOo2-rxMrLzoXDsBscOmiBpIy9S9heO.; l=eBSCuOQ4Oo5RpmjvBO5Zlurza7792CRfGsPzaNbMiInca1PlMixlVNQ2lYvpydtj_tfvkeKrJmGnAReWyTzdgETNJqHzH13XnxJ6-; isg=BLq63J7AscQGDj1W7hcR5qKXC-Dcaz5F8fJe48S30syFt17xrf8kVfCBB0trJ7bd",
                       "referer": "https://item.taobao.com/item.htm?spm=a1z0k.7386009.0.d4919233.4b4e3b89h67jem&id=%s&_u=t2dmg8j26111" % self.good_id,
                       "accept": "*/*"

                       }

        self.params = {"auctionNumId": self.good_id,  # 商品ID
                       "userNumId": self.userNumId,   # userNumId（网页按F12，在Parameters里找到）
                       "pageSize": "20",
                       "currentPageNum": self.page_num,  # 评论区页码
                       "callback": "jsonp_tbcrate_reviews_list",
                       "ua": "098#E1hvIpvRvPOvUvCkvvvvvjiWP2cOgjnHRLzy1jljPmP96jD8n2Fw6jtnPFcO6jiWdvhvm6E21BpDvhCEeNKBmvhvLhPvqQmFd5lNjV5v1EIfjVDQpJ2ybdiQpcX2waZOejaHjV5v1CAXjVDQpas9bdiQpcaCwaZOej3nOyTxfBeKNxYkLixre4tYL7QHYWoUvpvVpyUUCCAfuvhvmhCvCnDyYa3ZKvhv8hCvvvvvvhCvphvwv9vvpT1vpCQmvvChNhCvjvUvvhBGphvwv9vvBjQvvpvVphhvvvvv29hvCvvvMMGgvpvhphvvv8OCvvBvpvpZ39hvChCCvvvVvpvjzn147rGUe29CvvBvpvvv9vhv2n1wCVJqzYswzbTZ7F9CvvBvpvvv",
                       }
        self.file = 1

    def spider_url(self):
        # 详情页URL
        url = "https://item.taobao.com/item.htm?spm=a1z0k.6846577.0.0.7a4f3b89sYPha5&id=633476325808&_u=t2dmg8j26111"

        # 评论区URL
        feed_rate = "https://rate.taobao.com/feedRateList.htm"

        response = requests.get(url=feed_rate, params=self.params, headers=self.header).text
        # print(response)

        # 正则表达式 抓取买家秀URL（_400X400.jpg前面的才是原图）
        ret = re.compile(r'"url":"(//img.alicdn.com/imgextra/.*?_!!0-rate.jpg)_400x400.jpg"')
        url_list = ret.findall(response)
        # print(url_list)

        for img_url in url_list:
            # print(img_url)
            full_url = "https:" + img_url
            # print(full_url)
            self.img_save(full_url)

    def img_save(self, full_url):

        print("正在  借用  第%d张 买家秀......." % self.file)

        img_data = requests.get(url=full_url, headers=self.header).content

        with open(r'D:\买家秀\%s.jpg' % self.file, "wb") as fp:
            fp.write(img_data)
            self.file += 1
            time.sleep(1.5)


def main():
    web_tao = Spider()
    web_tao.spider_url()


if __name__ == '__main__':
    main()
