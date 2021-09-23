i = 0
while i <= 5:
    # continue  跳出当次循环 继续判断
    if i == 3:
        # 一定要确保循环的计数发生更改 不然就是死循环
        i += 1
        continue
    print(i)
    i += 1
print("over")
