### 一、`node`、`nvm`、`npm`、`npx`、`nrm` 区别
- `node`：是一个基于 `Chrome V8` 引擎的 `JS` 运行环境。
- `npm`：是 `node.js` 默认的包管理系统（用 `JavaScript` 编写的），在安装的 `node` 的时候，`npm` 也会跟着一起安装，管理 `node` 中的第三方插件。
- `npx`：`npm` 从 `v5.2.0` 开始新增了 `npx` 命令，`>=` 该版本会自动安装 `npx`，附带：[npx 有什么作用跟意义？为什么要有 npx？什么场景使用？](./npx介绍.md)。
- `nrm`：是一个 `npm` 源管理工具，使用它可以快速切换 `npm` 源，默认是官方源，当 `npm` 下载包过慢时，可能需要切换到第三方源（例如：淘宝、科大...），还有公司私有源地址等等。
- `nvm`：`node` 版本管理器，也就是说：一个 `nvm` 可以管理多个 `node` 版本（包含 `npm` 与 `npx`），可以方便快捷的 `安装`、`切换` 不同版本的 `node`。

### 二、`node`、`nvm`、`npm`、`npx`、`nrm` 关系
- `nvm` 管理 `node` (包含 `npm` 与 `npx`) 的版本，`npm` 可以管理 `node` 的第三方插件，`nrm` 可以管理 `npm` 的源地址（当然也可以直接使用 `npm` 自带命令管理，看个人习惯）。
- 切换不同的 `node` 版本，`npm` 与 `npx` 的版本也会跟着变化。
    ```shell
    $ nvm use v8.16.0
    Now using node v8.16.0 (npm v6.4.1)
    $ nvm use v14.15.4
    Now using node v14.15.4 (npm v6.14.10)
    $ nvm use v18.6.0
    Now using node v18.6.0 (npm v8.13.2)
    ```
