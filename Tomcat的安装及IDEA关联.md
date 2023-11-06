## 一、Tomcat卸载
1. 删除Tomcat安装目录
   - 因Tomcat的安装只需解压到某目录，卸载也只需将原Tomcat目录删除即可。
2. 删除相关注册表
   - win+r输入"regedit"
   - ctrl+f输入"tomcat" 逐项查找并逐项删除
3. 删除Tomcat service
   - 以管理员身份运行cmd，执行命令"sc delete tomcatx"(x为你下载的Tomcat版本)。
4. 清除环境变量
   - CATALINA_HOME
   - Path:"%CATALINA_HOME\bin"和"%CATALINA_HOME\lib"


## 二、Tomcat安装

### 1. 下载Tomcat安装包并解压
1. 访问 [Apache官网](http://tomcat.apache.org/)
2. 版本选择
   1. [版本兼容表](https://tomcat.apache.org/whichversion.html)
      Servlet Spec|JSP Spec|EL Spec|WebSocket Spec|Authentication (JASPIC) Spec|Apache Tomcat Version|Latest Released Version|Supported Java Versions
      -|-|-|-|-|-|-|-
      6.1|4.0|6.0|TBD|TBD|11.0.x|11.0.0-M13 (alpha)|21 and later
      6.0|3.1|5.0|2.1|3.0|10.1.x|10.1.15|11 and later
      5.0|3.0|4.0|2.0|2.0|10.0.x (superseded)|10.0.27 (superseded)|8 and later
      4.0|2.3|3.0|1.1|1.1|9.0.x|9.0.82|8 and later
      3.1|2.3|3.0|1.1|1.1|8.5.x|8.5.95|7 and later
      3.1|2.3|3.0|1.1|N/A|8.0.x (superseded)|8.0.53 (superseded)|7 and later
      3.0|2.2|2.2|1.1|N/A|7.0.x (archived)|7.0.109 (archived)|6 and later (7 and later for WebSocket)
      2.5|2.1|2.1|N/A|N/A|6.0.x (archived)|6.0.53 (archived)|5 and later
      2.4|2.0|N/A|N/A|N/A|5.5.x (archived)|5.5.36 (archived)|1.4 and later
      2.3|1.2|N/A|N/A|N/A|4.1.x (archived)|4.1.40 (archived)|1.3 and later
      2.2|1.1|N/A|N/A|N/A|3.3.x (archived)|3.3.2 (archived)|1.1 and later
   2. 在左边的Download选择版本，这里选择[Tomcat 10](https://tomcat.apache.org/download-10.cgi)（注意：Tomcat 10的包名由javax更换为了jakarta，所以Tomcat 10不兼容Tomcat 9及以下版本的项目）
3. 下拉找到Binary Distributions，其中有解压版及安装版可供选择：
   1. 安装版通用。
   2. 解压版需要下载对应自己电脑系统的位数。（推荐使用64位的解压版。【**64-bit Windows zip**】
4. 解压到合适位置（建议路径中不含中文和空格）


### 2. 配置环境变量（可选）
1. `CATALINA_HOME`: Tomcat解压路径，需要事先配置 `JAVA_HOME`
2. Path: `%CATALINA_HOME%\bin` 和 `%CATALINA_HOME%\lib`


## 三、启动Tomcat
进入Tomcat解压路径下的bin目录，双击startup.bat启动Tomcat。

在未更改Tomcat端口配置的情况下，若能在浏览器访问如下地址看到欢迎页，即代表Tomcat安装成功！ [http://localhost:8080](http://localhost:8080)


## 四、解决Tomcat控制台乱码
因为Windows系统中，其命令行窗口在解码字节数组时，默认使用本地字符集（对于我们就是GBK），而Tomcat默认输出的启动信息是通过UTF-8进行编码的，这就导致编码与解码所使用字符集的不一致，从而出现了乱码情况！

1. 进入Tomcat解压路径下的conf目录，选中 `logging.properties` 文件，使用文本编辑器打开。
2. 修改：`java.util.logging.ConsoleHandler.encoding = GBK`


## 五、IDEA关联Tomcat
1. 打开IDEA进入设置（快捷键：`Ctrl+Alt+S`）
2. 找到 Build, Execution, Deployment（构建、执行、部署） 下的 Application Servers（应用程序服务器）
3. 点击 `+` ，选择 Tomcat Server（Tomcat服务器）
4. 选择Tomcat主目录（这里是解压路径，是bin的上一级），点击OK

