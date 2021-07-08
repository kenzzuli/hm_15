use jing_dong;
show tables;
-- 三张表内连接查询
select g.*, c.name as cate_name, b.name as brand_name from goods as g left join goods_cates as c on g.cate_id = c.id
left join goods_brands as b on g.brand_id = b.id;
-- 将查询结果保存为视图
create view v_goods_info as
    select g.*, c.name as cate_name, b.name as brand_name from goods as g
        left join goods_cates as c on g.cate_id = c.id
        left join goods_brands as b on g.brand_id = b.id;
-- 查看数据库的所有表
show tables;
-- 查询创建的视图
select * from v_goods_info;
-- 视图仅用于查询，不能用于更新
update v_goods_info set name = "小王牌电脑" where id = 22;
-- The target table v_goods_info of the UPDATE is not updatable
