前端：vue3 + axios
后端：springboot

因为端口不同，会发生跨域问题，所以后端进行相应跨域配置。

在前端用户登录后进行数据请求时报错：已拦截跨源请求：同源策略禁止读取位于 xxx 的远程资源。（原因：CORS 头缺少 ‘Access-Control-Allow-Origin’）。状态码：200。

> 注意：这里是登录后发生，登录时没有问题。

后端controller方法加入注解：`@CrossOrigin` 无效。

~~查询资料：当 `allowCredentials` 为 `true` 时 `allowedOriginPatterns` 不能为 `*` 。~~

因为后端已经添加了 `allowedOriginPatterns("*")` 应该不会有跨域问题，登录、注册功能正常。发现登录拦截器放行了这两个路径。
那应该就是登录拦截器造成的。调试发现拦截了option方法。

因为OPTIONS请求方式不会携带cookie所以无法通过拦截器，相应的跨域配置也就无效了。

解决方案：拦截器放行OPTIONS请求。
```java
if ("OPTIONS".equals(request.getMethod())) {
    return true;
}
```
