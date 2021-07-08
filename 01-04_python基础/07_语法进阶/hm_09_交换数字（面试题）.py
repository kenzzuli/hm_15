a = 6
b = 100
print(a, b)

# 解法1 使用临时变量
c = a
a = b
b = c
print(a, b)

# 解法2 不使用临时变量 (利用二者的和）
a = a + b
b = a - b
a = a - b
print(a, b)

a = a - b  # 利用二者的差
b = a + b
a = b - a
print(a, b)

# 解法3 Python特有
# a, b = (b, a)
# 等号右侧是一个元组，只不过是把括号省略了
a, b = b, a
print(a, b)
