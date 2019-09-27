# 矩形的周长计算和面积计算
# 先定义一个矩形类
class Rectangle:
    def __init__(self, x, y):  # 设置初始化方法，传入形参x,y
        self.x = x
        self.y = y

    def get_peri(self):   # 定义周长的方法

        return (self.x + self.y) * 2  # 返回周长结果

    def get_area(self):   # 定义面积的方法

        return self.x * self.y  # 返回面积计算结果


# 用Rectangle创建一个对象
rect = Rectangle(3, 4)

# 创建出的rect对象调用Rectangle类里面定义好的方法
rect.get_peri()
print(rect.get_peri())

rect.get_area()
print(rect.get_area())

