import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Function to generate a DataFrame for each month with days as columns and 30-min slots as rows
def generate_monthly_schedule(year, month):
    start_date = datetime(year, month, 1)
    end_date = datetime(year, month + 1, 1) if month != 12 else datetime(year + 1, 1, 1)
    num_days = (end_date - start_date).days

    time_slots = pd.date_range(start_date.replace(hour=6, minute=30), start_date.replace(hour=6, minute=0) + timedelta(days=1), freq='30min').strftime('%H:%M')
    
    def day_suffix(day):
        if 4 <= day <= 20 or 24 <= day <= 30:
            return "th"
        else:
            return ["st", "nd", "rd"][day % 10 - 1]
    
    column_labels = [start_date.replace(day=i).strftime('%A %d') + day_suffix(i) for i in range(1, num_days + 1)]
    df = pd.DataFrame(index=time_slots, columns=column_labels)

    return df


# Create a new Excel workbook and add a worksheet for each month
year = 2023
output_file = 'daily_schedule.xlsx'
wb = Workbook()
wb.remove(wb.active)  # Remove default sheet

for month in range(1, 13):
    month_name = datetime(year, month, 1).strftime('%B')
    ws = wb.create_sheet(title=month_name)

    # Generate a DataFrame for the month and add it to the worksheet
    df_month = generate_monthly_schedule(year, month)
    for r in dataframe_to_rows(df_month, index=True, header=True):
        ws.append(r)

# Save the Excel workbook
wb.save(f'excel_stuff/{output_file}')
