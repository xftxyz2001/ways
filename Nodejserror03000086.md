## 报错信息
```js
opensslErrorStack: [ 'error:03000086:digital envelope routines::initialization error' ],
library: 'digital envelope routines',
reason: 'unsupported',
code: 'ERR_OSSL_EVP_UNSUPPORTED'
```


## 解决方案
在 `vue-cli-service` 前添加环境变量 `NODE_OPTIONS=--openssl-legacy-provider`

```js
"scripts": {
"serve": "set NODE_OPTIONS=--openssl-legacy-provider & vue-cli-service serve",
"build": "set NODE_OPTIONS=--openssl-legacy-provider & vue-cli-service build",
"lint": "vue-cli-service lint"
},
```
