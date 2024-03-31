import  pandas as pd
import numpy as np

info = {
    "Name":["Perker","Smith","William"],
    "Age":[32,28,39]
}
print("The Info is ")
print(info)
data = pd.DataFrame(info)
print("The Data Frame is ")
print(data)
# the Sum of The All Age Stored in Data Frame is
data["total"] = data["Age"].sum()
print("The Sum Of The All The Age is ")
print(data)