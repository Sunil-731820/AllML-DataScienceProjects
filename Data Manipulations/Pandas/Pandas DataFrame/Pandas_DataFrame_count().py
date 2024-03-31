import  pandas as pd
import  numpy as np
info = pd.DataFrame(
    {
        "Person":["Sunil","Harish","Sumanth","Abhisek"],
        "Age": [22, 23, 34, 45]
    },

)
print("The Data Frame is ")
print(info)
print("After Counting the Number of The Objects is ")
print(info.count())

