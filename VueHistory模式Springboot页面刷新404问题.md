## 问题描述
Vue项目中路由使用history模式，打包后部署到Springboot中，刷新页面导致404


## 解决方案
Springboot中添加配置类，将404错误重定向到index.html
```java
@Configuration
public class ErrorPageConfig implements ErrorPageRegistrar {

    @Override
    public void registerErrorPages(ErrorPageRegistry registry) {
        registry.addErrorPages(new ErrorPage(HttpStatus.NOT_FOUND, "/index.html"));
    }
}
```

---
- [Vue + Spring Boot History模式 打包后 刷新404问题](https://blog.csdn.net/bestone_1987/article/details/105507041)
