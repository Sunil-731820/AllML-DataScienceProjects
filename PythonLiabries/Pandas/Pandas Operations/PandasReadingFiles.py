import pandas as pd
import numpy as np

df = pd.read_csv("covid_worldwide.csv")
print("The CsV Data is ")
print(df)

# Reading The Json Data from The Json File is
json_dataFrame = pd.read_json("iris.json")
print("The Json Data is ")
print(json_dataFrame)
