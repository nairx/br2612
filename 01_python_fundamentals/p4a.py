#Employee Salary Calcultor
employee_name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
basic_salary = int(input("Enter basic salary: "))
hra = int(input("Enter HRA: "))
da = int(input("Enter DA: "))

print("Employee Name: " + employee_name,)
print("Employee ID: " + employee_id)
print("Basic Salary: " + str(basic_salary))
print("HRA: " + str(hra))
print("DA: " + str(da)) 
gross_salary = basic_salary + hra + da              
print("Gross Salary: " + str(gross_salary)) 
anual_salary = gross_salary * 12
print("Anual Salary: " + str(anual_salary))