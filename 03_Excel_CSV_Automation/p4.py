import csv 

data = {
    "EmployeeID":101,
    "Name":"John",
    "Department":"IT",
    "Salary":35000,
}

with open("emp.csv","w",newline="") as file:
    writer = csv.DictWriter(file,fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)