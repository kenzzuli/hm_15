def input_password():
    pwd = input("请输入密码：")
    if len(pwd) < 8:
        # 创建一个Exception异常类的实例 使用错误信息字符串作为参数
        invalid_password_error = Exception("密码长度不够")
        # 抛出异常
        raise invalid_password_error
    else:
        return pwd



"""
print(input_password())

Traceback (most recent call last):
  File "/Users/ken/PycharmProjects/10_异常/hm_06_抛出异常.py", line 12, in <module>
    print(input_password())
  File "/Users/ken/PycharmProjects/10_异常/hm_06_抛出异常.py", line 7, in input_password
    raise invalid_password_error
抛出的异常类型为 Exception 错误信息为 密码长度不够
Exception: 密码长度不够
"""
try:
    print(input_password())
# 上面函数定义抛出的异常是Exception异常类的对象，所以这里要捕获的异常类也是Exception
# result是捕获的异常的错误信息字符串
except Exception as result:
    print(result)
else:
    print("没有抛出异常，密码符合要求")
finally:
    print("程序运行结束")
