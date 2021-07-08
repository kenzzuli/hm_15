-- 数据准备
    -- 创建一个数据库
    create database python_test charset=utf8;
    -- 使用一个数据库
    use python_test;
    -- 显示当前使用的数据库
    select database();
    -- 创建一个数据表
    create table students(  -- 学生表
        id int unsigned not null primary key auto_increment,
        name varchar(20) default " ",
        age tinyint unsigned default 0,
        height decimal(5,2),
        gender enum('M','F','B', 'U') default 'U',
        cls_id int unsigned default 0,
        id_delete bit default 0
    );
    create table classes( -- 班级表
        id int unsigned auto_increment not null primary key,
        name varchar(30) not null
    );
    -- 查看所有的表
    show tables;
    -- 查看创建数据表的语句
    show create table classes;
    -- 插入一些数据
    insert into students values
        (0,'小明',18,180.00,2,1,0),
        (0,'小月月',18,180.00,2,2,1),
        (0,'彭于晏',29,185.00,1,1,0),
        (0,'刘德华',59,175.00,1,2,1),
        (0,'黄蓉',38,160.00,2,1,0),
        (0,'凤姐',28,150.00,4,2,1),
        (0,'王祖贤',18,172.00,2,1,1),
        (0,'周杰伦',36,NULL,1,1,0),
        (0,'程坤',27,181.00,1,2,0),
        (0,'刘亦菲',25,166.00,2,2,0),
        (0,'金星',33,162.00,3,3,1),
        (0,'静香',12,180.00,2,4,0),
        (0,'郭靖',12,170.00,1,4,0),
        (0,'周杰',34,176.00,2,5,0);
    insert into classes values (0, "python_01期"), (0, "python_02期");

-- 查询
    -- 查询所有字段
    select * from classes;
    select * from students;
    -- 查询指定字段
    select name, age from students;
    -- 使用as给字段起别名
    select id as 序号, name as 名字, gender as 性别 from students;
    -- 使用as给表起别名
    select students.id, students.name from students;
    select s.id, s.name from students as s;
    -- select students.id, students.name from students as s; 失败，如果用了别名，就要一直用别名
    -- 去除重复行
    select distinct gender from students;

-- 条件查询
    -- 比较运算符
        -- 大于 > 查询大于18岁的信息
        select * from students where age > 18;
        -- 小于 < 查询小于18岁的信息
        select * from students where age < 18;
        -- 大于等于 >=
        -- 小于等于 <=
        -- 等于 = 查询年龄等于18岁的学生的姓名
        select name from students where age = 18;
        -- 不等于 != 或<>（不常用）
        select name from students where age != 18;

    -- 逻辑运算符
        -- and
        -- 18-28之间的所有学生信息
        select * from students where age<=28 and age>=18;
        -- 18岁以上的女性
        select * from students where age>18 and gender="F";
        -- or
        -- 18岁以上或身高180以上
        select * from students where age > 18 or height >= 180;
        -- not
        -- 不在 18以上的女性 这个范围内的信息 not 整体否定
        select * from students where not (age>18 and gender="F");
        -- 年龄不是小于或者等于18 并且是女性  not 部分否定
        select * from students where (not age<=18) and gender="F";

    -- 模糊查询
        -- like
        -- %替换0个或多个字符
        -- _表示1个字符
        -- 查询姓名中 以"小"开始的名字
        select name from students where name like "小%";
        -- 查询姓名中包含"小"的名字
        select name from students where name like "%小%";
        -- 查询两个字的名字
        select name from students where name like "__";
        -- 查询至少有两个字的名字
        select name from students where name like "__%";

        -- rlike 正则
        -- 查询以 周 开始的姓名
        select name from students where name rlike "^周.*";
        -- 查询以 周 开头，以 伦 结尾的名字
        select name from students where name rlike "^周.*伦$";


    -- 范围查询
        -- in 表示在一个非连续的范围内
        -- 查询年龄为18、34、12的学生
        select * from students where age in (18, 12, 34);
        -- not in 不在非连续的范围内
        -- 年龄不是 18、34、12的学生
        select * from students where age not in (18, 12, 34);
        -- between ... and ... 表示在一个连续范围内
        -- 查询 年龄在18到34岁之间的信息
        select * from students where age between 18 and 34;
        -- not between ... and ... 表示不再一个连续范围内
        -- 查询 年龄不在18到34岁之间的信息
        select * from students where age not between 18 and 34;
        select * from students where not age between 18 and 34; # 这种也行，但不常用
        -- select * from students where age not (between 18 and 34); # 这种写法不对

    -- 空判断
        -- 判断 is null
        -- 查询身高为空的信息
        select * from students where height is null;
        -- 判断非空 is not null
        select * from students where height is not null;


-- 排序
    -- order by 字段
    -- asc 升序 desc 降序
    -- 查询年龄在18-34岁之间的男性，按照年龄从小到大排序  加上括号 可读性增强
    select * from students where (age between 18 and 34) and gender="M" order by age asc;
    -- 查询年龄在18到34岁之间的女性，身高从高到低排序
    select * from students where (age between 18 and 34) and gender="F" order by height desc;

    -- order by 多个字段
    -- 查询年龄在18到34之间的女性，身高从高到低排，如果身高相同按照年龄从小到大排
    select * from students where (age between 18 and 34) and gender="F" order by height desc, age asc;
    -- 查询年龄在18到34之间的女性，身高从高到低排，如果身高相同按照年龄从小到大排，如果年龄相同，按照id从大到小排
    select * from students where (age between 18 and 34) and gender="F" order by height desc, age asc, id desc;
    -- 按照年龄从小到大、身高从高到低排序
    select * from students order by age asc, height desc;


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

-- 自关联
  -- 查询有多少个省
  select * from areas where pid is null;
  select count(*) from areas where pid is null;
  -- 查询山东省有多少地级市
  select province.aid, province.atitle, city.atitle from areas as city inner join areas as province on city.pid = province.aid where province.atitle='山东省';
  select province.aid, province.atitle, city.atitle from areas as city inner join areas as province on city.pid = province.aid having province.atitle='山东省';
  -- 这里只能用where，如果用having，是对count后的结果再次过滤，那时候已经没有atitle字段了。
  select count(*) from areas as city inner join areas as province on city.pid = province.aid where province.atitle='山东省';
  -- 查询青岛有多少区县
  select city.atitle, district.atitle from areas as city inner join areas as district on city.aid = district.pid where city.atitle = "青岛市";
  select count(*) from areas as city inner join areas as district on city.aid = district.pid where city.atitle = "青岛市";

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




