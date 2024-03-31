import numpy as np
# creating the numpy Array using List
list = [1,2,3,4,5,6,7]
print("The List of The Numpy Array is ")
print(list)
a = np.array(list)
print("The Numpy Array is ")
print(a)

# creating the Numpy Array Using Tuples
tuple = (1,2,3,4,5,6)
print("the tuples is ")
print(tuple)
b = np.array(tuple)
print("The Numpy Array is ")
print(b)

#Creating the Numpy Array using fromiter() In the Numpy Array

list = [0,2,4,6]
print("The List is ")
print(list)
x = np.fromiter(list,dtype=float)
print("The x is ")
print(x)
print("The Type of The X is ")
print(type(x))
