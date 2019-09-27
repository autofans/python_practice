import requests
import re

def you_dao(key_w):
    """
有道词典在线翻译
    :param key_w: 用户输入的关键字
    :return: 返回翻译结果给函数本身
    """
    # 构造请求头信息
    header = {"User-Agent": "Mozilla/5.0 "
                            "(Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko)"
                            " Chrome/75.0.3770.142 Safari/537.36"}

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    key = key_w

    # post请求需要提交的表单参数
    form_data = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "15645091479298",
    "sign": "c36c6b48e20d4c841a78e8266f0d9467",
    "ts": "1564509147929",
    "bv": "53539dde41bde18f4a71bb075fcf2e66",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME"
    }

    response = requests.post(url, headers=header, data=form_data)

    # 正则表达式，提取tgt和}]]}之间的任意内容，用(.*?)表示
    pat = r'"tgt":"(.*?)"}]]}'

    result = re.findall(pat, response.text)

    return result


if __name__ == "__main__":

    key_w = str(input("请输入要翻译的字或者句子："))

    you_dao(key_w)

    print((you_dao(key_w))[0])
