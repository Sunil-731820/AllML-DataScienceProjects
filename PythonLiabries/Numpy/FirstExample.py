import numpy as np
a = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print("The Numpy Array is ")
print(a)
print("The Size of The Each Element Array is ")
print(a.itemsize)
print("The DataType is ")
print(a.dtype)

print("The Shape Of The Numpy Array is ")
print(a.shape)
print("The Size of The numpy Array is ")
print(a.size)

print("The Minimum Value of the Array is ")
print(a.min())
print("The Maximum Value of The Array is ")
print(a.max())
print("The Sum of The numpy Array is ")
print(a.sum())

# Numpy Array Axis

b = np.array([
    [1,2,30],
    [10,15,4]
])
print("The Array is ")
print(b)
print("The Maximum Element of the Columns is ",b.max(axis=0))
print("The Minimum Element of the Rows",b.min(axis=1))
print("the Sum Of The All Rows is ",b.sum(axis=1))
print("The Sum of The All Column is ",b.sum(axis=0))

# Finding The Square Root And Deviations
c = np.array([
    [1,2,30],
    [10,15,4]
])
print("The Numpy Array is ")
print(c)
print("The Square Root Of The Array is ")
print(np.sqrt(c))
print("The Standard Deviation is ")
print(np.std(c))

Num1 = np.array([
    [1,2,30],
    [10,15,4]
])
Num2 = np.array([
    [1,2,3],
    [12,19,29]
])

print("The first Numpy Array is ")
print(Num1)
print("The Second Numpy Array is ")
print(Num2)

print("The Sum Of The Array is ")
print(Num1+Num2)
print("The product of The Array is ")
print(Num1*Num2)
print("The Division of The Array is ")
print(Num1/Num2)

# Array Concatenation

num1 = np.array([
    [1,2,30],
    [10,15,4]
])

num2 = np.array([
    [1,2,3],
    [12,19,29]
])
print("The Arrays Vertically Concatenated ")
print(np.vstack((num1,num2)))

print("The Arrays Horizontal Concatenated")
print(np.hstack((num1,num2)))


