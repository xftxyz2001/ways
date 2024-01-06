抑制VSCode Spring Boot警告：Newer xxx version of Spring Boot available

将 `spring-boot.ls.problem.version-validation.` 下的对应项设置为 `ignore` 即可。

如：
```json
{
    "spring-boot.ls.problem.version-validation.SUPPORTED_COMMERCIAL_VERSION": "IGNORE",
    "spring-boot.ls.problem.version-validation.SUPPORTED_OSS_VERSION": "IGNORE",
    "spring-boot.ls.problem.version-validation.UNSUPPORTED_COMMERCIAL_VERSION": "IGNORE",
    "spring-boot.ls.problem.version-validation.UNSUPPORTED_OSS_VERSION": "IGNORE",
    "spring-boot.ls.problem.version-validation.UPDATE_LATEST_MAJOR_VERSION": "IGNORE",
    "spring-boot.ls.problem.version-validation.UPDATE_LATEST_MINOR_VERSION": "IGNORE",
    "spring-boot.ls.problem.version-validation.UPDATE_LATEST_PATCH_VERSION": "IGNORE",
}
```
