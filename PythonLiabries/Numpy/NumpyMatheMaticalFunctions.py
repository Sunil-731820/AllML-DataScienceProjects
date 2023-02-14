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
