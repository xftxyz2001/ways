## 问题
如题，表中的字段是（bigint）类型，实体类中对应的是Long类型，当序列化传给前端后导致精度丢失。


## 解决方案
使用Jackson进行JSON序列化的时候将Long类型Id转成String响应给前端。
```java
@Configuration
public class JacksonConfig {
    @Bean
    @Primary
    @ConditionalOnMissingBean(ObjectMapper.class)
    public ObjectMapper jacksonObjectMapper(Jackson2ObjectMapperBuilder builder) {
        ObjectMapper objectMapper = builder.createXmlMapper(false).build();

        // 全局配置序列化返回 JSON 处理
        SimpleModule simpleModule = new SimpleModule();
        //JSON Long ==> String
        simpleModule.addSerializer(Long.class, ToStringSerializer.instance);
        objectMapper.registerModule(simpleModule);
        return objectMapper;
    }
}
```

---
- [JS 的整型及最大安全整数 - 简书](https://www.jianshu.com/p/05395ded2569)
- [完美解决方案-雪花算法ID到前端之后精度丢失问题-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1703457)

