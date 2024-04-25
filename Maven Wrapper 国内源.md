## 一、Maven Wrapper简介
一般开发者初次遇见 `Maven Wrapper` 是在创建SpringBoot项目时看见根目录下有几个奇怪的文件，想必大部分都不会使用它而是随手删掉。其实 `Maven Wrapper` 是受了 `Gradle Wrapper` 的启发而来，其能够让开发者电脑上不需要安装Maven不用配置环境变量，也能使用Maven构建项目，并且在团队开发时，能够让每个开发人员都保持一致的Maven版本。其由两个文件一个目录组成，具体如下:
- .mvn
    - wrapper
        - maven-wrapper.jar
        - maven-wrapper.properties
        - MavenWrapperDownloader.java
- mvnw `供Unix使用`
- mvnw.cmd `供Windows使用`

## 二、Maven Wrapper 国内源
`Maven Wrapper` 的配置文件为 `.mvn/wrapper` 目录中的 `maven-wrapper.properties` 文件，默认内容是
```properties
distributionUrl=https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/x.y.z/apache-maven-x.y.z-bin.zip
wrapperUrl=https://repo.maven.apache.org/maven2/org/apache/maven/wrapper/maven-wrapper/a.b.c/maven-wrapper-a.b.c.jar
```

在开发者初次使用 `./mvnw xxx` 命令时，其会根据配置文件中的下载地址去下载指定maven文件，默认会下载到用户目录的 `.m2` 中，但由于不可抗力，大部分地区的下载速度都极慢，因此可配置国内源提提速，修改后内容如下（以阿里云为例）：
```properties
distributionUrl=https://mirrors.aliyun.com/apache/maven/maven-x/x.y.z/binaries/apache-maven-x.y.z-bin.zip
wrapperUrl=https://repo.maven.apache.org/maven2/org/apache/maven/wrapper/maven-wrapper/a.b.c/maven-wrapper-a.b.c.jar
```

## 三、Maven 国内源
光提速 `mvnw` 显然是不够的，通过 `mvnw` 安装依赖时仍然默认从中央仓库下载包。一般本机安装 `Maven` 时，我们可以在 `conf/setting.xml` 中配置maven的国内源，但是使用 `Maven Wrapper` 时并没有看到类似 `setting.xml` 的文件。此时可在根目录的 `pom.xml` 中直接指定国内源，若有多个项目则每个项目都配置上即可，具体内容如下：
```xml
<project>
    <!-- 省略其他配置 -->

    <repositories>
        <repository>
            <id>aliyunmaven</id>
            <name>阿里云公共仓库</name>
            <url>https://maven.aliyun.com/repository/public</url>
        </repository>
    </repositories>
    <pluginRepositories>
        <pluginRepository>
            <id>aliyunmaven</id>
            <name>阿里云公共仓库</name>
            <url>https://maven.aliyun.com/repository/public</url>
        </pluginRepository>
    </pluginRepositories>
</project>
```

---
- [Maven Wrapper 国内源](https://seepine.com/dev/maven/wrapper)
