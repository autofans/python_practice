import requests

# 使用session实现淘宝登录
header = {"User-Agent": "Mozilla/5.0 "
                            "(Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko)"
                            " Chrome/75.0.3770.142 Safari/537.36"}

# 创建session对象
ses = requests.session()

# 构造登录需要的参数
data = {"TPL_username": "autofans2005", "TPL_password": "liubo7891"}

# 通过传递账号和密码得到cookie信息
ses.post("https://login.taobao.com", data=data)

# 请求需要的页面 https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm?spm=a21bo.2017.1997525045.2.5af911d9XtzY9J
response = ses.get("https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm?spm=a21bo.2017.1997525045.2.5af911d9XtzY9J")

print(response.text)




