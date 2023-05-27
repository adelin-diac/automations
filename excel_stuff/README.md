# Excel Stuff

## **Links**

1. [Excel Planner](#excel_plannerpy)

## `excel_planner.py`

### **Pre-requisites**

- Python 3.6 or later
- pip
- virtualenv

### **How to Run**

Ensure that you have Python installed on your system. The script is compatible with Python 3.6 or later. There are two ways to run the script:

1. Run the script using my automation script from `python_start_app_venv` directory in the root folder [here](../python_start_app_venv/start_python_app.bat). This will start the script in a virtual environment with all the required dependencies installed. This is the recommended way to run the script.

2. Run the script directly from the command line. This will require you to install the required dependencies manually.

### **Manual Installation**

Install the required Python libraries, `pandas` and `openpyxl`, by running the following command in your terminal or command prompt:

```
pip install pandas openpyxl
```

Open a terminal or command prompt, navigate to the directory containing the script, and run the following command:

```
python excel_planner.py
```

The script will generate an Excel file named `daily_schedule.xlsx` in the `excel_stuff` directory. Open the file using Microsoft Excel or another compatible spreadsheet application to view and use your daily schedule planner.

### **Customization**

To customize the planner for a different year, modify the year variable in the script before running it. By default, the variable is set to the current year:

```py
year = 2023
```

Replace 2023 with the desired year, save the script, and run it as described in the "How to Run" section.

---
