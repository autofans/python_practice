import re

##########匹配单个字符##########

# 1，匹配某个字符
# text = "hello"
# ret = re.match("he", text)  # match函数：匹配字符串的开头
# print(ret.group())

# 2,  点.匹配任意字符
# text = "hello"
# ret = re.match(".", text)
# print(ret.group())

# 3, \d 匹配任意的数字0-9
# text = "6523"
# ret = re.match('\d', text)
# print(ret.group())

# 4, \D 匹配任意的非数字
# text = "kl"
# ret = re.match("\D", text)
# print(ret.group())

# 5, \s 匹配空白字符（\n, \t, \r, 空格）
# text = " "
# ret = re.match("\s", text)
# print(ret.group())

# 6, \w 匹配的是a-z,A-Z,数字和下划线_
# text = "152_58"
# ret = re.match("\w", text)
# print(ret.group())

# 7, \W 与\w匹配到的相反
# text = "#$$%"
# ret = re.match("\W", text)
# print(ret.group())

# 8, []组合的方式，只要满足中括号中某一个的字符，就可以匹配
# text = "4"
# ret = re.match("[a4]", text)
# print(ret.group())

##########匹配多个字符##########

# 9， + 加号 重复一次或多次前面的原子
# text = "0753-55222228"
# ret = re.match("[\d\-]+", text)
# print(ret.group())

# 10, * 可以匹配0个或者任意多个字符
# text = "0553"
# ret = re.match("\d*", text)
# print(ret.group())

# 11， ？ 问号  匹配一个或者0个（要么只有一个，要么没有）
text = "abcd"
ret = re.match("\w?", text)
print(ret.group())

