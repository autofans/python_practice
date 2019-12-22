import json

# 将json字符串转换成python对象
json_str = '[{"username": "张三", "age": 18, "country": "china"}, {"username": "武术", "age": 23, "country": "USA"}]'

persons = json.loads(json_str)

print(type(persons))
# print(persons)

for x in persons:
    print(x)

