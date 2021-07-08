# 要尝试的代码
try:
    num = int(input("请输入整数："))
    print(8/num)

# 捕获异常后的代码
except ValueError:
    print("请输入整数！")
# 捕获异常后的代码
# except ZeroDivisionError:
#     print("被除数不能为0")
# 捕获未知异常后的代码
except Exception as result:
    print("未知错误 %s" % result)

# 没有抛出异常才执行的代码
else:
    print("没有抛出异常")

# 无论是否抛出异常 都执行的代码
finally:
    print("程序运行结束")

print("-" * 50)
