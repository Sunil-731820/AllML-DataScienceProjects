'''
Pandas treat None and NaN as essentially interchangeable for indicating missing or null values. To facilitate this convention, there are several useful functions for detecting, removing, and replacing null values in Pandas DataFrame :

isnull()
notnull()
dropna()
fillna()
replace()
interpolate()
'''

# Step 1 :  Checking for missing values using isnull() and notnull()
import pandas as pd
import numpy as np

df = pd.read_csv("employees.csv")
print("The Data Frame is : ")
print(df)
print("The top 5 ROws is : ")
print(df.head())
