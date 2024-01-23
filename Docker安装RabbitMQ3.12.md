## 一、拉取镜像
```bash
# 拉取镜像
docker pull rabbitmq:3.12-management

# 检查镜像
docker images
```


## 二、创建rabbitmq挂载目录
```bash
# 创建目录
mkdir -p ~/rabbitmq3.12
```


## 三、启动rabbitmq容器并挂载目录
启动脚本 [rabbitmq3.12.sh](./rabbitmq3.12.sh)
```bash
# 执行脚本 启动镜像
sh rabbitmq3.12.sh

# 查看是否启动成功
docker ps
```

---
- [Docker 安装 rabbitmq 容器 (完整详细版)](https://blog.csdn.net/u011788214/article/details/132492478)
- [docker-hub/rabbitmq](https://hub.docker.com/_/rabbitmq)
