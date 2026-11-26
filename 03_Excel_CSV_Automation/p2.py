import csv 

data = [
    ["EmployeeID","Name","Salary"],
    [101,"John",25000],
    [102,"Amy",35000]
]

with open("output.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)