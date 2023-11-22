CLS
@ECHO OFF
@REM 下面的盘符是maven的本地仓库所在的盘符，如果不是C盘，请修改
@REM SET CLEAR_PATH=C:
@REM 下面的路径是maven的本地仓库路径，如果不是默认路径，请修改
SET CLEAR_DIR=%USERPROFILE%\.m2\repository

@REM color 0a 设置颜色
TITLE ClearLastUpdated For Windows
GOTO MENU

:MENU
CLS
ECHO.
ECHO. * * * * ClearLastUpdated For Windows  * * * *
ECHO. *
ECHO. *          【1】 清理 *.lastUpdated
ECHO. *
ECHO. *          【2】 查看 *.lastUpdated
ECHO. *
ECHO. *          【3】 退出
ECHO. *
ECHO. * * * * * * * * * * * * * * * * * * * * * * *
ECHO.
ECHO.请输入选择项目的序号：
set /p ID=
IF "%id%"=="1" GOTO cmd1
IF "%id%"=="2" GOTO cmd2
IF "%id%"=="3" EXIT
PAUSE

:cmd1
ECHO.开始清理...
%CLEAR_PATH%
cd %CLEAR_DIR%
for /r %%i in (*.lastUpdated) do del %%i
ECHO.OK
PAUSE
GOTO MENU

:cmd2
ECHO.*.lastUpdated文件列表：
%CLEAR_PATH%
cd %CLEAR_DIR%
for /r %%i in (*.lastUpdated) do echo %%i
ECHO.OK
PAUSE
GOTO MENU
