class MusicPlayer(object):

    # 定义一个(类属性)记录第一个被创建对象的引用（分配内存空间的地址）
    instance = None

    def __new__(cls, *args, **kwargs):

        # 判断类属性instance是否是空对象
        if cls.instance is None:
            # 调用父类方法，为第一个对象分配内存空间
            cls.instance = super().__new__(cls)

        # 必须返回类属性保存的对象引用（分配的内存地址）
        return cls.instance


# 创建多个对象（留意内存地址）
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)

