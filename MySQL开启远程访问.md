## 报错信息
ERROR 1130: Host 'x.x.x.x' is not allowed to connect to thisMySQL server

## 解决方法
改表法。
可能是你的帐号不允许从远程登陆，只能在localhost。
这个时候只要在localhost的那台电脑，登入mysql后，更改"mysql" 数据库里的 "user" 表里的 "host"项，从"localhost"改成"%"

在安装mysql的机器上运行：
```
mysql -u root -p
mysql>usemysql;
mysql>update user set host = '%' where user ='root';
mysql>select host, user from user; 
mysql>FLUSH PRIVILEGES
```

> 连接测试，成功可以忽略下面步骤！

## 异常处理
Navicat连接MySQL 8 出现2059 - authentication plugin 'caching_sha2_password'
```
mysql>use mysql;
mysql>ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```

这里的localhost对应本地，如果是远程访问 mysql的话，需要将localhost改成%；
password是root的密码，使用时也要进行对应修改。
