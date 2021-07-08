def demo1():
    return int(input("请输入一个整数："))


def demo2():
    print(demo1())


# 利用异常的传递性，在主程序补捕获异常，使代码整洁
try:
    demo2()
except Exception as result:
    print(result)

# demo2()
"""
从主程序调用demo2 demo又调用demo1 demo1 内部报错
异常从demo1传到demo2再传到主程序，在主程序中没有针对异常进行处理，程序被终止
Traceback (most recent call last):

  File "/Users/ken/PycharmProjects/10_异常/hm_05_异常的传递.py", line 13, in <module>
    demo2()
    
  File "/Users/ken/PycharmProjects/10_异常/hm_05_异常的传递.py", line 6, in demo2
    print(demo1())
    
  File "/Users/ken/PycharmProjects/10_异常/hm_05_异常的传递.py", line 2, in demo1
    return int(input("请输入一个整数："))
    
ValueError: invalid literal for int() with base 10: 'a'
"""
