import pandas as pd
import  numpy as np

data = {
    "Name":["Smith","Perker"],
    "Id":[101,102],
    "Labguage":["hindi","English"]
}
print("The Data is ")
print(data)

print("Converting this Data To DataFrame is ")
info = pd.DataFrame(data)
print("The Data Frame is ")
print(info)

print("Converting This data Frame to CSv file ")
csv_Data = info.to_csv()
print("The CSv Data is ")
print(csv_Data)
