-- 事务
drop table money;
create table money(
    id int unsigned not null primary key auto_increment,
    balance int unsigned not null
);
show tables;
insert into money values (0, 100), (0, 200), (0, 0);
select * from money;
-- 开启事务
-- start transaction;
begin;
-- id为1的人的余额减去100
update money set balance = balance - 100 where id = 1;
select * from money;
-- id为2的人余额加上100
update money set balance = balance + 100 where id = 2;
select * from money;
commit;
-- rollback;
select * from money;