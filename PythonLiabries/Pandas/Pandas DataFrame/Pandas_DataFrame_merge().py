import pandas as pd
import numpy as np
left = pd.DataFrame(
    {
        "Id":[1,2,3,4,5],
        "Name":["Alex","Amy","Allen","Alice","Ayoung"],
        "Subject":["Sub1","Sub2","Sub3","Sub4","Sub5"]
    }
)

right = pd.DataFrame(
    {
        "Id":[1,2,3,4,5],
        "Name":["Billy","Brian","Bran","Bryce","Betty"],
        "Subject":["sub2","sub4","sub3","sub6","sub5"]
    }
)

print("The Left Data frame is ")
print(left)
print("The Right Data Frame is ")
print(right)

print("After Merging The Left and Right DataFrame is  ")
print(pd.merge(left,right,on="Id"))
