xiaoming = {"name": "xiaoming",
            "age": 18}

# 统计键值对数量
print(len(xiaoming))

# 合并字典
temp_dic = {"height": 1.85,
            "gender": True,
            "age": 29}
# 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原来的键值对 age
xiaoming.update(temp_dic)

xiaoming.setdefault("height", 1.9)
xiaoming.setdefault("sex", "male")
print(xiaoming.popitem())
print(xiaoming)
del xiaoming["age"]
print(xiaoming)
ll = xiaoming.fromkeys("hello", 5)
zz = xiaoming.copy()
print(zz)
print(ll)
# 清空字典
xiaoming.clear()

print(xiaoming)
