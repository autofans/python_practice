# 题目：暂停一秒输出，并格式化当前时间

import time
import datetime

time.sleep(1)

Time = datetime.datetime.now()

print(Time.strftime("%Y-%m-%d %H:%M:%S"))

