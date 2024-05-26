## 一、背景
基于 `SpringBoot` 构建了一个 `http` 文件下载服务，检查 `tomcat access` 发现偶尔出现 500 状态码的请求，检查抛出的异常堆栈

```log
2019-03-20 10:03:14,273 ERROR [http-bio-8080-exec-3] o.s.b.w.s.s.ErrorPageFilter - Forwarding to error page from request [/demo.xls] due to exception [org.springframewo
rk.web.util.NestedServletException: Request processing failed; nested exception is java.lang.IllegalStateException: InputStream has already been read - do not use InputStreamResource if a stream needs to be
read multiple times]
javax.servlet.ServletException: org.springframework.web.util.NestedServletException: Request processing failed; nested exception is java.lang.IllegalStateException: InputStream has already been read - do not
 use InputStreamResource if a stream needs to be read multiple times
        at com.vdian.vtrace.VtraceFilter.doFilter(VtraceFilter.java:65)
        at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:241)
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:208)
        at org.springframework.web.filter.RequestContextFilter.doFilterInternal(RequestContextFilter.java:99)
        at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
        at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:241)
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:208)
        at org.springframework.web.filter.HttpPutFormContentFilter.doFilterInternal(HttpPutFormContentFilter.java:109)
        at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
        at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:241)
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:208)
        at org.springframework.web.filter.HiddenHttpMethodFilter.doFilterInternal(HiddenHttpMethodFilter.java:81)
        at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
        at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:241)
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:208)
        at org.springframework.boot.web.servlet.support.ErrorPageFilter.doFilter(ErrorPageFilter.java:115)
        at org.springframework.boot.web.servlet.support.ErrorPageFilter.access$000(ErrorPageFilter.java:59)
        at org.springframework.boot.web.servlet.support.ErrorPageFilter$1.doFilterInternal(ErrorPageFilter.java:90)
        at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
        at org.springframework.boot.web.servlet.support.ErrorPageFilter.doFilter(ErrorPageFilter.java:108)
        at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:241)
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:208)
        at org.springframework.web.filter.CharacterEncodingFilter.doFilterInternal(CharacterEncodingFilter.java:200)
        at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
        at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:241)
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:208)
        at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:220)
        at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:122)
        at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:505)
        at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:169)
        at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:103)
        at org.apache.catalina.valves.AccessLogValve.invoke(AccessLogValve.java:956)
        at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:116)
        at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:436)
        at org.apache.coyote.http11.AbstractHttp11Processor.process(AbstractHttp11Processor.java:1078)
        at org.apache.coyote.AbstractProtocol$AbstractConnectionHandler.process(AbstractProtocol.java:625)
        at org.apache.tomcat.util.net.JIoEndpoint$SocketProcessor.run(JIoEndpoint.java:316)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
        at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
        at java.lang.Thread.run(Thread.java:745)
Caused by: org.springframework.web.util.NestedServletException: Request processing failed; nested exception is java.lang.IllegalStateException: InputStream has already been read - do not use InputStreamResource if a stream needs to be read multiple times
        at org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:986)
        at org.springframework.web.servlet.FrameworkServlet.doGet(FrameworkServlet.java:870)
        at javax.servlet.http.HttpServlet.service(HttpServlet.java:624)
        at org.springframework.web.servlet.FrameworkServlet.service(FrameworkServlet.java:855)
        at javax.servlet.http.HttpServlet.service(HttpServlet.java:731)
        at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:303)
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:208)
        at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:52)
        at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:241)
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:208)
        at com.vdian.vtrace.VtraceFilter.doFilter(VtraceFilter.java:50)
        ... 40 common frames omitted
Caused by: java.lang.IllegalStateException: InputStream has already been read - do not use InputStreamResource if a stream needs to be read multiple times
        at org.springframework.core.io.InputStreamResource.getInputStream(InputStreamResource.java:97)
        at org.springframework.http.converter.ResourceHttpMessageConverter.writeContent(ResourceHttpMessageConverter.java:130)
        at org.springframework.http.converter.ResourceHttpMessageConverter.writeInternal(ResourceHttpMessageConverter.java:124)
        at org.springframework.http.converter.ResourceHttpMessageConverter.writeInternal(ResourceHttpMessageConverter.java:45)
        at org.springframework.http.converter.AbstractHttpMessageConverter.write(AbstractHttpMessageConverter.java:230)
        at org.springframework.web.servlet.mvc.method.annotation.AbstractMessageConverterMethodProcessor.writeWithMessageConverters(AbstractMessageConverterMethodProcessor.java:274)
        at org.springframework.web.servlet.mvc.method.annotation.HttpEntityMethodProcessor.handleReturnValue(HttpEntityMethodProcessor.java:218)
        at org.springframework.web.method.support.HandlerMethodReturnValueHandlerComposite.handleReturnValue(HandlerMethodReturnValueHandlerComposite.java:82)
        at org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:119)
        at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:870)
        at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.handleInternal(RequestMappingHandlerAdapter.java:776)
        at org.springframework.web.servlet.mvc.method.AbstractHandlerMethodAdapter.handle(AbstractHandlerMethodAdapter.java:87)
        at org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:991)
        at org.springframework.web.servlet.DispatcherServlet.doService(DispatcherServlet.java:925)
        at org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:978)
        ... 50 common frames omitted
```


