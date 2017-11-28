import xlsxwriter 

workbook= xlsxwriter.Workbook("Details.xlsx")
worksheet= workbook.add_worksheet()

worksheet.write('A1','First name')
worksheet.write('B1','Last name')
worksheet.write('C1','Date of Birth')
worksheet.write('D1','City')

for i in range(1,10):
	print("Add first name of person:",i)
	worksheet.write('A'+str(i),input())
	print("Add last name of person:",i)
	worksheet.write('B'+str(i),input())
	print("Add date of birth of person in the format dd/mm/yyyy:",i)
	worksheet.write('C'+str(i),input())
	print("Add city of person:",i)
	worksheet.write('D'+str(i),input())

workbook.close()
