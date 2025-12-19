#finding summary of our data
import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Kunal", "Sneha"],
    "Age": [28, 32, 26, 29, 35, 27],
    "Salary": [45000, 60000, 38000, 52000, 75000, 42000],
    "Department": ["IT", "HR", "IT", "Finance", "Marketing", "IT"]
})

print(df)

#finding avg of salary
print("Average salary from our data:")
avg_salary = df['Salary'].mean()
print(avg_salary)
