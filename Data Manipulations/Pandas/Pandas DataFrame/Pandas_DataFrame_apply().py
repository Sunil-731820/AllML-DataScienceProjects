import pandas as pd
import numpy as np
info = pd.DataFrame([[2,7]]*4,columns=["firstColumn ","secondColumn"])
print("The First Data Frame Is ")
print(info)

# Now I Am Going To Apply The Square root Method To get The Data
print("After The Use Of The Apply method In Pandas")
print(info.apply(np.sqrt))
print("The Sum of The Column is Is Using Sum()")
print(info.apply(np.sum))

print("Again The Sum of The Column Wise Number is ")
print(info.apply(np.sum))







