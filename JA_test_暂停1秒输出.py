# 题目：暂停一秒输出。
#
# 程序分析：使用 time 模块的 sleep() 函数

import time

a = [100, 200, 300, 400, 500, 600]

for i in a:
    print(i)
    time.sleep(1)
