-- 子查询
  -- 标量子查询
  -- 查询出高于平均身高的信息
  select * from students where height > (select avg(height) from students);
  -- 查询身高最高的男生信息
  select * from students where height = (select max(height) from students where gender = "M") and gender= "M";
  -- 查询青岛有多少区县  子查询速度较慢
  select * from areas where pid = (select aid from areas where atitle="青岛市");

  -- 列级子查询
  -- 查询还有学生再办的所有班级名称
  select name from classes where id in (select distinct cls_id from students);

  -- 行级子查询
  -- 查询班级年龄最大，且身高最高的学生
  select * from students where (age, height) = (select max(age), max(height) from students);
