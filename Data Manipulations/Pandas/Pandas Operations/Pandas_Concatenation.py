import  pandas as pd
import  numpy as np

first_data = pd.Series(["P","Q"])
second_Data = pd.Series(["R","S"])
print("The First data series is ")
print(first_data)
print("The Second data Series is ")
print(second_Data)

print("After Concateing The Data is ")
concated_data = pd.concat([first_data,second_Data],ignore_index=True)
print("The Data is ")
print(concated_data)

# Concatening The Series using append()

first_Series = pd.Series(
    {
        "Name":["Smith","Perker","Allen","John","Parker"],
        "Subject":["sub1","sub2","sub4","sub6","sub5"],
        "Marks_Scored":[98,90,87,69,78]
    }
)

second_Series = pd.Series(
    {
        "Name":["Billy","Brian","Bran","Bryce","betty"],
        "Subject":["sub2","sub4","sub3","sub6","sub5"]
        ,"Marks_scored":[89,80,79,97,88]
    }
)
print("The First Data Series is")
print(first_Series)
print("The Second Data Series is")
print(second_Series)
print("After The Use of The append() for Concatenating The Series is ")
print(first_Series.append(second_Series))
