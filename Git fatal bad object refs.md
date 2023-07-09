### 问题：
> fatal: bad object refs/remotes/origin/xxx  
> error: ssh://xxx.git did not send all necessary objects

### 解决：
1. 删除 `.git/refs/remotes/origin/` 目录下所有文件；
2. `git fetch --all` ，解决问题

