关闭 ndu 服务，全名是 network data usage monitor driver。
该服务存在内存泄漏问题，即使电脑一直 idle，开了这个服务，内存也会一直增长，禁用该服务不会影响电脑的正常工作。
该服务在 services.msc 中找不到，所以需要使用命令行禁掉。

命令行为:
```
sc config ndu start=disabled
```
