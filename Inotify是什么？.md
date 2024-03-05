`inotify` 是 `Linux` 内核 2.6.13 (June 18, 2005) 版本新增的一个子系统（API），它提供了一种监控文件系统（基于 `inode` 的）事件的机制，可以监控文件系统的变化如文件修改、新增、删除等，并可以将相应的事件通知给应用程序。几乎所有的主流 `Linux` 发行版都支持 `Inotify` 机制。如何知道你的 `Linux` 内核是否支持 `Inotify` 机制呢？很简单，执行下面这条命令：

```bash
grep INOTIFY_USER /boot/config-$(uname -r)
CONFIG_INOTIFY_USER=y 
```

如果输出 `CONFIG_INOTIFY_USER=y`，代表当前系统支持 `Inotify` 机制。

---
查看 Inotify 在内核中的默认配置。

```bash
sysctl fs.inotify
```

输出如下：
```bash
fs.inotify.max_queued_events = 16384 # inotify 管理的队列的最大长度
fs.inotify.max_user_instances = 128 # 每个用户所能创建的 Inotify 实例的上限
fs.inotify.max_user_watches = 65536 # 每个 Inotify 实例最多能关联几个监控 (watch)
```

或者
```bash
cat /proc/sys/fs/inotify/max_queued_events
16384
cat /proc/sys/fs/inotify/max_user_instances
128
cat /proc/sys/fs/inotify/max_user_watches
65536
```
