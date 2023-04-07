import numpy as np
import  pandas as pd

# Reading The dataSets Using pandas Lib
df = pd.read_csv("linear-regression-dataset.csv")
print("The data Set is ")
print(df)

# Showing The Top 5 data set is
print(df.head(5))

# Showing The last 5 data set is
print(df.tail(5))
