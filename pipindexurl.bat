@echo off
setlocal enabledelayedexpansion

set PIP_DIR=%APPDATA%\pip
set PIP_INI=%PIP_DIR%\pip.ini

if not exist "%PIP_DIR%" mkdir "%PIP_DIR%"

set "sources=清华#https://pypi.tuna.tsinghua.edu.cn/simple#pypi.tuna.tsinghua.edu.cn 阿里#https://mirrors.aliyun.com/pypi/simple#mirrors.aliyun.com 中科大#https://pypi.mirrors.ustc.edu.cn/simple#pypi.mirrors.ustc.edu.cn 豆瓣#http://pypi.douban.com/simple#pypi.douban.com 腾讯#http://mirrors.cloud.tencent.com/pypi/simple#mirrors.cloud.tencent.com 华为#https://repo.huaweicloud.com/repository/pypi/simple#repo.huaweicloud.com 北大#https://mirrors.pku.edu.cn/pypi/web/simple#mirrors.pku.edu.cn 哈工大#https://mirrors.hit.edu.cn/pypi/web/simple#mirrors.hit.edu.cn 大连东软#https://mirrors.neusoft.edu.cn/pypi/web/simple#mirrors.neusoft.edu.cn"

set i=1
for %%a in (%sources%) do (
    for /f "tokens=1 delims=#" %%b in ("%%a") do (
        echo !i!. %%b
    )
    set "source!i!=%%a"
    set /a i+=1
)

:input
set /p choice=请输入你的选择 (1-%i%): 
if not defined source%choice% (
    echo 输入无效，请重新输入。
    goto input
)

for /f "tokens=1,2,3 delims=#" %%a in ("!source%choice%!") do (
    echo [global]> "%PIP_INI%"
    echo index-url = %%b>> "%PIP_INI%"
    echo [install]>> "%PIP_INI%"
    echo trusted-host = %%c>> "%PIP_INI%"
)

for /f "tokens=1 delims=#" %%a in ("!source%choice%!") do (
    echo 切换成功，当前使用的源是 %%a。
)
endlocal