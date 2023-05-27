@echo off

@REM This script will create a virtual environment, install dependencies, and run your app.

@REM Set Path to your app
set "app_path=C:\Users\adeli\Desktop\codes\automations\excel_stuff"

@REM Set name of your app (or name of script file to run)
set "app_name=excel_planner.py"

@REM set virtualenvironment name
set "venv_name=venv"

set "full_app_path=%app_path%\%app_name%"
set "venv_dir=%app_path%\%venv_name%"

if not exist "%venv_dir%" (
    echo Creating virtual environment...
    cd %app_path% & virtualenv "%venv_name%"
)

echo Activating virtual environment...
call "%venv_dir%\Scripts\activate.bat"

echo Installing dependencies...
cd %app_path% & pip install -r requirements.txt

echo Running app...
cd %app_path% & python "%app_name%"

echo Deactivating virtual environment...
call deactivate
