import re

# 分组（）

a = "!!!f*$$^python$#^*())**&^java!@#!!@#!#***aaa13929411922bbb&&&*^$$$#@@@@@@"

pat1 = r"(python).{0,}(java).{0,}(1[368]\d{9})"

pat2 = r"aaa(.*?)bbb"

print(re.search(pat1, a).group(1))

print(re.findall(pat2, a))
