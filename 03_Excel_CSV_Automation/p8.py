from openpyxl import Workbook 

workbook = Workbook() 

sheet1 = workbook.active
sheet1.title = "Employees"
sheet2 = workbook.create_sheet("Sales")
sheet3 = workbook.create_sheet("Expenses")

sheet1.append(["ID","Name","Department","Salary"])
sheet1.append([101,"John","IT",25000])
sheet1.append([102,"Amy","IT",20000])
sheet1.append([103,"Mike","IT",45000])

sheet2.append(["Product","Sales"])
sheet2.append(["Laptop",25000])
sheet2.append(["Desktop",20000])

sheet3.append(["Categoy","Amount"])
sheet3.append(["Travel",25000])
sheet3.append(["Rent",27000])

workbook.save("company_data.xlsx")