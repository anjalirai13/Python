import xlrd as XL
loc = ("./Line_Extension.xlsx")
wb = XL.open_workbook(loc)
sheet_array = wb.sheet_names()
sheet = wb.sheet_by_name('Input')
row_count = sheet.nrows
print(row_count)
headers = sheet.row_values(0)
for i in range(1, row_count):
  row = sheet.row_values(i)
  result = dict(zip(headers, row))
  print(result)
