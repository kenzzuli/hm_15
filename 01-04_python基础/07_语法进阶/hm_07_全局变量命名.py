# 全局变量定义在所有函数上方，就可以保证所有函数都能够正常访问每一个全局变量
gl_num = 10


gl_name = "xiaoming"
gl_title = "SISU"


def demo():

    # 如果局部变量的名字和全局变量的名字相同
    # pycharm会在局部变量下面加一条波浪线
    num = 99
    print("%d" % num)
    print("%s" % gl_name)
    print("%s" % gl_title)



# # 再定义一个全局变量
# name = "xiaoming"

demo()


# # 再定义一个全局变量
# title = "SISU"
