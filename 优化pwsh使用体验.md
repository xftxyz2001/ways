# 1. 安装模块
```powershell
Install-Module posh-git -Scope CurrentUser
Install-Module oh-my-posh -Scope CurrentUser -RequiredVersion 2.0.496
```



# 2. 修改字体

## 2.1 下载字体
[Meslo2.1.0.zip](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Meslo.zip)


## 2.2 终端
终端使用快捷键`Ctrl+Shift+,`
```json
{
    "profiles": 
        {
            "defaults": 
            {
                "font": 
                {
                    "face": "MesloLGM NF"
                },
                "useAtlasEngine": true
            },
        }
}
```


## 2.3 VSCode
```json
{
    "terminal.integrated.fontFamily": "MesloLGM NF",
}
```



# 3. 创建并修改$PROFILE
```powershell
if (!(Test-Path -Path $PROFILE )) { New-Item -Type File -Path $PROFILE -Force }
code $PROFILE
```

[profile](./Microsoft.PowerShell_profile.ps1)


# 参考
- https://github.com/JanDeDobbeleer/oh-my-posh2#installation
- https://ohmyposh.dev/docs/installation/windows

