## 一、拉取并启动镜像
```bash
# 拉取镜像
docker pull mysql:8.2.0

# 启动镜像
docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:8.2.0

# 查看是否启动成功
docker ps -a
```


## 二、拷贝配置文件到宿主机
```bash
# 拷贝容器的/etc/mysql目录 到 用户家目录的mysql8.2.0目录
docker cp mysql:/etc/mysql ~/mysql8.2.0
```


## 三、删除mysql容器
```bash
# 停止容器
docker stop mysql

# 删除容器
docker rm mysql
```


## 四、启动mysql容器并挂载配置文件、数据持久化
启动脚本 mysql8.2.0.sh 脚本内容如下：
```bash
#!/bin/sh
docker run \
-p 3306:3306 \
--name mysql \
--privileged=true \
--restart unless-stopped \
-v ~/mysql8.2.0/conf.d:/etc/mysql/conf.d \
-v ~/mysql8.2.0/log:/var/log/mysql \
-v ~/mysql8.2.0/data:/var/lib/mysql \
-v /etc/localtime:/etc/localtime \
-e MYSQL_ROOT_PASSWORD=123456 \
-d mysql:8.2.0
```
```bash
# 执行脚本 启动镜像
sh mysql8.2.0.sh

# 查看是否启动成功
docker ps -a
```


## 五、修改mysql的配置信息
直接修改挂载出来的配置文件即可。

修改完记得重启
```bash
# 停止mysql  
docker stop mysql

# 启动 mysql 
docker start mysql
```


---
- [docker安装mysql 8.0.20 版本 超详细教程](https://blog.csdn.net/u014576291/article/details/105890286)
- [docker-hub/mysql](https://hub.docker.com/_/mysql)
- [docker启动mysql报错Can't read dir of '/etc/mysql/conf.d/'](https://www.cnblogs.com/eternality/p/17170773.html)
