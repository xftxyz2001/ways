@REM example:
@REM del "%USERPROFILE%/AppData/Local/Microsoft/vscode-cpptools/ipch/" /s /q /f
@REM rd "%USERPROFILE%/AppData/Local/Microsoft/vscode-cpptools/ipch/" /s /q
@REM md "%USERPROFILE%/AppData/Local/Microsoft/vscode-cpptools/ipch/"

@echo off

call:EmptyOneDir "%USERPROFILE%\AppData\Local\Microsoft\vscode-cpptools\ipch"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\CachedExtensionVSIXs"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\Cache"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\CachedData"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\CachedExtensions"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\CachedExtensionVSIXs"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\Code Cache"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\Crashpad"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\logs"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\Service Worker\CacheStorage"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\Service Worker\ScriptCache"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\User\workspaceStorage"
call:EmptyOneDir "%USERPROFILE%\AppData\Roaming\Code\User\History"

goto end

:EmptyOneDir  rem same as Let empty [path] /q
    echo empty %1
    echo del %1 /s /q /f
    del %1 /s /q /f
    echo rd %1 /s /q
    rd %1 /s /q
    echo md %1
    md %1
:end