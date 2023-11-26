### 前情提要
[VSCode](https://code.visualstudio.com/)是一款**轻量级**代码编辑器。
但，“轻量级”的VSCode并不轻量。
使用一段就会很快发现，VSCode占用C盘10G+的空间！
于是决定治理一下VSCode，让VSCode变得真正的轻量级。


### VSCode的空间占用分析
VSCode所占用的空间，主要包括四大部分：
1. `程序的安装目录`：大约会占用350M
2. `%USERPROFILE%\.vscode`：可达800M。主要为：各个拓展。VSCode卸载拓展似乎不会删除硬盘上的文件，因此这个里面很大，并且混有很多不用的
3. `%USERPROFILE%\AppData\Local\Microsoft\vscode-cpptools\ipch`：用一段时间能达到4G 与C(++)语言有关，关闭程序后可以直接删。不使用VSCode编辑C/C++的用户可能无此痛苦
4. `%USERPROFILE%\AppData\Roaming\Code`：2G+ 存放用户数据、配置等。 （可以通过启动时添加 `--user-data-dir NewDir` 来使其他目录作为配置）

可以定期删除的地方，有`3. ipch`（可完全删除） 和 `4. Romaing`（不可完全删除）


### `%USERPROFILE%\AppData\Roaming\Code`分析（跳过）
> 以下内容来自GitHub Copilot

```
├─Backups: 存储未保存文件的备份，以防止数据丢失。大小取决于未保存的文件数量和大小。可以删除，但可能会丢失未保存的更改。
├─^blob_storage: 用于存储大型对象数据。大小取决于使用的扩展和功能。通常不建议删除。
├─Cache: 存储缓存数据，以提高性能。大小取决于使用的扩展和功能。可以删除，但可能会影响性能。
├─CachedConfigurations: 存储缓存的配置数据。大小通常较小。可以删除，但可能需要重新加载配置。
├─CachedData: 存储缓存的数据，以提高性能。大小取决于使用的扩展和功能。可以删除，但可能会影响性能。
├─CachedExtensions: 存储缓存的扩展数据。大小取决于安装的扩展数量和大小。可以删除，但可能需要重新加载扩展。
├─CachedExtensionVSIXs: 存储缓存的 VSIX 扩展安装包。大小取决于下载的 VSIX 文件数量和大小。可以删除，但可能需要重新下载扩展。
├─CachedProfilesData: 存储缓存的用户配置文件数据。大小通常较小。可以删除，但可能需要重新加载用户配置文件。
├─clp: 未知目录，可能与特定扩展或功能相关。大小和是否可以删除取决于具体使用情况。
├─Code Cache: 存储代码缓存，以提高性能。大小取决于使用的扩展和功能。可以删除，但可能会影响性能。
├─Crashpad: 存储崩溃报告和诊断信息。大小通常较小。可以删除，但可能会丢失崩溃诊断信息。
├─databases: 存储数据库文件，可能与特定扩展或功能相关。大小和是否可以删除取决于具体使用情况。
├─DawnCache: 未知目录，可能与特定扩展或功能相关。大小和是否可以删除取决于具体使用情况。
├─Dictionaries: 存储字典文件，用于拼写检查等功能。大小通常较小。可以删除，但可能会影响拼写检查等功能。
├─GPUCache: 存储 GPU 缓存，以提高性能。大小取决于使用的扩展和功能。可以删除，但可能会影响性能。
├─IndexedDB: 存储 IndexedDB 数据库文件，可能与特定扩展或功能相关。大小和是否可以删除取决于具体使用情况。
├─Local Storage: 存储本地存储数据，可能与特定扩展或功能相关。大小和是否可以删除取决于具体使用情况。
├─logs: 存储日志文件。大小取决于日志的数量和详细程度。可以删除，但可能会丢失重要的诊断信息。
├─Network: 未知目录，可能与特定扩展或功能相关。大小和是否可以删除取决于具体使用情况。
├─Service Worker: 存储服务工作者相关的数据。大小通常较小。可以删除，但可能会影响相关的功能。
  ├─CacheStorage: 存储服务工作者的缓存数据。大小通常较小。可以删除，但可能会影响相关的功能。
  ├─Database: 存储服务工作者的数据库数据。大小通常较小。可以删除，但可能会影响相关的功能。
  └─ScriptCache: 存储服务工作者的脚本缓存。大小通常较小。可以删除，但可能会影响相关的功能。
├─Session Storage: 存储会话存储数据，可能与特定扩展或功能相关。大小和是否可以删除取决于具体使用情况。
├─shared_proto_db: 存储共享的 Protocol Buffers 数据库文件。大小通常较小。可以删除，但可能会影响相关的功能。
├─^User: 存储用户设置和配置。大小通常较小。不建议删除，否则会丢失用户设置和配置。
  ├─^globalStorage: 存储全局用户设置和配置。大小通常较小。不建议删除，否则会丢失用户设置和配置。
  ├─History: 存储用户的操作历史。每保存（仅限有修改的成功的重新保存）一次就会生成一个副本，删除之后将会影响历史版本的还原。
  ├─^snippets: 存储用户自定义的代码片段。大小通常较小。不建议删除，否则会丢失自定义的代码片段。
  ├─^sync: 存储用户设置和配置的同步数据。大小通常较小。不建议删除，否则会丢失同步数据。
  └─workspaceStorage: 存储工作区相关的用户设置和配置。（每打开一个工作目录就会在这个目录下生成一个文件夹），大小取决于工作区的数量和大小。可以删除，但可能会丢失工作区设置和数据。
├─VideoDecodeStats: 存储视频解码统计信息。大小通常较小。可以删除，但可能会丢失统计信息。
├─WebStorage: 存储 Web 存储数据，可能与特定扩展或功能相关。大小和是否可以删除取决于具体使用情况。
└─Workspaces: 存储工作区相关的数据。大小取决于工作区的数量和大小。可以删除，但可能会丢失工作区设置和数据。
```

### 能定时删除的目录
1. `%USERPROFILE%\AppData\Local\Microsoft\vscode-cpptools\ipch`
2. `%USERPROFILE%\AppData\Roaming\Code\CachedExtensionVSIXs`
3. `%USERPROFILE%\AppData\Roaming\Code\Cache`
4. `%USERPROFILE%\AppData\Roaming\Code\CachedData`
5. `%USERPROFILE%\AppData\Roaming\Code\CachedExtensions`
6. `%USERPROFILE%\AppData\Roaming\Code\CachedExtensionVSIXs`
7. `%USERPROFILE%\AppData\Roaming\Code\Code Cache`
8. `%USERPROFILE%\AppData\Roaming\Code\Crashpad`
9. `%USERPROFILE%\AppData\Roaming\Code\logs`
10. `%USERPROFILE%\AppData\Roaming\Code\Service Worker\CacheStorage`
11. `%USERPROFILE%\AppData\Roaming\Code\Service Worker\ScriptCache`
12. `%USERPROFILE%\AppData\Roaming\Code\User\workspaceStorage`
13. `%USERPROFILE%\AppData\Roaming\Code\User\History`

### 脚本
```bat
@REM example:
@REM del "%USERPROFILE%/AppData/Local/Microsoft/vscode-cpptools/ipch/" /s /q /f
@REM rd "%USERPROFILE%/AppData/Local/Microsoft/vscode-cpptools/ipch/" /s /q
@REM md "%USERPROFILE%/AppData/Local/Microsoft/vscode-cpptools/ipch/"

@echo off

call:EmptyOneDir "%USERPROFILE%\AppData\Local\Microsoft\vscode-cpptools\ipch"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\CachedExtensionVSIXs"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\Cache"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\CachedData"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\CachedExtensions"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\CachedExtensionVSIXs"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\Code Cache"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\Crashpad"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\logs"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\Service Worker\CacheStorage"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\Service Worker\ScriptCache"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\User\workspaceStorage"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\User\History"

goto end

:EmptyOneDir  rem same as Let empty [path] /q
    echo empty %1
    echo del %1 /s /q /f
    del %1 /s /q /f
    echo rd %1 /s /q
    rd %1 /s /q
    echo md %1
    md %1
:end
```

**只需要将这个脚本另存为 [CleanVSCode.bat](./CleanVSCode.bat) ，并定期双击运行一次，就能定期释放大量空间**

当然，释放的空间直接取决于你的VSCode所产生的缓存大小，间接取决于你的VSCode的使用次数。

最好关闭VSCode后再运行脚本。

---
#### ⚠️Warning
运行脚本后再次运行VSCode基本上看不出什么不同，只是当前工作路径下所打开的文件需要重新手动点击打开。

毕竟是一个**能删除很多东西**的脚本，因此请**谨慎使用**。


————————————————
版权声明：本文为CSDN博主「Tisfy」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Tisfy/article/details/126082324
