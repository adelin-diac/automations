# Automations

List of scripts for automating some of the stuff I do.

**Last Update:** 27 May 2023

**TODO:**

- Move the detailed descriptions of each script into it's own folder

- Only keep basic explanation of what it does here

## Quick Links

- [Server Starts](#server-starts)
  - [Local Environment startup for React & Firebase](#react_frontend_with_firebase_functionsbat)
- [Excel Stuff](#excel-stuff)
  - [Excel Planner](#excel_plannerpy)

# Server Starts

## `react_frontend_with_firebase_functions.bat`

## **Local Development Environment Startup Script**

### **Description**

This BAT script is designed to simplify the process of starting your React frontend and Firebase functions local testing servers. When executed, the script opens two separate command prompt windows, one for each server. Additionally, it opens the respective directories in Visual Studio Code.

### **How to Use**

Place the provided BAT script in a directory of your choice.

Before running the script, ensure that the paths for the `create_react_app_frontend` and `firebase_functions` variables are correctly set to the locations of your React frontend and Firebase functions folders on your system. This script assumes that the `functions` directory for Firebase is located in the folder generated by `create-react-app`.

```batch
set create_react_app_frontend="path\to\react_frontend"
set firebase_functions="react_frontend\functions"
```

To start your local development environment, double-click the BAT script, or open a command prompt, navigate to the directory containing the script, and run the script by typing its filename and pressing Enter.

The script will start the React frontend and Firebase functions servers in separate command prompt windows, and it will open the respective directories in Visual Studio Code.

<br/>

# Excel Stuff

## `excel_planner.py`

**Disclaimer:** `excel_planner.py` script and docs were generated by GPT Plus with some tweaks from me to get it to work/exlpain exactly how I wanted. It really surprised me how quickly I was able to get the code generated, working and documented with the help of AI.

### **Description**

This Python script generates an Excel file containing a daily schedule planner for an entire year. The planner is organized into separate worksheets for each month, with columns representing days of the month and rows representing 30-minute time slots, starting from 6:30 AM and ending at 6:00 AM the following day. The column headers show the day of the week and day of the month with the appropriate ordinal suffix (e.g., "Monday 1st").

### **How to Run**

Ensure that you have Python installed on your system. The script is compatible with Python 3.6 or later.

Install the required Python libraries, `pandas` and `openpyxl`, by running the following command in your terminal or command prompt:

```
pip install pandas openpyxl
```

Download the script `daily_schedule_generator.py` and place it in a directory of your choice.

Open a terminal or command prompt, navigate to the directory containing the script, and run the following command:

```
python daily_schedule_generator.py
```

The script will generate an Excel file named `daily_schedule.xlsx` in the `excel_stuff` directory. Open the file using Microsoft Excel or another compatible spreadsheet application to view and use your daily schedule planner.

### **Customization**

To customize the planner for a different year, modify the year variable in the script before running it. By default, the variable is set to the current year:

```py
year = 2023
```

Replace 2023 with the desired year, save the script, and run it as described in the "How to Run" section.
