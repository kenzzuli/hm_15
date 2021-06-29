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
