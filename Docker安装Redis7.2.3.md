## 一、拉取镜像
```bash
# 拉取镜像
docker pull redis:7.2.3

# 检查镜像
docker images
```


## 二、创建Redis配置文件
```bash
# 创建目录
mkdir -p ~/redis7.2.3
# 创建配置文件
touch ~/redis7.2.3/redis.conf
```


## 三、启动redis容器并挂载配置文件、数据持久化
启动脚本 [redis7.2.3.sh](./redis7.2.3.sh)
```bash
# 执行脚本 启动镜像
sh redis7.2.3.sh

# 查看是否启动成功
docker ps
```


## 四、修改redis的配置信息
直接修改挂载的配置文件即可。

修改完记得重启
```bash
# 停止redis  
docker stop redis

# 启动 redis 
docker start redis
```


---
- [Docker 安装 Redis 容器 (完整详细版)](https://blog.csdn.net/BThinker/article/details/123374236)
- [docker-hub/redis](https://hub.docker.com/_/redis)
- [redis 7.2.3 官方配置文件 redis.conf sentinel.conf](https://blog.csdn.net/wuyujin1997/article/details/135094906)
