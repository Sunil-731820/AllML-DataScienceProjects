import numpy as np
import pandas as pd

a = pd.Series(range(5))
print("After The USe Of where")
print(a.where(a>0))
print("getting Whole values Which is Less Than 4")
print(a.where(a<4))
