### 1. 修改 index.html
- 把 `public/index.html` 移动到项目 **根目录**
- 把文件中的`<%= xxx %>` 去掉(是webpack内置的全局环境变量，vite无法使用，vite的环境变量属性存放在`import.meta.env`中)
- 在 `index.html` 文件中引入`mian.js`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <link rel="icon" href="/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vite App</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
```

### 2. 修改 package.json
1. 删除不需要的依赖，如 `eslint`, `babel`, `webpack`,各种 `loader`, `plugin` 和 `@vue/cli-xx` 等
2. 修改 `scripts`, 和`devDependencies`

```json
{
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^5.0.4",
    "vite": "^5.2.8"
  }
}
```

### 3. 重新安装依赖
1. 删除 `node_modules` 文件夹
2. 删除 `package-lock.json` 或 `yarn.lock` 等锁文件
3. 删除 `config` , `scripts` 文件夹， 这些文件夹，包含了一些 webpack 的配置和启动脚本（如果项目没有，可以忽略这一步）
4. 并重新安装依赖（`npm install` 或 `yarn install`）

### 4. 创建 `vite.config.js`
删除 `vue.config.js` ，新建 `vite.config.js` 配置文件。

初始配置：
```js
import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
```

### 5. 修改require导入
- `require` 是 `webpack` 的导入方式，`vite` 须用`import` 导入
- 找到你项目中全部的 `require` 函数进行替换

手动封装一个 `vite` 版的 `require` 导入参考如下：
```js
// 封装一个 vite 版的 require 导入
export const require = (url) => {
  // 将图片导为模块
  const picModules = import.meta.globEager("../assets/images/**");
  const _url = url.replace("@", "");
  // 获取图片模块
  // 获取指定的图片
  const path = `..${_url}`;
  return picModules[path].default;
};
```

使用：
```html
<template>
  <el-image :src="require('@/assets/images/login-bg.jpg')" />
</template>

<script setup>
import { require } from '@/utils' // 引入自定义的 require
</script>
```

### 6. 修改环境变量判断
如项目中使用了[环境变量](https://cn.vitejs.dev/guide/env-and-mode.html)判断，需要修改为`import.meta.env`，如：
```js
// axios.defaults.baseURL = process.env.VUE_APP_BASEURL
axios.defaults.baseURL = import.meta.env.VITE_BASEURL
```

- `.env.development`：
    ```js
    VITE_BASEURL = 'https://dev.xxx.com/api/'
    ```
- `.env.production`：
    ```js
    VITE_BASEURL = 'https://pro.xxx.com/api/'
    ```
- `.env.test`：
    ```js
    VITE_BASEURL = 'https://test.xxx.com/api/'
    ```

最后 `npm run dev` 即可 （使用 `--mode` 指定环境）

---
- [手把手教你从webpack迁移到vite，仅6步~！](https://blog.csdn.net/x550392236/article/details/133752932)
