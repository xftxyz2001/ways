CLS
@ECHO OFF
@REM ������̷���maven�ı��زֿ����ڵ��̷����������C�̣����޸�
@REM SET CLEAR_PATH=C:
@REM �����·����maven�ı��زֿ�·�����������Ĭ��·�������޸�
SET CLEAR_DIR=%USERPROFILE%\.m2\repository

@REM color 0a ������ɫ
TITLE ClearLastUpdated For Windows
GOTO MENU

:MENU
CLS
ECHO.
ECHO. * * * * ClearLastUpdated For Windows  * * * *
ECHO. *
ECHO. *          ��1�� ���� *.lastUpdated
ECHO. *
ECHO. *          ��2�� �鿴 *.lastUpdated
ECHO. *
ECHO. *          ��3�� �˳�
ECHO. *
ECHO. * * * * * * * * * * * * * * * * * * * * * * *
ECHO.
ECHO.������ѡ����Ŀ����ţ�
set /p ID=
IF "%id%"=="1" GOTO cmd1
IF "%id%"=="2" GOTO cmd2
IF "%id%"=="3" EXIT
PAUSE

:cmd1
ECHO.��ʼ����...
%CLEAR_PATH%
cd %CLEAR_DIR%
for /r %%i in (*.lastUpdated) do del %%i
ECHO.OK
PAUSE
GOTO MENU

:cmd2
ECHO.*.lastUpdated�ļ��б�
%CLEAR_PATH%
cd %CLEAR_DIR%
for /r %%i in (*.lastUpdated) do echo %%i
ECHO.OK
PAUSE
GOTO MENU
