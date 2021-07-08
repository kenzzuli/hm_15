# 导入随机工具包
# 注意：在导入工具包的时候，应该将导入的语句放在文件的顶部
# 因为，这样可以方便下面的代码，在任何需要的时候，使用工具包中的工具
import random

# 1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
player = int(input("stone(1), scissor(2), cloth(3):"))
# 2. 电脑 **随机** 出拳 —— 先假定电脑只会出石头，完成整体代码功能
computer = random.randint(1, 3)
# print(computer)
# 3. 比较胜负
# # easy to understand
# if player == 1:
#     print("stone")
# elif player == 2:
#     print("scissor")
# elif player == 3:
#     print("cloth")
# if computer == 1:
#     print("stone")
# elif computer == 2:
#     print("scissor")
# elif computer == 3:
#     print("cloth")
#
# if player == computer:
#     print("equal")
# elif player == 1 and computer == 2:
#     print("you win")
# elif player == 1 and computer == 3:
#     print("you lose")
# elif player == 2 and computer ==1:
#     print("you lose")
# elif player == 2 and computer ==3:
#     print("you win")
# elif player ==3 and computer==1:
#     print("you win")
# elif player == 3 and computer == 2:
#     print("you lose")
# 石头（1）／剪刀（2）／布（3）
print("player: %d, computer: %d." % (player, computer))
# 1石头 胜 剪刀
# 2剪刀 胜 布
# 3布 胜 石头
"""
一行代码太长需分成多行
if () or () or ()
分成
if (()
        or ()
        or ()):
        
    新的语句
"""
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("player win!")
elif player == computer:
    print("one more round!")
else:
    print("computer win!")
