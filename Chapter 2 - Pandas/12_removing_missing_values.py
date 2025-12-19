# When we find missing values in our data, we need to handle them.
# Handling missing values includes either removing them or filling them with specific values.

import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Rahul", "Priya", None, "Kunal"],
    "Age": [28, None, 26, 29, 31, None],
    "Salary": [45000, 60000, None, 52000, 58000, None],
    "Department": ["IT", "HR", None, "Finance", "Operations", "IT"]
})

print(df)

# Handling missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].min())
df["Department"] = df["Department"].fillna(method="ffill")

print(df)
