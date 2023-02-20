import numpy
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

# accessing The data from the Series With Positions

x = pd.Series([1,2,3],index=['Number1','Number2','Number3'])
print("The Series is ")
print(x)

# Retrieving the Array Index and Data Array of a series Objects

x = pd.Series(data=[2,4,6,8])
print("The Series x is ")
print(x)
y = pd.Series(data=[11.2,18.6,22.5],index=['Number1','Number2','Number3'])
print("The series y is ")
print(y)
print("the Index of The x is ")
print(x.index)
print("The Index Of Y is ")
print(y.index)
print("The values of The  Y is ")
print(y.values)
print("The values Of The X is ")
print(x.values)

# Retrieving the Types (dtypes) and Size of the Type (ItemSize)

a = pd.Series(data=[1,2,3,4])
b = pd.Series(data=[4.9,8.2,5.6])
print("The First Series a is ")
print(a)
print("The Second series is")
print(b)
index = ['x','y','z']
print("The Data type is ")
print(a.dtype)
print("The Item Size is ")
# print(a.itemsize)

# Retrieving The Shape of The Series

c = pd.Series(data=[1,2,3,4])
print("The Series is ")
print(c)
print("The Shape of The series is ")
print(c.shape)

# Retrieving the Dimension , Size and Number of The Bytes

d = pd.Series(data=[1,2,3,4])
e = pd.Series(data=[4.9,8.2,5.6])
print("The First Series is ")
print(d)
print("The Second Series is")
print(e)
print("The Dimension Of tHe First Series is ")
print(d.ndim)
print("The Dimension of The Second Series is ")
print(e.ndim)
print("The Size Of The First Series is ")
print(d.size)
print("The Size of The Second Series is ")
print(e.size)
Arr = numpy.array([1,2,3,4,5])
print('The Size Of The Array is ')
print(Arr)
