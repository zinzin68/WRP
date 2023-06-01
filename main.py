import openpyxl
wb = openpyxl.load_workbook("C:/Users/dnwls/WRP/engword.xlsx")
wb_sheet = wb.active

for row in wb_sheet:
    if row[0].value == None:
        break
    print(row[0].value, row[1].value, row[2].value)

wb.close()