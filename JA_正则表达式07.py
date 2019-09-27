import re

# 多个表达式

a = "13956544155"
b = "020-3658445"

pat = r"1[358]\d{9}|\d{3}-\d{7}"

print(re.search(pat, b))
