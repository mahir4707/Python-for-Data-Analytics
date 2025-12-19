#we have to find the missing values in our data to maintain its consistency
#function used df.isnull()

import pandas as pd

df = pd.DataFrame ({
    "Name": ['Mahir', 'Rahul', 'Krish', 'Deep'],
    "Roll_no": [58, 38, None, 32],
    "department": ["CE", None, "EC", "IT"]
})

print(df)

#to count the no. of None values in our data in each column 
print("Number of None values in our data:")
print(df.isnull().sum())