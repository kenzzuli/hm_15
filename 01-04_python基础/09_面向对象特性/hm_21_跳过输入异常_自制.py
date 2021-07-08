# 如果用户输入的不是数字，会报异常
num = int(input("请输入一个整数:"))
print(num)

# 为解决异常，可以这样改写
while True:
    input_str = input("请输入一个整数:")
    if input_str.isdecimal():
        print(int(input_str))
        break
