## 报错信息
```
错误: 缺少 JavaFX 运行时组件，需要使用该组件来运行此应用程序
```


## 错误原因
在 Java 8 之后，JavaFX 从 JDK 中分离出来，然后在 Java 9 时，Java 引入了 Java 模块系统。
从那之后，JavaFX 要求使用 Java 模块系统来运行 JavaFX。因此，Java 8 的时候，是没有 Java 模块系统的，而且此时 JavaFX 尚未从 JDK 中分离出来（没有分离出来意味着运行 JavaFX 项目不需要添加 JavaFX 依赖），所以很多老的 JavaFX 项目使用的是 Java 8。
因此，当直接使用 Java 8 以上的环境运行没有使用 Java 模块 JavaFX 老项目时就会出现如上报错。


## 解决方案

### 方法1：使用 Java 8
直接使用 Java 8 运行 JavaFX 项目，而且这样做了之后还无需添加 JavaFX 依赖。
个人是很不建议使用这种方法的，但是很多遇到此问题的读者只是一个刚使用 JavaFX 的新人，他们拿着从网上免费下载的代码却不知道如何运行，他们只是想先试着看看运行效果，而且他们还不清楚如何引入 JavaFX 依赖，更不擅长使用 Maven 或 Gradle。那么，可以使用这种方法。从短期来看，可以省一些事情。

### 方法2：使用 Java 模块系统
使用 Java 模块系统，建议使用这种方法。这里不详细介绍什么 Java 模块系统以及它的语法，因为这不是本文的重点。
构建 Java 模块系统只需要在顶级目录中添加一个模块声明文件 module-info.java。
如果读者不知道应该在模块声明文件中编写什么，可以使用 IntelliJ IDEA 来新建一个 JavaFX 项目，然后生成的示例项目中就会有一个简单的 module-info.java 示例。
```java
module com.example.demo {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demo to javafx.fxml;
    exports com.example.demo;
}
```

### 方法3：使用引导类
使用一种引导类来代理启动 JavaFX 应用。举个例子，现在笔者将 方法 2 中使用 IntelliJ IDEA 新建的 JavaFX 示例项目中的 module-info.java 删除。此时运行此项目应该会报前述的错误。现在，只需要编写一个引导类调用 JavaFX 入口 main 方法即可消除这个错误。
```java
package com.example.demo;

public class JavaFXBootstrap {
    // 方法3-1
    public static void main(String[] args) {
        HelloApplication.main(args);
    }

    // 方法3-2
    public static void main(String[] args) {
        Application.launch(HelloApplication.class, args);
    }
}
```
