@echo off
cls
color 0A
title SayOne UserBot Installer

clear

:: Проверка Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Python is not installed or added to PATH
    echo Install Python from the website https://www.python.org/downloads/
    pause
    exit /b
)

:: Проверка git
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Git is not installed!
    echo Install it from here: https://git-scm.com/download/win
    pause
    exit /b
)

:: Основные параметры
set REPO_URL=https://github.com/nurawerdey/sayone.git
set FOLDER_NAME=SayOne

echo.
echo [1/4] Cloning a repository...
git clone %REPO_URL% %FOLDER_NAME%
cd %FOLDER_NAME%

echo.
echo [2/4] Installing dependencies...
pip install -r requirements.txt

echo.
echo [3/4] Creation config.py...
(
echo API_ID = 12345
echo API_HASH = "ваш_api_hash"
) > config.py

echo.
echo [4/4] Launch UserBot...
python main.py

pause
