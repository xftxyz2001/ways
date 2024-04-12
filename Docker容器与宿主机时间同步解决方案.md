## 概述
如果在启动Docker容器的过程中没有单独配置localtime，很可能造成Docker容器时间与主机时间不一致的情况，比如UTC和CST相差8小时，换句话来说就是容器时间与北京时间相差8个小时。

可以通过 `date` 命令分别查看容器和宿主机系统时间


## 解决方案

### 方案1. `docker run` 添加参数
```bash
-v /etc/localtime:/etc/localtime
```

如 [MySQL容器启动](./mysql8.2.0.sh)

### 方案2. `DockerFile`

#### ※法1※
添加时区（亚洲/上海）环境变量，使用软连接将时区配置覆盖 `/etc/timezone`
```Dockerfile
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```

#### 法2
CentOS系统
```Dockerfile
RUN echo "Asia/Shanghai" > /etc/timezone
```

#### 法3
Ubuntu系统
```Dockerfile
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

### 方案3. `docker-compose.yml`

#### ※法1※
```yml
environment:
  TZ: Asia/Shanghai
```

#### 法2
```yml
environment:
  SET_CONTAINER_TIMEZONE=true
  CONTAINER_TIMEZONE=Asia/Shanghai
```

#### 法3
```yml
volumes:
  - /etc/timezone:/etc/timezone
  - /etc/localtime:/etc/localtime
```

### 方案4. 宿主机直接执行命令给某个容器同步时间

#### 法1：直接在宿主机操作
```bash
docker cp /etc/localtime 【容器ID或者NAME】:/etc/localtime
docker cp -L /usr/share/zoneinfo/Asia/Shanghai 【容器ID或者NAME】:/etc/localtime
```

#### 法2：登录容器同步时区timezone
```bash
ln -sf /usr/share/zoneinfo/Asia/Singapore /etc/localtime
```

> 注：这种方式在容器中运行的程序的时间不一定能更新过来，比如在容器运行的mysql服务，在更新时间后，通过sql查看mysql的时间：
```sql
select now() from dual;
```
如果时间并没有更改过来 ，则须重启mysql服务或者重启docker容器，mysql才能读取到更改过后的时间。


---
- [Docker容器与宿主机时间同步解决方案 - 知乎](https://zhuanlan.zhihu.com/p/456167599)
