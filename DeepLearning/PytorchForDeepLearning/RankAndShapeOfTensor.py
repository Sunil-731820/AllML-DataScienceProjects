import torch
t1 = torch.tensor([1,2,3,4])
t2 = torch.tensor([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

print("The First Tensor is ")
print(t1)
print("The Second Tensor is ")
print(t2)

print('The rank Of The First tensor is ')
print(len(t1.shape))
print("The rank of The Second Tensor is ")
print(len(t2.shape))

print("the Shape Of The first tensor is ")
print(t1.shape)
print("The Shape Of The Second tensor is ")
print(t2.shape)
