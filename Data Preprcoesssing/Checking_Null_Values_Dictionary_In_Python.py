# importing pandas as pd
import pandas as pd

# importing numpy as np
import numpy as np

# dictionary of lists
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
print("The Dict is : ")
print(dict)
# creating a dataframe from list
df = pd.DataFrame(dict)
print("The Data Frame Will be ")
print(df)
# using isnull() function
print(df.isnull())
print("After The Use Of The isnull method is: ")
print(df)

# Part2 :
# making data frame from csv file
data = pd.read_csv("employees.csv")
print("The Data Frame is : ")
print(data)
# creating bool series True for NaN values
bool_series = pd.notnull(data["Gender"])
print("The Bool Series Is  ")
print(bool_series)
# filtering data
# displaying data only with Gender = Not NaN
print("The Data is : =")
print(data[bool_series])

# Filling missing values using fillna(), replace() and interpolate()


df1 = pd.read_csv("employees.csv")
print("The New Data Frame is : ")
print(df1)

print("Filling The Missing values using fillna method : ")
print(df1.fillna(0))

# Filling With the previous value

df2 = pd.read_csv("employees.csv")
print("The Data Frame 2 is : ")
print(df2)

print("Filling With Previous Value In Below Cells ")
print(df2.fillna(method='pad'))
print("Printing the Whole Gender Columns :")
print(df2['Gender'])

# Filling The Next Value in Place of Nan values

df4 = pd.read_csv("employees.csv")
print("The Data Frame 4 Is : ")
print(df4)

print("After Filling The next Value in Nan Values ")
print(df4.fillna(method='bfill'))


# parts 3 :

df5 = pd.read_csv("employees.csv")
print("The Data Frame Is : ")
print(df5)

# Filling The Gender Which is Having no values With No gender Values

print(df5['Gender'].fillna("No Gender" , inplace=True))
print("After Filling The No Values With user Given Data Values  ")
print(df5)

# Now we are going to replace the all Nan value in the data frame with -99 value.
import numpy as np
df6 = pd.read_csv("employees.csv")
print("The data rame is : ")
print(df6)

df6.replace(to_replace = np.nan, value = -99)
print("After Replacing the Data is ")
print(df6)
