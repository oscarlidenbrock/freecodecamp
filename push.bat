@echo off
setlocal

set "challenge_date=%~1"

if not defined challenge_date (
    for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format ''dd/MM/yyyy''"') do set "challenge_date=%%i"
)

git add .
git commit -a -m "upload daily challenge %challenge_date%"
git push origin main
