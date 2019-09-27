import re

# split() 按照能够匹配的子串将字符串分割后返回列表
# sub() 用于替换

a = "张三，，，李四，，，，，王五，，，，，，，赵六"

pat1 = re.compile(r"，+")

result1 = pat1.split(a)

print(result1)


b = "hello 123,hello 456"

pat2 = re.compile(r"\d+")

result2 = pat2.sub("666", b)

print(result2)
