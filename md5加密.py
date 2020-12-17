# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 23:46
# @Author  : Liu BO
# @FileName: md5加密.py
# @Software: PyCharm
import hashlib


def get_md5(data):

    obj = hashlib.md5("ihgidkjgkdhdieidn:jidje:kiFDKiheEkid%%@ki%k".encode("utf8"))

    obj.update(data.encode("utf8"))

    result = obj.hexdigest()

    return result


v = get_md5("234555")

print(v)

