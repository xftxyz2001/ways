## 如题
在nuxt项目中运行nuxt相关命令时，会出现：
```
Are you interested in participation ?
```

## 解决方法
在 `nuxt.config.js` 中添加如下配置：
```js
// ...
telemetry: false,
// ...
```

--- 
- [解决app项目出现Are you interested in participation的问题](https://blog.csdn.net/qq_45863690/article/details/124376844)
