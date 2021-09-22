from pymongo import MongoClient

# 实例化client，建立连接
client = MongoClient(host="127.0.0.1", port=27017)  # 本地不需要写host和port
# 选中集合
collection = client["python"]["t1"]  # python数据库中的t1集合

# 插入一条数据，接收字典，返回的是objectId
# ret = collection.insert({"name": "liulei", "age": 10})
# print(ret)
# ret = collection.insert({"_id": 10086, "name": "liulei", "age": 10})
# print(ret)

# 插入多条数据，接收由字典组成的列表，返回的是InsertManyResult类的实例
# data_list = [{"name": "test{}".format(i)} for i in range(10)]
# ret = collection.insert_many(data_list)
# print(ret)
# for i in ret.inserted_ids:
#     print(i)

# 查询一条记录
# t = collection.find_one({"name": "liulei"})
# print(t)

# 查询多条记录，如果条件为空，则返回数据库的所有数据
# t = collection.find({"name": "liulei"})
# print(t)
# <pymongo.cursor.Cursor object at 0x7f8d1a09ab00>
# 结果是一个cursor游标对象，可迭代，类似读文件的指针
# for i in t:
#     print(i)

# 此时游标已经到了末尾，如果再遍历，为空
# for i in t:  # 此时t中没有内容
#     print(i)

# 可将游标对象转成列表
# print(list(t))
# [{'_id': ObjectId('60f29813a08138ee5c7e0a4d'), 'name': 'liulei', 'age': 10},
# {'_id': 10086, 'name': 'liulei', 'age': 10}]

# 更新一条
# collection.update_one({"name": "liulei"}, {"$set": {"name": "ken"}})
# 更新多条
# collection.update_many({"name": "liulei"}, {"$set": {"name": "ken"}})

# 删除一条
# collection.delete_one({"name": "ken"})
# 删除多条
# collection.delete_many({"name": "ken"})
