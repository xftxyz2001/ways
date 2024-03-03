### 报错信息
XML Parser Error on line 1: 文档根元素 "generatorConfiguration" 必须匹配 DOCTYPE 根 "null"。


### 错误原因
于在配置文件mybatis-generator-config.xml中，文档根元素"generatorConfiguration"与DOCTYPE根"null"不匹配导致。


### 解决方法
在 `<configuration>` 标签前面添加以下内容: 
```xml
<?xml version="1.0" encoding="UTF-8"?> 
<!DOCTYPE generatorConfiguration PUBLIC "-//mybatis.org//DTD mybatis Generator Configuration 1.0//EN" "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd">
```


### 参考链接
- [Mybatis代码生成器Mybatis-Generator使用详解 - 知乎](https://zhuanlan.zhihu.com/p/522648349)
- [XML Parser Error on line 1: 文档根元素 "generatorConfiguration" 必须匹配 DOCTYPE 根 "null"。 - CSDN文库](https://wenku.csdn.net/answer/7bj5wna7b5)

