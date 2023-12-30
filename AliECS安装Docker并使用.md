[原网页：云服务器 ECS》实践教程》搭建应用》安装Docker并使用（Linux）](https://help.aliyun.com/zh/ecs/use-cases/deploy-and-use-docker-on-alibaba-cloud-linux-2-instances)

## 准备资源

已创建一台基础ECS实例，并满足以下配置。如果您还未创建，请参见[自定义购买实例](https://help.aliyun.com/zh/ecs/user-guide/create-an-instance-by-using-the-wizard#task-vwq-5g4-r2b)。

- 操作系统：CentOS 7.x 64位、CentOS 8.x 64位、Alibaba Cloud Linux 3 64位、Alibaba Cloud Linux 2 64位

- 网络类型：专有网络VPC

- IP地址：实例已分配公网IP地址或绑定弹性公网IP（EIP）。具体操作，请参见[绑定和解绑弹性公网IP](https://help.aliyun.com/zh/ecs/user-guide/associate-or-disassociate-an-eip#section-jwk-pjm-5qh)。

- 安全组：入方向放行80、22、8080端口。具体操作，请参见[添加安全组规则](https://help.aliyun.com/zh/ecs/user-guide/add-a-security-group-rule)。


## 安装Docker

1. 远程连接ECS实例。

    关于连接方式的介绍，请参见[连接方式概述](https://help.aliyun.com/zh/ecs/user-guide/connection-methods#concept-tmr-pgx-wdb)。

2. 安装Docker。

    - Alibaba Cloud Linux 3

        1. 运行以下命令，添加docker-ce的dnf源。
    
            ```shell
            sudo dnf config-manager --add-repo=https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
            ```
    
        2. 运行以下命令，安装Alibaba Cloud Linux 3专用的dnf源兼容插件。
    
            ```shell
            sudo dnf -y install dnf-plugin-releasever-adapter --repo alinux3-plus
            ```
    
        3. 运行以下命令，安装Docker。
    
            ```shell
            sudo dnf -y install docker-ce --nobest
            ```
    
            - 如果执行命令时，出现类似如下的报错信息，您需要执行`sudo dnf clean packages`清除软件包缓存后，重新安装docker-ce。
    
                ```shell
                (8-9/12): docker-ce-24.0.7-1.el8.x86_64.rpm 38% [================- ] 8.2 MB/s | 38 MB 00:07 ETA
                The downloaded packages were saved in cache until the next successful transaction.
                You can remove cached packages by executing 'dnf clean packages'.
                Error: Error downloading packages:
                containerd.io-1.6.26-3.1.el8.x86_64: Cannot download, all mirrors were already tried without success
                ```
    
            - 如果执行命令时，出现类似下图的报错信息，您需要注释/etc/yum.repos.d下的CentOS源，注释后重新安装docker-ce。
    
                ![adad566](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1286511071/p477222.png)
    
    
    - Alibaba Cloud Linux 2
    
        1. 运行以下命令，下载docker-ce的yum源。
    
            ```shell
            sudo wget -O /etc/yum.repos.d/docker-ce.repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
            ```
    
        2. 运行以下命令，安装Alibaba Cloud Linux 2专用的yum源兼容插件。
    
            ```shell
            sudo yum install yum-plugin-releasever-adapter --disablerepo=* --enablerepo=plus
            ```
    
        3. 运行以下命令，安装Docker。
    
            ```shell
            sudo yum -y install docker-ce
            ```
    
    - CentOS 7.x
    
        1. 运行以下命令，下载docker-ce的yum源。
    
            ```shell
            sudo wget -O /etc/yum.repos.d/docker-ce.repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
            ```
    
        2. 运行以下命令，安装Docker。
    
            ```shell
            sudo yum -y install docker-ce
            ```
    
    - CentOS 8.x
    
        1. 切换CentOS 8源地址。
    
            CentOS 8操作系统版本结束了生命周期（EOL），按照社区规则，CentOS 8的源地址http://mirror.centos.org/centos/8/内容已移除，您在阿里    云上继续使用默认配置的CentOS 8的源会发生报错。如果您需要使用CentOS 8系统中的一些安装包，则需要手动切换源地址。具体操作，请参见    [CentOS 8 EOL如何切换源？](https://help.aliyun.com/zh/ecs/user-guide/change-centos-8-repository-addresses#task-2182261)。
    
        2. 运行以下命令，安装DNF。
    
            ```shell
            sudo yum -y install dnf
            ```
    
        3. 运行以下命令，安装Docker存储驱动的依赖包。
    
            ```shell
            sudo dnf install -y device-mapper-persistent-data lvm2
            ```
    
        4. 运行以下命令，添加稳定的Docker软件源。
    
            ```shell
            sudo dnf config-manager --add-repo=https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
            ```
    
        5. 运行以下命令，检查Docker软件源是否已添加。
    
            ```shell
            sudo dnf list docker-ce
            ```
    
            出现如下图所示回显，表示Docker软件源已添加。
    
            ![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8611226861/p680635.png)
    
        6. 运行以下命令安装Docker。
    
            ```shell
            sudo dnf install -y docker-ce --nobest
            ```


3. 执行以下命令，检查Docker是否安装成功。

    ```javascript
    sudo docker -v
    ```

    如下图回显信息所示，表示Docker已安装成功。

    ![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6489086861/p683254.png)

4. 执行以下命令，启动Docker服务，并设置开机自启动。

    ```shell
    sudo systemctl start docker
    sudo systemctl enable docker
    ```

5. 执行以下命令，查看Docker是否启动。

    ```shell
    sudo systemctl status docker
    ```

    如下图回显所示，表示Docker已启动。

    ![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9710116861/p679571.png)


## Docker基本使用

下文只列出Docker基本用法，更详细的操作命令，请参见[Docker官网](https://docs.docker.com/get-started/overview/)。

- **管理Docker守护进程**

    ```shell
    sudo systemctl start docker     #运行Docker守护进程
    sudo systemctl stop docker      #停止Docker守护进程
    sudo systemctl restart docker   #重启Docker守护进程
    sudo systemctl enable docker    #设置Docker开机自启动
    sudo systemctl status docker    #查看Docker的运行状态
    ```

- **管理镜像**

    本文以阿里云仓库的Apache镜像为例，介绍如何使用Docker管理镜像。

    - 拉取镜像。

        ```shell
        sudo docker pull registry.cn-hangzhou.aliyuncs.com/lxepoo/apache-php5
        ```

    - 修改标签。如果镜像名称较长，您可以修改镜像标签以便记忆区分。

        ```shell
        sudo docker tag registry.cn-hangzhou.aliyuncs.com/lxepoo/apache-php5:latest aliweb:v1
        ```

    - 查看已有镜像。

        ```shell
        sudo docker images
        ```

    - 强制删除镜像。

        ```shell
        sudo docker rmi -f registry.cn-hangzhou.aliyuncs.com/lxepoo/apache-php5
        ```

- **管理容器**

    下文的<镜像ID>可通过`docker images`命令查询。

    - 启动一个新容器。

        ```shell
        sudo docker run -it <镜像ID> /bin/bash
        ```

    - 启动一个新的容器，让容器在后台运行，并且指定容器的名称。

        ```shell
        sudo docker run -d --name <容器名> <镜像ID>
        ```

    - 查看容器ID。

        ```shell
        sudo docker ps
        ```

    - 将容器做成镜像。

        ```shell
        sudo docker commit <容器ID或容器名> <仓库名>:<标签>
        ```


## **使用Docker制作镜像**

本步骤指导如何通过Dockerfile定制制作一个简单的Nginx镜像。

1. 执行以下命令，拉取镜像。本示例以拉取阿里云仓库的Apache镜像为例。

    ```shell
    sudo docker pull registry.cn-hangzhou.aliyuncs.com/lxepoo/apache-php5
    ```

2. 修改镜像名称标签，便于记忆。

    ```shell
    sudo docker tag registry.cn-hangzhou.aliyuncs.com/lxepoo/apache-php5:latest aliweb:v1
    ```

3. 执行以下命令，新建并编辑Dockerfile文件。

    1. 执行以下命令，新建并编辑Dockerfile文件。

        ```shell
        vim Dockerfile
        ```

    2. 按`i`进入编辑模式，并添加以下内容，改造原镜像。

        ```shell
        #声明基础镜像来源。
        FROM aliweb:v1
        #声明镜像拥有者。
        MAINTAINER DTSTACK
        #RUN后面接容器运行前需要执行的命令，由于Dockerfile文件不能超过127行，因此当命令较多时建议写到脚本中执行。
        RUN mkdir /dtstact
        #开机启动命令，此处最后一个命令需要是可在前台持续执行的命令，否则容器后台运行时会因为命令执行完而退出。
        ENTRYPOINT ping www.aliyun.com
        ```

    3. 按`Esc`键，输入`:wq`并按`Enter`键，保存并退出Dockerfile文件。

4. 执行以下命令，基于基础镜像nginx构建新镜像。

    命令格式为`docker build -t <镜像名称>:<镜像版本> .`，**命令末尾的**`**.**`**表示Dockerfile文件的路径，不能忽略。**以构建新镜像aliweb:v2为例，则命令为：

    ```shell
    sudo docker build -t aliweb:v2 .
    ```

5. 执行以下命令，查看新镜像是否构建成功。

    ```shell
    sudo docker images
    ```

    如下图回显所示，表示构建成功。

    ![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8611226861/p680542.png)


## **安装并使用docker-compose**

docker-compose是Docker官方提供的用于定义和运行多个Docker容器的开源容器编排工具，可以使用YAML文件来配置应用程序需要的所有服务，然后使用docker-compose运行命令解析YAML文件配置，创建并启动配置文件中的所有Docker服务，具有运维成本低、部署效率高等优势。

关于docker-compose的更多信息，请参见[Docker官网](https://github.com/docker/compose)。

**重要**

仅Python 3及以上版本支持docker-compose，并请确保已安装pip。

### **安装docker-compose**

1. 运行以下命令，安装setuptools。

    ```shell
    sudo pip3 install -U pip setuptools
    ```

2. 运行以下命令，安装docker-compose。

    ```shell
    sudo pip3 install docker-compose
    ```

3. 运行以下命令，验证docker-compose是否安装成功。

    ```shell
    docker-compose --version
    ```

    如果回显返回docker-compose版本信息，表示docker-compose已安装成功。


### 使用docker-compose部署应用

下文以部署WordPress为例，介绍如何使用docker-compose部署应用。

1. 创建并编辑docker-compose.yaml文件。

    1. 运行以下命令，创建docker-compose.yaml文件。

        ```shell
        sudo vim docker-compose.yaml
        ```

    2. 按下`i`键，进入编辑模式，新增以下内容。

        本示例以安装WordPress为例。

        ```shell
        version: '3.1'             # 版本信息

        services:

          wordpress:               # 服务名称
            image: wordpress       # 镜像名称
            restart: always        # docker启动，当前容器必启动
            ports:
              - 80:80              # 映射端口
            environment:           # 编写环境
              WORDPRESS_DB_HOST: db
              WORDPRESS_DB_USER: wordpress
              WORDPRESS_DB_PASSWORD: 123456
              WORDPRESS_DB_NAME: wordpress
            volumes:               # 映射数据卷
              - wordpress:/var/www/html

          db:                      # 服务名称
            image: mysql:5.7       # 镜像名称
            restart: always        # docker启动，当前容器必启动
            ports:
               - 3306:3306         # 映射端口
            environment:           # 环境变量
              MYSQL_DATABASE: wordpress
              MYSQL_USER: wordpress
              MYSQL_PASSWORD: 123456
              MYSQL_RANDOM_ROOT_PASSWORD: '1'
            volumes:               # 卷挂载路径
              - db:/var/lib/mysql

        volumes:
          wordpress:
          db:
        ```

    3. 按下`Esc`键，退出编辑模式，然后输入`:wq`保存并退出。

2. 执行以下命令，启动应用.

    ```shell
    sudo env "PATH=$PATH" docker-compose up -d
    ```

3. 在浏览器中输入`https://云服务器ECS实例的公网IP`，即可进入WordPress配置页面，您可以根据界面提示配置相关参数后，访问WordPress。


## **相关文档**

- Docker的更多使用方法，请参见[Docker官方文档](https://docs.docker.com/reference/)。

- 使用Docker镜像。

    阿里云容器镜像服务ACR推出了[制品中心](https://help.aliyun.com/zh/acr/user-guide/artifact-center)，为容器开发者免费提供了来源于阿里云官方、龙蜥社区的安全可信容器基础镜像。部署Docker后，您可以直接使用[制品中心](https://help.aliyun.com/zh/acr/user-guide/artifact-center)的Docker容器镜像来实现特定业务需求，例如部署应用、开发环境、操作系统、AI/大数据学习框架等。

    您可以参考[在容器中使用Alibaba Cloud Linux镜像](https://help.aliyun.com/zh/alinux/getting-started/use-an-alibaba-cloud-linux-image-in-docker)，了解如何使用制品中心的容器镜像。

- Docker镜像加速。

    您可以使用P2P加速功能提升镜像拉取速度，减少应用部署时间。具体操作，请参见[在其他容器环境中使用P2P加速](https://help.aliyun.com/zh/acr/user-guide/use-the-p2p-acceleration-feature-on-hosts-where-docker-is-installed)。

- 您可以在Docker中配置CLI来管理您的阿里云资源。具体操作，请参见[在Docker中配置阿里云CLI](https://help.aliyun.com/document_detail/110805.html)。

- 如果您需要在轻量应用服务器上部署Docker，可参考[基于轻量应用服务器上部署并使用Docker](https://help.aliyun.com/zh/simple-application-server/use-cases/deploy-and-use-docker)。

- 您还可以选择使用[阿里云容器镜像服务ACR](https://help.aliyun.com/zh/acr/product-overview/what-is-container-registry)，管理和运行容器化应用程序。

