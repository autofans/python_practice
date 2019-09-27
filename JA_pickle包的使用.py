import pickle

list1 = [58, 79, "密码"]

pickle_file = open("D:\\list1.pickle", "wb")  # 在D盘创建一个名为list1.pickle的文件，与二进制方式wb写入
pickle.dump(list1, pickle_file)  # 用pickle.dump方法将list1里面的字符串导入到pickle_file文件中
pickle_file.close()  # 关闭文件

pickle_file = open("D:\\list1.pickle", "rb")  # 调用D盘里面之前创建的文件，与二进制rb读取
list2 = pickle.load(pickle_file)
pickle_file.close()
print(list2)
