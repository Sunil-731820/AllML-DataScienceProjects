import numpy as np
import pandas as pd

# 1 : Reading The Data using pandas
df = pd.read_csv("TitanicTrainData.csv")
print("The dataFrame is ")
print(df)

# 2 : Getting The description of The data Sets
print(df.describe())

# 3 : getting The Top 10 Rows of The Data Set is
print("'The top 10 Rows of The Data is ")
print(df.head(10))

# 4 : getting The Last 10 Rows of The Data Set is
print("The last 10 Rows of The data is ")
print(df.tail(10))



