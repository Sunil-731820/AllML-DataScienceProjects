import  pandas as pd
import numpy as np

info = pd.DataFrame(
    {
        "P":[8,2,None,3],
        "Q":[4,14,12,None],
        "R":[2,4,6,7],
        "S":[12,23,None,23]
    }
)
print("The Info is ")
print(info)
index = ["A_row","B_row","C_row","D_row"]
info.index = index
print("The Data Frame After Setting The Index is ")
print(info)