@echo off

rem Set path to virtual environment directory
set "VIRTUAL_ENV=scrap_keluhan_user"

rem Check if virtual environment exists
if not exist "%VIRTUAL_ENV%\Scripts\activate.bat" (
    echo Virtual environment "%VIRTUAL_ENV%" not found.
    echo Please make sure you have created the virtual environment.
    exit /b 1
)

rem Activate virtual environment
call "%VIRTUAL_ENV%\Scripts\activate"

rem Display activation message
echo Virtual environment "%VIRTUAL_ENV%" activated.
