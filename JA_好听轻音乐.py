import re
import requests
import time

# 第一页url
# http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20
# 第二页url
# http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
# 第三页url
# http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20
#
# 歌曲URL
# http://www.htqyy.com/play/33
# 歌曲资源所在的真实URL
# http://f2.htqyy.com/play7/33/mp3/8

page = int(input("Which page number do you want to crawl："))

header = {"User-Angent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/75.0.3770.142 Safari/537.36"}
song_id = []
song_name = []

for i in range(0, page):
    url = "http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"+&pageSize=20"

    html = requests.get(url)

    str_r = html.text

    pat1 = r'title="(.*?)" sid'
    pat2 = r'sid="(.*?)"'

    id_list = re.findall(pat2, str_r)
    name_list = re.findall(pat1, str_r)

    song_id.extend(id_list)
    song_name.extend(name_list)

    for j in range(0, len(song_id)):
        song_url = "http://f2.htqyy.com/play7/"+str(song_id[j])+"/mp3/8"
        song_name2 = song_name[j]

        data = requests.get(song_url, headers=header).content

        print("正在下载第", j+1, "首")

        with open("D:\\轻音乐爬取\\{}.mp3".format(song_name2), "wb") as f:
            f.write(data)

        time.sleep(0.5)







