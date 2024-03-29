# Win7、Win10 隐藏任务栏

程序主要功能在快捷键及托盘图标；快捷键为Ctrl + ~(可修改)。

## 更新记录：
(2021.03.18) V0.1.2.1
1.添加开机启动选项，通过创建启动文件夹快捷方式实现，无需管理员权限。
(2021.03.11) V0.1.2.0
1.重构，添加`[启动时隐藏]`、`[双击自动隐藏]`、`[显示任务栏时保持自动隐藏开启]`选项，单实例运行。
2.使用Delphi 10.2编译，含32位及64位，非中文系统，正常显示，无乱码。
3.去除-h参数。
(2021.03.10) V0.1.1.2
1.bug修复；
2.改用Delphi 10.2编译，英文系统不乱码，win10系统支持缩放。
(2021.01.27) V0.1.1.1
1.更换图标。
(2020.12.10) V0.1.1.0
1.添加自定义快捷键入口(右键菜单-关于，点击自定义快捷键开关，输入快捷键，点注册按钮即可)；
2.添加图标双击功能-自动隐藏任务栏；
3.换了个图标，契合Win10风格。
(2012.10.21) V0.0.5
1.@A123: 添加启动参数-h，程序运行后即自动隐藏任务栏，方便随机启动使用。
(2012.08.22) V0.0.4
1.@darkwolf: 在隐藏状态下，定时隐藏维持状态，避免其他程序显示任务栏。
(2012.08.20) V0.0.3
1.添加右键菜单“自动”项，单独开启/关闭`[自动隐藏任务栏]`功能；
2.修复一些疏漏。
(2012.08.19) V0.0.2
1.结合单纯的隐藏任务栏和任务栏自动隐藏，使得任务栏隐藏后，腾出的空间可用；
2.可记忆运行本程序前任务栏自动隐藏状态，并于退出时恢复。


- [参考资料](https://zyhh.me/delphi/taskbarhider.html)
- [下载链接](https://txyz.lanzoue.com/iyarg1cf1ioh)

TaskbarHider.ini
```ini
[OPTION]
HotKey=Shift+Alt+\
AutoStart=1
StartHide=1
DoubleClicktoHide=0
KeepAutoState=0

```