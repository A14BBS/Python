from openpyxl import load_workbook

book = load_workbook(filename= 'C:/tit/tit_test.xlsx')

sheet = book['Project Timeline']

for i in range(1,20):
    print(sheet['C' + str(i)].value)