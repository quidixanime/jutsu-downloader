@echo off
color 2
title Launcher app
:::              _     _ _      
:::             (_)   | (_)     
:::   __ _ _   _ _  __| |___  __
:::  / _` | | | | |/ _` | \ \/ /
::: | (_| | |_| | | (_| | |>  < 
:::  \__, |\__,_|_|\__,_|_/_/\_\
:::     | |                     
:::     |_|                     

for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A
echo ya russkiy (1)
echo Im English (2)
echo Credits (3)
set /p choice=

if %choice% == 1 goto rus
if %choice% == 2 goto eng
if %choice% == 3 goto cred

:rus
start python app_ru.py
echo u can still choose!!
set /p choice=

:eng
start python app_en.py
echo u can still choose!!
set /p choice=

:cred
start https://t.me/quidixcode
echo u can still choose!!
set /p choice=