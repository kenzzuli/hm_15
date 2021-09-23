xiaoming = {"name": "xiaoming"}

# 取值
print(xiaoming["name"])
# 在取值时，如果key不存在，程序会报错！
# print(xiaoming["name123"])

# 增加/修改
# 如果key不存在，会新增键值对
xiaoming["age"] = 18
# 如果key存在，会修改键值对
xiaoming["name"] = "Peter"

# 删除
xiaoming.pop("name")
# 删除键值对时，如果指定的key不存在，会报错！
# xiaoming.pop("kkkk")

print(xiaoming)

