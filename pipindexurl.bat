@echo off
setlocal enabledelayedexpansion

set PIP_DIR=%APPDATA%\pip
set PIP_INI=%PIP_DIR%\pip.ini

if not exist "%PIP_DIR%" mkdir "%PIP_DIR%"

set "sources=�廪#https://pypi.tuna.tsinghua.edu.cn/simple#pypi.tuna.tsinghua.edu.cn ����#https://mirrors.aliyun.com/pypi/simple#mirrors.aliyun.com �пƴ�#https://pypi.mirrors.ustc.edu.cn/simple#pypi.mirrors.ustc.edu.cn ����#http://pypi.douban.com/simple#pypi.douban.com ��Ѷ#http://mirrors.cloud.tencent.com/pypi/simple#mirrors.cloud.tencent.com ��Ϊ#https://repo.huaweicloud.com/repository/pypi/simple#repo.huaweicloud.com ����#https://mirrors.pku.edu.cn/pypi/web/simple#mirrors.pku.edu.cn ������#https://mirrors.hit.edu.cn/pypi/web/simple#mirrors.hit.edu.cn ��������#https://mirrors.neusoft.edu.cn/pypi/web/simple#mirrors.neusoft.edu.cn"

set i=1
for %%a in (%sources%) do (
    for /f "tokens=1 delims=#" %%b in ("%%a") do (
        echo !i!. %%b
    )
    set "source!i!=%%a"
    set /a i+=1
)

:input
set /p choice=���������ѡ�� (1-%i%): 
if not defined source%choice% (
    echo ������Ч�����������롣
    goto input
)

for /f "tokens=1,2,3 delims=#" %%a in ("!source%choice%!") do (
    echo [global]> "%PIP_INI%"
    echo index-url = %%b>> "%PIP_INI%"
    echo [install]>> "%PIP_INI%"
    echo trusted-host = %%c>> "%PIP_INI%"
)

for /f "tokens=1 delims=#" %%a in ("!source%choice%!") do (
    echo �л��ɹ�����ǰʹ�õ�Դ�� %%a��
)
endlocal