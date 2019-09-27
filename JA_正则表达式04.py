import re

# 原子表
# 定义一组平等的原子
b = "13926985563"
pat = "1[3578]\d\d\d\d\d\d\d\d\d"
result = re.search(pat, b)
print(result)

c = "iksigmkspythonuidklsikggd"
pat2 = r"py[ditkl]hon"
result2 = re.search(pat2, c)
print(result2)