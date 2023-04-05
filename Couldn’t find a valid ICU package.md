## 报错信息
“Couldn‘t find a valid ICU package installed on the system. Set the configuration flag System.”

## 解决方法
安装相应依赖库：
```bash
yum install libicu
```

一般就可以了。  
如果还不行，再安装：

```bash
yum -y install libicu-devel
yum install libunwind
```
