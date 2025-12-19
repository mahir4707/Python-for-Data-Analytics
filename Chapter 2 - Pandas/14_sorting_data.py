#Sorting our data to ascending or descending
# function used - df.sort_values(by="column_name", ascending=True/false, inplace=true)

import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Kunal", "Sneha"],
    "Age": [28, 32, 26, 29, 35, 27],
    "Salary": [45000, 60000, 38000, 52000, 75000, 42000],
    "Department": ["IT", "HR", "IT", "Finance", "Marketing", "IT"]
})

print("Before Sorting:")
print(df)

df.sort_values(by=["Salary", "Age"], ascending=[True, False], inplace=True)
print("After Sorting:")
print(df)