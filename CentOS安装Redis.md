### 1、下载fedora的 epel 仓库
```
yum install epel-release
```

### 2、安装 redis
```
yum install redis
```

### 3、查看 redis 状态
安装完毕后需要启动
```
# 启动redis
service redis start
# 停止redis
service redis stop
# 查看redis运行状态
service redis status
# 查看redis进程
ps -ef | grep redis
```

### 4、设置 redis 开启启动
```
chkconfig redis on
```

### 5、进入 redis 服务
```
# 进入本机redis
redis-cli
# 列出所有key
keys *
```

### 6、防火墙开放端口
```
# 开启6379
/sbin/iptables -I INPUT -p tcp --dport 6379 -j ACCEPT
# 开启6380
/sbin/iptables -I INPUT -p tcp --dport 6380 -j ACCEPT
# 保存
/etc/rc.d/init.d/iptables save
# centos 7下执行
service iptables save
```

### 7、修改redis默认端口和密码
默认端口一般是 6379 ，但也可以改成你想要的端口。

打开配置文件
vi /etc/redis.conf

修改默认端口，查找 port 6379 修改为相应端口即可

修改默认密码，查找 requirepass foobared 将 foobared 修改为你的密码

### 使用配置文件启动
```
redis-server /etc/redis.conf &
```

### 使用端口登陆
```
redis-cli -h 127.0.0.1 -p 6179
```

输入刚才输入的密码
```
auth 111
```

### 关闭 redis
使用命令关闭
```
redis-cli -h 127.0.0.1 -p 6179
shutdown
```

杀掉进程
```
ps -ef | grep redis
kill -9 XXX
```
