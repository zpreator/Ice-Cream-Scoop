@echo off

SET this_directory=%~dp0

cd %this_directory%

call venv\scripts\activate


powershell.exe "python main.py" > "C:\Users\User\PycharmProjects\Ice-Cream-Scoop\log.txt"

call deactivate

::pause