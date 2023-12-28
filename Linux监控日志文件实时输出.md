## Linux中使用 tail 命令实时监控日志文件

### 一、tail 命令简介
`tail` 命令是Linux系统中常用的一个命令，主要用于输出文件末尾的内容。
默认情况下， `tail` 命令会输出文件的最后10行。
然而，我们可以通过参数 `-n` 指定行数参数来改变这个默认行为。

```bash
tail -n 20 /var/log/syslog
```

在上面的例子中， `tail` 命令会输出 `/var/log/syslog` 文件的最后20行。

### 二、实时监控日志文件
使用`tail`命令实时监控日志文件非常简单。我们只需要添加`-f`选项即可。
这个选项会让`tail`命令保持打开状态，并在文件增长时输出新添加的行。

```bash
tail -f /var/log/syslog
```

这个命令将会持续打印出 `/var/log/syslog` 文件的新内容，直到你停止它。

### 三、多文件同时监控
如果你想要同时监控多个日志文件，你可以在 `tail` 命令后添加多个文件路径。
`tail` 命令将会对所有指定的文件进行跟踪，并在有新内容时显示出来。

```bash
tail -f /var/log/syslog /var/log/auth.log
```

在上述示例中，`tail`命令会同时监控`/var/log/syslog`和`/var/log/auth.log`两个文件，实时打印出新的日志信息。

### 四、配合grep使用
我们还可以将 `tail` 命令与 `grep` 命令结合使用，以便在大量日志中筛选出我们关心的部分。

例如，我们可能只关心错误消息：
```bash
tail -f /var/log/syslog | grep ERROR
```

这个命令将会过滤出包含 "ERROR" 字符串的日志条目，并实时显示它们。

### 五、退出
要退出 `tail` 命令，只需要按下 `Ctrl+C` 或者 `Ctrl+Z` 即可。

---
- [linux 监控日志文件实时输出的方法（tail命令）](https://blog.csdn.net/Dontla/article/details/124143910)
- [如何退出tail -f 命令](https://blog.csdn.net/weixin_50599271/article/details/115385422)
