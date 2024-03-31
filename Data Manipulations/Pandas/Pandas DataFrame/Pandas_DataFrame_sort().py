import  pandas as pd
import numpy as np

info = pd.DataFrame(
    np.random.randn(10,2),index=[1,4,7,2,5,3,0,8,9,6],columns=["Col4","Col5"]
)
print("The Info is ") 
print("Before The Use Of The Sort_index")
print(info)
info2 = info.sort_index(ascending=False)
print("After The Use of The Sort_index")
print(info2)
