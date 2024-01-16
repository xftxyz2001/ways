解决Vue文件用Prettier格式化后，结束标签 `>` 跑到下一行的问题

在项目目录下的 `.prettierrc` 文件中添加如下配置：

```json
{
  "htmlWhitespaceSensitivity": "ignore"
}
```

---
- [前端 - 解决Vue文件用Prettier格式化后，结束标签>跑到下一行的问题 - 个人文章 - SegmentFault 思否](https://segmentfault.com/a/1190000039991789)
