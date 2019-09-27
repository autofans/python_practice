import re

# findall()  查找匹配到的所有内容，装到列表中
# finditer() 查找匹配到的所有内容，装到迭代器中，用for循环遍历取出

a = "-----hello--------------" \
    "--hello--------hello-------------------hello----" \
    "-------------hello-----------hello------" \
    "-------hello-----------"

pat = re.compile("hello")

result1 = pat.findall(a)

result2 = pat.finditer(a)

list1 = []

for i in result2:

    list1.append(i.group())

print(list1)

print(result1)

print(result2)
