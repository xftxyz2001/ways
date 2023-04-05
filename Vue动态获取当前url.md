# Vue 配置 axios 的 baseURL

## 关于 window.location 的详解

window.location 对象不仅可以获得当前页面的地址 (URL)，还能够将浏览器重定向到新的页面。

下面，以`http://www.myurl.com:8866/test?id=123&username=xxx`为例来进行解释：

1. **window.location.href** 【当前 url】-> `http://www.myurl.com:8866/test?id=123&username=xxx`
2. **window.location.protocol** 【协议】-> `http:`
3. **window.location.host** 【域名 + 端口】-> `www.myurl.com:8866`
4. **window.location.hostname** 【域名】-> `www.myurl.com`
5. **window.location.port** 【端口】-> `8866`
6. **window.location.pathname** 【路径】-> `/test`
7. **window.location.search** 【请求的参数】-> `?id=123&username=xxx`
8. **window.location.origin** 【路径前面的 url】-> ` http://www.myurl.com:8866`

`main.js` 中：

```js
...
import axios from 'axios';

let path =  '/contentPath'
let url = window.location.origin + path; //path为上下文路径，如果后端有配置就添加
axios.defaults.baseURL = url;
```

参考

- [https://www.jianshu.com/p/c9324d237a8e](https://www.jianshu.com/p/c9324d237a8e)
- [vue——动态获取当前 url，配置 axios 的 baseURL](https://www.cnblogs.com/linjiangxian/p/13097863.html)
