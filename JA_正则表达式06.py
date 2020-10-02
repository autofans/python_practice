import re

# 匹配固定次数

a = "265845652"

pat1 = r"\d{6}"    # {n}前面的原子出现了n次

pat2 = r"\d{8,}"   # {8,}前面的原子至少出现n次

pat3 = r"\d{7,9}"  # {n,m}前面的原子出现次数介于n-m之间

print(re.search(pat1, a))
