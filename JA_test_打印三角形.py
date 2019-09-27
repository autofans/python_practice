rows = int(input("输入行数："))
i = 1  # i控制行数
k = 1  # k控制列数
print("等腰直角三角形")
for i in range(0, rows):
    for k in range(0, rows - i):
        print("*", end=" ")  # end=" "起到不换行的作用
        k = k + 1
    i = i + 1
    print("")
