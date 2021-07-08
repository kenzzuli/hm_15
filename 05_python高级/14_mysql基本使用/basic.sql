create database python charset = utf8;
use python;
show tables;
create table students
(
    id     int unsigned not null primary key auto_increment,
    name   varchar(10),
    age    int unsigned,
    height decimal(5, 2),
    gender varchar(1),
    cls_id int unsigned
);
show tables;
desc students;
drop table students;
show tables;
create table students
(
    id     int unsigned not null primary key auto_increment,
    name   varchar(30)  not null,
    age    tinyint unsigned default 0,
    height decimal(5, 2),
    gender enum ("男","女","中性", "保密"),
    cls_id int unsigned     default 0

);

alter table students
    change gender gender enum ('男','女','中性', '保密') default '男';

desc students;
alter table students
    add birthday datetime;
desc students;
insert into students
values (0, '郭靖', 18, 180.11, '男', 0, '2011-1-1');
select *
from students;

-- 创建班级表
create table classes
(
    id   int unsigned primary key not null auto_increment,
    name varchar(10)              not null
);
insert into classes value (1, 'python1'), (2, 'python2');
select *
from classes;
insert into classes(name)
values ('python3'),
       ('python4');
desc classes;
alter table students
    modify birthday date not null;
desc students;
select *
from students;
alter table students
    change birthday birth date not null;
alter table students
    modify birth date default '2000-1-1';
desc students;
select *
from students;
show create table students;
insert into classes value (0, 'python5');
select * from classes;
delete from classes where id=6;
insert into classes values(null,'python6');
insert into classes values(default, 'python7');
desc students;
insert into students values(default, "刘磊", 20, 181.1, 1, 2, '1990-1-1');
insert into students values(default, "ken", 24, 185.1, 3, 2, '1998-1-1');
select * from students;
insert into classes(name) values("java1"), ("java2");
select * from classes;
update students set name="ken", gender=2 where id=2;
delete from students where id=1;
update students set isdelete=1 where id=3;
select name,age from students;
select id,name, age from students where id>1;
select name as n, age as a from students;
alter table students add is_delete bit default 0;
update students set is_delete=1 where id=3;
select * from students;