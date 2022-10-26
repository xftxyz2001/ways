## 问题描述
The method xxx of type must override a superclass method.


## 问题原因
java1.5中继承接口是不需要@Override的，而在1.6中是需要添加@Override注解的。
如果项目编译环境是1.5版本的就可能报以上错误。


## 解决方法
```xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
</properties>
```
