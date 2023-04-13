import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
# What is churn prediction? Churn prediction is predicting which customers are at high risk
# of leaving your company or canceling a subscription to a service, based on their behavior with your
# product.

# 1 : Reading The Data by using the pandas DataFrame

df = pd.read_csv("Churn_Modelling.csv")
print("The Data frame is ")
print(df)

#  2 : printing the Top 10 values
print("The Top 10 values is ")
print(df.head(10))

# 3 : Printing the tail 10 Values
print("The last 10 values is ")
print(df.tail(10))

# 4 : Checking the Null Values
print(df.isnull().sum())

# Checking The Shape of The data Frame is
print(df.shape)

# Dropping The Duplicate values
print(df.drop_duplicates(inplace=True))

x=df.drop('Exited',axis=1)
y=df.Exited
print("The x values is ")
print(x)
print("The y values is ")
print(y)

# Scalling The Data Sets

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
# x_features = ss.fit_transform(x)
print("The X features is ")







