# 题目：将一个列表的数据复制到另一个列表中

# 方法1
a = [1, 2, 3]
b = []
b.extend(a)
print(b)


# 方法2
# a = [1, 2, 3]
# b[len(b):] = a
# print(b)

# 方法3
# a = [1, 2, 3]
# b = a[:]
# print(b)

