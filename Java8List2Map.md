Java8 使用 `stream` 将 `List` 转为 `Map`

### `Collectors.toMap`

```java
public Map<Long, String> getIdNameMap(List<Account> accounts) {
    return accounts.stream().collect(Collectors.toMap(Account::getId, Account::getUsername));
}
```

### 收集对象实体本身

```java
public Map<Long, Account> getIdAccountMap(List<Account> accounts) {
    return accounts.stream().collect(Collectors.toMap(Account::getId, account -> account));
    // or
    return accounts.stream().collect(Collectors.toMap(Account::getId, Function.identity()));
}
```

### 重复 `key` 问题

转换中 `key` 值重复时，流的处理会抛出异常：`Java.lang.IllegalStateException:Duplicate key`

处理方式：（指定 `key` 重复时的处理方式， `toMap` 的第三个参数）

```java
public Map<Long, Account> getIdAccountMap(List<Account> accounts) {
    // 保留旧值
    return accounts.stream().collect(Collectors.toMap(Account::getId, Function.identity(), (k1, k2) -> k1));
    // 使用新值
    return accounts.stream().collect(Collectors.toMap(Account::getId, Function.identity(), (k1, k2) -> k2));
}
```

### 分组

```java
public Map<Integer, List<Person>> getAgePersonMap(List<Person> persons) {
    return persons.stream().collect(Collectors.groupingBy(Person::getAge));
}
```

### 条件分组

```java
public Map<Boolean, List<Person>> getAgePersonMap(List<Person> persons) {
    // 特殊的groupingBy，根据条件分为两组
    return persons.stream().collect(Collectors.partitioningBy(person -> person.getAge() < 18));
}
```

---
- [Java8中list转map方法总结_将list转变为map-CSDN博客](https://blog.csdn.net/zlj1217/article/details/81611834)
