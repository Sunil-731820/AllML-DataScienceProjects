import numpy
import numpy as np
from numba.np.npyfuncs import np_int_smin_impl

arr = numpy.array([1,2,3])
print("The Array is ")
print(arr)

# Making The one Dim Array to two Dim Array is
arr1 = numpy.array([1,2.,3.],ndmin=2)
print("The Two Dim Array is ")
print(arr1)

#type provide in The Numpy array
arr = numpy.array([12,45,67],dtype=complex)
print("The Array is ")
print(arr)


# Creating the Array from the Sub Class

arr11 = np.array(np.mat('1,2;3,4'))
print("The Array is ")
print(arr11)


print("The Matrix Of The Above Array is ")
arr12 = np.array(np.mat('10 20; 30 40'),subok=True)
print(arr12)


# The use of The numpy.concatenate()
x = numpy.array([[1,2],[3,4]])
print("The First Array is ")
print(x)
y = numpy.array([[12,30]])
print("the Second Array is ")
print(y)
print("after the use of The numpy.concatenate()")
z = numpy.concatenate((x,y))
print(z)

# Concatnening the Two Array According column Wise and Rows Wise

x1 = numpy.array([[1,2],[3,4]])
y1 = numpy.array([[12,30]])
print("the x1 is ")
print(x1)
print("The y1 is ")
print(y1)
print("After Concatening According to column Wise")
print(numpy.concatenate((x1,y1),axis=0))
print("After Concatening According to the Row Wise")
# print(numpy.concatenate((x1,y1),axis=1))


# The use of The numpy.append()

firstArray = numpy.array([[10,20,30],[40,50,60],[70,80,90]])
secondArray = numpy.array([[11,21,31],[42,52,62],[73,83,93]])
print("The first Array is ")
print(firstArray)
print("the Second array is ")
print(secondArray)
print("after appending Both the Array is  ")
appendArray = numpy.append(firstArray,secondArray)
print(appendArray)

# Appending the array according to axis Wise
firstArray1 = numpy.array([[10,20,30],[40,50,60],[70,80,90]])
secondArray1 = numpy.array([[11,21,31],[42,52,62],[73,83,93]])
print("The First array is ")
print(firstArray1)
print("The Second Array is ")
print(secondArray1)
appendArray1 = numpy.append(firstArray1,secondArray1,axis=0)
print("after The appending The array is ")
print(appendArray1)
rowWiseAppending = numpy.append(firstArray1,secondArray1,axis=1)
print("after Appending The Rows Wise is ")
print(rowWiseAppending)


# The Use Of The sum() in The Numpy Array is :

sumOfFirstArray = numpy.array([0.4,0.5,0.9,6.1])
print("The Given array is  ")
print(sumOfFirstArray)
print("The Sum of The first array is ")
print(numpy.sum(sumOfFirstArray))

# adding  two Dimnensional Array

firstArray2 = numpy.array([[1,4],[3,5]])
print("The first array is ")
print(firstArray2)
print("The Sum of The two Dim Array is ")
print(numpy.sum(firstArray2))

# The use of The numpy.zeroes()
firstZeroes = numpy.zeros(6)
print("The First Zero is ")
print(firstZeroes)

# Creating the array of The Zeroes With 6 Row and 2 Columns

sixRowAndTwoColumns = numpy.zeros((6,2))
print("The Array is ")
print(sixRowAndTwoColumns)





