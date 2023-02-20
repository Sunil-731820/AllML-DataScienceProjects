import pandas as pd
import numpy as np

# Assign Is USed to add New Column To The Data Frame
info = pd.DataFrame()
print("The First Data Frame is ")
print(info)
info['ID'] = [101,102,103]
print("The Id Data Frame Is ")
print(info)
info["Name"] = ["Sunil","Kumar","gupta"]
print("The New info is ")
print(info)

info.assign(Age=[20,21,23])
print("After The use Of THE Assign Functions")
print(info)
x = pd.Series([1,2],dtype='int64',index=["firstNumber",'SecondNumber'])
print("The Series is x")
print(x)


