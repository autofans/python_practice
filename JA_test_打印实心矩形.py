rows = int(input("输入行数："))
i = 1  # 控制行数的循环
k = 1  # 控制列数的循环

for i in range(0, rows):
    for k in range(0, rows):
        print("*", end=" ")
        k = k + 1
    i = i + 1
    print("")
