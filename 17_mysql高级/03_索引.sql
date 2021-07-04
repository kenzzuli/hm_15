-- 索引
-- 创建测试表testindex
create table test_index(title varchar(10));
-- 用python添加数据后，查看表格中的数据
select * from test_index;
-- 开启运行时间监测
set profiling = 1;
select * from test_index where title='ha-99999';
-- 查看执行时间
show profiles;
-- 为表title_index的title列创建索引：
create index title_index on test_index(title(10));
select * from test_index where title='ha-99999';
show profiles;
+----------+------------+---------------------------------------------------+
| Query_ID | Duration   | Query                                             |
+----------+------------+---------------------------------------------------+
|        1 | 0.03207400 | select * from test_index where title='ha-99999'   |
|        2 | 0.12883100 | create index title_index on test_index(title(10)) |
|        3 | 0.00024000 | select * from test_index where title='ha-99999'   |
+----------+------------+---------------------------------------------------+
