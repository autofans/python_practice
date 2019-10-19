import json

# 将python对象转换成json字符串
# 在python中，只有基础的数据类型才能转换成json格式的字符串，比如，int float str list dict tuple
persons = [
    {
        'username':'zhiming',
        'age': 18,
        'country': 'china'
    },
    {
        'username': 'xiaoxue',
        'age': 23,
        'country': 'USA'
    }
]

json_str = json.dumps(persons)

print(type(json_str))

print(json_str)
