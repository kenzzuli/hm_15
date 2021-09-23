"""
**需求**

* 1. 编写一个打招呼 `say_hello` 的函数，封装三行打招呼的代码
* 2. 在函数下方调用打招呼的代码
"""
name = "peter"


def say_hello():
    """函数的文档注释
    say hello to us"""
    i = 1
    while i <= 3:
        print("hello")
        i += 1

print(name)
say_hello()
print(name)
