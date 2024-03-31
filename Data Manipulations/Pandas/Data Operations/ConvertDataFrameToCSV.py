import  numpy as np
import pandas as pd

data = {
    "Name":["Smith","parker"],
    "Id":[101,pd.NaT],
    "Language":[pd.NaT,"JS"]
}
print("The Data is ")
print(data)

dataFrame = pd.DataFrame(data)
print("The data Fame is ")
print(dataFrame)
csv_data = dataFrame.to_csv()
print("The CSv file is ")
print(csv_data)