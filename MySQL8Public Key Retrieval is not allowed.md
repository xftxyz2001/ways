## 问题描述
JDBC链接MySQL8时报错：
```
java.sql.SQLNonTransientConnectionException: Public Key Retrieval is not allowed
```


## 问题原因
mysql 8.0 默认使用 `caching_sha2_password` 身份验证机制 （即从原来 `mysql_native_password` 更改为 `caching_sha2_password` ）。

从 5.7 升级 8.0 版本的不会改变现有用户的身份验证方法，但新用户会默认使用新的 `caching_sha2_password` 。
客户端不支持新的加密方式。修改用户的密码和加密方式。


## 解决方案

### 方案一
在命令行模式下进入mysql，运行以下命令：
```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
-- 或
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
```

### 方案二※
在配置数据源的时候直接将属性allowPublicKeyRetrieval设置为true
```yml
spring:
  datasource:
    url: jdbc:mysql:///db?serverTimezone=Asia/Shanghai&characterEncoding=utf-8&useSSL=false&allowMultiQueries=true&allowPublicKeyRetrieval=true
    driver-class-name: com.mysql.cj.jdbc.Driver
    # ...
```


---
- [完美解决：MySQL8报错：Public Key Retrieval is not allowed](https://blog.csdn.net/white0718/article/details/131790493)
