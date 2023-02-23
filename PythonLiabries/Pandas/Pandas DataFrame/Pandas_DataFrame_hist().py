import pandas as pd
import numpy as np

info = pd.DataFrame({
    'length':[2,1.7,3.6,2.4,1],
    "width":[4.2,2.6,1.6,5.1,2.9]
})
print("The Info Data is ")
print(info)
print("The Histogram Data is ")
hist = info.hist(bins=4)
print(hist)



