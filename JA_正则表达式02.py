import re

# 匹配通用字符
# \w 任意字母/数字/下划线 小写w
# \W 和小写w相反
# \d 十进制数字
# \D 除了十进制数字以外的值
# \s 空白字符 小写s
# \S 非空白字符 大写S

b = "13929411922"

pat = "\d\d\d\d\d\d\d\d\d\d\d"

result = re.search(pat, b)

print(result)
