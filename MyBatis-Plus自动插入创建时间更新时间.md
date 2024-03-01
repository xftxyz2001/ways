### 1. 数据库表字段
| 字段名      | 字段类型            | 注释     |
| ----------- | ------------------- | -------- |
| create_time | timestamp或datetime | 创建时间 |
| update_time | timestamp或datetime | 更新时间 |


### 2. 实体类注解
```java
/**
 * 创建时间
 */
@TableField(value = "create_time", fill = FieldFill.INSERT) // 插入时自动填充
private Date createTime;

/**
 * 更新时间
 */
@TableField(value = "update_time", fill = FieldFill.INSERT_UPDATE) // 插入和更新时自动填充
private Date updateTime;
```


### 3. 配置类
```java
@Configuration
public class DateConfig implements MetaObjectHandler {

    @Override
    public void insertFill(MetaObject metaObject) {
        this.setFieldValByName("createTime", new Date(), metaObject);
        this.setFieldValByName("updateTime", new Date(), metaObject);
    }

    @Override
    public void updateFill(MetaObject metaObject) {
        this.setFieldValByName("updateTime", new Date(), metaObject);
    }
}
```

---
- [mybatisPlus实现创建时间、更新时间自动添加_在创建时间和更改时间属性加一个什么注解,让他们分别只在增加和修改时间时生效-CSDN博客](https://blog.csdn.net/weixin_44774355/article/details/116302436)
