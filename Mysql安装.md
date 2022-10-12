# mysql-8.0.30-winx64.zip安装配置方法

## 一、下载mysql-8.0.30-winx64.zip
下载地址：https://dev.mysql.com/downloads/mysql/

选择【Windows (x86, 64-bit), ZIP Archive】即可

点击【Download】【No thanks, just start my download.】


## 二、解压缩
## 三、新建data文件夹
## 四、配置my.ini初始化文件
记得修改basedir和datadir
```ini
[mysqld]
# 设置3306端口
port=3306
# 设置mysql的安装目录
basedir=C:\Software\Mysql
# 设置mysql数据库的数据的存放目录
datadir=C:\Software\Mysql\data
# 允许最大连接数
max_connections=200
# 允许连接失败的次数。
max_connect_errors=10
# 服务端使用的字符集默认为utf8mb4
character-set-server=utf8mb4
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
# 默认使用“mysql_native_password”插件认证
#mysql_native_password
default_authentication_plugin=mysql_native_password
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8mb4
[client]
# 设置mysql客户端连接服务端时默认使用的端口
port=3306
default-character-set=utf8mb4
```


## 五、初始化MySQL
进入mysql的bin目录，输入命令：`mysqld --initialize --user=mysql --console` ，完成MySQL的初始化。

在初始化成功后的提示最后一行末尾有MySQL的初始密码，请务必记住。便于后面进行密码的修改。


## 六、安装MySQL服务
输入命令：`mysqld --install`，完成MySQL服务的安装。

若MySQL服务提示已存在，可通过命令：`sc delete mysql`，将已存在服务删除。


## 七、启动MySQL服务
Mysql服务安装成功后，输入命令：`net start mysql`，完成MySQL服务的启动。


## 八、修改MySQL初始密码
输入命令：`mysql -u root -p`，再输入初始化生成的初始密码，进入MySQL工作窗口。

输入命令：`ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';`（其中123456为新设置的密码，用户自行定义。后面的 ; 为MySQL命令的结束标记，不能省略不写）。


## 九、退出MySQL工作窗口
在MySQL工作窗口中，输入命令exit 或 quit可退出MySQL。


## 十、停止MySQL服务
当不再使用MySQL服务后，输入命令：`net stop mysql`，完成MySQL服务的停止工作。


## 十一、配置环境变量
配置mysql的bin目录为环境变量（略）
