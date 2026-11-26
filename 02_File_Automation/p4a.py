from pathlib import Path
import os
class Student:
    def __init__(self, name, id, age, course, phone):
        self.name = name
        self.id = id
        self.age = age
        self.course = course
        self.phone = phone
    def register_student(self):
        file = Path("students.txt")
        if not file.exists():
            file.touch()
        with open(file, "a") as f:
            f.write(f"{self.name},{self.id},{self.age},{self.course},{self.phone}\n")
    def list_students():
        file = Path("students.txt")
        if file.exists():
            with open(file, "r") as f:
                for line in f:
                    print(line.strip())
        else:
            print("No students found.")
while True:
    print("1. Register Student")
    print("2. List Students")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        id = input("Enter ID: ")
        age = input("Enter age: ")
        course = input("Enter course: ")
        phone = input("Enter phone: ")
        student = Student(name, id, age, course, phone)
        student.register_student()
    elif choice == "2":
        Student.list_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")