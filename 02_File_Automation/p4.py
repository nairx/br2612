# from glob import glob
# files = glob("*.py")
# print(files)

# from glob import glob
# files = glob("01_python_fundamentals/*.py")
# # print(files)
# for file in files:
#     print(file)

# from glob import glob
# from pathlib import Path
# folder = Path(".")
# for file in folder.rglob("*.py"):
#     print(file)

from pathlib import Path 
# file = Path("students.txt")
file = Path("backup/reports.txt")
print(file.name)
print(file.suffix)
print(file.stem)
print(file.parent)


