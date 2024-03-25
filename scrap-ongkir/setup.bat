@echo off

rem Buat virtual environment
python -m venv scrap_keluhan_user

rem Aktifkan virtual environment
call scrap_keluhan_user\Scripts\activate

rem Instalasi Selenium
pip install selenium

rem Jalankan instalasi package file requirements.txt
call pip install -r requirements.txt

echo Virtual environment telah disiapkan.
echo Modul Selenium telah diinstal.
echo File requirements.txt telah dibuat.
echo.
echo Jalankan "activate.bat" untuk masuk ke virtual environment.