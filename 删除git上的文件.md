Github for Windows/Mac桌面应用以及网页版都没有提供清除某个文件操作记录的功能，就是说即便你删了这个文件重新Push，那么别人依然可以查看你上一个版本。
所以我们需要的是把和这个文件有关的所有Commit等记录全部删掉当然也包括文件本身。  
首先在Git Bash或者CMD或者PowerShell中cd进入到你的本地项目文件夹，然后依次执行下面**6行命令**即可：

```bash
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch FILE_PATH' --prune-empty --tag-name-filter cat -- --all
git push origin main --force
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now
git gc --aggressive --prune=now
```

FILE_PATH：你要删除的文件的路径

[参考资料](https://help.github.com/articles/remove-sensitive-data/)
