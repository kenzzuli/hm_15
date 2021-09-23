"""
1. 定义布尔型变量 `has_ticket` 表示是否有车票
2. 定义整型变量 `knife_length` 表示刀的长度，单位：厘米
3. 首先检查是否有车票，如果有，才允许进行 **安检**
4. 安检时，需要检查刀的长度，判断是否超过 20 厘米
   * 如果超过 20 厘米，提示刀的长度，不允许上车
   * 如果不超过 20 厘米，安检通过
5. 如果没有车票，不允许进门
"""
has_ticket = bool(int(input("Do you have ticket? 0 for no, 1 for yes:")))
if has_ticket:
    print("ticket checked, please do security check.")
    knife_length = int(input("the length of the knife:"))
    if knife_length > 20:
        print("the length of your knife is %d, you are not allowed to aboard." % knife_length)
    else:
        print("welcome aboard!")
else:
    # 大哥先买票
    print("please buy a ticket first.")
