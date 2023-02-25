import  numpy as np
import pandas as pd

info = pd.DataFrame(
    {
        "Weight":[23,34,56,78],
        "Name":["William","John","Smith","Parker"],
        "Age":[23,32,12,21]
    }
)
print("The Info is ")
print(info)
index_ = pd.date_range("2023-02-26 12:13",periods=4,freq="H")
info.index = index_
print("The Info is ")
print(info)
print("After transpose of The Data Frame is ")
result = info.transpose()
print(result)
