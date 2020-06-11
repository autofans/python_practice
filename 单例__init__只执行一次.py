class MusicPlayer(object):

    # 定义一个(类属性)记录第一个被创建对象的引用（分配内存空间的地址
    instance = None

    # 定义一个（类属性）记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 判断类属性instance是否是空对象
        if cls.instance is None:
            # 调用父类方法，为第一个对象分配内存空间
            cls.instance = super().__new__(cls)

        # 必须返回类属性保存的对象引用（分配的内存地址）
        return cls.instance

    def __init__(self):

        # 判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return

        # 如果没有执行过，再执行初始化动作
        print("初始化")

        # 修改类属性的标记
        MusicPlayer.init_flag = True


# 创建多个对象（留意内存地址）
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
