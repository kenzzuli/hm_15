# 模块的搜索顺序，先搜索当前目录，再搜索Python的系统目录
# 如果当前目录有random.py 就不会搜索系统目录 此时再调用randint方法会提示模块中没有这个方法
# 所以 我们在开发中，模块的名字千万不要和系统模块的名字相同
import random

# rand = random.randint(0, 10)
# print(rand)
print(random.__file__)
# 此时输出
# /Users/ken/PycharmProjects/11_模块/random.py
