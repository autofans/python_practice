import requests
import json
import pandas as pd
import time


def page():

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
                "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
                "Accept": "application/json, text/javascript, */*; q=0.01"
    }

    url_1 = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
    url_2 = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

    for x in range(1, 10):
        form_data = {
                        "first": "true",
                        "pn": str(x),
                        "kd": "python"
        }

        session = requests.Session()  # 维持会话

        session.get(url_1, headers=headers, timeout=3)
        cookies = session.cookies  # 通过session函数获取第一个URL的cookies

        response = requests.post(url_2, data=form_data, cookies=cookies, headers=headers, timeout=3)
        time.sleep(5)
        json_t = response.text
        # print(json_t)

        #  将json字符串转换成python对象 字典
        result = json.loads(json_t)
        # print(result)

        info = result["content"]["positionResult"]["result"]

        for i in info:
            positionName_list.append(i["positionName"])
            companyFullName_list.append(i["companyFullName"])
            companyShortName_list.append(i["companyShortName"])
            companySize_list.append(i["companySize"])
            industryField_list.append(i["industryField"])
            salary_list.append(i["salary"])

        # print(positionName_list)
        # print(companyFullName_list)
        # print(companyShortName_list)
        # print(companySize_list)
        # print(industryField_list)
        # print(salary_list)

    info_end = pd.DataFrame({
                "公司全称": companyFullName_list,
                "公司简称": companyShortName_list,
                "经营领域": industryField_list,
                "公司规模": companySize_list,
                "需求工作职位": positionName_list,
                "月薪水平": salary_list
    })
    info_end.to_csv("D:\lagou.csv")


if __name__ == "__main__":

    positionName_list = []
    companyFullName_list = []
    companyShortName_list = []
    companySize_list = []
    industryField_list = []
    salary_list = []
    page()
