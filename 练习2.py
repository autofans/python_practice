import requests
import time


def main():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"}

    url = "https://www.baidu.com/s?"
    kw = input("请输入关键词：")
    wd = {"wd": kw}

    response = requests.get(url=url, params=wd, headers=headers).text
    print(response)

    file_name = kw
    time.sleep(2)
    with open(r"C:\Users\autof\Desktop\%s.txt" % file_name, "w", encoding="utf-8") as f:
        f.write(response)


if __name__ == '__main__':
    main()