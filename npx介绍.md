### 一、简介
- `npx` 是 `npm` 从 `v5.2.0` 开始新增了 `npx` 命令，`>=` 该版本会自动安装 `npx`，如果不能使用就手动安装一下：
    ```shell
    $ npm install -g npx
    ```

### 二、`npx` 的作用
- `npm` 只能管理包的依赖，`npx` 则可以快捷的运用包中的命令行工具和其他可执行文件，让项目内部安装的模块用起来更方便。
- 当执行 `$ npx <command>` 相关命令的时候，`npx` 会先本地找（可以是项目中的也可以是本机的）寻找这个 `command`。
    - 找到了：就用本地的版本
    - 没找到：直接下载最新版本（这里是在缓存里），完成命令要求
    - 使用完之后就会完全清除，不会在本机或项目留下任何东西
    - 这样就不会污染本机、永远使用最新版本的 `dependency`

### 三、`npx` 举例常见功能场景，每个案例都有一种常见的用处

#### 案例一
- `npm` 是安装第三方包的，但是安装之后，如何快捷的使用这些包？比如，项目内部安装了测试工具 `webpack`
    ```shell
    # 非全局安装
    $ npm i webpack -D
    ```

- 如果要执行 `webpack` 的命令，要么直接运行下面的命令，要么只能在项目脚本的 `package.json` 中的 `scripts` 字段里面按下面这样配置一个新的命令：
    ```shell
    $ ./node_modules/.bin/webpack -v
    ```

- 类似这样的用法就很不方便有时候一些一次性调试，这个使用可以使用 `npx` 来做这件事，结果是一样的：
    ```shell
    $ npx webpack -v
    ```

#### 案例二
- 另外，使用 `npx` 可以避免全局安装模块，比如：`create-react-app` 这个模块是全局安装，`npx` 可以运行它，而且不进行全局安装。
    ```shell
    $ npx create-react-app my-react-app
    ```

- 上面代码运行时，`npx` 将 `create-react-app` 下载到一个临时目录，使用以后再删除。所以以后再次执行上面的命令，会重新下载 `create-react-app` 提供使用后再移除。

- 下载全局模块时，`npx` 允许指定版本：
    ```shell
    $ npx webpack@4.44.1 ./src/index.js -o ./dist/main.js
    ```

    上面代码指定使用 `v4.44.1` 版本的 `webpack` 进行打包操作。

#### 案例三
- 注意：只要 `npx` 后面的模块无法在本地发现，就会下载同名模块。比如：本地没有安装 `webpack-dev-server` 模块，下面的命令会自动下载该模块，在当前目录启动一个 `Webpack dev` 服务。
    ```shell
    npx webpack-dev-server
    ```

- 如果想让 `npx` 强制使用本地模块，不下载远程模块，可以使用 `--no-install` 参数，如果本地不存在该模块，就会报错：
    ```shell
    $ npx --no-install webpack-dev-server
    ```

- 反过来，如果本地存在同名的模块，但是还是想使用远程的新版本模块，可以使用 `--ignore-existing` 参数。比如：本地已经全局安装了 `create-react-app`，但还是想使用远程模块，就用这个参数：
    ```
    $ npx --ignore-existing create-react-app my-react-app
    ```

#### 案例四
- 利用 `npx` 指定 `node` 版本运行脚本。
    ```
    $ npx node@14.15.0 -v
    ```

- 上面命令会使用 `v14.15.0` 版本的 `node` 执行脚本。原理是从 `npm` 下载这个版本的 `node`，使用后再删掉。

- 在某些场景下，这个方法用来切换 `node` 版本，要比 `nvm` 那样的版本管理器方便一些。
