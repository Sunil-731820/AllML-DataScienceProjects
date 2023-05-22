from scipy.integrate import quad, dblquad
import  numpy as np
def I(n):
    return dblquad(lambda t, x: np.exp(-x*t)/t**n, 0, np.inf, lambda x: 1, lambda x: np.inf)
print(I(4))