class Employee:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def display_salary(self):
        print(10000)

class FullTimeEmployee(Employee):
    def __init__(self,id,name,age):
        super().__init__(id,name,age)
    def display_salary(self):
        print(12000)

class Contractor(Employee):
    def __init__(self,id,name,age):
        super().__init__(id,name,age)


e1 = FullTimeEmployee("E001","John",23)
e1.display_salary()

e2 = Contractor("E002","Amy",25)
e2.display_salary()