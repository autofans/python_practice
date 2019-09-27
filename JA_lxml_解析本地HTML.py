from lxml import etree

a = etree.parse("D:\332.html")  # 获取本地HTML文档

result = etree.tostring(a)

print(a)
