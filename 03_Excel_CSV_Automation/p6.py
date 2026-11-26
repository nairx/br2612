from openpyxl import Workbook 

workbook = Workbook() 

sheet = workbook.active

sheet.title = "Employees"

sheet.append(["ID","Name","Department","Salary"])

sheet.append([101,"John","IT",25000])
sheet.append([102,"Amy","IT",20000])
sheet.append([103,"Mike","IT",45000])

workbook.save("employees.xlsx")