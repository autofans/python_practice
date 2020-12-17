# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 23:46
# @Author  : Liu BO
# @FileName: md5加密.py
# @Software: PyCharm
import hashlib


USER_LIST = []    # 存用户名和密码


def get_md5(data):

    obj = hashlib.md5("ihgidkjgkdhdieidn:jidje:kiFDKiheEkid%%@ki%k".encode("utf8"))

    obj.update(data.encode("utf8"))

    result = obj.hexdigest()

    return result


def register():
    print("**********用户注册**********")

    while True:
        user = input("请输入用户名：")
        if user == "N":
            return

        pwd = input("请输入密码：")
        temp = {"username": user, "password": get_md5(pwd)}
        USER_LIST.append(temp)


def login():
    print("**********用户登录**********")
    user = input("请输入用户名：")
    pwd = input("请输入密码：")

    for item in USER_LIST:
        if item["username"] == user and item["password"] == get_md5(pwd):
            return True


register()
result = login()

if result:
    print("登录成功！")
else:
    print("登录失败！！！")

