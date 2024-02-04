# WinGet 源使用帮助

## 地址

[https://mirrors.ustc.edu.cn/winget-source](https://mirrors.ustc.edu.cn/winget-source)

## 说明

Windows Package Manager (aka. WinGet) 默认软件源

## 使用说明

备注

> 修改 WinGet 软件源需要管理员权限，请以管理员身份运行终端。

替换 USTC 镜像：
```shell
winget source remove winget
winget source add winget https://mirrors.ustc.edu.cn/winget\-source
```

备注

> 若出现 0x80073d1b : smartscreen reputation check failed. 错误，请检查网络连接或暂时关闭 SmartScreen。

重置为官方地址：
```shell
winget source reset winget
```
