import openpyxl

wb = openpyxl.load_workbook("C:/Users/dnwls/WRP/engword.xlsx")
wb_sheet = wb.active
A=[]

for row in wb_sheet:
    if row[0].value == None:
        break
    A.append(row[0].value)

print (A[5])