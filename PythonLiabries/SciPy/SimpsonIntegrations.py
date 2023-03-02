import numpy as np
def f1(x):
   return x**2

def f2(x):
   return x**3


x = np.array([1,3,4])
y1 = f1(x)
from scipy import integrate
I1 = integrate.simpson(y1, x)
print(I1)