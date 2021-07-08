# 计算 0 ~ 100 之间 所有 **偶数** 的累计求和结果
result = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1
print("0-100之间所有偶数之和为:%d" % result)
