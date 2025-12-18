#To filter the row and column with specific condition
import pandas as pd

df = pd.read_csv("output.csv")
print("Our Data:")
print(df)

#with one condition
#employee name with salary > 50k
print("Employee with >50k salary")
high_salary = df[df['Salary'] > 50000]
print(high_salary)

#multiple condition
#Employee name with salary > 50k and department is marketing
print("\nEmployee with salary >50k and department Marketing")
result = df[(df['Salary']>50000) & (df['Department'] == 'Marketing')]
print(result)