import json

# 从文件中读取json
with open("persons.json", "r", encoding="utf-8") as fp:
    persons = json.load(fp)
    print(type(persons))
    for x in persons:
        print(x)
