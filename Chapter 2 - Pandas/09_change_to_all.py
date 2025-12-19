#changing the value for all entries in our data
#function used df["column_name"] = df["column_name"](change)

import pandas as pd

df = pd.DataFrame({
    "Name": [
        "Amit Sharma", "Neha Patel", "Rahul Verma", "Priya Singh", "Kunal Mehta",
        "Anjali Desai", "Rohit Gupta", "Sneha Iyer", "Vikas Malhotra", "Pooja Nair",
        "Arjun Rao", "Kavita Joshi", "Suresh Kumar", "Meenal Shah", "Aditya Jain"
    ],
    "Age": [
        28, 32, 26, 29, 35,
        31, 27, 34, 38, 25,
        33, 30, 41, 28, 36
    ],
    "Salary": [
        45000, 60000, 38000, 52000, 75000,
        58000, 42000, 68000, 82000, 36000,
        70000, 55000, 90000, 48000, 78000
    ],
    "Department": [
        "IT", "HR", "IT", "Finance", "Marketing",
        "Operations", "IT", "Finance", "Management", "HR",
        "Operations", "Marketing", "Management", "Finance", "IT"
    ]
})

print(df)

#increasing salary of all employee by 10%
print("salary increased by 10% for all employees:")
df["Salary"] = df["Salary"] * 1.1
print(df)
