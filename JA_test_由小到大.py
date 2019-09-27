# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
# 然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小

# 方法1 if语句判断
# try:
#     x = int(input("输入一个整数："))
#     y = int(input("输入一个整数："))
#     z = int(input("输入一个整数："))
#
#     if x <= y <= z:
#         print(x, y, z)
#     elif x <= z <= y:
#         print(x, z, y)
#     elif y <= x <= z:
#         print(y, x, z)
#     elif y <= z <= x:
#         print(y, z, x)
#     elif z <= x <= y:
#         print(z, x, y)
#     else:
#         print(z, y, x)
# except ValueError:
#     print("请输入整数")
# except Exception as result:
#     print("未知错误 %s" % result)

# 方法2 利用list.sort()函数自动由小到大排列
try:
    x = int(input("请输入第一个整数："))
    y = int(input("请输入第二个整数："))
    z = int(input("请输入第三个整数："))

    a = [x, y, z]
    a.sort()
    print(a)
except ValueError:
    print("请输入整数")
except Exception as result:
    print("未知错误 %s" % result)




