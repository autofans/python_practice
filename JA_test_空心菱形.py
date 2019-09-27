rows = int(input("输入边上的星星数："))
i = 1
j = 1
k = 1
for i in range(rows):
    for j in range(rows - i):
        print(" ", end=" ")
        j = j + 1
    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        k = k + 1
    print("")
    i = i + 1

for i in range(rows):
    for j in range(i):
        print(" ", end=" ")
        j = j + 1
    for k in range(2 * (rows - i)):
        if k == 0 or k == 2 * (rows - i) - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        k = k + 1
    print("")
    i = i + 1
    