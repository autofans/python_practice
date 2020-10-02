import requests
import json


def main():

    kw = input("请输入要查询的城市名：")

    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"

    form_data = {
            "cname": kw,
            "pid": "",
            "keyword": kw,
            "pageIndex": "1",
            "pageSize": "300"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }

    response = requests.post(url, data=form_data, headers=headers).text

    if response == '{"Table":[{"rowcount":0}],"Table1":[]}':

        data_1 = "抱歉，未找到相关搜索结果，请重新搜索"
        print(data_1)

        file_name = kw
        with open(r"C:\Users\autof\Desktop\%s.text" % file_name, "w", encoding="utf-8") as fp:
            fp.write(data_1)

    else:
        print(response)

        data = json.dumps(response, ensure_ascii=False)

        file_name = kw
        with open(r"C:\Users\autof\Desktop\%s.text" % file_name, "w", encoding="utf-8") as fp:
            fp.write(data)


if __name__ == '__main__':
    main()
