【转载】CentOS7 升级 Git (最新方法,秒杀一切旧方法!)
> 作者：HinGwenWoong  
> 一个有着清晰目标不停奋斗的程序猿，热爱技术，喜欢分享，共同进步！  
> CSDN: HinGwenWoong  
> 原文链接：[CentOS7 升级 Git (最新方法,秒杀一切旧方法!)](https://blog.csdn.net/hxj0323/article/details/119751427)

### 1. 卸载旧版本的Git
```bash
yum remove git
```

### 2. 安装 IUS：
```bash
yum install \
https://repo.ius.io/ius-release-el7.rpm \
https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```

### 3. 去到 IUS 的 [Github repo](https://github.com/search?q=org%3Aiusrepo+topic%3Arpm&s=updated) 查看需要的库和版本：
![1680684548823](image/CentOS7升级Git/1680684548823.png)  

### 4. 我这里安装的是 `Git 2.36`  
去到 CentOS 在命令行直接敲：

```bash
yum install git236
```

### 5. 成功
