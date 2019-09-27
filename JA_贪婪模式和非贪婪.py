import re

# 贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配；
# 非贪婪模式：在整个表达式匹配成功的前提下，尽可能的少匹配；
# python里默认是贪婪模式；

a = "aa<div>test1</div>bb<div>test2</div>cc"

pat1 = r"<div>.*</div>"     # 贪婪模式

print(re.search(pat1, a))


b = "aa<div>test1</div>bb<div>test2</div>cc"

pat2 = r"<div>.*?</div>"    # 非贪婪模式

print(re.search(pat2, b))


c = "aa<div>test1</div>bb<div>test2</div>cc"

pat3 = r"<div>(.*?)</div>"    # 非贪婪模式2

print(re.findall(pat3, c))
