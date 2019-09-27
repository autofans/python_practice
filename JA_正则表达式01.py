import re

str_r = "张三李四王五赵六"  # 针对字符串进行数据筛选的表达式

pat = "王五"

result = re.search(pat, str_r)

print(result)


