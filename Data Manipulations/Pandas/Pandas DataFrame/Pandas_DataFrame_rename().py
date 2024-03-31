import  pandas as pd
import numpy as np

info = {
    "name":["perker","Smith","William","Robert"],
    "Age":[23,34,45,56],
    "Language":["Java","Python","C++","C#"]
}
print("The Info is ")
print(info)
info_df = pd.DataFrame(info)
print("The data Frame is ")
print(info_df)
print("After The Use Of The rename()")
print(info_df.rename(columns={"name":"Name"},inplace=True))
print(info_df.columns)
