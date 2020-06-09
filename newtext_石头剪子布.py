import random

# 石头（1），剪刀（2），布（3）
player = int(input("石头（1），剪刀（2），布（3）请出拳："))

computer = random.randint(1, 3)

print("你出的是%d,电脑出的是%d" % (player, computer))

# 玩家赢的三种可能：player石头 computer剪刀
#                   player剪刀 computer布
#                   player布   computer石头
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("恭喜你赢了！！！")

# 平局
elif player == computer:

    print("平局！")

else:
    print("不好意思，电脑赢了！！")

