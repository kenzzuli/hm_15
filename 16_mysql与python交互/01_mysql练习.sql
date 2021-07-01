-- 创建 "京东" 数据库
create database jing_dong charset=utf8;

-- 使用 "京东" 数据库
use jing_dong;

-- 创建一个商品goods数据表
create table goods(
    id int unsigned primary key auto_increment not null,
    name varchar(150) not null,
    cate_name varchar(40) not null,
    brand_name varchar(40) not null,
    price decimal(10,3) not null default 0,
    is_show bit not null default 1,
    is_saleoff bit not null default 0
);
-- 向goods表中插入数据

insert into goods values(0,'r510vc 15.6英寸笔记本','笔记本','华硕','3399',default,default);
insert into goods values(0,'y400n 14.0英寸笔记本电脑','笔记本','联想','4999',default,default);
insert into goods values(0,'g150th 15.6英寸游戏本','游戏本','雷神','8499',default,default);
insert into goods values(0,'x550cc 15.6英寸笔记本','笔记本','华硕','2799',default,default);
insert into goods values(0,'x240 超极本','超级本','联想','4880',default,default);
insert into goods values(0,'u330p 13.3英寸超极本','超级本','联想','4299',default,default);
insert into goods values(0,'svp13226scb 触控超极本','超级本','索尼','7999',default,default);
insert into goods values(0,'ipad mini 7.9英寸平板电脑','平板电脑','苹果','1998',default,default);
insert into goods values(0,'ipad air 9.7英寸平板电脑','平板电脑','苹果','3388',default,default);
insert into goods values(0,'ipad mini 配备 retina 显示屏','平板电脑','苹果','2788',default,default);
insert into goods values(0,'ideacentre c340 20英寸一体电脑 ','台式机','联想','3499',default,default);
insert into goods values(0,'vostro 3800-r1206 台式电脑','台式机','戴尔','2899',default,default);
insert into goods values(0,'imac me086ch/a 21.5英寸一体电脑','台式机','苹果','9188',default,default);
insert into goods values(0,'at7-7414lp 台式电脑 linux ）','台式机','宏碁','3699',default,default);
insert into goods values(0,'z220sff f4f06pa工作站','服务器/工作站','惠普','4288',default,default);
insert into goods values(0,'poweredge ii服务器','服务器/工作站','戴尔','5388',default,default);
insert into goods values(0,'mac pro专业级台式电脑','服务器/工作站','苹果','28888',default,default);
insert into goods values(0,'hmz-t3w 头戴显示设备','笔记本配件','索尼','6999',default,default);
insert into goods values(0,'商务双肩背包','笔记本配件','索尼','99',default,default);
insert into goods values(0,'x3250 m4机架式服务器','服务器/工作站','ibm','6888',default,default);
insert into goods values(0,'商务双肩背包','笔记本配件','索尼','99',default,default);

select * from goods;

-- 查询类型cate_name为 '超极本' 的商品名称、价格
select name, price from goods where cate_name = '超级本';
-- 显示商品的种类
select distinct cate_name from goods;
select cate_name, group_concat(name) from goods group by cate_name;
-- 求所有电脑产品的平均价格,并且保留两位小数
select round(avg(price), 2) from goods;
-- 显示每种商品的平均价格
select cate_name, avg(price) from goods group by cate_name;
-- 查询每种类型的商品中 最贵、最便宜、平均价、数量
select cate_name, max(price), min(price), avg(price), count(*) from goods group by cate_name;
-- 查询所有价格大于平均价格的商品，并且按价格降序排序
select id, name, price from goods where price > (select avg(price) from goods) order by price desc;
-- 查询每种类型中最贵的电脑信息
select max(price) as max_price from goods group by cate_name order by max_price desc;
select goods.cate_name, goods.id, goods.name, goods.price, goods.brand_name, goods.is_saleoff, goods.is_show
from goods inner join (select max(price) as max_price from goods group by cate_name) as t2
on goods.price=t2.max_price order by goods.price desc;
select * from goods
inner join
    (
        select
        cate_name,
        max(price) as max_price
        from goods group by cate_name
    ) as goods_new_info
