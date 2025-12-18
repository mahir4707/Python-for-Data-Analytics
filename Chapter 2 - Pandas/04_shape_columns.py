#Use of shape and column function
import pandas as pd

df = pd.read_excel("output.xlsx")
print("Our Data:")
print(df)

#shape function - find number of rows and columns of data
print(f"\nShape: {df.shape}") #shape(rows, columns)

#columns function - for finding names of column in data
print(f"Column: {df.columns}")
