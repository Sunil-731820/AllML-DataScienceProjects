import  numpy as np
import  pandas as pd
readingCsvData = pd.read_csv("Cleaned-Data.csv")
print("The Data is ")
print(readingCsvData)
print("The Data Size of The Given data Sets is ")
print(readingCsvData.dtypes)
print("printing the Specific COlumn From The Given Data Sets is ")
print(readingCsvData["Country"])
