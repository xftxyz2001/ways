问题：插件Pylance v2023.10.50不能正常工作

输出-Python语言服务器 打印如下日志：
```
TypeError: _0x2f33cc[(_0x1efd68(...) + _0x1efd68(...))] is not a function
```

stackoverflow给出的临时解决方案：
使用Pylance v2023.10.50时也出现了同样的错误，并降级到v2023.10.40，问题就解决了。

- [参考链接](https://stackoverflow.com/questions/77371542/i-have-a-problem-with-python-in-vscode-typeerror-is-not-a-function)
