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
