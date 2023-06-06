import openpyxl

list = openpyxl.load_workbook('wordfile.xlsx')
sheet = list.get_sheet_names()
#print(sheet)

word = list.get_sheet_by_name(sheet[0])
count =0

for row in word:
        count +=1

i=1
while i<=count:
        print(word.cell(row=i,column=1).value)
        #i+=1
        if (int(input())==1):
                i+=1
        else:
                break

#for i in count:
        

