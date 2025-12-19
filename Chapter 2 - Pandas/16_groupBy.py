import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Kunal", "Sneha"],
    "Age": [28, 32, 28, 29, 29, 27],
    "Salary": [45000, 60000, 38000, 52000, 75000, 42000],
    "Department": ["IT", "HR", "IT", "Finance", "Marketing", "IT"]
})

print(df)

print("Group by on age and salary")
grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)