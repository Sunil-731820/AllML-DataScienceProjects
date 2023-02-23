import pandas as pd
import numpy as np

info = pd.DataFrame(
    {
        "Name":{
            0:"Perker",
            1: "Smith",
            2:"John"
        },
        "Language":{
            0:"Python",
            1:"Java",
            2:"C++"
        },
        "Age":{
            0:22,
            1:26,
            2:30
        }
    }
)
print("The Given data is ")
print(info)

# After The Use Of The melt()

info1 = pd.DataFrame(
    {
        "A":{
            0:"P",
            1:"Q",
            2:"R"
        },
        "B":{
            0:40,
            1:55,
            2:25
        },
        "C":{
            0:56,
            1:62,
            2:42
        }
    }
)
print("After The Use Of The melt()")
print(pd.melt(info1,id_vars=["A"],value_vars=["C"]))


