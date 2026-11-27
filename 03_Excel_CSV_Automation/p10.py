import pandas as pd
data = {
    "Name":["John","Cathy","Amy","Mike","Dan"],
    "Department":["IT","HR","Finance","IT","IT"],
    "Salary":[50000,45000,60000,55000,90000]
}
df = pd.DataFrame(data)
df = df[df["Department"]=="IT"]
df = df[df["Salary"]>50000]
df = df.sort_values(by="Salary",ascending=False)
df.to_excel("IT_Employees.xlsx",index=False)