#Automatically Organize Files
# Arrange the files in downloads directory
import os
from pathlib import Path
 
downloads_dir = Path("Downloads")
downloads_dir.mkdir(exist_ok=True)
 
file = downloads_dir / "employees.txt"
file.touch(exist_ok=True)
 
file2=downloads_dir / "departments.txt"
file2.touch(exist_ok=True)
 
file3 = downloads_dir / "photo.png"
file3.touch(exist_ok=True)
 
file4 = downloads_dir / "resume.pdf"
file4.touch(exist_ok=True)
 
file5 = downloads_dir / "notes.xlsx"
file5.touch(exist_ok=True)
 
file6 = downloads_dir / "presentation.pptx"
file6.touch(exist_ok=True)
 
file7 = downloads_dir / "script.py"
file7.touch(exist_ok=True)
 
file8 = downloads_dir / "data.csv"
file8.touch(exist_ok=True)
 
file9 = downloads_dir / "archive.zip"
file9.touch(exist_ok=True)
 
file10 = downloads_dir / "video.mp4"
file10.touch(exist_ok=True)
 
 
from pathlib import Path
import shutil
folder = Path("./Downloads")
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".docx", ".pptx", ".zip"],
    "Excel": [".xlsx", ".xls", ".csv"],
    "Videos": [".mp4", ".avi", ".mov"],
    "programming": [".py", ".js"]
}

for category, extensions in categories.items():
    target_folder = folder / category
    target_folder.mkdir(exist_ok=True)
    for file in folder.iterdir():
        if file.is_file() and file.suffix.lower() in extensions:
            shutil.move(
                str(file),
                str(target_folder / file.name)
            )
print("Files organized successfully!")