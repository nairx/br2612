import csv 

data = [
    [103,"Brian",25000],
    [104,"Shawn",35000]
]

with open("output.csv","a",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)