class Employee:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def display_info(self):
        print(self.name,self.age)

class FullTimeEmployee(Employee):
    def __init__(self,id,name,age,basic_salary):
        super().__init__(id,name,age)
        self.basic_salary = basic_salary
    def display_Salary(self):
        print(self.basic_salary)

class Contractor(Employee):
    def __init__(self,id,name,age,fees):
        super().__init__(id,name,age)
        self.fees = fees
    def display_fees(self):
        print(self.fees)

e1 = FullTimeEmployee("E001","John",23,10000)
e1.display_Salary()

e2 = Contractor("E002","Amy",25,5000)
e2.display_fees()