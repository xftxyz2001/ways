## 一、安装 `nvm`
```shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
# or
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

国内源
```shell
$ bash -c "$(curl -fsSL https://gitee.com/mirrors/nvm/blob/master/install.sh)"
```


## 二、 卸载
进入文件夹删除 `nvm`
```shell
$ cd ~
$ rm -rf .nvm
```

移除掉当前使用 `Shell` 的配置文件中属于 `nvm` 的配置。

配置文件包含：`~/.profile`、`~/.bash_profile`、`~/.zshrc`、 `~/.bashrc`，这里以 `zsh` 解释器的 `~/.zshrc` 

配置文件举例：
```shell
$ vim ~/.zshrc
```

然后移除里面 `export NVM_DIR` 那段配置，然后按 `ESC` 退出编辑，`:wq` 进行保存，然后重新加载一遍配置文件，使其生效：
```shell
$ source ~/.zshrc
```

然后重启当前命令行工具即可。


## 三、使用
要下载、编译并安装最新版本的 ，请执行以下操作：
```bash
nvm install node # "node" 是最新版本的别名
```

要安装特定版本的 ，请执行：
```bash
nvm install 14.7.0 # 或者 16.3.0, 12.22.1 等等
```

首次安装的版本将成为默认版本。新启动的 shell 将使用默认的  版本（例如，`nvm alias default`）。

您可以使用 `ls-remote` 列出所有可用版本：
```bash
nvm ls-remote
```

然后在任何新 shell 中只需使用已安装的版本：
```bash
nvm use node
```

或者直接运行它：
```bash
nvm run node --version
```

您还可以在子 shell 中使用所需版本运行任何任意命令：
```bash
nvm exec 4.2 node --version
```

此外，您还可以获取到安装路径下的可执行文件：
```bash
nvm which 12.22
```

在诸如 "14.7"、"16.3" 或 "12.22.1" 这样的版本指针位置，对于 `nvm install`、`nvm use`、`nvm run`、`nvm exec`、`nvm which` 等命令，您可以使用以下特殊默认别名：

- `node`: 安装最新版本的 [](https://nodejs.org/en/)
- `iojs`: 安装最新版本的 [io.js](https://iojs.org/en/)
- `stable`: 此别名已被弃用，只适用于 `` `v0.12` 及更早版本。当前，这是一个指向 `node` 的别名。
- `unstable`: 此别名指向 `` `v0.11`——最后一个“不稳定” 版本，因为自 1.0 后的所有  版本都被视为稳定版本。（根据 SemVer 规范，版本表示的是破坏性变更，而非稳定性）。

---
- [nvm 官方文档](https://github.com/nvm-sh/nvm/blob/master/README.md)
- [nvm 安装、卸载与使用（详细步骤）](https://juejin.cn/post/7000652162950758431)
