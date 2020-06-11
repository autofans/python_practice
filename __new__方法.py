class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

        # 创建对象时，new方法会自动被调用
        print("创建对象后会自动调用new方法")

        # 为对象分配内存空间
        instance = super().__new__(cls)

        # 必须返回对象的引用给python解析器
        return instance

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()
print(player)

player2 = MusicPlayer()
print(player2)
