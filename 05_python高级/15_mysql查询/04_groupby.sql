-- 分组
  -- group by
  -- 按照性别分组，查询所有的性别
  select gender from students group by gender; -- 不常用
  select name from students group by gender; -- 失败，因为分为四组后，从每组里面取名字，每组中包含多个不同的名字，到底取哪个？
  -- 计算每种性别中的人数
  select gender, count(*) from students group by gender;
  -- 计算男性的人数
  select gender, count(*) from students where gender="M" group by gender;

  -- group_concat()
  -- 查询同种性别中的姓名
  select gender, group_concat(name) from students group by gender;
  -- 查询所有男性的姓名, id, age
  select gender, group_concat(name, "_", id, "_", age) from students where gender="M" group by gender;

  -- having
  -- 查询平均年龄超过30岁的性别，以及性别中的姓名
  select gender, group_concat(name) from students group by gender having avg(age)>30;
  -- 查询每种性别中的人数多于2个的信息
  select gender,count(*) from students group by gender having count(*) > 2;