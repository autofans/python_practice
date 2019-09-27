from bs4 import BeautifulSoup

# 基础例子
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 解析字符串形式的html
soup = BeautifulSoup(html, "lxml")

# 根据标签名获取标签信息  soup.标签名
# print(soup.title)

# 获取标签内容
# print(soup.title.string)

# 获取标签名
# print(soup.title.name)

# 获取标签内的所有属性 与 p 标签为例
# print(soup.p.attrs)
# print(soup.p.attrs["name"])

# 获取直接子标签，得出的是一个列表 与head标签为例
# print(soup.head.contents)
# 获取直接子标签，得出的是一个生成器，要用for循环遍历出来 与head标签为例
# for i in soup.head.children:
#     print(i)
# 获取所有子标签，得出的是一个生成器，要用for循环遍历出来 与p标签为例
for x in soup.p.descendants:
    print(x)