import numpy as np
a = np.array([1,2,3,4,5,6,7])
b = np.array([2,4,6,8,10,12,14])
print("The first Array is ")
print(a)
print("The Second Array is ")
print(b)
c = a*b
print("The Product Of The Array is ")
print(c)

#After using Broadcasting technique
num1 = np.array([
    [1,2,3,4],
    [2,4,5,6],
    [10,20,39,3]
])
print("The First Numpy Array is ")
print(num1)
num2 = np.array([2,4,6,8])
print("The Second Numpy Array is ")
print(num2)
sum = num2+num1
print("The Sum of The Array is ")
print(sum)
