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


# The USe Of The linSpace That Means it returns the evenly Spaced values Over The given interval .
# i am  going to print The 10 Values Which is Equally Spaced Between 5 and 15 Which Includes The initial And final values Of The ranges In LinSpaces

linSpace = numpy.linspace(5,15,10)
print("The Lin Space values are ")
print(linSpace)

# finding The Maximum and Minimum Values Of The Array Elements are:

maximum = numpy.array([1,2,3,10,15,4])
print("The maximum Array is ")
print(maximum)
print("The maximum Values is ")
print(maximum.max())

minimum = numpy.array([1,2,3,10,15,4])
print("The Array is ")
print(minimum)
print("The Minimum Values Of The array is ")
print(minimum.min())


# Finding  the Minimum and Maximum values In  Numpy Array In Two Dimensional Array
maximumValuesIntwoDim = numpy.arange(10).reshape(2,5)
print("The Maximum values Of The Two Dimensional array is ")
print(maximumValuesIntwoDim)
print(numpy.max(maximumValuesIntwoDim))

#The Minimum Values In The two Dimensional array is

minimumValuesInTwoDim = numpy.arange(20).reshape(4,5)
print("The Array is ")
print(minimumValuesInTwoDim)
print("The Size Of The Array is ")
print(numpy.size(minimumValuesInTwoDim))
print("The Shape of The Two Dim Array is ")
print(numpy.shape(minimumValuesInTwoDim))
print("The Minimum Values in The two Dim array is ")
print(numpy.min(minimumValuesInTwoDim))

# finding the minimum Values in The Row Wise of The Array is
#if you are using axis = 1 then It is called as Row Wise and If axis = 0 called as column Wise

print("The Minimum Element of The Row Wise is ")
print(numpy.min(minimumValuesInTwoDim,axis=1))

#Finding The maximum values In The column Wise Of The Array is
print("The Maximum ElemenT of The Array using The Row Wise Is ")
print(numpy.max(maximumValuesIntwoDim,axis=0))

#Find The Sum Of The All The Rows

sumOfAllRow = numpy.array([[1,2,30],[10,15,4]])
print("The Sum of all rows is ")
print(sumOfAllRow)
print("The SUm Of The Array in Row Wise Is ")
print(sumOfAllRow.sum(axis=1))
print('The Sum of The Array in Column Wise is ')
print(sumOfAllRow.sum(axis=0))

# Finding The Square root and Standard Deviations
SquareRootOfTheArray = numpy.array([[1,2,30],[10,15,4]])
print("The Square Root Of The array is ")
print(numpy.sqrt(SquareRootOfTheArray))

#Finding The Standard Deviation Is :

standardDeviationOfTheArray = numpy.array([[1,2,30],[10,15,4]])
print("The Array is ")
print(standardDeviationOfTheArray)
print("The Standard Deviations Is ")
print(numpy.std(standardDeviationOfTheArray))

# AritheMatic Operation On The Numpy Array is :

firstArray = numpy.array([[1,2,30],[10,15,4]])
secondArray = numpy.array([[1,2,3],[12,19,29]])
print("The first Array is ")
print(firstArray)
print("The Second Array is ")
print(secondArray)

print("The Sum of The Array is ")
print(firstArray+secondArray)

print("The Multiplication Of The Array is ")
print(firstArray*secondArray)

print("The Division of The two Array is ")
print(firstArray/secondArray)


