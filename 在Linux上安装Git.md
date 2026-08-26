在 Linux 上安装 Git 最简单的方法是使用您的 Linux 发行版的首选包管理器。
如果您更喜欢从源代码构建，可以在 kernel.org 上找到 [tarballs](https://www.kernel.org/pub/software/scm/git/)。最新版本是 [2.44.0](https://www.kernel.org/pub/software/scm/git/git-2.44.0.tar.gz)。

### Debian/Ubuntu

对于您的 Debian/Ubuntu 发行版的最新稳定版本
```bash
# apt-get install git
```

对于 Ubuntu，此 PPA 提供了最新的稳定上游 Git 版本
```bash
# add-apt-repository ppa:git-core/ppa 
# apt update; apt install git
```

### Fedora
```bash
# yum install git (直到 Fedora 21)
# dnf install git (Fedora 22 及以后)
```

### Gentoo
```bash
# emerge --ask --verbose dev-vcs/git
```

### Arch Linux
```bash
# pacman -S git
```

### openSUSE
```bash
# zypper install git
```

### Mageia
```bash
# urpmi git
```

### Nix/NixOS
```bash
# nix-env -i git
```

### FreeBSD
```bash
# pkg install git
```

### Solaris 9/10/11 (OpenCSW)
```bash
# pkgutil -i git
```

### Solaris 11 Express
```bash
# pkg install developer/versioning/git
```

### OpenBSD
```bash
# pkg_add git
```

### Alpine
```bash
$ apk add git
```

### Red Hat Enterprise Linux, Oracle Linux, CentOS, Scientific Linux 等
RHEL 及其衍生产品通常会提供 git 的较旧版本。您可以下载 [tarball](https://www.kernel.org/pub/software/scm/git/) 并从源代码构建，或者使用第三方仓库，如 [IUS](https://ius.io/) 社区项目，以获取 git 的更近版本。

### Slitaz
```bash
$ tazpkg get-install git
```

## 从源码安装（以2.44.0版本为例）

### 1. 下载源码并解压

```shell
wget https://www.kernel.org/pub/software/scm/git/git-2.44.0.tar.gz
tar -zxvf git-2.44.0.tar.gz
cd git-2.44.0
```

### 2. 安装到 `/usr/local`

```shell
make prefix=/usr/local all
sudo make prefix=/usr/local install
```

### 3. 安装Git文档（可选）

```shell
make prefix=/usr/local doc info
sudo make prefix=/usr/local install-doc install-html install-info
```

### 4. 配置命令补齐（可选）

```shell
cp contrib/completion/git-completion.bash /etc/bash_completion.d/
. /etc/bash_completion
```

为了在终端启动时自动加载命令补齐，可在本地配置文件 `~/.bash_profile` 或全局文件 `/etc/bashrc` 中添加：

```shell
if [ -f /etc/bash_completion ]; then
  . /etc/bash_completion
fi
```

## 参考

- [Git官网](https://git-scm.com/)
- [Git下载页](https://git-scm.com/downloads)
- [Git源码包](https://www.kernel.org/pub/software/scm/git/)
- [Git源码包镜像](https://mirrors.edge.kernel.org/pub/software/scm/git/)
