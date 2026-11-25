# EMPLOYEE PAYROLL SYSTEM
 
# Initial Values
name = ""
basic = 0
hra = 0
allowance = 0
gross = 0
tax = 0
 
details_entered = False
gross_calculated = False
tax_calculated = False
 
 
# Function 1: Enter Employee Details
def enterEmployeeDetails():
 
    name = input("Employee Name: ")
    basic = float(input("Basic Salary: "))
    hra = float(input("HRA: "))
    allowance = float(input("Other Allowance: "))
 
    return name, basic, hra, allowance
 
 
# Function 2: Calculate Gross Salary
def calculateGrossSalary(basic, hra, allowance):
 
    gross = basic + hra + allowance
 
    return gross
 
 
# Function 3: Calculate Tax
def calculateTax(grossSalary):
 
    annualSalary = grossSalary * 12
    taxableIncome = max(0, annualSalary - 75000)
 
    tax = 0
 
    # New Tax Regime - FY 2026-27
 
    if taxableIncome <= 1200000:
        tax = 0
 
    elif taxableIncome <= 1600000:
        tax = (taxableIncome - 1200000) * 0.15
 
    elif taxableIncome <= 2000000:
        tax = 60000 + (taxableIncome - 1600000) * 0.20
 
    elif taxableIncome <= 2400000:
        tax = 140000 + (taxableIncome - 2000000) * 0.25
 
    else:
        tax = 240000 + (taxableIncome - 2400000) * 0.30
 
    # Health and Education Cess
    tax = tax + (tax * 0.04)
 
    return tax / 12
 
 
# Function 4: Display Salary Slip
def displaySalarySlip(name, basic, hra, allowance, gross, tax):
 
    netSalary = gross - tax
 
    print("\n========== SALARY SLIP ==========")
    print("Employee Name:", name)
    print("Basic Salary:", basic)
    print("HRA:", hra)
    print("Other Allowance:", allowance)
    print("---------------------------------")
    print("Gross Salary:", gross)
    print("Tax:", round(tax, 2))
    print("Net Salary:", round(netSalary, 2))
    print("=================================")
 
 
# Main Menu
while True:
 
    print("\n===== EMPLOYEE PAYROLL SYSTEM =====")
    print("1. Enter Employee Details")
    print("2. Calculate Gross Salary")
    print("3. Calculate Tax")
    print("4. Display Salary Slip")
    print("5. Exit")
 
    choice = int(input("Enter your choice: "))
 
    if choice == 1:
 
        name, basic, hra, allowance = enterEmployeeDetails()
 
        details_entered = True
        gross_calculated = False
        tax_calculated = False
 
    elif choice == 2:
 
        if details_entered == True:
 
            gross = calculateGrossSalary(basic, hra, allowance)
 
            gross_calculated = True
            tax_calculated = False
 
            print("Gross Salary:", gross)
 
        else:
            print("Please enter employee details first!")
 
    elif choice == 3:
 
        if gross_calculated == True:
 
            tax = calculateTax(gross)
 
            tax_calculated = True
 
            print("Monthly Tax:", round(tax, 2))
 
        else:
            print("Please calculate gross salary first!")
 
    elif choice == 4:
 
        if tax_calculated == True:
 
            displaySalarySlip(name, basic, hra, allowance, gross, tax)
 
        else:
            print("Please complete the previous calculations first!")
 
    elif choice == 5:
 
        print("Thank you for using Employee Payroll System!")
        break
 
    else:
 
        print("Invalid choice! Please select between 1 and 5.")