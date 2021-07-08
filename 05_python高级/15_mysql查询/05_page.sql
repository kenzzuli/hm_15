-- 分页
  -- limit start, count
  -- 限制查询出来的数据个数
  select * from students limit 5;
  -- 查询前5个数据
  select * from students limit 0, 5;
  -- 每页显示2个，显示第6页的信息，按照年龄从小到大排序
  select * from students order by age asc limit 10, 2;
  -- 查询所有的女性信息，按照身高从高到低排序，只显示前两个信息
  select * from students where gender="F" order by height desc limit 0, 2;