## 二、问题解决
从 exception message 看，是
```log
Caused by: java.lang.IllegalStateException: InputStream has already been read - do not use InputStreamResource if a stream needs to be read multiple times
```

**把 Response body 由 InputStreamResource 类型改为 ByteArrayResource 即可。**


## 三、问题探究

### （一）初步尝试
取异常请求的 `URL` ，在 `chrome` 浏览器上重试，并没有复现问题

### （二）抓包查看
![](https://img2018.cnblogs.com/blog/1151813/201903/1151813-20190321114802771-1479390153.png)

发现 500 的请求中有 **Range Header**

### （三）问题复现
```bash
curl -v -o test.amr -H "Range:bytes=0-" "http://aud.idcheihei.com/se1-sellerexpt-31e9000001698f06b9370a216239.amr"
```

使用 `curl` 命令带上 `Range header` 请求后端，请求返回 500，复现问题

### （四）根据堆栈查看代码
`org.springframework.core.io.InputStreamResource#getInputStream`

![](https://img2018.cnblogs.com/blog/1151813/201903/1151813-20190321115931566-2022995046.png)

`InputStream` 只能读取一次内容，所以这里有一个 `read` 成员变量，控制 `resource` 的读取

当 `resource` 被读取一次后，第二次读取就会抛异常

那为什么会读取两次呢？

### （五）本地debug

根据堆栈，打断点，`org.springframework.core.io.InputStreamResource#getInputStream`

逐步调试发现发起第一次 `getInputStream` 调用的地方是：
```java
org.springframework.web.servlet.mvc.method.annotation.AbstractMessageConverterMethodProcessor#writeWithMessageConverters(T, org.springframework.core.MethodParameter, org.springframework.http.server.ServletServerHttpRequest, org.springframework.http.server.ServletServerHttpResponse)
```

![](https://img2018.cnblogs.com/blog/1151813/201903/1151813-20190321141204226-747389141.png)

由 `outputValue = HttpRange.toResourceRegions(httpRanges, resource);` 抛异常，进入 `catch` 逻辑

`org.springframework.http.HttpRange#toResourceRegion` 实现体：
```java
public ResourceRegion toResourceRegion(Resource resource) {
   Assert.isTrue(resource.getClass() != InputStreamResource.class, "Cannot convert an InputStreamResource to a ResourceRegion");
 
    try {
        long contentLength = resource.contentLength();
        Assert.isTrue(contentLength > 0L, "Resource content length should be > 0");
        long start = this.getRangeStart(contentLength);
        long end = this.getRangeEnd(contentLength);
        return new ResourceRegion(resource, start, end - start + 1L);
    } catch (IOException var8) {
        throw new IllegalArgumentException("Failed to convert Resource to ResourceRegion", var8);
    }
}
```

`org.springframework.core.io.AbstractResource#contentLength` 实现体：
```java
public long contentLength() throws IOException {
    InputStream is = this.getInputStream();

    try {
        long size = 0L;

        int read;
        for(byte[] buf = new byte[255]; (read = is.read(buf)) != -1; size += (long)read) {
        }

        long var6 = size;
        return var6;
    } finally {
        try {
            is.close();
        } catch (IOException var14) {
        }
    }
}
```

第二次 getInputStream 调用的地方是输出内容的地方，`/org/springframework/web/servlet/mvc/method/annotation/AbstractMessageConverterMethodProcessor.class:214`

debug 到这里，已定位问题

### （六）结论
1. 文件下载 `http` 请求使用 `Range header` 时，`response` 需要设置一个 `Content-Range header`，设置这个 `header` 需要获取 `response body` 的 `contentlength`，对于 `InputStreamResource` 这种 `resource`，需要读取整个 `InputStream` 的内容后才能得到 `body` 的长度  
2. `resonse` 填充文件内容的时候，由于 `InputStream` 读取完成后不能再次读取，所以抛出了 `InputStream has already been read - do not use InputStreamResource if a stream needs to be read multiple times` 异常

---
本文作者：Blyde  
原文链接：[https://www.cnblogs.com/gliu/p/10570687.html](https://www.cnblogs.com/gliu/p/10570687.html "view: InputStream has already been read - do not use InputStreamResource if a stream needs to be read multiple times")   
版权归作者所有，转载请注明出处
