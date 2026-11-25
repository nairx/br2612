import os 
# print(os.getcwd())
# items = os.listdir(".")
# items = os.listdir("D:/console_apps")
# print(items)
# for item in items:
#     print(item)

# os.mkdir("reports")

# os.makedirs("reports/2026/11")

# if os.path.exists("reports"):
#     print("File/Folder Exists")

# if os.path.isfile("reports"):
#     print("Yes")
# else:
#     print("No")

# if os.path.isdir("reports"):
#     print("Yes")
# else:
#     print("No")

# file = open("students.txt","w")
# file.write("John\n")
# file.write("Amy\n")
# file.write("Cathy\n")
# file.close()

# with open("students.txt","w") as file:
#     file.write("Mike\n")
#     file.write("Amy\n")
#     file.write("Cathy\n")

# with open("students.txt","a") as file:
#     file.write("Chastity\n")

# with open("students.txt","r") as file:
#     data = file.read()
#     print(data)

# with open("students.txt","r") as file:
#     for line in file:
#         print(line)

# os.rename("students.txt","students_backup.txt")

os.remove("students_backup.txt")