import pandas as pd
import numpy as np

emp = {
    "Name":["Sunil","Harish","Arti","Sunil"],
    "Age":[21,32,29,21]
}
print("The Employ is ")
print(emp)
info = pd.DataFrame(emp)
print("The Data Frame is ")
print(info)
print("After The use Of The drop_duplicate()")
info = info.drop_duplicates()
print(info)

