# sort
# 查询学生信息，按年龄升序排列
db.stu.aggregate(
    {$sort:{age:1}}
    )
# 查询男生女生人数，按照人数降序排列
db.stu.aggregate(
    {$group:{_id:"$gender", count:{$sum:1}}},
    {$sort:{count:-1}}
    )

# $limit
# 查询两条学生信息
db.stu.aggregate(
    {$limit:2}
    )

# $skip
# 查询从第3条开始的学生信息
db.stu.aggregate(
    {$skip:2}
    )
# 统计男生女生人数，按照人数升序，取第二条数据
db.stu.aggregate(
    {$group:{_id:"$gender", count:{$sum:1}}},
    {$sort:{count:1}},
    {$skip:1},
    {$limit:1}
    )

# $unwind
db.t2.insert({_id:1,item:'t-shirt',size:['S','M','L']})
# 对尺码进行拆分
db.t2.aggregate(
    {$unwind:"$size"}
    )
{ "_id" : 1, "item" : "t-shirt", "size" : "S" }
{ "_id" : 1, "item" : "t-shirt", "size" : "M" }
{ "_id" : 1, "item" : "t-shirt", "size" : "L" }

# 数据库中有一条数据：{"username":"Alex","tags": ['C#','Java','C++']}，如何获取该tag列表的长度？
db.t2.insert({"username":"Alex","tags": ['C#','Java','C++']})
# 此时t2中有两条数据，要先过滤

db.t2.aggregate(
    {$match:{username:"Alex"}},
    {$unwind:"$tags"},
    {$group:{_id:null, count:{$sum:1}}},
    {$project:{_id:0, count:1}}
    )


# preserveNullAndEmptyArrays
db.t3.find()
{ "_id" : 1, "item" : "a", "size" : [ "S", "M", "L" ] }
{ "_id" : 2, "item" : "b", "size" : [ ] }
{ "_id" : 3, "item" : "c", "size" : "M" }
{ "_id" : 4, "item" : "d" }
{ "_id" : 5, "item" : "e", "size" : null }

# 如果不加这个字段，发现size为null或空列表或缺失的都没了
db.t3.aggregate(
    {$unwind:"$size"}
    )
{ "_id" : 1, "item" : "a", "size" : "S" }
{ "_id" : 1, "item" : "a", "size" : "M" }
{ "_id" : 1, "item" : "a", "size" : "L" }
{ "_id" : 3, "item" : "c", "size" : "M" }

# 加上这个字段
db.t3.aggregate(
    {$unwind:{path:"$size", preserveNullAndEmptyArrays:true}}
    )

{ "_id" : 1, "item" : "a", "size" : "S" }
{ "_id" : 1, "item" : "a", "size" : "M" }
{ "_id" : 1, "item" : "a", "size" : "L" }
{ "_id" : 2, "item" : "b" }
{ "_id" : 3, "item" : "c", "size" : "M" }
{ "_id" : 4, "item" : "d" }
{ "_id" : 5, "item" : "e", "size" : null }

# 索引
# 测试：插入100万条数据到数据库中
for(i=0;i<1000000;i++){db.tt.insert({name:'test'+i,age:i})}
# 不建立索引，查看运行时间
db.tt.find({name:'test500000'}).explain('executionStats')

# 建立索引
db.tt.ensureIndex({name:1})
# 再查询，查询运行时间
db.tt.find({name:'test500000'}).explain('executionStats')

# 查看当前集合的所有索引
db.tt.getIndexes()

[
	{
		"v" : 2,
		"key" : {
			"_id" : 1
		},
		"name" : "_id_"
	},
	{
		"v" : 2,
		"key" : {
			"name" : 1
		},
		"name" : "name_1"
	}
]

# 删去索引
db.tt.dropIndex({name:1})

show dbs
use douban

show collections
db.tv1.find()

# 1.获取每条数据中的title，count(所有评分人数),rate(评分),country(国家)的这些字段
db.tv1.aggregate(
    {$project:{_id:0, title:1, count:"$rating.count", rate:"$rating.value", country:"$tv_category"}}
    )

# 2.获取上述结果中的不同国家电视剧的数据量
db.tv1.aggregate(
    {$project:{_id:0, title:1, count:"$rating.count", rate:"$rating.value", country:"$tv_category"}},
    {$group:{_id:"$country", sum:{$sum:1}}},
    {$project:{_id:0, country:"$_id", sum:1}}
    )
# 3.获取上述结果中分数大于8分的不同国家电视剧的数据量
db.tv1.aggregate(
    {$project:{_id:0, title:1, count:"$rating.count", rate:"$rating.value", country:"$tv_category"}},
    {$match:{rate:{$gt:8}}},
    {$group:{_id:"$country", sum:{$sum:1}}},
    {$project:{_id:0, country:"$_id", sum:1}}
    )

use test
show collections
db.t1.find()
# 统计t1中每个name出现的次数
db.t1.aggregate(
    {$group:{_id:"$name", count:{$sum:1}}}
    )
# 统计t1中所有的name的出现的次数中次数大于4的name
db.t1.aggregate(
    {$group:{_id:"$name", count:{$sum:1}}},
    {$match:{count:{$gt:4}}}
    )
# 统计t1中所有的name的出现的次数中次数大于4的次数（只显示次数）
db.t1.aggregate(
    {$group:{_id:"$name", count:{$sum:1}}},
    {$match:{count:{$gt:4}}},
    {$project:{_id:0, count:1}}
    )