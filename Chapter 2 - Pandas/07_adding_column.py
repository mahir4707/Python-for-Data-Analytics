#adding column to our data 
import pandas as pd

df = pd.read_json("output.json")
print(df)

#adding bonus column - this is usually not used as it created column at last of our data
# print("New Bonus column added to our data:")
# df["Bonus"] = df["Salary"] * 0.1
# print(df)

#using insert function - df.insert(location, "column_name", some_data)
print("inserting employee id column using insert function:")
df.insert(0, "Employee_Id", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(df)