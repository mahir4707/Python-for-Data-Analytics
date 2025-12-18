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

# write into diff files
df.to_csv("output.csv")
df.to_excel("output.xlsx")
df.to_json("output.json")

#read diff types of files
print(pd.read_csv("output.csv", encoding="utf-8"))
print(pd.read_excel("output.xlsx"))
print(pd.read_json("output.json"))
