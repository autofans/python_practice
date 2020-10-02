import requests
import json


def main():

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }

    list_id = list()  # 存所有企业ID
    list_data = list()  # 存所有企业详情

    # 先获取各企业对应的ID
    full_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"

    for page in range(1, 2):
        x = str(page)

        form_data = {
                "on": "true",
                "page": x,
                "pageSize": 15,
                "productName": "",
                "conditionType": 1,
                "applyname": "",
                "applysn": ""
        }

        json_str = requests.post(url=full_url, data=form_data, headers=headers).json()

        for dic in json_str["list"]:
            list_id.append(dic["ID"])

    # 拿到ID后再获取各企业详情数据
    de_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"

    for i in list_id:

        form_data = {
                "id": i
        }

        det_data = requests.post(url=de_url, data=form_data, headers=headers).json()

        list_data.append(det_data)

    # 存到指定位置
    file_data = json.dumps(list_data, ensure_ascii=False)
    file_name = "药品监督"
    with open(r'C:\Users\autof\Desktop\%s.text' % file_name, "w", encoding="utf-8") as fp:
        fp.write(file_data)
    print(list_data)


if __name__ == '__main__':
    main()