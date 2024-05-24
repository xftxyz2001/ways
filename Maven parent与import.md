### parent
在 `maven` 配置文件 `pom.xml` 中可以 引入 `parent`，方式如下：

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>x.y.z</version>
    <relativePath/> <!-- lookup parent from repository -->
</parent>
```

这是 `maven` 中的继承关系，表示该 `maven` 项目将会继承目标项目（`org.springframework.boot:spring-boot-starter-parent:x.y.z`）中的依赖，通过这种方式可以实现复用父类中的依赖。

> 这种复用可以针对两种依赖，一种是定义在 `<dependencies>` 中的 `<dependency>`，这种是无条件继承的；还有一种是定义在 `<dependencyManagement>` 中的 `<dependencies>`，这种的如果要在子类中使用，需要手动声明，只需要声明 `groupId` 和 `artifactId` 就行，版本则不必声明。

使用 `parent` 不仅可以实现复用，还可以统一管理依赖的版本。

### import
> `import` 能实现类似的功能，它能够解决 `parent` 不能实现的部分问题，比如**多继承**。但是相比 `parent`，它只能作用于 `<dependencyMannagement>` 元素，它所实现的就是能将目标中的配置导入当前 `pom` 中，但是不包括插件管理 `<pluginManagement>`。

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>${cloud.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-alibaba-dependencies</artifactId>
            <version>${alibaba.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

---
- [maven parent 与 import 的区别](https://www.cnblogs.com/bityinjd/p/9046061.html)
