from pathlib import Path 

# path = Path("students.txt")
# print(path.exists())
# print(path.is_file())

# folder = Path("backup")
# folder.mkdir(exist_ok=True)

# file = Path("backup/reports.txt")
# # file.write_text("Sales Report")

# data = file.read_text()
# print(data)


file = Path("backup/reports1.txt")
with file.open(mode='a',encoding="utf-8") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")