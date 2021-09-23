input_str = input("请输入算术题：")
print(eval(input_str))

# 输入的字符串可以是下面的代码

# 打印当前目录的内容
__import__('os').system('ls')
# 创建文件
__import__("os").system("touch aaa")
# 删除文件
__import__("os").system("rm aaa")

# 上面的代码效果和下面是一样的
import os

os.system("终端命令")
