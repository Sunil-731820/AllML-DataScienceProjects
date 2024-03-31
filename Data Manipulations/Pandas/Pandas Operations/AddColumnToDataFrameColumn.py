import pandas as pd
import  numpy as np
aa = pd.read_csv("covid_worldwide.csv")
print("The Data is fro The kaggle is ")
print(aa)
df = pd.DataFrame(aa)
print("The Data Frame is ")
print(df)
print("The Head of The Data Frame is ")
print(df.head())

print("Adding The New Column To The existing Data Frame is ")
df["Age"] = "20"
print("After The Addition of tHe New Column to The existing Data Frame is  ")
print(df)
print("After This Top 10 Element  of The Data is ")
print(df.head())

print("Again Adding The New Column to The Existing Data Frame is ")
df["defects"] = "Defects"
print("The Data Frame is ")
print(df)
print("The Top 10 Rows data is ")
print(df.head(10))

# Adding The New column using insert()

df.insert(2,column="Populations",value="India & USA")
print("After The Use of The Insert() to add The Column In Yhe Existing data Frame is ")
print(df)
print("The Top 10 rows of The Data is from The Data Frame is ")
print(df.head(10))

