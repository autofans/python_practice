class Game(object):

    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    # 游戏帮助信息（静态方法）
    @staticmethod
    def show_help():
        print("游戏帮助信息: 让僵尸进入大门！")

    # 查看历史最高分（类方法）
    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    # 开始游戏的方法
    def start_game(self):
        print("%s 开始游戏啦。。。" % self.player_name)


# 查看游戏帮助信息
Game.show_help()

# 查看历史最高分
Game.show_top_score()

# 创建游戏对象
game = Game("小明")
game.start_game()
