import pandas as pd
import numpy as np

info = pd.DataFrame(
    {
        "P":["Smith","John","William","Parker"],
        "Q":["Python","C","Java","C++"],
        "R":[19,24,22,25]
    }

)
print("The Info is ")
print(info)
table = pd.pivot_table(info,index=["P","Q"])
print("The Table is ")
print(table)
