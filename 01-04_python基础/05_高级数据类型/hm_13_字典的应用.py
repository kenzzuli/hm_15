# 通常在字典中使用多个键值对，描述一个物体的相关信息
# 将多个字典放到一个列表中，再遍历，对列表中的每一个字典进行相同的处理

card_list = [{"name": "zhangsan",
              "age": 18,
              "sex": True},
             {"name": "Peter",
              "age": 20,
              "sex": False},
             {"name": "Ken",
              "age": 40,
              "sex": True}]
print(card_list)
# 遍历列表
for dic in card_list:
    print(dic)
print('*' * 50)
# 先遍历列表，每次返回一个字典，再遍历字典，每次返回一个key，通过key来获取value
for dic in card_list:
    for key in dic:
        print(key, dic[key])

