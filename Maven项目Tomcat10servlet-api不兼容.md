Tomcat10中的javax.servlet-api 改为了 jakarta.servlet-api。
与在pom.xml里面添加的依赖不匹配，会导致服务器无法实例化servlet类

修改依赖
```xml
   <dependency>
      <groupId>jakarta.servlet</groupId>
      <artifactId>jakarta.servlet-api</artifactId>
      <version>5.0.0</version>
      <scope>provided</scope>
    </dependency>
```

可以到https://mvnrepository.com/上面去搜索 jakarta servlet，选择其他版本。
或者不使用Tomcat10，换成Tomcat9或者更早的版本。