## 一、拉取镜像
```bash
# 拉取镜像
docker pull mongo:6.0.12

# 检查镜像
docker images
```


## 二、创建mongo挂载目录
```bash
# 创建目录
mkdir -p ~/mongo6.0.12/{data,conf,backup}
```


## 三、启动mongo容器并挂载配置文件、数据持久化
启动脚本 [mongo6.0.12.sh](./mongo6.0.12.sh)
```bash
# 执行脚本 启动镜像
sh mongo6.0.12.sh

# 查看是否启动成功
docker ps
```


## 四、修改mongo的配置信息
直接修改挂载的配置文件即可。

修改完记得重启
```bash
# 停止mongo  
docker stop mongodb

# 启动 mongo 
docker start mongodb
```


---
- [docker安装mongoDB详细步骤](https://blog.csdn.net/qhl_904463348/article/details/120284218)
- [docker-hub/mongo](https://hub.docker.com/_/mongo)
- 
