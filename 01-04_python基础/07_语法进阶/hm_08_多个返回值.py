def measure():
    """测量温度和湿度"""

    print("测量开始。。。")
    temp = 39
    wetness = 50
    num = 1
    print("测量结束。。。")

    # 元组-可以包含多个数据，因此可以使用元组让函数一次返回多个值
    # 可以不加括号（Python建议不加括号）
    return temp, wetness, num


# result为元组
result = measure()
print(result)

# 需要单独处理温度和湿度 - 不方便
print(result[0])
print(result[1])

# 如果函数的返回类型为元组，同时希望单独处理元组中的元素
# 可以使用多个变量，一次接收函数的返回结果
# 注意：使用多个变量接收结果时，变量的个数应和元组的元素个数一致

# ValueError: not enough values to unpack (expected 4, got 3)
# gl_temp, gl_wetness, num, hi = measure()

# ValueError: too many values to unpack (expected 2)
# gl_temp, gl_wetness = measure()

gl_temp, gl_wetness, num = measure()
print(gl_temp)
print(gl_wetness)

a = 6
b = 100
a, b = (b, a)
print(a, b)
