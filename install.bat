
@echo off

move %~dp0\MakeRef.ico %~dp0..\sys\BgPic\
move %~dp0\seqtk-1.3 %~dp0..\sys\tools\
move %~dp0\Make_Reference_Genome %~dp0..\sys\home\
move %~dp0\bashrc.MakeRef %~dp0..\sys\
move %~dp0\MakeRef.bat %~dp0..\sys\

(echo Set WshShell=CreateObject("WScript.Shell"^)
	echo Set oShellLink=WshShell.CreateShortcut("%~dp0..\SNPGT-bulid.lnk"^)
	echo oShellLink.TargetPath="%~dp0..\sys\MakeRef.bat"
	echo oShellLink.Description="MakeRef"
	echo oShellLink.IconLocation="%~dp0..\sys\BgPic\MakeRef.ico"
	echo oShellLink.Save) > MakeRef.vbs
MakeRef.vbs
del /f /q MakeRef.vbs
del /f /q install.bat
del /f /q %~dp0..\Make_RefGenome.exe


