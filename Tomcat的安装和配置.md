## 一、Tomcat卸载
1. 删除Tomcat安装目录
   - 因tomcat的安装只需解压到某目录，卸载也只需将原tomcat目录删除即可。
2. 删除相关注册表
   - win+r输入"regedit"
   - ctrl+f输入"tomcat" 逐项查找并逐项删除
3. 删除Tomcat service
   - 以管理员身份运行cmd，执行命令"sc delete tomcatx"(x为你下载的tomcat版本)。
4. 清除环境变量
   - CATALINA_HOME
   - Path:"%CATALINA_HOME\bin"和"%CATALINA_HOME\lib"


## 二、Tomcat安装

### 1. 下载Tomcat安装包并解压
1. 访问 [Apache官网](http://tomcat.apache.org/)
2. 在左边的Download选择版本，推荐使用Tomcat8版本及以上版本，但是也不用追求最新版本（切记：不要用10.x，会有很多问题）。
3. Binary Distributions种有解压版及安装版可供选择，解压版需要下载对应自己电脑系统的位数，安装版通用。此处使用64位的解压版。【64-bit Windows zip】
4. 解压到合适位置（建议路径中不含中文和空格）


### 2. 配置环境变量
1. CATALINA_HOME:Tomcat解压路径，在这之前可能还需要配置JAVA_HOME
2. Path:"%CATALINA_HOME\bin"和"%CATALINA_HOME\lib"

### 3. 将Tomcat注册为Windows服务（可选）
项目在tomcat中运行时，需要在Tomcat的bin目录下运行startup.bat，如果把Tomcat注册为Windows服务，可以设置该服务为开机自启动，不再需要bin目录下运行startup.bat，或者想启动Tomcat时，不进入Tomcat目录去找，而是直接启动该服务以启动Tomcat。

前提：一定要保证JDK和Tomcat位数是一致的，要么都是32位，要么都是64位的，不然会报错：windows不能在本地计算机启动Apache Tomcat。

1. 在Tomcat的bin目录下输入cmd，之后点击回车，进入命令行界面。
2. 在命令行输入如下命令，点击回车，即能看到服务已经注册成功！
```sh
service.bat install Tomcat   # Tomcat为注册的服务的名字，可选，不输入会有默认的【建议默认】
```

### 4. 启动Tomcat服务
1. 启动
   - 如果将Tomcat注册为Windows服务，可以使用`net start Tomcat服务名`启动Tomcat服务。
   - 不管有没有将Tomcat注册为Windows服务，我们都可以进入Tomcat安装的bin目录，双击startup.bat启动Tomcat。
2. 验证
   - 在未改端口的情况下，我们在浏览器访问如下地址，能看到如下网页，即代表Tomcat安装成功！ [http://localhost:8080](http://localhost:8080)


## 三、解决Tomcat控制台乱码
因为windows系统中，其命令行窗口在解码字节数组时，默认使用本地字符集（对于我们就是GBK），而tomcat默认输出的启动信息是通过utf8进行编码的，这就导致编码与解码所使用字符集的不一致，从而出现了乱码情况！

1. 进入Tomcat的conf目录，选中logging.properties文件，使用文本编辑器打开。
2. 修改：`java.util.logging.ConsoleHandler.encoding = GBK`

