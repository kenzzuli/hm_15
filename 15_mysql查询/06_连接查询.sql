-- 连接查询
  -- inner join .. on
  -- 查询能够对应班级的学生以及班级信息
  select * from students as s inner join classes as c on s.cls_id = c.id;
  -- 内连接，只显示姓名和班级
  select s.name, c.name from students as s inner join classes as c on s.cls_id = c.id;
  -- 查询 有能够对应班级的学生以及班级信息，显示学生的所有信息，只显示班级名称
  select s.*, c.name from students as s inner join classes as c on s.cls_id = c.id;
  -- 在以上的查询中，将班级名放在第一列
  select c.name, s.* from students as s inner join classes as c on s.cls_id = c.id;
  -- 在以上的查询中，按照班级进行排序
  select c.name, s.* from students as s inner join classes as c on s.cls_id = c.id order by c.name;
  -- 在以上的查询中，如果班级相同，按照学生id从小到大排序
  select c.name, s.* from students as s inner join classes as c on s.cls_id = c.id order by c.name, s.id;

  -- left join
  -- 查询每位学生对应的班级信息
  select * from students as s left join classes as c on s.cls_id = c.id;
  -- 查询没有对应班级信息的学生
  -- 原表过滤用where，查出来的新表过滤用having，这里用having比较好。
  select * from students as s left join classes as c on s.cls_id = c.id where c.id is null;
  select * from students as s left join classes as c on s.cls_id = c.id having c.id is null;

  -- right join 一般不用，将两个表格换下顺序就变成了left join。
