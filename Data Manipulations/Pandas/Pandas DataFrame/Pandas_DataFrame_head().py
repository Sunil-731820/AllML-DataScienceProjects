import  pandas as pd
import numpy as np
data = {
    "Language":["C","C++","Java","Python","PHP"]
}
df = pd.DataFrame(data)
print("The Given Data Frame is ")
print(df)
print("the First Three Head Object is ")
print(df.head(3))

# Now I am going To Read The CSV files

data1 = pd.read_csv("organizations-100.csv")
print("The Data of The CSv File is ")
print(data1)

print("The Top 10 records From The CSV Files is ")
print(data1.head(10))

