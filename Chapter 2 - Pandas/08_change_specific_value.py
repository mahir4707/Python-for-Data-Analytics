#changing specific value in our data
#function used df.loc[row_index, "column_name"] = new_value

import pandas as pd

df = pd.read_excel("output.xlsx")
print(df)

print("changing salary of row index 4:")
df.loc[4, "Salary"] = 72000
print(df)

