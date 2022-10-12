1、在 VSCode 中安装 `PicGo`

2、获取Github Token
- 单击右上角头像，下来菜单中选择 Settings
- 在左侧导航栏找到 Developer settings
- Personal access tokens

3、创建Github仓库

4、打开PicGo的扩展配置 `@ext:Spades.vs-picgo`
```json
"picgo.picBed.uploader": "github",
"picgo.picBed.github.repo": "username/reponame",
"picgo.picBed.github.branch": "main",
"picgo.picBed.github.token": "github token",
```
