import pandas as pd

df = pd.read_json("output.json")
print("Our Data:")
print(df)

#specific column
print("\nOnly printing Name column")
print(df['Name'])

#multiple column
print("\nPrinting Name and Age of an Employee")
print(df[['Name', 'Age']])
