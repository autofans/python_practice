# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 1:24
# @Author  : Liu BO
# @FileName: 搜款网视频专区01.py
# @Software: PyCharm
import requests
import re


class Spider(object):

    def __init__(self):
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                     " AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                                     "/86.0.4240.75 Safari/537.36"}

        self.file = 1

        self.keyword = int(input("请输入要爬取的类目ID："))

        self.page = int(input("请输入要爬取的页数："))

    def spider_url(self):

        # all_url = "https://www.vvic.com/gz/video/list.html?merge=1"

        url = "https://www.vvic.com/gz/video/list.html?merge=1&vcid=%d&sort=up_time-desc&currentPage=%d"\
              % (int(self.keyword), self.page)
        #
        # vid = requests.get(all_url, headers=self.header).text
        # # print(vid)
        # obj = re.compile(r'data-key="vcid" data-val="(\d+?)" class="h-item " title="(.*?)"')
        # obj_list = obj.findall(vid)
        #
        # print(obj_list)
        #
        response = requests.get(url, headers=self.header).text
        # print(response)

        video_url = re.compile(r'data-vurl="(.*?)"')

        # 视频URL
        video_data_list = video_url.findall(response)
        print(video_data_list)
        for x in video_data_list:
            print(x)
            self.video_save(x)

    def video_save(self, x):
        video_data = requests.get(url=x, headers=self.header).content
        with open(r'C:\Users\autof\Desktop\VVIC视频\%s.mp4' % self.file, "wb") as fp:
            fp.write(video_data)
            self.file += 1


def main():
    video_spider = Spider()
    video_spider.spider_url()


if __name__ == '__main__':
    vid_list = [('20000106', '连衣裙'), ('20000035', 'T恤'), ('20000389', '时尚套装'), ('20000019', '蕾丝衫/雪纺衫'), ('20000021', '牛仔裤'), ('20000018', '衬衫'), ('20000020', '休闲裤'), ('20000001', '半身裙'), ('20000006', '大码连衣裙'), ('20000129', '短外套'), ('20000038', '毛针织衫'), ('20000144', '连衣裙'), ('20000128', '牛仔短外套'), ('20000364', '背心吊带'), ('20000068', '卫衣/绒衫'), ('20000017', '毛衣'), ('20000013', '大码套装'), ('20000070', '棉衣/棉服'), ('20000025', '休闲运动套装'), ('20000000', '牛仔半身裙'), ('20000071', '风衣'), ('20000057', '打底裤'), ('20000014', '其他大码女装'), ('10000137', '低帮鞋'), ('20000148', '套装'), ('20000321', '孕妇裤/托腹裤'), ('20000078', '卫衣'), ('20000055', '旗袍'), ('20000036', '毛针织裙'), ('20000109', '衬衫'), ('20000024', '其它套装'), ('20000170', '保暖套装'), ('10000139', '凉鞋'), ('20000009', '大码裤子'), ('20000062', '保暖上装'), ('10000141', '低帮帆布鞋')]
    print(vid_list)
    main()
