## 报错信息
Linux上运行一些程序时，报错：  
```bash
Couldn’t find a valid ICU package installed on the system.
```


## 解决方法
安装相应依赖库即可：
```bash
yum install libicu
```

如果执行上面的命令仍未解决，再：
```bash
yum -y install libicu-devel
yum install libunwind
```


## 参考
- [CSDN-解决报错：“Couldn‘t find a valid ICU package installed on the system. Set the configuration flag System.”](https://blog.csdn.net/weixin_42744102/article/details/107193189)
