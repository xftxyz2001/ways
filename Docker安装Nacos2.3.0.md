## 一、拉取并启动镜像
```bash
# 拉取镜像
docker pull nacos/nacos-server:v2.3.0

# 启动镜像
docker run -p 8848:8848 --name nacos -e MODE=standalone -d nacos/nacos-server:v2.3.0

# 查看是否启动成功
docker ps
```


## 二、拷贝配置文件到宿主机
```bash
# 创建挂载目录
mkdir -p ~/nacos2.3.0

# 拷贝容器的/home/nacos目录 到 用户家目录的nacos2.3.0目录
docker cp nacos:/home/nacos/conf ~/nacos2.3.0
docker cp nacos:/home/nacos/logs ~/nacos2.3.0
```


## 三、删除nacos容器
```bash
# 停止容器
docker stop nacos

# 删除容器
docker rm nacos
```


## 四、启动nacos容器并挂载配置文件
启动脚本 [nacos2.3.0.sh](./nacos2.3.0.sh)
```bash
# 执行脚本 启动镜像
sh nacos2.3.0.sh

# 查看是否启动成功
docker ps
```


## 五、修改nacos的配置信息
直接修改挂载出来的配置文件即可。

修改完记得重启
```bash
# 停止nacos  
docker stop nacos

# 启动 nacos 
docker start nacos
```


---
- [Docker启动安装nacos（详情讲解，全网最细）](https://blog.csdn.net/ilvjiale/article/details/129417768)
- [docker-hub/nacos](https://hub.docker.com/r/nacos/nacos-server)
- [Nacos使用2.0.1版本启动出现9848端口错误的解决方式(亲测有效)](https://blog.csdn.net/li1325169021/article/details/121626299)
