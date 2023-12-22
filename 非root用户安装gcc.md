## 下载
打开 [下载链接](https://ftp.gnu.org/gnu/gcc/) 找到合适的版本。

> 一般情况下，`tar.xz` 比 `tar.gz` 要小，所以建议下载 `tar.xz` 包，这里以 [gcc-9.5.0](https://ftp.gnu.org/gnu/gcc/gcc-9.5.0/gcc-9.5.0.tar.xz) 为例

gcc的国内大学镜像：
```
http://mirrors.ustc.edu.cn/gnu/gcc/
https://mirrors.tuna.tsinghua.edu.cn/gnu/gcc/
http://mirrors.nju.edu.cn/gnu/gcc/
http://mirror.hust.edu.cn/gnu/gcc/
```

> 可以在本地下载好后，再上传到服务器上。


## 解压
```bash
# 解压
tar -xJf gcc-9.5.0.tar.xz
# 进入目录
cd gcc-9.5.0
```


## 下载依赖
直接运行
```bash
./contrib/download_prerequisites
```

### 方案二：更换下载源
下载速度太慢的话，可以更换下载源：
将 `./contrib/download_prerequisites` 中的 `ftp://gcc.gnu.org/pub/gcc/infrastructure` 替换为 `http://www.mirrorservice.org/sites/sourceware.org/pub/gcc/infrastructure` 即可。

一条命令更换下载源：
```bash
sed -i 's/ftp:\/\/gcc\.gnu\.org\/pub\/gcc\/infrastructure/http:\/\/www\.mirrorservice\.org\/sites\/sourceware\.org\/pub\/gcc\/infrastructure/g' ./contrib/download_prerequisites
```

### 方案三：本地下载
> 也可以在本地[下载](http://www.mirrorservice.org/sites/sourceware.org/pub/gcc/infrastructure)好后，再上传到刚才解压的目录（这里是`gcc-9.5.0`）中（这四个文件无需解压）：
> - gmp-6.1.0.tar.bz2
> - mpfr-3.1.4.tar.bz2
> - mpc-1.0.3.tar.gz
> - isl-0.18.tar.bz2

> 方案二、三操作完后，再运行 `./contrib/download_prerequisites` 即可。


## 创建编译目录/安装目录
```bash
# 创建编译目录
mkdir build
cd build
# 因为非root用户没有root权限，所以指定到自己有权限的目录下面
# 这里使用--prefix指定安装目录（这里路径不一定要和我一样，下面配置PATH时，也要对应修改）
../configure --prefix=/home/xxx/tools/gcc-9.5.0 --disable-multilib
```


## 编译
```bash
# 使用make命令编译
# 使用-j参数指定并发数（一般设置为CPU核心数的2倍）
make -j8
```

> make命令编译时间较长（具体取决于CPU性能），请耐心等待。


## 安装
```bash
make install
```


## 配置环境变量
```bash
# 编辑 ~/.bashrc 文件
vim ~/.bashrc
```

在文件末尾添加如下内容：
```bash
# gcc
export PATH=/home/xxx/tools/gcc-9.5.0/bin:$PATH
export LD_LIBRARY_PATH=/home/xxx/tools/gcc-9.5.0/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/xxx/tools/gcc-9.5.0/lib64:$LD_LIBRARY_PATH
```

> LD_LIBRARY_PATH 按需添加

保存后，执行 `source ~/.bashrc` 使配置生效。


## 验证
```bash
# 查看gcc路径
which gcc
# 查看gcc版本
gcc -v
```


---
参考
- [无root权限安装GCC（一遍成功）_非root安装gcc-CSDN博客](https://blog.csdn.net/qq_38308388/article/details/127574517)
- [gcc国内镜像-CSDN博客](https://blog.csdn.net/mnmiaoyi/article/details/98847144)
- [安装/升级gcc时，执行 ./contrib/download_prerequisites 太慢_linux 连接 connecting to gcc.gnu.org 建立 连接慢-CSDN博客](https://blog.csdn.net/qq_29695701/article/details/115182856)
- [GCC9.5离线安装_gcc离线安装包-CSDN博客](https://blog.csdn.net/ab0902cd/article/details/125541985)
