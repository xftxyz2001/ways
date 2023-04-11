想法：在拦截器中使用@Autowired等Spring注解，但是由于拦截器不是Spring管理的Bean，所以无法使用@Autowired等注解。

```java
@Bean
public SecurityInterceptor securityInterceptor() {
    return new SecurityInterceptor();
}

@Override
public void addInterceptors(InterceptorRegistry registry) {
    registry.addInterceptor(securityInterceptor()).addPathPatterns("/**");
}
```

- [SpringBoot系列之拦截器注入Bean的几种姿势](https://juejin.cn/post/7030752047859236877)
