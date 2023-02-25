import pandas as pd
import numpy as np

info_marks = pd.DataFrame(
    {
        "name":["Perker","Smith","William","Terry"],
        "Maths":[23,34,45,67],
        "Science":[34,45,67,89],
        "English":[65,78,90,54]
    }
)
print("The Marks Of The Student Stored is ")
print(info_marks)
writer = pd.ExcelWriter("output.xlsx")
info_marks.to_excel(writer)
writer.save()
print("The Info Marks Is Saved SuccesFully In Excel Sheet")
