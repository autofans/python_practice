import requests
import re
import xlsxwriter



def main():
    # 爬取的URL
    url = "https://changyongdianhuahaoma.51240.com/"

    # UA伪装
    headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                          " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }

    response = requests.get(url, headers=headers).text
    # print(response)

    pat1 = r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>'  # 服务名称
    pat2 = r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>'  # 电话号码

    server_name = re.compile(pat1)  # 服务名称
    server_tel = re.compile(pat2)  # 电话号码

    data1 = server_name.findall(response)
    data2 = server_tel.findall(response)

    # print(data1)
    # print(data2)

    # 写入EXCEL
    workbook = xlsxwriter.Workbook(r"C:\Users\autof\Desktop\123.xlsx")
    worksheet = workbook.add_worksheet()

    for i in range(len(data1)):
        # print(i)
        # print(data1[i])

        worksheet.write("A%d" % int(i+1), data1[i])

    for x in range(len(data2)):

        worksheet.write("B%d" % int(x+1), data2[x])

    workbook.close()


if __name__ == '__main__':
    main()
