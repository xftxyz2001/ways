## 包管理器方式安装

### Ubuntu 10.10(maverick)或更新版本，Debian 6.0(squeeze)或更新版本
```shell
sudo aptitude install git
sudo aptitude install git-doc git-svn git-email gitk
```

其中git软件包包含了大部分git命令，是必装的软件包。
软件包git-svn、git-email、gitk本来也是git软件包的一部分，但是因为有着不一样的软件包依赖（如更多perl模块，tk等），所以单独作为软件包发布。

### RHEL、Fedora、CentOS
```shell
yum install git
yum install git-svn git-email gitk
```


## 从源码开始安装（以2.44.0版本为例）

### 1. 下载源码并解压
```shell
wget https://www.kernel.org/pub/software/scm/git/git-2.44.0.tar.gz
tar -zxvf git-2.44.0.tar.gz
cd git-2.44.0
```

### 2. 安装（以下安装到 `/usr/local` 目录下）
```shell
make prefix=/usr/local all
sudo make prefix=/usr/local install
```

### 3. 安装Git文档（可选）
```shell
make prefix=/usr/local doc info
sudo make prefix=/usr/local install-doc install-html install-info
```

### 4. 命令补齐
Linux的shell环境(bash)通过bash-completion软件包提供命令补齐功能，能够实现在录入命令参数时按一下或两下TAB键，实现参数的自动补齐或提示。例如输入 `git com` 后按下TAB键，会自动补齐为 `git commit`。
```shell
# 将源码包中的命令补齐脚本复制到bash-completion对应的目录下
cp contrib/completion/git-completion.bash /etc/bash_completion.d/
# 重新加载自动补齐脚本
. /etc/bash_completion
```

为了能够在终端开启时自动加载bash_completion脚本，需要在本地配置文件 `~/.bash_profile` 或全局文件 `/etc/bashrc` 中添加如下内容：
```shell
if [-f /etc/bash_completion ]; then
. /etc/bash_completion
fi
```


---
- [Git官网](https://git-scm.com/)
  - [下载页](https://git-scm.com/downloads)
- [Git源码包](https://www.kernel.org/pub/software/scm/git/)
  - [镜像](https://mirrors.edge.kernel.org/pub/software/scm/git/)

