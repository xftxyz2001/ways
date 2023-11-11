## 下载
[下载地址](https://github.com/coreybutler/nvm-windows/releases)
选择 `nvm-setup.exe` 下载即可，安装过程中一路下一步即可。


## 使用
| 命令                    | 说明                                          |
| ----------------------- | --------------------------------------------- |
| `nvm list available`    | 显示所有可以下载的 Node.js 版本               |
| `nvm install <version>` | 安装 version（可省略小版本号） 版本的 Node.js |
| `nvm list`              | 显示已安装的版本                              |
| `nvm use <version>`     | 切换 version 的 Node.js                       |


## 常用命令
| 命令                           | 介绍                                                                                                                                                  |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nvm arch`                     | 显示node是运行在32位还是64位。                                                                                                                        |
| `nvm install <version> [arch]` | 安装node， version是特定版本也可以是最新稳定版本latest。可选参数arch指定安装32位还是64位版本，默认是系统位数。可以添加--insecure绕过远程服务器的SSL。 |
| `nvm list [available]`         | 显示已安装的列表。可选参数available，显示可安装的所有版本。list可简化为ls。                                                                           |
| `nvm on`                       | 开启node.js版本管理。                                                                                                                                 |
| `nvm off`                      | 关闭node.js版本管理。                                                                                                                                 |
| `nvm proxy [url]`              | 设置下载代理。不加可选参数url，显示当前代理。将url设置为none则移除代理。                                                                              |
| `nvm node_mirror [url]`        | 设置node镜像。默认是`https://nodejs.org/dist/`。如果不写url，则使用默认url。设置后可至安装目录settings.txt文件查看，也可直接在该文件操作。            |
| `nvm npm_mirror [url]`         | 设置npm镜像。`https://github.com/npm/cli/archive/`。如果不写url，则使用默认url。设置后可至安装目录`settings.txt`文件查看，也可直接在该文件操作。      |
| `nvm uninstall <version>`      | 卸载指定版本node。                                                                                                                                    |
| `nvm use [version] [arch]`     | 使用制定版本node。可指定32/64位。                                                                                                                     |
| `nvm root [path]`              | 设置存储不同版本node的目录。如果未设置，默认使用当前目录。                                                                                            |
| `nvm version`                  | 显示nvm版本。version可简化为v。                                                                                                                       |

## 参考
- [nvm文档手册 - nvm是一个nodejs版本管理工具 - nvm中文网](https://nvm.uihtm.com/)
