## 目录结构
| 目录及文件               | 说明                                                                                                                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| bin                      | 用于存放 Tomcat的启动、停止等批处理脚本和Shell脚本                                                                                                                                               |
| bin/startup. bat         | 用于在 Windows下启动 Tomcat                                                                                                                                                                      |
| bin/startup.sh           | 用于在 Linux下启动 Tomcat                                                                                                                                                                        |
| bin/shutdown. bat        | 用于在 Windows下停止 Tomcat                                                                                                                                                                      |
| bin/shutdown.sh          | 用于在 Linux下停止 Tomcat                                                                                                                                                                        |
| conf                     | 用于存放 Tomcat的相关配置文件                                                                                                                                                                    |
| conf/Catalina            | 用于存储针对每个虚拟机的 Context 配置                                                                                                                                                            |
| conf/context.xml         | 用于定义所有Web应用均需要加载的 Context 配置，如果Web应用指定了自己的context.xml，那么该文件的配置将被覆盖                                                                                       |
| conf/catalina.properties | Tomcat环境变量配置                                                                                                                                                                               |
| conf/catalina.policy     | 当 Tomcat在安全模式下运行时，此文件为默认的安全策略配置                                                                                                                                          |
| conf/logging.properties  | Tomcat日志配置文件，可通过该文件修改 Tomcat日志级别以及日志路径等                                                                                                                                |
| conf/server.xml          | Tomcat服务器核心配置文件，用于配置 Tomcat的链接器、监听端口、处理请求的虚拟主机等。可以说，Tomcat主要根据该文件的配置信息创建服务器实例                                                          |
| conf/tomcat-users.xml    | 用于定义 Tomcat默认用户及角色映射信息，Tomcat的 Manager模块即用该文件中定义的用户进行安全认证                                                                                                    |
| conf/web.xml             | Tomcat中所有应用默认的部署描述文件，主要定义了基础 Servlet和MIME映射。如果应用中不包含 Web. xml，那么 Tomcat将使用此文件初始化部署描述，反之，Tomcat会在启动时将默认部署描述与自定义配置进行合并 |
| lib                      | Tomcat服务器依赖库目录，包含 Tomcat服务器运行环境依赖lar包                                                                                                                                       |
| logs                     | Tomcat默认的日志存放路径                                                                                                                                                                         |
| webapps                  | Tomcat默认的Web应用部署目录                                                                                                                                                                      |
| work                     | 存放Web应用JSP代码生成和编译后产生的class文件目录                                                                                                                                                |
| temp                     | 存放tomcat在运行过程中产生的临时文件                                                                                                                                                             |

## 原理
客户端用户点击浏览器服务连接，浏览器通过客户端底层服务通过路由传送报文，目标服务器获取解析报文，Tomcat监听程序触发处理请求

### 一、Tomcat 软件目录结构及功能
bin： 服务相关脚本，例如：启动、关闭等
conf： 存放不同的配置文件，列如：server.xml、web.xml
lib： tomcat 运行需要的库文件
logs： 运行的日志文件
webapps： web部署的根目录
work ：存放jsp编译后的class文件

### 二、server分析系统结构
1. server：提供一个接口让其它程序能够访问到这个 Service 集合、同时要维护它所包含的所有 Service 的生命周期，包括如何初始化、如何结束服务、如何找到别人要访问的 Service
2. service：是server下一个集合，service包含多个接收请求的connector并有一个处理所有连接的容器container
3. connector：作用是监听客户端请求，并将请求封装提交container处理，然后将处理结果返回客户端
   - tomcat有两个典型的connector，一个用来监听浏览器的http，另一个是用来监听webservice
   - Coyote Http/1.1 Connector 在端口8080处侦听来自客户browser的http请求
   - Coyote AJP/1.3 Connector 在端口8009处侦听来自其它WebServer(Apache)的servlet/jsp代理请求
4. container
   1. Engine
      - Engine下可以配置多个虚拟主机Virtual Host，每个虚拟主机都有一个域名
      - 当Engine获得一个请求时，它把该请求匹配到某个Host上，然后把该请求交给该Host来处理
      - Engine有一个默认虚拟主机，当请求无法匹配到任何一个Host上的时候，将交给该默认Host来处理
   2. Host
      - 代表一个Virtual Host，虚拟主机，每个虚拟主机和某个网络域名Domain Name相匹配
      - 每个虚拟主机下都可以部署(deploy)一个或者多个Web App，每个Web App对应于一个Context，有一个Context path
      - 当Host获得一个请求时，将把该请求匹配到某个Context上，然后把该请求交给该Context来处理
      - 匹配的方法是“最长匹配”，所以一个path==""的Context将成为该Host的默认Context
      - 所有无法和其它Context的路径名匹配的请求都将最终和该默认Context匹配
   3. Context
      - 一个Context对应于一个Web Application，一个Web Application由一个或者多个Servlet组成
      - Context在创建的时候将根据配置文件$CATALINA_HOME/conf/web.xml和$WEBAPP_HOME/WEB-INF/web.xml载入Servlet类
      - 当Context获得请求时，将在自己的映射表(mapping table)中寻找相匹配的Servlet类
      - 如果找到，则执行该类，获得请求的回应，并返回
5. Context的部署配置文件web.xml的说明
   - 一个Context对应于一个Web App，每个Web App是由一个或者多个servlet组成的
   - 当一个Web App被初始化的时候，它将用自己的ClassLoader对象载入“部署配置文件web.xml”中定义的每个servlet类
   - 它首先载入在$CATALINA_HOME/conf/web.xml中部署的servlet类
   - 然后载入在自己的Web App根目录下的WEB-INF/web.xml中部署的servlet类
   - web.xml文件有两部分：servlet类定义和servlet映射定义
   - 每个被载入的servlet类都有一个名字，且被填入该Context的映射表(mapping table)中，和某种URL PATTERN对应
   - 当该Context获得请求时，将查询mapping table，找到被请求的servlet，并执行以获得请求回应
   - 分析一下所有的Context共享的web.xml文件，在其中定义的servlet被所有的Web App载入

### 三、例子：Tomcat Server处理一个http请求的过程
假设来自客户的请求为：http://localhost:8080/wsota/wsota_index.jsp

请求被发送到本机端口8080，被在那里侦听的Coyote HTTP/1.1 Connector获得
1. Connector把该请求交给它所在的Service的Engine来处理，并等待来自Engine的回应
2. Engine获得请求localhost/wsota/wsota_index.jsp，匹配它所拥有的所有虚拟主机Host
3. Engine匹配到名为localhost的Host（即使匹配不到也把请求交给该Host处理，因为该Host被定义为该Engine的默认主机）
4. localhost Host获得请求/wsota/wsota_index.jsp，匹配它所拥有的所有Context
5. Host匹配到路径为/wsota的Context（如果匹配不到就把该请求交给路径名为""的Context去处理）
6. path="/wsota"的Context获得请求/wsota_index.jsp，在它的mapping table中寻找对应的servlet
7. Context匹配到URL PATTERN为*.jsp的servlet，对应于JspServlet类
8. 构造HttpServletRequest对象和HttpServletResponse对象，作为参数调用JspServlet的doGet或doPost方法
9.  Context把执行完了之后的HttpServletResponse对象返回给Host
10. Host把HttpServletResponse对象返回给Engine
11. Engine把HttpServletResponse对象返回给Connector
12. Connector把HttpServletResponse对象返回给客户browser

 