from pymongo import MongoClient

client = MongoClient()
collection = client["python"]["t3"]  # python数据库中的t3集合

# 1. 使用python向集合中插入1000条文档，文档的属性包括_id, name，其中
# id的值为：0，1，2...
# name的值为: py0, py1....
data_list = [{"_id": i, "name": "py{}".format(i)} for i in range(1000)]
# collection.insert_many(data_list)

# 2. 查询出_id为100的整数倍的文档，如100，200等，并将name输出
ret = collection.find()
for i in ret:
    if i["_id"] % 100 == 0 and i["_id"] != 0:
        print(i["name"])

# 或使用列表推导式
ret_list = [i["name"] for i in collection.find() if i["_id"] % 100 == 0 and i["_id"] != 0]
print(ret_list)