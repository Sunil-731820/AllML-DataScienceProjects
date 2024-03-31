import  pandas as pd
import  numpy as np
data = pd.read_csv("organizations-100.csv")
print('The CSV file is ')
print(data)
for i, j in data.iterrows():
    print(i,j)
    print()

