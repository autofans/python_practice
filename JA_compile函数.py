import re

# compile函数：将正则表达式转换成内部格式，提高执行效率

a = "Python666Java"

pat1 = re.compile(r"\d+")

result = pat1.search(a)

pat2 = re.compile("python", re.I)  # re.I 模式修正符，忽略大小写

result2 = pat2.search(a)

print(result)
print(result2)

URL = r'"thumbnail":"//img.alicdn.com/imgextra/i1/0/O1CN01y3JxGT1ILFb1M0fqo_!!0-rate.jpg'

pat3 = re.compile(r'"thumbnail":"(.*?)_!!0-rate.jpg')
result3 = pat3.search(URL)
print(result3)
