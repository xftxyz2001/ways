# 一 .vue-cli2

## 方式1. vue-cli2中端口文件存放目录为：`根目录下/config/index.js`

```javascript
// Various Dev Server settings
    host: 'localhost', // can be overwritten by process.env.HOST
    port: 80, // can be overwritten by process.env.PORT, if port is in use, a free one will be determined
    autoOpenBrowser: false, // 运行后自动打开浏览器
    errorOverlay: true, // 在浏览器是否展示错误蒙层
    notifyOnErrors: true, // 是否展示错误的通知
```

> host:：改为电脑IP，同局域网内其余电脑可访问你的项目 例：**19.168.43.20:80**



# 二.vue-cli3/vue-cli4

## 方式1. 端口文件存放目录为：`node_modules/@vue/cli-service/lib/commands/serve.js`
```javascript
const defaults = {
  host: '0.0.0.0',
  port: 80,
  https: false
}
```

## 方式2. 在 package.json 文件中修改 scripts
```javascript
"scripts": {
	"serve": "vue-cli-service serve --port 80",
	"build": "vue-cli-service build",
},
```

## 方式3 在运行项目的时候追加端口号
```javascript
npm run serve -- --port 80
```

## 方式4 在根目录新建【`vue.config.js`】，并配置如下，将覆盖默认的配置（更多配置详情参见[vue官网](https://cli.vuejs.org/zh/config/#vue-config-js)
```javascript
module.exports = {
  publicPath: "/", //根路径  Vue CLI 3.3 前使用 baseUrl
  outputDir: "dist1", //构建输出目录
  assetsDir: "assets", //静态资源目录
  lintOnSave: false, //是否开启eslint保存检测
  runtimeCompiler: true,
  publicPath: "/", // 设置打包文件相对路径
  devServer: {
    open: true, //配置自动启动浏览器
    host: "localhost",
    https: false,
    hotOnly: false, //热更新
    port: 80,
    // 配置跨域-请求后端的接口
    proxy: { 
     // "/api": {
     //   target: "http://172.20.10.3:80", //对应自己的接口
     //   changeOrigin: true,
     //   ws: true,
     //   pathRewrite: {
     //     "^/api": ""
     //   }
     // }
    }
  }
}

```

**注意：** 改端口后，项目需要重新运行


原文链接：https://blog.csdn.net/qq_45594237/article/details/115302876
