import pandas as pd

df1 = pd.DataFrame({
    "EmpID": [101, 102, 103, 104],
    "Name": ["Amit", "Neha", "Rahul", "Priya"],
    "Department": ["IT", "HR", "Finance", "IT"]
})

df2 = pd.DataFrame({
    "EmpID": [103, 104, 105, 106],
    "Salary": [55000, 62000, 48000, 70000],
    "Location": ["Ahmedabad", "Delhi", "Mumbai", "Pune"]
})

# function used - pd.merge(df1, df2, on="key", how=type of join)
df_merged1 = pd.merge(df1, df2, on="EmpID", how="inner")
print("Inner join:")
print(df_merged1)

#right join
df_merged2 = pd.merge(df1, df2, on="EmpID", how="right")
print("Right join:")
print(df_merged2)

#left join
df_merged3 = pd.merge(df1, df2, on="EmpID", how="left")
print("Left Join:")
print(df_merged3)

#outer join
df_merged4 = pd.merge(df1, df2, on="EmpID", how="outer")
print("Outer Join:")
print(df_merged4)


