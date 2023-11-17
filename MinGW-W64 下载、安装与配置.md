## 一、简介

### 1. MinGW 和 MinGW-W64 区别和联系
MinGW和MinGW-W64都是用于Windows平台的轻量级GNU工具链，用于开发和编译C和C++程序。
- MinGW（Minimalist GNU for Windows）是一个32位的GNU工具链，它提供了一套基于GNU的开发环境，包括GCC编译器和一些GNU库，可以用来编译Windows下的C和C++程序。但MinGW只支持32位程序的编译。
- MinGW-W64是一个64位的GNU工具链，是MinGW的升级版，原本它是MinGW的分支，后来成为独立发展的项目，它支持同时编译32位和64位程序。它包括了一系列的GNU库和工具，例如GCC、Binutils、GDB等，还支持一些实用工具和库，如OpenMP、MPI等。

总的来说，MinGW-W64可以看作是MinGW的升级版，它支持更多的编译选项和更多的库，可以编译出更加高效和安全的程序。

另外，MinGW-W64原本是从MinGW项目fork出来的独立的项目。MinGW 早已停止更新，内置的GCC最高版本为4.8.1，而MinGW-W64目前仍在维护，它也是GCC官网所推荐的。

> 关于更多 MinGW 和 MinGW-W64 相关的知识：
> - [科普MinGW MinGW-W64](https://blog.csdn.net/whatday/article/details/87113007)
> - [what-is-the-difference-between-mingw-mingw-w64-and-mingw-builds](https://stackoverflow.com/questions/25582110/what-is-the-difference-between-mingw-mingw-w64-and-mingw-builds)
>     
> MinGW-w64官网：[MinGW-w64](https://www.mingw-w64.org/)
> 
> GCC官网：[GCC, the GNU Compiler Collection - GNU Project](https://gcc.gnu.org/)

### 2. MSVCRT 和 UCRT 介绍
MSVCRT和UCRT都是用于Windows平台的C运行时库，提供了基本的C函数和类型，用于C程序的开发和运行。
- MSVCRT（Microsoft Visual C Runtime）是Microsoft Visual C++早期版本使用的运行时库，用于支持C程序的运行。它提供了一些常用的C函数，如printf、scanf、malloc、free等。MSVCRT只能在32位Windows系统上运行，对于64位系统和Windows Store应用程序不支持。
- UCRT（Universal C Runtime）是在Windows 10中引入的新的C运行时库，用于支持C程序的运行和开发。UCRT提供了一些新的C函数，同时还支持Unicode字符集和安全函数，如`strcpy_s`、`strcat_s`、`_itoa_s`等。UCRT同时支持32位和64位系统，并且可以与Windows Store应用程序一起使用。

总的来说，UCRT是Microsoft为了更好地支持Windows 10和Windows Store应用程序而开发的新一代C运行时库，相比于MSVCRT，UCRT提供了更多的功能和更好的兼容性。但对于旧的32位Windows系统，MSVCRT仍然是必需的。


## 二、下载
MinGW-w64 更新日志：
- [Changelog - MinGW-w64](https://www.mingw-w64.org/changelog/)

MinGW-w64 源码地址：
- `Github`上的：[mingw-w64/mingw-w64: (Unofficial) Mirror of mingw-w64-code](https://github.com/mingw-w64/mingw-w64)
- `sourceforge.net`上的：[mingw-w64](https://sourceforge.net/p/mingw-w64/mingw-w64/ci/master/tree/)

如果你对源码感兴趣或想要自己从源码编译`MinGW-w64`应用程序，上述源码供你使用。

> 如果你的github不稳定，可以参考：[几款Github加速神器](https://blog.csdn.net/B11050729/article/details/132131659)

官方没在任何地方提供二进制安装程序。

**哪里找`MinGW-w64`二进制应用程序？**

下面提供几种方式：  

### 1. 从 sourceforge.net 下载
- 在线安装
  - Win32 位：[Toolchains targetting Win32/Personal Builds/mingw-builds/installer/mingw-w64-install.exe](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe)
- 离线安装：
  - Win32 位：[Toolchains targetting Win32/Personal Builds/mingw-builds](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/)
  - Win64 位：[Toolchains targetting Win64/Personal Builds/mingw-builds](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/)

不推荐在线安装，安装过程特别慢，而且还可能失败！  
注意：这里提供的二进制安装程序是旧的，支持的GCC版本停留在了"MinGW-W64 GCC-8.1.0"

> _截至目前GCC最新版本为：GCC-13.2  
> 详情请参考：[GCC Releases - GNU Project](https://gcc.gnu.org/releases.html)_

如果你有特定需求，需要使用旧版本的，你可以参考下面的文章进行安装及配置：
- [下载安装MinGW-w64详细步骤（c/c++的编译器gcc的windows版，win10真实可用）](https://blog.csdn.net/jjxcsdn/article/details/123058745)
- [MinGW-w64的安装及配置教程](https://blog.csdn.net/didi_ya/article/details/111240502)

### 2. 从 github 下载
- 在线安装：
  - [Releases · Vuniverse0/mingwInstaller (github.com)](https://github.com/Vuniverse0/mingwInstaller/releases)
- 离线安装：
  - [Releases · mmozeiko/build-gcc-mingw (github.com)](https://github.com/mmozeiko/build-gcc-mingw/releases)
  - [Releases · niXman/mingw-builds-binaries (github.com)](https://github.com/niXman/mingw-builds-binaries/releases)

在线安装，需要先下载 [mingwInstaller.exe (Installer of MinGW-W64 with GUI)](https://github.com/Vuniverse0/mingwInstaller/releases/download/1.2.0/mingwInstaller.exe)，后面介绍

### 3. 从 镜像站点 下载
网上找到的一个MinGW-w64镜像站点（不知道何方神圣提供的，用就完了）  
[http://files.1f0.de/mingw/](http://files.1f0.de/mingw/)  
![MinGW-w64镜像站点](https://img-blog.csdnimg.cn/8a1654d7fcda409581f59a93b76de069.png)  

### 4. 自己编译
直接编译会比较复杂，这里推荐几个大神写好的`MinGW-w64`编译工具：
- [niXman/mingw-builds: Scripts for building the 32 and 64-bit MinGW-W64 compilers for Windows (github.com)](https://github.com/niXman/mingw-builds)
- [mmozeiko/build-gcc-mingw: Automatic 32-bit and 64-bit Windows build of gcc, mingw-w64, gdb and make. (github.com)](https://github.com/mmozeiko/build-gcc-mingw)

怎么使用？看对应的Readme介绍，本文不介绍。


## 三、安装与配置

### 1. 在线安装
_这里不介绍 `sourceforge.net`上的在线安装，它上面的GCC版本太老了_

这里介绍 [Releases · Vuniverse0/mingwInstaller (github.com)](https://github.com/Vuniverse0/mingwInstaller/releases) 的在线安装方式：

1. 下载`mingwInstaller.exe`  
   ![下载安装程序](https://img-blog.csdnimg.cn/e5ff72505f114f92b15094b782b1f1bd.png)  
2. 以管理员身份运行`mingwInstaller.exe`，开始安装  
   ![安装引导](https://img-blog.csdnimg.cn/a37d59f097ac4d5f87c128f2f3ec5cd4.png)  
3. 选择GCC版本  
   注意：[Releases · Vuniverse0/mingwInstaller (github.com)](https://github.com/Vuniverse0/mingwInstaller/releases) 有好几个版本的`mingwInstaller.exe`，不同的版本支持的GCC版本不一样，我这里使用的是1.2.0版  
   ![选择gcc版本](https://img-blog.csdnimg.cn/09afdcf07c0a44f98c696c8a730e8e2a.png)  
4. 选择软件架构  
   选择32bit还是64bit，看你自己的操作系统是多少位的  
   ![系统架构](https://img-blog.csdnimg.cn/784e3743a2eb4305977aebb94cff9221.png)  
5. 选择线程模型  
   你开发的程序如果是运行在Windows系统上就选`win32`，如果是运行在其他系统（如 Linux，Unix，Mac OS等）就选`posix`  
   更多信息请参考：[mingw-w64-threads-posix-vs-win32](https://stackoverflow.com/questions/17242516/mingw-w64-threads-posix-vs-win32)  
   ![选择线程模型](https://img-blog.csdnimg.cn/9c2747a530e74d28bb94a54135f8afc0.png)  
6. 选择构建版本  
   选择构建版本，这里好像只有一个`rev1`，一般保持默认即可  
   ![选择构建版本](https://img-blog.csdnimg.cn/52b2a702196544df9232546fd8ced0d5.png)  
7. 选择运行时库类型  
   选择运行时库类型，前面简介里有介绍  
   ![选择运行时类型](https://img-blog.csdnimg.cn/1c55dc48a50c4c02b9fb4bbbb8caf1f2.png)  
8. 选择安装位置  
   可以勾选上`Create shortcut on Desktop`，使用会方便些  
   ![选择安装位置](https://img-blog.csdnimg.cn/d79bde5708d947e696688d1828bc33f0.png)  
9. 安装过程（自动下载、解压、安装配置）  
   ![下载解压过程](https://img-blog.csdnimg.cn/76b63142bb014007bb0a9a6ebaa9d929.png)  
   ![安装完成](https://img-blog.csdnimg.cn/c1978c34ba9d43c892758897c2966127.png)

### 2. 离线安装
从 GitHub或镜像站点下载编译好的安装程序包（【二、下载】中提供的有地址）

以 [niXman/mingw-builds-binaries/releases](https://github.com/niXman/mingw-builds-binaries/releases) 为例，离线安装比较简单，只需下载解压即可

1. 下载`MinGW-w64`的安装包  
   根据你自己的需要选择适合的安装包
   - 32位的操作系统，选择`i686`，64位的操作系统，选择`x86_64`；
   - `13.1.0` 是GCC的版本号，其他版本的你需要往下找；
   - `win32`是开发windows系统程序的协议，`posix`是其他系统的协议（例如Linux、Unix、Mac OS），更多信息参考：[mingw-w64-threads-posix-vs-win32](https://stackoverflow.com/questions/17242516/mingw-w64-threads-posix-vs-win32)；
   - 异常处理模型`seh`（新的，仅支持64位系统），`sjlj`（稳定的，64位和32位都支持）， `dwarf`（优于sjlj的，仅支持32位系统），更多信息参考：[what-is-difference-between-sjlj-vs-dwarf-vs-seh/15685229](https://stackoverflow.com/questions/15670169/what-is-difference-between-sjlj-vs-dwarf-vs-seh/15685229)；
   - `msvcrt`、`ucrt` 运行时库类型，有关介绍请参考文章简介部分；
   - `rt_v11` 运行时库版本；
   - `rev1` 构建版本；

   ![下载MinGW-w64离线安装包](https://img-blog.csdnimg.cn/e5654723da414e6ba5055cd7a28988ef.png)

2. 找一个地方解压（记住这个路径，后面配置环境变量用）

### 3. 环境配置
1. 如果你是按照【1.在线安装】的，可以不用配置环境变量，直接打开`MinGW-W64-64bit`快捷方式（桌面或开始菜单），然后在打开的命令行窗口中直接就可以使用`gcc`等命令  
   ![验证MinGW-w64安装是否成功](https://img-blog.csdnimg.cn/0e8f52dd0e90464c9c2ddc1da5b11d64.png)

2. 如果你是按照【2.离线安装】的，将解压后的目录下的bin路径，手动添加到系统的`PATH`环境变量，怎么配置不用我就不演示了（实在是小白的话，自行百度吧），配置完后就可以在工作目录下使用`gcc`等命令了  
   （我这里的解压路径为：`D:\Chen\MySoft\mingw64`，配置的环境变量是这个路径下的`bin`目录路径）  
   ![配置环境变量](https://img-blog.csdnimg.cn/12bcf4453dd645d0822857bbd748b9f8.png)  
   ![验证MinGW-w64是否安装成功](https://img-blog.csdnimg.cn/4309b38a3e96424a913f6dd991b78fc0.png)


## 四、总结
1. 【[从sourceforge.net下载](https://blog.csdn.net/B11050729/article/details/132176767#sfnet)】中提供的安装程序，支持的GCC 8.1.0，版本太老了，不推荐你从这里下载安装；
2. 【[2.从github下载](https://blog.csdn.net/B11050729/article/details/132176767#github)】、【[3.从镜像网站下载](https://blog.csdn.net/B11050729/article/details/132176767#mirror)】中提供的安装程序，支持的GCC版本都比较新，推荐从这里下载安装；
3. 如果想要自己编译安装程序，你可以从【[4.自己编译](https://blog.csdn.net/B11050729/article/details/132176767#selfbuild)】中推荐的工具进行编译安装你需要的MinGW-w64程序。




---
版权声明：本文为CSDN博主「小青龍」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/B11050729/article/details/132176767
