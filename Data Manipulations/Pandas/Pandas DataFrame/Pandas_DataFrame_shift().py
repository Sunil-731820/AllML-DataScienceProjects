import  pandas as pd
import numpy as np

info = pd.DataFrame(
    {
        "a_data":[45,28,39,32,18],
        "b_data":[22,19,11,25,16],
        "c_data":[22,19,11,25,16]
    }
)
print("The given Info is ")
print(info)
print("After The Use Of The shift()")
print(info.shift(periods=2, fill_value=0,axis=1))
