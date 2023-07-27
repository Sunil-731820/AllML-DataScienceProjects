import torch
import numpy as np
# Creating The tensor using list and Numpy Array

data1 = [1,2,3,4,5,6]
data2 = np.array(
    [1.5,3.4,6.8,9.3,7.0,2.8]
)
print("The First data is ")
print(data1)
print("The Second Data is ")
print(data2)

# Now Creating the tensor And Printing to The Screen using tensor In Pytorch

t1 = torch.tensor(data1)
t2 = torch.Tensor(data1)
t3 = torch.as_tensor(data2)
t4 = torch.from_numpy(data2)
print("The tensor 1 is ")
print(t1)
print("the Tensor t2 is ")
print(t2)
print("The tensor 3 is ")
print(t3)
print("The tensor 4 is ")
print(t4)
