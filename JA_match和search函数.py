import re

# match函数和search函数

# match函数：匹配字符串的开头
# search函数：匹配任意位置
# 这两个函数都是只匹配一次，匹配到就不再往后匹配

a = "javapythonjavahtmljs"

pat = re.compile("java")

print(pat.match(a))