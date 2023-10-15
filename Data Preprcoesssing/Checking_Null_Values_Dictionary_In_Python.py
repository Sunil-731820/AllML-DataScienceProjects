# importing pandas as pd
import pandas as pd

# importing numpy as np
import numpy as np

# dictionary of lists
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
print("The Dict is : ")
print(dict)
# creating a dataframe from list
df = pd.DataFrame(dict)
print("The Data Frame Will be ")
print(df)
# using isnull() function
print(df.isnull())
print("After The Use Of The isnull method is: ")
print(df)
