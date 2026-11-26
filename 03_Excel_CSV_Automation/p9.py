from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment 

workbook = Workbook() 
sheet = workbook.active 
sheet.title = "Employee Report"
headers = ["ID","Name","Department","Salary"]
sheet.append(headers)
sheet.append([101,"John","IT",45000])
sheet.append([102,"Amy","Admin",15000])

for cell in sheet[1]:
    cell.font = Font(bold=True,color="FFFFFF"),
    cell.fill = PatternFill(start_color="4472C4",fill_type="solid" )
    cell.alignment = Alignment(horizontal="center")

for cell in sheet["D"][1:]:
    cell.number_format = '₹#,##0,00'

sheet.column_dimensions["A"].width = 12 
sheet.column_dimensions["B"].width = 20
sheet.column_dimensions["C"].width = 20
sheet.column_dimensions["D"].width = 15

workbook.save("formatted_report.xlsx")