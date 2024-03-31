import  numpy as np
d = np.dtype([('salary',np.float)])
arr = np.array([
    (10000.12),
    (200000.50),
    (40000.60),
],dtype=d)
print("The Numpy Array is ")
print(arr)
