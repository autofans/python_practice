class Cat:
    def __init__(self, new_name):
        print("这是一个初始化法方")
        self.name = new_name

    def eat(self):
        print("%s爱吃鱼"% self.name)

# 使用类名（）创建对象，会自动调用初始化方法__init__

tom = Cat("Tom")
tom.eat()

lazy_cat = Cat("大懒猫")
lazy_cat.eat()
