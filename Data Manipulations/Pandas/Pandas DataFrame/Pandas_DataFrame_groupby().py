import pandas as pd
import numpy as np

data = {
    "Name":["Parker","Smith","John","William"],
    "Percentage":[82,98,91,87],
    "Courses":["BSC","MSC","BA","Btech"]
}
print("The Data is ")
print(data)
df = pd.DataFrame(data)
print("The Data Frame is ")
print(df)
grouped = df.groupby('Courses')
print("After The USe of The group By()")
print(grouped['Percentage'].agg(np.mean))

