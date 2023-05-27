# Automations

List of scripts for automating some of the stuff I do.

**Last Update:** 27 May 2023

## Quick Links

- [Server Starts](#server-starts)
- [Excel Stuff](#excel-stuff)
- [Python App with Virtual Environment](#python-app-with-virtual-environment)

# Server Starts

## `react_frontend_with_firebase_functions.bat`

Link: [react_frontend_with_firebase_functions.bat](./server_starts/README.md)

### **Description**

This BAT script is designed to simplify the process of starting your React frontend and Firebase functions local testing servers. When executed, the script opens two separate command prompt windows, one for each server. Additionally, it opens the respective directories in Visual Studio Code.

<br/>

# Excel Stuff

## `excel_planner.py`

Link: [excel_planner.py](./excel_stuff/README.md)

**Disclaimer:** Parts of `excel_planner.py` script and docs were generated by GPT Plus with some tweaks from me to get it to work/exlpain exactly how I wanted. It really surprised me how quickly I was able to get the code generated, working and documented with the help of AI.

### **Description**

This Python script generates an Excel file containing a daily schedule planner for an entire year. The planner is organized into separate worksheets for each month, with columns representing days of the month and rows representing 30-minute time slots, starting from 6:30 AM and ending at 6:00 AM the following day. The column headers show the day of the week and day of the month with the appropriate ordinal suffix (e.g., "Monday 1st").

# Python App with Virtual Environment

## `start_python_app.bat`

Link: [start_python_app.bat](./python_start_app_venv/README.md)

### **Description**

This BAT script is designed to simplify the process of starting a Python app in a virtual environment. When executed, the script opens a command prompt window and activates the virtual environment, it downloads any dependancies, and then it runs the app/script.
