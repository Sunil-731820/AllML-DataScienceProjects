import numpy
from numpy import number
from numpy.distutils.system_info import numpy_info

a = numpy.array([[1,2,3],[4,5,6]])
print("The First Numpy array is ")
print(a)

# to change The Data type of The Array to complex here

b = numpy.array([[10,20,30],[40,50,60]],complex)
print("The Complex Array is ")
print(b)

# Finding The Dimension of The Array
arr = numpy.array([[1,2,3,4],[4,5,6,7],[9,10,11,12]])
print("The New Array is ")
print(arr)
print("The Dimension of The Array is ")
print(arr.ndim)

# Finding The Size of The Each Element of The Array is

arr1 = numpy.array([[1,2,3]])
print("The New Array is ")
print(arr1)
print(arr1.itemsize)

#Finding The Data Type Of The Each Element

num1 = numpy.array([1,2,3])
print("The Array is ")
print(num1)

print("The Data Type Of The Each ELemnent is ")
print(num1.dtype)

# Finding The Shape And Size Of The Array

num2 = numpy.array([[1,2,3,4,5,6,7]])
print("The New Array is ")
print(num2)

print("The Shape of Yhe Array is ") # Shape Means The Dimension of The Array Called as Shape
print(num2.shape)

print("The Size Of THe Array is ") # Size Means The Number Of The Element In The Array is Called as Size
print(num2.size)

# Reshaping Of The array Means That You are changing the  Row & Columns Into the COlumns And Rows

reshape = numpy.array([[1,2],[3,4],[5,6]])
print("The Reshaping of The Array ")
print(reshape)
print("The Dimension Of The Array is ")
print(reshape.ndim)

print("The Size of The Array is ")
print(reshape.size)

print("The Shape Of The Array is ")
print(reshape.shape)


#Slicing In The Numpy array

slicing = numpy.array([[1,2],[3,4],[5,6]])
print("The Slicing of The Array is ")
print(slicing)

print("Printing the Some Element Of The Array is ")
print(slicing[0,1])
print("again Printing the Some Element Of The Array is ")
print(slicing[2,0])


