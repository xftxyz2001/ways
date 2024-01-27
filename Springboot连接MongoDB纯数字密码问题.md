## 报错
```
java.lang.IllegalArgumentException: Prohibited character at position 0
```

## 原因
`password` 是纯数字，在 `org.springframework.boot.autoconfigure.mongo.MongoProperties` 中的 `password` 字段是 `char[]` 类型，在遇到纯数字的时候会将其转换为该数字（字符编码）对应的字符。


## 修改
将 `password` 用引号包裹起来即可
```yml
spring:
  mongodb:
    host: mongodb
    database: xxx
    username: admin
    password: "123456"
    authentication-database: admin
```

---
- [记用MongoDB时遇到的一个小问题](https://blog.csdn.net/qq_45781295/article/details/120936287)
