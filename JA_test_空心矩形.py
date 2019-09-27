rows = int(input("输入行数："))
i = 1
j = 1

for i in range(0, rows):
    for j in range(0, rows):
        if i != 0 and i != rows - 1:
            if j == 0 or j == rows - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            print("*", end=" ")
        j = j + 1
    i = i + 1
    print("")
