## 报错信息
```
Could not extract response: no suitable HttpMessageConverter found for response type.... content type [text/html;charset=UTF-8]
```

```
Could not extract response: no suitable HttpMessageConverter found for response type.... content type [text/plain;charset=UTF-8]
```

## 报错原因
RestTemplate默认使用的是MappingJackson2HttpMessageConverter，其只支持 `application/*+json` 的 `Content-Type` 。

## 解决方案
在实例化RestTemplate时，手动添加 `text/plan` 、 `text/html` 格式

```java
@Configuration
public class RestTemplateConfig {

    @Bean
    public RestTemplate restTemplate() {
        RestTemplate restTemplate = new RestTemplate();
        MappingJackson2HttpMessageConverter mappingJackson2HttpMessageConverter = new MappingJackson2HttpMessageConverter();
        mappingJackson2HttpMessageConverter.setSupportedMediaTypes(Arrays.asList(
                MediaType.TEXT_HTML,
                MediaType.TEXT_PLAIN));
        restTemplate.getMessageConverters().add(mappingJackson2HttpMessageConverter);

        return restTemplate;
    }
}
```

---
- [RestTemplate请求：Could not extract response: no suitable HttpMessageConverter found for response type-CSDN博客](https://blog.csdn.net/weixin_43901865/article/details/120430681)
