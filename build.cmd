@echo off
setlocal
cd /d "%~dp0"
set "PATH=%~dp0pandoc;%PATH%"

set "PANDOC=pandoc"
if exist "pandoc\pandoc.exe" set "PANDOC=pandoc\pandoc.exe"
"%PANDOC%" --defaults=document.yaml
exit /b %errorlevel%
