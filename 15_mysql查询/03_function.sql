-- 聚合函数
  -- 总数 count
  -- 查询男生多少人，女生多少人
  select count(*) as 男生个数 from students where gender="M";
  select count(*) as 女生个数 from students where gender="F";

  -- 最大值 max
  -- 查询最大的年龄
  select max(age) from students;
  -- 查询女性的最高身高
  select max(height) from students where gender="F";

  -- 最小值 min

  -- 求和 sum
  -- 计算所有人的年龄总和
  select sum(age) from students;

  -- 平均值 avg
  -- 计算平均年龄
  select avg(age) from students;
  select sum(age)/count(*) from students;

  -- 四舍五入 round(123.223, 1) 保留1位小数
  -- 计算平均年龄，保留两位小数
  select round(avg(age), 2) from students;
  -- 计算男性平均身高，保留两位小数
  select round(avg(height), 2) from students where gender="M";