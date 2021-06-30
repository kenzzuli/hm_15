-- 自关联
  -- 查询有多少个省
  select * from areas where pid is null;
  select count(*) from areas where pid is null;
  -- 查询山东省有多少地级市;
  select province.aid, province.atitle, city.atitle from areas as city inner join areas as province on city.pid = province.aid where province.atitle='山东省';
  select province.aid, province.atitle, city.atitle from areas as city inner join areas as province on city.pid = province.aid having province.atitle='山东省';
  -- 这里只能用where，如果用having，是对count后的结果再次过滤，那时候已经没有atitle字段了。
  select count(*) from areas as city inner join areas as province on city.pid = province.aid where province.atitle='山东省';
