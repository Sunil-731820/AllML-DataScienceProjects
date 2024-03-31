import numpy as np
import pandas as pd

aa = pd.read_csv("organizations-100.csv")
print("The CSV file Data is ")
print(aa)

# Now Adding The Age in the existing Data Frame is
aa["Age"] = 24
print("After Adding The Age as The Column Name is ")
print(aa)

# Inserting The Dept At The Specific Positins
aa.insert(2,column="Department",value="B.Tech")
print("After inserting into the specific Column Into Specific Positions is ")
print(aa)
