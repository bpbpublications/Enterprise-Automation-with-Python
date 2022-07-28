from openpyxl import load_workbook

# load the test workbook
workbook = load_workbook(filename="test_workbook.xlsx")
sheet = workbook.active

# Access columns A and B - gives cell tuple as output
print(sheet["A:B"])

# Access row 1
print(sheet[1])
