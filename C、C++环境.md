# 小熊猫C++
~~什么年代了，vc++6.0和Dev-C++就免了吧~~

## 下载
- [royqh1979-小熊猫C++](https://royqh.net/redpandacpp/)
  - [下载页（含下载说明）](https://royqh.net/redpandacpp/download/)
- [gitee](https://gitee.com/royqh1979/RedPanda-CPP)
  - [gitee.io-小熊猫C++](https://royqh1979.gitee.io/redpandacpp/)
    - [下载页（含下载说明）](https://royqh1979.gitee.io/redpandacpp/download/)
- [github](https://github.com/royqh1979/RedPanda-CPP)


## 安装
对于绿色版，直接解压即可，运行 `RedPandaIDE.exe` 即可。

对于安装版，运行安装程序，一路下一步即可。（默认安装至 `C:\Program Files\RedPanda-Cpp\` 目录下，会自动创建快捷方式）



---
# VSCode + MinGW-W64
[MinGW-W64 下载、安装与配置](./MinGW-W64%20下载、安装与配置.md)

## VSCode

### 下载
- [Visual Studio Code](https://code.visualstudio.com/)
  - 网站会自动识别你的操作系统环境，直接点击下载即可。

### 安装
运行安装程序，一路下一步即可。（能勾的尽量勾上，后面用起来方便）
- `选择附加任务/添加到PATH(重启后生效)` 一定要勾选，很重要。

### 安装扩展
- 简体中文：`ms-ceintl.vscode-language-pack-zh-hans`
- C/C++：`ms-vscode.cpptools`

### 运行
在编写好的代码文件中，按 `Ctrl + F5` 运行， `F5` 调试。（选择C++(GDB/LLDB)）



#### ~~+ VS~~
如果你安装过 `Visual Studio` ，且安装了 `使用C++的桌面开发` 组件。
启动 `Developer Command Prompt for VS` 或 `Developer PowerShell for VS` ，键入 `code` ，打开VSCode。
在编写好的代码文件中，按 `Ctrl + F5` 运行， `F5` 调试。（选择C++(Windows)）
