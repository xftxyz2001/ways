## 下载解压
- [Maven官网](https://maven.apache.org/)
  - [下载页面](https://maven.apache.org/download.cgi#files)

1. 下载：点击 Binary zip archive 行 Link 列 `apache-maven-x.x.x-bin.zip` 下载

2. 解压：这里假设解压到了 `<DIR>` 目录下。（此处的目录为bin目录的上级目录）


## 配置环境变量
1. 新建环境变量 `MAVEN_HOME`，值为 `<DIR>`
2. 修改环境变量 `Path`，添加 `%MAVEN_HOME%\bin`

> 测试是否安装成功：`mvn -v`


## 配置本地仓库（非必须）
修改 `<DIR>\conf\settings.xml` 文件，添加 `<localRepository>` 标签，修改其值为本地仓库的路径，如：
```xml
<localRepository>D:\maven\repository</localRepository>
```

> 缺省为 `${user.home}/.m2/repository` 即 `C:\Users\<username>\.m2\repository`


## 配置[阿里云镜像](https://developer.aliyun.com/mvn/guide)（非必须）
修改 `<DIR>\conf\settings.xml` 文件，在 `<mirrors>` 标签下添加 `<mirror>` 标签，如：
```xml
<mirror>
    <id>aliyunmaven</id>
    <mirrorOf>*</mirrorOf>
    <name>阿里云公共仓库</name>
    <url>https://maven.aliyun.com/repository/public</url>
</mirror>
```

> 若不配置，默认使用中央仓库，中央仓库在国外，国内访问速度可能较慢。（~~当然如果你科学上网那另当别论~~）


## 配置默认JDK版本（非必须）
修改 `<DIR>\conf\settings.xml` 文件，在 `<profiles>` 标签下添加 `<profile>` 标签，以JDK17为例：
```xml
<profile>
    <id>jdk-17</id>
    <activation>
        <activeByDefault>true</activeByDefault>
        <jdk>17</jdk>
    </activation>
    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <maven.compiler.compilerVersion>17</maven.compiler.compilerVersion>
    </properties>
</profile>
```

当然也可以通过项目的 pom.xml 文件来指定 JDK 版本，如：
```xml
<properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
    <maven.compiler.compilerVersion>17</maven.compiler.compilerVersion>
</properties>
```


## IDEA配置本地Maven（推荐）
1. 打开IDEA进入设置（快捷键：`Ctrl+Alt+S`）
2. 找到 Build, Execution, Deployment（构建、执行、部署） -> Build Tools（构建工具） -> Maven
3. 修改 Maven home path（Maven 主路径）为 `<DIR>`


---
## Maven Wrapper（自用）
很多项目可能包含了 [Maven Wrapper](https://maven.apache.org/wrapper/) 的配置，可以通过 `mvnw` 或 `mvnw.cmd` 来执行 Maven 命令。

在执行 Maven 命令时，会自动下载项目 `.mvn/wrapper/maven-wrapper.jar` 和 `.mvn/wrapper/maven-wrapper.properties` 文件中指定的 Maven 版本至 `%homepath%/.m2/wrapper/dists` 目录下，然后使用该版本的 Maven 来执行命令。

既然如此，那么我就不再额外安装 Maven 了，直接修改 `MAVEN_HOME` 环境变量为项目 Maven Wrapper 使用的 Maven 的路径，通常为 `%homepath%/.m2/wrapper/dists/apache-maven-x.x.x-bin/<hash>/apache-maven-x.x.x`。

