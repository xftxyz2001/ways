## 1、下载 jdk21

```bash
wget https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.tar.gz
```

## 2、编写 Dockerfile

```Dockerfile
FROM centos:7

ENV JAVA_HOME=/usr/local/jdk-21
ENV PATH=$JAVA_HOME/bin:$PATH

ADD jdk-21_linux-x64_bin.tar.gz /usr/local/
```

## 3、构建镜像

```bash
# docker build -t <image_name>:<tag> .
docker build -t xftxyz2001/jdk21:latest .
```

---
- [dockerfile制作jdk17基础镜像](https://blog.csdn.net/guan3515/article/details/131982635)
