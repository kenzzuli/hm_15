# 全部遍历后，执行else语句
for num in [1, 2, 3]:
    print(num)
else:
    print("全部遍历结束")

# 未能全部遍历，循环体内部使用break跳出循环，则不会执行else语句
for num in [1, 2, 3]:
    if num != 2:
        print(num)
    else:
        break
else:
    print("未全部遍历")