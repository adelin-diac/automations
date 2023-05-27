# Python Start App Venv

## **Links**

1. [Start Python App](#start_python_appbat)

## `start_python_app.bat`

### **Description**

This BAT script is designed to simplify the process of starting a Python app in a virtual environment. When executed, the script opens a command prompt window and activates the virtual environment, it downloads any dependancies, and then it runs the app/script.

You can then copy the `.bat` file to an easy location to access, and you can start your python app with a double-click.

### Pre-requisites

- Python
- Virtualenv
- pip

Also, ensure there is a `requirements.txt` file in the root of your app folder.

### **How to Use**

1. Edit the variables at the top of the script to match your needs.

```batch
@REM Set Path to your app
set "app_path=path\to\app\folder"

@REM Set name of your app (or name of script file to run)
set "app_name=app_name.py"

@REM set virtualenvironment name (preferably "venv")
set "venv_name=venv"
```

Once these are set, your app should run with the virtual environment activated.
