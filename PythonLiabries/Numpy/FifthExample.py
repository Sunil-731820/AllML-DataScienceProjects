import  numpy as np
arr = np.arange(0,10,2,float)
print("The Numpy Array is ")
print(arr)

#Another Example of The Numpy Array

arr1 = np.arange(10,100,5,int)
print("The Arr1 is ")
print(arr1)

# The use Of the linSpace() in The Numpy Array
arr = np.linspace(10,20,5,endpoint=False,retstep=True)
print("The LinSpace Array ")
print(arr)

# The use of The LogSpace() In Numpy Array
arr = np.logspace(10,20,num=15,endpoint=True)
print("The Numpy Array is ")
print(arr)
print("The Length of the Numpy Array is ")
print((arr.size))

#Again The use of The logspace()
arr = np.logspace(10,20,num=5,base=2,endpoint=True)
print("The Numpy array is ")
print(arr)