on goods.cate_name=goods_new_info.cate_name and goods.price=goods_new_info.max_price
order by goods.price desc;

select t1.cate_name, t1.max_price, t2.name, t2.brand_name, t2.is_show, t2.is_saleoff
from (select cate_name, max(price) as max_price from goods group by cate_name) as t1
left join goods as t2 on t1.cate_name = t2.cate_name and t1.max_price = t2.price
order by t2.price desc;

-- 加一个最高价格
insert into goods values(0,'老王牌电脑','笔记本','laowang','4999',default,default);
-- 再次执行上面的查询语句，发现在笔记本分类下会出现两行记录，两个都是最高价格。

-- 创建商品分类表
create table if not exists goods_cates(
    id int unsigned auto_increment primary key not null,
    name varchar(40) not null
);
-- 查询goods表中商品的种类
select cate_name from goods group by cate_name;
-- 将分组结果写入到goods_cates数据表
insert into goods_cates(name) (select cate_name from goods group by cate_name);
select * from goods_cates;
-- 通过goods_cates数据表来更新goods表
update goods as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name = c.id;
select * from goods;

-- 创建 "商品品牌表" 表
-- 通过create...select来创建数据表并且同时写入记录,一步到位
-- 在创建数据表的时候一起插入数据
-- 注意: 需要对brand_name 用as起别名，否则name字段就没有值
create table if not exists goods_brands(
    id int unsigned auto_increment primary key not null,
    name varchar(40) not null
) select brand_name as name from goods group by brand_name;
select * from goods_brands;

-- 通过goods_brands数据表来更新goods数据表
update goods as g inner join goods_brands b on g.brand_name=b.name set g.brand_name=b.id;
select * from goods;

-- 修改表结构
desc goods;
-- 通过alter table语句修改表结构
alter table goods change cate_name cate_id int unsigned not null,
    change brand_name brand_id int unsigned not null;

-- 外键
-- 分别在 goods_cates 和 goods_brands表中插入记录
insert into goods_cates(name) values ('路由器'),('交换机'),('网卡');
insert into goods_brands(name) values ('海尔'),('清华同方'),('神舟');
-- 在 goods 数据表中写入任意记录
insert into goods (name, cate_id, brand_id, price)
values('LaserJet Pro P1606dn 黑白激光打印机', 12, 4,'1849');

-- 查询所有商品的详细信息 (通过内连接)
select g.id, g.name, gc.name, gb.name, g.price from goods as g
    inner join goods_brands as gb on g.brand_id = gb.id
    inner join goods_cates as gc on g.cate_id = gc.id;

-- 查询所有商品的详细信息 (通过左连接)
select g.id, g.name, c.name, b.name, g.price from goods as g
    inner join goods_cates as c on g.cate_id = c.id
    inner join goods_brands as b on g.brand_id = b.id;

-- 给brand_id 添加外键约束成功
alter table goods add foreign key (brand_id) references goods_brands(id);
-- 给cate_id 添加外键失败
-- 会出现1452错误
-- 错误原因:已经添加了一个不存在的cate_id值12,因此需要先删除
delete from goods where cate_id not in (select distinct id from goods_cates);
alter table goods add foreign key (cate_id) references goods_cates(id);

-- 验证插入非法数据
insert into goods (name, cate_id, brand_id, price)
values('LaserJet Pro P1606dn 黑白激光打印机', 12, 4,'1849');
-- a foreign key constraint fails (`jing_dong`.`goods`, CONSTRAINT `goods_ibfk_2` FOREIGN KEY (`cate_id`) REFERENCES `goods_cates` (`id`))

-- 如何取消外键约束
-- 需要先获取外键约束名称,该名称系统会自动生成,可以通过查看表创建语句来获取名称
show create table goods;
-- 获取名称之后就可以根据名称来删除外键约束
alter table goods drop foreign key goods_ibfk_2;

-- 一般不要使用外键，太慢
alter table goods drop foreign key goods_ibfk_2;
alter table goods drop foreign key goods_ibfk_3;


