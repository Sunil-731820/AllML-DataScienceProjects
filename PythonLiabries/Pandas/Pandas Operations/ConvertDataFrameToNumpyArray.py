import pandas as pd
import  numpy as np

df = pd.DataFrame({
    "P":[2,3],
    "Q":[4,5],
    "R":[1,2]
})
print("THe Data Frame is ")
print(df)
print("After Converting The Dtaa Frame to Numpy Array is ")
print(df.to_numpy())
