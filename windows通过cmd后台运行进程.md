Linux后台运行进程时，通常使用如下方法：

```bash
nohup "运行的内容" &
```

windows相应功能的命令行如下(此方法进程有页面，可能会在桌面展示，关闭窗口后进程消失。)

```shell
call start /min "n" "运行的内容"
```

cmd下难以实现`nohup`能力，但使用`powershell`可以。  
以下powershell方法，可实现后台运行，退出powershell后依然运行。

```powershell
Start-Process -WindowStyle hidden -FilePath "运行的内容"
```
