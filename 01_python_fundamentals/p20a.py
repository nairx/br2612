def enterEmployeeDetails(emp_name,basic_salary,HRA,other_allowance):
    print(f"Employee name is {emp_name}")
    print(f"Employee basic salary is {basic_salary}")
    print(f"Employee HRA is {HRA}")
    print(f"Employee other allowance is {other_allowance}")

def calculateGrossSalary(basic_salary,HRA,other_allowance):
    salary = basic_salary+HRA+other_allowance
    #print(f"Gross salary is {salary}")
    return salary

def calculateTax():
    salary = calculateGrossSalary(basic_salary,HRA,other_allowance)
    if salary < 1200000 :
        print ("zero tax")
        return 0
    elif salary > 1200001 and salary < 1600000:
        tax = salary * 0.15
        print(f"you tax is 15 % and its value {tax}")
        return tax
    elif salary > 1600001 and salary < 2000000:
        tax = salary * 0.2
        print(f"you tax is 20 % and its value {tax}")
        return tax
    elif salary > 2000001 and salary < 2400000:
        tax = salary * 0.25
        print(f"you tax is 25 % and its value {tax}")
        return tax
    elif salary > 2400001:
        tax = salary * 0.3
        print(f"you tax is 30 % and its value {tax}")
        return tax


def displaySalarySlip():
    print("========== SALARY SLIP ==========")
    enterEmployeeDetails(emp_name,basic_salary,HRA,other_allowance)
    print("====================")
    gross_salary = calculateGrossSalary(basic_salary,HRA,other_allowance)
    print(f"Gross salary is : {gross_salary}")
    tax = calculateTax()
    print(f"Tax is : {tax}")
    #net_salary = calculateGrossSalary(basic_salary,HRA,other_allowance) - calculateTax()
    net_salary = gross_salary - tax
    print(f"Net salary : {net_salary}")


emp_name = input("please enter name : ")
basic_salary = int(input("please enter basic salary : "))
HRA = int(input("please enter HRA : "))
other_allowance = int(input("please enter other allowance : "))

print(f"===== EMPLOYEE PAYROLL SYSTEM =====", "\n", "1. Enter Employee Details","\n","2. Calculate Gross Salary","\n","3. Calculate Tax","\n","4. Display Salary Slip","\n","5. Exit")

#print(details)
choice = int(input("please enter value from 1 to 5 : "))
while choice < 7:
    match choice:
        case 1:
            enterEmployeeDetails(emp_name,basic_salary,HRA,other_allowance)
            choice = int(input("please enter value from 1 to 5 : "))
            continue
        case 2:
            grossSalary = calculateGrossSalary(basic_salary,HRA,other_allowance)
            print(f"Gross salary is {grossSalary}")
            choice = int(input("please enter value from 1 to 5 : "))
            continue
        case 3:
            calculateTax()
            choice = int(input("please enter value from 1 to 5 : "))
            continue
        case 4:
            displaySalarySlip()
            choice = int(input("please enter value from 1 to 5 : "))
            continue
        case 5:
            print("Exit")
            break
        case _:
             print("Invalid choice")
             break

 