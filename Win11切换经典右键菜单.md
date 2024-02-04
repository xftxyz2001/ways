## 启用
[Win11EnableClassicContextMenu.bat](./Win11EnableClassicContextMenu.bat)

```bat
@REM 启用经典右键菜单
reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
taskkill /f /im explorer.exe & start explorer.exe
```

## 禁用
[Win11DisableClassicContextMenu.bat](./Win11DisableClassicContextMenu.bat)

```bat
@REM 禁用经典右键菜单
reg delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" /f
taskkill /f /im explorer.exe & start explorer.exe
```
