import pandas as pd 
df = pd.read_csv("software_licenses.csv")
df["Available Licenses"] = (df["Purchased Licenses"] - df["Used Licenses"])
df["Total Purchase Cost"] = (df["Purchased Licenses"] * df["Cost Per License"])
df["Utilization %"] = (df["Used Licenses"]/df["Purchased Licenses"] * 100)
df = df.sort_values(by="Total Purchase Cost",ascending=False)

department_summary = df.groupby("Department").agg(
    {
        "Purchased Licenses":"sum",
        "Used Licenses":"sum",
        "Available Licenses":"sum",
        "Total Purchase Cost":"sum"
    }
).reset_index()
# print(df)

department_summary["Utilization %"] = (department_summary["Used Licenses"] / department_summary["Purchased Licenses"] * 100)
# print(department_summary)

with pd.ExcelWriter("Software_License_Report.xlsx",engine="openpyxl") as writer:
    df.to_excel(writer,sheet_name="License Details",index=False)
    department_summary.to_excel(writer,sheet_name="Department Summary",index=False)



