from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Employees"
employees = [
    ["EmployeeName", "EmployeeID", "Company"],
    ["Dharma", "E001", "Broadridge"],
    ["John", "E002", "Broadridge"],
    ["Alice", "E003", "ABC"]
]
for employee in employees:
    ws.append(employee)
wb.save('./03_Excel_CSV_Automation/employee_excel.xlsx')
employees_attendance = [
    ["EmployeeName", "EmployeeID", "Date", "Status"],
    ["Dharma", "E001", "2024-06-01", "Present"],
    ["John", "E002", "2024-06-01", "Absent"],
    ["Alice", "E003", "2024-06-01", "Present"],
    ["Dharma", "E001", "2024-06-02", "Absent"],
    ["John", "E002", "2024-06-02", "Absent"],
    ["Alice", "E003", "2024-06-02", "Present"]
]
ws = wb.create_sheet(title="Attendance")
for attendance in employees_attendance:
    ws.append(attendance)
wb.save('employee_excel.xlsx')