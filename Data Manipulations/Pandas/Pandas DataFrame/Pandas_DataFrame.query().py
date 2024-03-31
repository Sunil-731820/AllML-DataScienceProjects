import  pandas as pd
import numpy as np

info = pd.DataFrame(
    {
        "X":range(1,6),
        "Y":range(10,0,-2),
        "Z Z": range(10,5,-1)
    }
)
print("The info is ")
print(info)
print(info.query("X > Y"))
print("The use of The ==")
print(info.Y==info['Z Z'])


