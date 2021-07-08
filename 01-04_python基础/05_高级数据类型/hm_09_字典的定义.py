xiaoli = {"name": "xiaoli"}
print(xiaoli)
# 字典是一个无序的数据集合，使用print函数输出字典时，通常输出顺序和定义顺序是不一样的！
xiaoming = {"name": "xiaoming",
            "age": 18,
            "sex": True,
            "height": 1.85,
            "school": "SISU",
            "weight": 80.5}
print(xiaoming)
print(xiaoming["name"])
print(xiaoming["age"])
print(xiaoming["sex"])
print(xiaoming["height"])
print(xiaoming["school"])
print('*' * 50)
print(xiaoming.get("name"))
print(xiaoming.get("age"))
print(xiaoming.get("sex"))
print(xiaoming.get("height"))
print(xiaoming.get("school"))
print('*' * 50)
print(xiaoming.keys())
print(xiaoming.values())
print(xiaoming.items())

