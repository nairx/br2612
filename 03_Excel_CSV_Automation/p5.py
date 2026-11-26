import csv 
import json 

json_data = '''
[
{"id":101,"name":"John","Salary":25000},
{"id":102,"name":"Amy","Salary":20000},
{"id":103,"name":"Mike","Salary":45000}
]
'''
data = json.loads(json_data)
with open("empdata.csv","w",newline="") as file:
    writer = csv.DictWriter(file,fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)