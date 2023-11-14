@echo off

del "%~dp0\home\%USERNAME%\.bashrc"
copy "%~dp0\bashrc.MakeRef" "%~dp0\home\%USERNAME%\.bashrc" > nul
cd /d "%~dp0\bin" && .\bash --login -i