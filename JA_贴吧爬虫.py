from urllib import request
import urllib
import time
from urllib import parse

# 构造请求头信息
header = {"User-Angent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/75.0.3770.142 Safari/537.36"}

# 分析每一页的URL规律
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0   # 第一页  (1-1)*50
#
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50  # 第二页  (2-1)*50
#
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100 # 第三页  (3-1)*50
#
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150 # 第四页  (4-1)*50

# for i in range(1, 4):
#     print("http://tieba.baidu.com/f?kw=python&ie=utf-8&pn="+str((i-1)*50))


def load_page(fullurl, filename):
    """爬取网页的函数
    :param fullurl: 完整的网址
    :param filename: 保存的文件名
    :return: 返回
    """
    print("正在下载：", filename)
    req = request.Request(fullurl, headers=header)
    response = request.urlopen(req).read()
    return response


def write_page(html, filename):
    """把爬取到的网页写入到本地的函数

    :param html: 网页
    :param filename: 保存的文件名
    """
    print("正在保存：", filename)

    with open(filename, "wb") as f:
        f.write(html)

        print("-------------------------------------------")


def tb_spider(url, begin, end):
    """构造url的函数
    :param url: url
    :param begin: 起始页数
    :param end: 结束页数
    """
    for i in range(begin, end+1):        # 利用for循环迭代遍历网页
        pn = (i-1)*50
        full_url = url + "&pn="+str(pn)  # 每次请求的完整URL
        filename = "D:/第"+str(i)+"页.html"  # 每次请求后保存的路径以及文件名

        html = load_page(full_url, filename)  # 调用爬虫，爬取网页
        write_page(html, filename)  # 把获取到的网页写入本地


if __name__ == "__main__":
    """执行的主程序"""

    kw = input("请输入贴吧名：")
    begin = int(input("请输入起始页："))
    end = int(input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    keyword = urllib.parse.urlencode({"kw": kw})
    url = url + keyword

    tb_spider(url, begin, end)

    time.sleep(10)

