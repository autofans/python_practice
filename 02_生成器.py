def creat_num(all_num):
    a, b = 0, 1

    current_num = 0
    while current_num < all_num:

        yield a  # 如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器模板

        a, b = b, a+b
        current_num += 1


ob = creat_num(10)  # 此时creat_num创建出来的是一个生成器对象

ret = next(ob)
print(ret)

ret = next(ob)
print(ret)