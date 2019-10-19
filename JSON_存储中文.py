import json

persons = [
    {
        'username':'张三',
        'age': 18,
        'country': 'china'
    },
    {
        'username': '武术',
        'age': 23,
        'country': 'USA'
    }
]

# 存中文时候要填参数enconding="uft-8"和ensure_ascii=False才不会乱码
with open("persons.json", "w", encoding="utf-8") as fp:
    json.dump(persons, fp, ensure_ascii=False)
