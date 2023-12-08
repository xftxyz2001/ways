@echo off

REM 请将下面的路径改为你的jdk安装目录
set "jdkshome=C:\Users\25810\.jdks"

REM 循环生成切换脚本
for /D %%i in ("%jdkshome%\*") do (
    echo Generating %jdkshome%\use%%~nxi.bat...
    echo setx JAVA_HOME "%%i" > "%jdkshome%\use%%~nxi.bat"
)
