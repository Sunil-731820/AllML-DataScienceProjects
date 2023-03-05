import  pandas as pd
import  numpy as np

first_data = pd.Series(["P","Q"])
second_Data = pd.Series(["R","S"])
print("The First data series is ")
print(first_data)
print("The Second data Series is ")
print(second_Data)

print("After Concateing The Data is ")
concated_data = pd.concat([first_data,second_Data],ignore_index=True)
print("The Data is ")
print(concated_data)
