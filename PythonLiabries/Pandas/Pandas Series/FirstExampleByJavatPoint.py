import  pandas as pd
x = pd.Series()
print("The First Series is ")
print(x)
import  numpy as np

# Creating the Series Using The Array
info = np.array(['P','a','n','d','a','s'])
print("The Numpy array is ")
print(info)
series = pd.Series(info)
print("The Series is ")
print(series)

# Creating the series Using The Dict

info1 = {'x':0,'y':1,'z':2}
print("The Dict is ")
print(info1)

ser = pd.Series(info1)
print("The Series of The Data using Dict is ")
print(ser)


# Creating the Series using Scalar values

x = pd.Series(4,index=[0,1,2,3])
print("The Series Of tHe Data using Scalar values is ")
print(x)

