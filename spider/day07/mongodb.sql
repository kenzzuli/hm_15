# mongodb java驱动版本不对，很多函数都deprecated
show databases

# 使用test数据库
use test
# 显示集合
show collections

# 插入
db.temp.insert({name: "liulei", gender: 1})
# 插入时指定_id参数
db.temp.insert({_id: "20210716", name: "zhouyan", gender: 0})
# 查看集合里的内容
db.temp.find()

# 更新
db.temp.update({name: "lihang"}, {name: "peter"})
use test
# 年龄大于等于18
db.stu.find({age: {$gte: 18}})
# 年龄大于等于18 或 家乡为大理或蒙古
db.stu.find({$or: [{age: {$gt: 18}}, {hometown: {$in: ["大理", "蒙古"]}}]})

# 删除
db.stu.remove({name: "ken"})

# 支持正则表达式

# 查询姓黄的学生,对中文的支持不太好
db.stu.find()
db.stu.insertOne({name: "ken", age: 10, gender: false, hometown: "cn"})

db.stu.find({name: /^k/})
db.stu.find({name: {$regex: "n$"}})

db.products.find()
db.products.find({sku: /^a/})
db.products.find({sku: {$regex: "^x"}})

# limit skip
db.products.find().limit(2)
db.products.find().skip(2)

# 自定义函数查询
db.stu.find({
    $where: function () {
        return this.age > 18;
    }
})

# 投影
db.stu.find({}, {_id: 0, name: 1})
db.stu.find({age: {$gt: 18}}, {name: 1, age: 1, _id: 0})

# 排序
db.stu.find().sort({age: 1, gender: -1})
# 年龄大于18的按照年龄升序排序，只显示name
db.stu.find({age: {$gt: 18}}, {name: 1, _id: 0}).sort({age: 1})

# 统计个数
db.stu.find().count()
# 统计年龄大于18的个数
db.stu.find({age: {$gt: 18}}).count()
# 统计年龄大于20且性别为true的个数
db.stu.count({age: {$gt: 20}, gender: true})
db.stu.find()

# 去重
db.stu.distinct("hometown")
db.stu.distinct("hometown", {age: {$gt: 18}})

#分组
# 不同性别的人数
db.stu.aggregate(
    {
        $group:
            {
                _id: "$gender",
                counter: {$sum: 1}
            }
    }
    )
# 不同性别的年龄的平均值
db.stu.aggregate(
    {$group:{
        _id:"$gender",
            avg_age:{$avg:"age"}
        }}
    )

# 按照家乡分组后，求年龄的平均值
db.stu.aggregate(
    {$group:{
        _id:"$hometown",
            avg_age:{$avg:"$age"}
        }}
    )
# group by null 将集合中所有文档分为一组
# 求学生的总人数，平均年龄
db.stu.aggregate({
    $group:{
        _id:null,
        total_num:{$sum:1},
        avg_age:{$avg:"$age"}
    }
})
# $project
# 查询学生的姓名、年龄
db.stu.aggregate(
    {$project:{_id:0, name:1, age:1}}
    )

# 查询男生人数、女生人数，只输出人数
db.stu.aggregate(
    {$group:{_id:"$gender", number:{$sum:1}}},
    {$project:{_id:0, number:1}}
)

# $match
# 查询年龄大于20或家乡在蒙古或华山的男生和女生人数，并输出性别和人数
db.stu.aggregate(
    {$match:{$or:[{hometown:{$in:["蒙古", "华山"]}},{age:{$gt:20}}]}},
    {$group:{_id:"$gender", number:{$sum:1}}},
    {$project:{gender:"$_id", number:1, _id:0}}
    )
db.tv3.find()
db.tv3.update({userid:"c"}, {country:"uk", userid:"c", province:"sh"})
# 需求：统计出每个country/province下的userid的数量（同一个userid只统计一次）
# 1.同时按照所有字段进行分组，就可以达到去重的效果
# 2.再按照country和province进行分组并计数
# 3.投影，修改结果字段
db.tv3.aggregate(
    {$group:{_id:{country:"$country", province:"$province", userid:"$userid"}}},
    {$group:{_id:{country:"$_id.country", province:"$_id.province"}, number:{$sum:1}}},
    {$project:{_id:0, country:"$_id.country", province:"$_id.province", number:1}}
    )