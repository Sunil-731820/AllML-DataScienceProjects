import pandas as pd
import numpy as np

info = pd.DataFrame(
    {
        "data1":[2,4,6,8],
        "data2":[2,0,0,0],
        "data3":[10,2,1,8]
    }
)
print("The Info is ")
print(info)
df = pd.DataFrame(info)
print("The data Frame is ")
print(df)
index = ["John","Parker","Smith","William"]
print(info)
print(info["data1"].sample(n=3,random_state=1))

