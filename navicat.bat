@echo off
set dn=Info
set dn2=ShellFolder
set rp=HKEY_CURRENT_USER\Software\Classes\CLSID
:: reg delete HKEY_CURRENT_USER\Software\PremiumSoft\NavicatPremium\Registration14XCS /f  %’Î∂‘<strong><font color="#FF0000">navicat</font></strong>15%
reg delete HKEY_CURRENT_USER\Software\PremiumSoft\NavicatPremium\Registration16XCS /f
reg delete HKEY_CURRENT_USER\Software\PremiumSoft\NavicatPremium\Update /f
echo finding.....
for /f "tokens=*" %%a in ('reg query "%rp%"') do (
 echo %%a
for /f "tokens=*" %%l in ('reg query "%%a" /f "%dn%" /s /e ^|findstr /i "%dn%"') do (
  echo deleteing: %%a
  reg delete %%a /f
)
for /f "tokens=*" %%l in ('reg query "%%a" /f "%dn2%" /s /e ^|findstr /i "%dn2%"') do (
  echo deleteing: %%a
  reg delete %%a /f
)
)
echo re trial done!
  
start /d "C:\Program Files\PremiumSoft\Navicat Premium 16" navicat.exe
