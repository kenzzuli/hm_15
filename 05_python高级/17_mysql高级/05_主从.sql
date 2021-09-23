
GRANT REPLICATION SLAVE ON *.* TO 'slave'@'%' identified by 'slave';
FLUSH PRIVILEGES;
SHOW MASTER STATUS;


change master to master_host='10.4.9.200', master_user='slave', master_password='slave',master_log_file='mysql-bin.000001', master_log_pos=600;
start slave;
show slave status;
