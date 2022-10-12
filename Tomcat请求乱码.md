## 产生原因
Tomcat接受浏览器请求，在处理数据时产生乱码，原因是：tomcat不知道浏览器发来数据的编码格式，此时tomcat会使用默认的ISO8859-1去解析，导致乱码。


## get请求
对于get请求提交的数据，在不同版本的tomcat中有不同的处理方式，在tomcat8及以上的版本，服务器默认以utf-8的编码方式处理请求参数，这一点可以从tomcat8官方文档中可以看出

> URIEncoding: This specifies the character encoding used to decode the URI bytes, after %xx decoding the URL. If not specified, UTF-8 will be used unless the org.apache.catalina.STRICT_SERVLET_COMPLIANCE system property is set to true in which case ISO-8859-1 will be used.

而对于tomcat8以下的版本，服务器会默认以ISO8859-1的编码方式处理请求参数，在tomcat7官方文档中可以看出

> URIEncoding: This specifies the character encoding used to decode the URI bytes, after %xx decoding the URL. If not specified, ISO-8859-1 will be used.

因此在tomcat8及以上版本的tomcat服务器中，如果浏览器页面是utf-8编码，就不用设置get请求的请求参数编码处理方式，服务器默认就会用utf-8的方式处理请求参数，而在tomcat8以下的tomcat服务器中，需要我们手动编解码处理请求参数，如下所示。
```java
String username = request.getParameter("username");
username = new String(username.getBytes("iso8859-1"),"utf-8");
```

或者在tomcat配置文件（server.xml）加上如下配置
```xml
<Connector connectionTimeout="20000" port="8080" protocol="HTTP/1.1" redirectPort="8443" URIEncoding="UTF-8" useBodyEncodingForURI = "true"/>
```

1. URIEncoding：这个参数用来针对url传参方式，也就是get请求的编码类型的设定
2. useBodyEncodingForURI：一个boolean类型的参数，用来决定url传参方式的编码是否与请求体编码一致，


## post请求
在获取请求参数之前设置
```java
request.setCharacterEncoding("utf-8");
```


## 关于响应编码
ServletResponse有两个方法用于设置响应的编码格式：
```java
setContentType("text/html;charset=UTF-8");
setCharacterEncoding("UTF-8");
```

这两个方法其实有两个作用：
1. 向客户端浏览器回响应时，会添加一个content-type头，并指定编码类型为UTF-8，让浏览器知道字节数据的解码类型并正确显示。
2. 当通过ServletResponse.getWriter()获取Writer，并通过其写入的所有字符串都会默认以UTF-8进行编码为字节输出到浏览器。

当然如果你是通过ServletResponse.getOutputStream()进行直接写入时，tomcat不做任何处理，直接输出到浏览器。
