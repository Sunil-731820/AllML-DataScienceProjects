import numpy as np
import  pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.metrics import mean_squared_error
# 1 : First Step is To Read THe Data from the CSV FIle

df = pd.read_csv("ds_salaries.csv")
print("The Data Frame is ")
print(df)
print("The Top 10 Rows of The Data From The DataFrame is ")
print(df.head(10))

print("The info Of The Data is ")
print(df.info())

# Taking the Samples from The Data Frame is
print("The 5 Samples from The Above dataframe is  ")
print(df.sample(5))

# Getting The Shape Of The Data Frame is
print("The Shape Of The Data Frame is ")
print(df.shape)

# Describing The DataFrame
print(df.describe())

# Checking The Null values from The DataSets is
print("After Checking The Null values is ")
print(df.isnull().sum())

# Getting The Data type of The Data Sets is
print(df.dtypes)

# Now printing The Existing  Column Name Only from The Data Frame is
print("The Existing COlumn Names is ")
for col in df.columns:
    print(col)

# printing The Values With Column Name
print("After printing The values Count With Column Names is ")
for col in df.columns:
    print(col)
    print("++++++++++++++")
    print(df[col].value_counts())

# Now plotting The Work Experinces In Graph

sns.di