import xlrd

wb = xlrd.open_workbook('报名表.xlsx')

print(f'excel中有{wb.nsheets}个工作簿')

print(f'excel中sheets的名字：{wb.sheet_names()}')
