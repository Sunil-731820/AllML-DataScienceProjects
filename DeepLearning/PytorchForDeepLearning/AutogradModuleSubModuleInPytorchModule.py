# # 1. Autograd Module: The autograd provides the functionality of easy calculation of gradients without the explicitly manual implementation of forward and backward pass for all layers.
#
# For training any neural network we perform backpropagation to calculate the gradient. By calling the .backward() function we can calculate every gradient from the root to the leaf.

import  torch
t1 = torch.tensor(1.0,requires_grad=True)
t2 = torch.tensor(2.0,requires_grad=True)
z = 100*t1*t2
print("The Backward Propogation is ")
print(z.backward())
print("The first Gradient is")
print(t1.grad.data)
print("The Second Gradient is ")
print(t2.grad.data)
