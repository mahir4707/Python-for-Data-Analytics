#using info and describe function in pandas library

import pandas as pd

df = pd.read_csv("output.csv")
print("Our Data:")
print(df)


#info function
print("\nInformation of Our Data:")
print(df.info())

#describe function - used to find statistical info of data 
print("\nStatistical Data of our DataFrame:")
print(df.describe())
