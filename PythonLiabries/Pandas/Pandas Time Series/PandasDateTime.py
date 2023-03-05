
import pandas as pd
import numpy as np

info = pd.DataFrame({
    "year":[2014,2012],
    "month":[5,7],
    "day":[20,27]
})
print("Yje Info is ")
print(info)
print("After The USe Of The date time() in pandas")
print(pd.to_datetime(info))
