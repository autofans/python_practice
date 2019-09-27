# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？共有多少组无重复的三位数？
# 利用for循环迭代遍历依次取值，再利用if语句判断，最后输出结果

# 第一种方法
# count = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != k) and (i != j) and (j != k):
#                 count += 1
#                 print(i, j, k)
# print("总数是：", count)

# 第二种方法
num_list = [1, 2, 3, 4]
count = 0  # 定义整个循环执行的次数计数器
for i in num_list:
    for j in num_list:
        for k in num_list:
            if (i != j) and (i != k) and (j != k):
                count += 1  # 循环执行完一次count+1
                print(i, j, k)
print("总数是：", count)


