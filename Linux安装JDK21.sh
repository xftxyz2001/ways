#!/bin/bash

# 下载JDK 21
mkdir -p /usr/local/java
cd /usr/local/java
wget https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.tar.gz

# 解压文件
tar -zxvf jdk-21_linux-x64_bin.tar.gz

# 获取解压出的 JDK 文件夹的名字
jdk_folder=$(ls -d */ | grep 'jdk-21')

# 配置环境变量
echo "export JAVA_HOME=/usr/local/java/$jdk_folder" >> ~/.bashrc
echo 'export PATH=$PATH:$JAVA_HOME/bin' >> ~/.bashrc

# 使环境变量生效
source ~/.bashrc

# 验证安装
java -version
