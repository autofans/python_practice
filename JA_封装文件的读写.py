def save_file(boy, girl, count):
    file_name_boy = "boy_" + str(count) + ".txt"
    file_name_girl = "girl_" + str(count) + ".txt"

    boy_file = open(file_name_boy, "w")
    girl_file = open(file_name_girl, "w")

    boy_file.writelines(boy)
    boy_file.close()
    girl_file.writelines(girl)
    girl_file.close()

def split_file(file_name):
    f = open("D:\pythontest.txt")

    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:6] != "======":   # 如果each_line不等于======，那么对字符串进行分割操作
            (role, line) = each_line.split("：", 1)
            if role == "大明":
                boy.append(line)
            if role == "阿美":
                girl.append(line)
        else:
            save_file(boy, girl, count)

            boy = []
            girl = []

            count += 1

    save_file(boy, girl, count)

    f.close()

split_file("D:\pythontest.txt")

