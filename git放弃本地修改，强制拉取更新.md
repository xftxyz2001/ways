开发项目时，对于本地已修改但又不想保留的代码（比如你代码改崩了），可以用如下两种方法来重置代码：

### 1、restore 重置
如果你修改了代码，但是并未执行 `git add` 操作，可直接执行：
```bash
git restore .
```

. 表示所有文件，如果想重置个别文件，指定文件路径即可
```bash
git restore [文件]...
```

> 注意⚠️：如果你已经执行了 `git add` 操作，此时代码已保存至暂存区，需要先取消暂存区变更：
```bash
git restore --staged .
```

或者
```bash
git reset .
```

然后，再执行 `git pull` 拉取远程代码同步即可。

### 2、reset 回退★
`reset` 比较暴力，相当于 可适用于 代码在工作区、暂存区、仓库区等任何场景，重置后不可恢复🙅‍♂️，对于新手有一定的安全隐患。
```bash
git fetch --all
git reset --hard origin/master  # 根据实际情况修改分支名
git pull  # 这一步为了同步远程代码，不需要的话可不执行
```

- git fetch 指令是下载远程仓库最新内容，不做合并。
- git reset 指令把HEAD指向master最新版本。

> reset --hard：重置后不保留暂存区和工作区  
> reset --soft：保留工作区，并把重置 HEAD 所带来的新的差异放进暂存区（此时代码的变更状态相当于执行完 `git add`命令）  
> reset --mixed：reset的默认参数，保留工作目录，并重置暂存区（此时代码的变更状态相当于执行 `git add`命令之前）

### 3、stash 暂存（推荐）
我比较喜欢的方法，是用stash，暂存代码再同步。

首先，将所有代码添加至暂存区：
```bash
git add .
```

然后，将代码临时保存：
```bash
git stash
```

此时代码会重置到修改前的状态，可以同步远程仓库区，完事儿。
```bash
git pull
```

同步后，**如果**还想继续修改原来的代码，可将临时代码恢复至工作区：
```bash
git stash pop
```

> 注意⚠️，stash 用法有很多，比如save，push，pop，clear等，需要使用可以查阅[stash 命令](https://git-scm.com/docs/git-stash)


## 参考
- [CSDN-git 放弃本地修改，强制拉取更新](https://blog.csdn.net/haoaiqian/article/details/78284337)
- [git官方文档](https://git-scm.com/docs/)
- [菜鸟教程-Git教程](https://www.runoob.com/git/git-tutorial.html)
