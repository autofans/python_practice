import re
# 匹配数字，中文，英文
# 数字 [0-9]
# 英文 [a-z]或[A-Z]
# 中文 [\u4e00-\u9fa5]

d = "!$%$^**&张三()(^%*(())*&*boy^^%&^%23%$$$#*&^@@@"

pat1 = r"[\u4e00-\u9fa5][\u4e00-\u9fa5]"

pat2 = r"[a-z][a-z][a-z]"

pat3 = r"[0-9][0-9]"

result1 = re.search(pat1, d)
result2 = re.search(pat2, d)
result3 = re.search(pat3, d)

print(result1)
print(result2)
print(result3)


