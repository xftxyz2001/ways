## 报错信息
```bash
java.lang.IllegalArgumentException: Invalid value type for attribute 'factoryBeanObjectType': java.lang.String
```


## 报错原因
```xml
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.5.4.1</version>
</dependency>
```
MybatisPlus版本中依赖的mybatis-spring版本过低，不兼容spring-boot3.2


## 解决方案

### 方案一、使用高版本的mybatis-spring替换mybatis-plus-boot-starter中的mybatis-spring
```xml
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.5.4.1</version>
    <exclusions>
        <exclusion>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis-spring</artifactId>
        </exclusion>
    </exclusions>
</dependency>

<!-- 解决Invalid value type for attribute 'factoryBeanObjectType': java.lang.String -->
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-spring</artifactId>
    <version>3.0.3</version>
</dependency>
```

### 方案二、使用spring-boot3.1.6
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.1.6</version>
    <relativePath/> <!-- lookup parent from repository -->
</parent>
```
