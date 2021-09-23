def input_password():
    pwd = input("请输入密码：")
    # 若密码长度大于等于8 则返回密码
    if len(pwd) >= 8:
        return pwd
    # 以下皆是密码长度小于8才会执行的代码
    ex = ValueError("密码长度不够")
    raise ex


try:
    print(input_password())
# except BaseException as result:
#     print("Base Exception==> %s" % result)
# except Exception as result:
#     print("Exception==> %s" % result)
except ValueError as result:
    print("ValueError==> %s" % result)
else:
    print("密码长度符合要求")
finally:
    print("程序执行结束")