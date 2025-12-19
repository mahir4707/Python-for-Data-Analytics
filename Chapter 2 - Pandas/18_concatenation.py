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

df_concat = pd.concat([df1, df2], axis=1, ignore_index=True)
print(df_concat)
