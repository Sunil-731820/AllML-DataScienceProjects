import  numpy as np
import pandas as pd

A_Data = pd.Series(["P","Q"])
B_Data = pd.Series(["R","S"])
print("The First data is ")
print(A_Data)
print("The Second data is ")
print(B_Data)
print("After Concatening The two Series Data is ")
print(pd.concat([A_Data,B_Data]))

# The ANother Example is

one = pd.DataFrame(
    {
        "Name":["Perker","Smith","William","Allen","John"],
        "Subject":["sub1","sub2","sub3","sub4","sub5"],
        "Marks":[100,20,30,40,50]
    }
)
print("The Fisrt One Data is ")
print(one)

two = pd.DataFrame(
    {
        "Name":["Billly","Brain","Bryce","betty","Sunil"],
        "Subject":["sub6","sub7","sub8","sub9","Sub10"],
        "Marks":[10,20,30,40,10]

    }
)
print("The Second Data Frame is ")
print(two)
index = [1,2,3,4,5]
print("The Index is ")
print(index)
print("After Appending The fisrt Data Frame into The Second Data frame is  ")
print(one.append(two))
