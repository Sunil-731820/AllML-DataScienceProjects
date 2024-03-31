import  pandas as pd
import numpy as np

info = pd.DataFrame(
    {
        "A":[8,2,7,12,6],
        "B":[26,19,7,5,9],
        "C":[10,11,15,4,3],
        "D":[16,24,14,22,1]
    }
)
print("The info is ")
print(info)
print("The Mean of The Given DataFrame is ")
print(info.mean(axis=0))

print("Finding The Mean of The All Given data When Axis =1")
print(info.mean(axis=1,skipna=True))



