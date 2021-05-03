# 通过send来唤醒生成器
def fibonacci(n):
    i = 0
    a, b = 0, 1
    while i < n:
        tmp = yield a  # 通过send可以在唤醒时向断点传入一个附加数据
        print(tmp)
        a, b = b, a + b
        i += 1
    return "Done"


f = fibonacci(10)

# ret = f.send("aa")
# TypeError: can't send non-None value to a just-started generator
# 对于第一次迭代的生成器，如果使用send方法，里面的值必须是None

# 第一次，还没执行到print(msg)就停了
ret = next(f)
print(ret)  # 0

# 第二次，此次没有发送额外消息，msg为None，会打印出来，然后返回新的值
ret = next(f)  # None
print(ret)  # 1

# 第三次，此次发送额外消息，msg为"fuck"，会打印出来，然后返回新的值
ret = f.send("fuck")  # fuck
print(ret)  # 1

# 第四次，无额外消息，msg为None，会打印出来，然后返回新的值
ret = f.__next__()  # None
print(ret)  # 2
