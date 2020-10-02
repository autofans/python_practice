import re

#####################################匹配单个字符#################################################

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

#########################################匹配多个字符#######################################################

# 9， + 加号 重复一次或多次前面的原子
# text = "0753-55222228"
# ret = re.match("[\d\-]+", text)
# print(ret.group())

# 10, * 可以匹配0个或者任意多个字符
# text = "0553"
# ret = re.match("\d*", text)
# print(ret.group())

# 11， ？ 问号  匹配一个或者0个（要么只有一个，要么没有）
# text = "abcd"
# ret = re.match("\w?", text)
# print(ret.group())

# 12， {3} 花括号里面的数字表示要匹配多少个字符
# text = "abcd"
# ret = re.match("\w{3}", text)
# print(ret.group())

# 13,  {1,5} 花括号里面的数字是匹配1-5个字符
# text = "abcdef"
# ret = re.match("\w{1,4}", text)
# print(ret.group())

##############################################小案例########################################################

# 验证手机号码
# text = "13965366366"
# ret = re.match("1[34578]\d{9}", text)
# print(ret.group())

# 验证邮箱
# text = "hidnki_@qq.com"
# ret = re.match("\w+@[a-z0-9]+\.[a-z]+", text)
# print(ret.group())

# 验证URL     (http|https|ftp) | 竖线表示或者， \s表示匹配空白字符，[^\s]表示非空白字符
# text = "https://www.bilibili.com/video/av63494239/?p=42"
# ret = re.match("(http|https|ftp)://[^\s]+", text)
# print(ret.group())

# 匹配18位身份证，最后一位可以是数字或者X，或者x
# text = "44152565254715689X"
# ret = re.match("\d{17}[\dxX]", text)
# print(ret.group())

#  $ 表示以....结尾   表示以@163.com结尾的才能匹配到
# text = "sddss@163.com"
# ret = re.match("\w+@163.com$", text)
# print(ret.group())

##############################分组group###################################################
# text = "apple is price $99,orange is price $89"
# ret = re.search(".*(\$\d+).*(\$\d+)", text)
# print(ret.group())
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(1, 2))
# print(ret.groups())  # groups()是将所有的子分组都提取出来，相当于group(1,2,3,......)

# findall函数，将所有满足条件的值提取出来，返回的是一个列表
# text = "apple is price $99,orange is price $89"
# ret = re.findall("\$\d+", text)
# print(ret)

# sub()函数 替换满足条件的字符，比如，将$99和$89替换成0
# text = "apple is price $99,orange is price $89"
# ret = re.sub("\$\d+", "0", text)
# print(ret)

# html = """
# <p>4、 负责问题排查、调试、性能调优等开发相关工作。
# <br>
# <br>【岗位要求】<br>1、1年以上工作经验，本科以上学历，计算机相关专业；
# <br>2、良好的编程开发能力，熟悉Python爬虫开发和Web开发；
# <br>3、熟悉MySQL与SQL Server部署、开发与维护；
# <br>4、对新技术敏感，乐于研究新技术，具有良好的团队合作精神
# <br>5、熟悉.NET开发或Java开发。<br><br>【梵讯给您提供】
# <br>☞入职即享有的薪酬福利体系：五险一金，年终奖金，带薪年假/病假，入职免费体检，年度免费体检，周末双休等；
# <br>☞最专业的互联网培训：5-10天带薪岗前培训，不定期的在职培训、外部培训，致力于打造学习型的组织团队；
# <br>☞快速晋升发展的机会，公平透明的选拔机制：公司处于快速发展期，岗位空缺多，晋升机会大；
# <br>☞公平开放，积极坦诚的企业文化：生日party，团建活动，户外拓展，公司提供丰富的下午茶（玫瑰花茶、立顿专供）咖啡茶饮，每周五俱乐部活动（乒乓球、篮球、羽毛球、狼人杀、瑜伽）；
# <br>☞办公环境：新装修的5A级办公环境，免费娱乐设施随意用。
# </p>
# """
# ret = re.sub("<.+?>", "", html)
# print(ret)

#  split函数 分割： 返回也是一个列表
# text = "hello world ni hao"
# ret = re.split("[^a-zA-Z]", text)
# print(ret)

# compile函数：将正则表达式提前编译，提高执行效率，还可以注释
# text = "the number is 20.53"
# t = re.compile(r"""
#     \d+  # 小数点前面的数字
#     \.?  # 小数点
#     \d*  #小数点后面的数字
# """, re.VERBOSE)
# ret = re.search(t, text)
# print(ret.group())