> [ERROR] Failed to execute goal org.apache.maven.plugins:maven-war-plugin:2.2:war (default-war) on project web-demo: Execution default-war of goal org.apache.maven.plugins:maven-war-plugin:2.2:war failed: Unable to load the mojo 'war' in the plugin 'org.apache.maven.plugins:maven-war-plugin:2.2' due to an API incompatibility:org.codehaus.plexus.component.repository.exception.ComponentLookupException: Cannot access defaults field of Properties 


> 翻译：
> 
> 在项目web-demo上执行目标org.apache.maven.plugins:maven-war:2.2:war失败:无法加载插件org.apache.maven.plugins:maven-war:2.2中的mojo 'war'，因为API不兼容:org.codehaus.plexus.component.repository. exception.com componentlookupexception:无法访问属性的默认字段

从错误提示我们可以知道，这是因为插件版本与API不兼容导致的错误。

解决方法：
在pom.xml文件的 `<project> </project>` 中添加如下插件：

```xml
<build>
    <!-- To define the plugin version in your parent POM -->
    <pluginManagement>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.1</version>
            </plugin>
        </plugins>
    </pluginManagement>
    <!-- To use the plugin goals in your POM or parent POM -->
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-war-plugin</artifactId>
            <version>3.3.1</version>
        </plugin>
    </plugins>
</build>
```
