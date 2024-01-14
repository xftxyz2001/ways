## 需求
同时使用Spring Data的MongoRepository和MongoTemplate
1. 使用MongoRepository派生机制或手动定义的简单查询接口
2. 对于更复杂的查询，向Reposity添加手动实现的方法，通过使用MongoTemplate实现


## 实现

### 1. 自定义复杂查询接口或更新接口
```java
public interface CustomizedXxxRepository {

    // 自定义复杂查询接口
    yyy customizedMethod();
}
```

### 2. 实现自定义接口
```java
public class CustomizedXxxRepositoryImpl implements CustomizedXxxRepository {

    @Autowired
    private MongoTemplate mongoTemplate;

    @Override
    public yyy customizedMethod() {
        // 使用mongoTemplate实现
    }
}
```

### 3. 为自定义接口添加代理
```java
public interface XxxRepository extends MongoRepository<Xxx, String>, CustomizedXxxRepository {
    // 照常使用MongoRepository派生机制或手动定义的简单查询接口
}
```

### 4. 使用自定义接口
```java
@Autowired
private XxxRepository xxxRepository;

// 通过 xxxRepository 既可以调用MongoRepository的方法，也可以调用自定义接口的方法
```

---
- [同时使用Spring Data的MongoRepository和MongoTemplate - 简书](https://www.jianshu.com/p/8385607822da)
