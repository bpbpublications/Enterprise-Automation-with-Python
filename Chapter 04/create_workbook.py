from openpyxl import Workbook
# Import the date time and os modules in Python
import datetime
import os

# Create a new workbook
workbook = Workbook()
# Get the active worksheet
active_worksheet = workbook.active
# Data can be assigned directly to cells
active_worksheet['A1'] = "Hello World"
# Python types will automatically be converted to excel format
active_worksheet['B1'] = datetime.datetime.now()
# Save the workbook
workbook.save("test_workbook.xlsx")
print(os.listdir('.'))
