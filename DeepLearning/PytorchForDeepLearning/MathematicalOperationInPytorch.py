import  torch
t1 = torch.tensor([1,2,3,4])
t2 = torch.tensor([5,6,7,8])

print("The First tensor is ")
print(t1)
print("The Second Tensor is ")
print(t2)
print("The Addition of The two tensor is ")
print(t1+t2)
print("Adding the two Tensor using Add()")
print(torch.add(t1,t2))
print("Subtracting The Two tensor is ")
print(torch.sub(t1,t2))
print("The Multiplication of The Two tensor is ")
print(torch.mul(t1,t2))
print("The Division of The two tensor is ")
print(torch.div(t2,t1))
