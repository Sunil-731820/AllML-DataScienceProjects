import pandas as pd
import numpy as np

info = pd.DataFrame(
    {
        "Key":["K0","K1","K2","K3","K4","K5"],
        "A":["A0","A1","A2","A3","A4","A5"],
    }
)
print("The First Data Frame is ")
print(info)

second_Data = pd.DataFrame(
    {
        'key':["K0","K1","K2"],
        "B":["B0","B1","B2"]
    }
)
print("The Second Data Frame is ")
print(second_Data)

# info.join(x,lsuffix='_caller',rsuffix='_x')
