import  numpy as np

arr = np.array([0,30,60,90,120,150,180])
print("The Array is ")
print(arr)
print("The Sin Values of The sin() is ")
print(np.sin(arr))

print("The tan Values of The tan() is ")
print(np.tan(arr*np.pi/180))

arr1 = np.array([0,30,60,90])
print("The Inverse of The Sin is ")
# print(np.arcsin(arr))
print(np.arcsin(arr1))


