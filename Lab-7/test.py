import numpy as np
from numpy import linalg as la

# M = np.array([[-0.3, 0.2, 0.1], [0.8, -0.9, 0.1], [1, 1, 1]])
# print(la.solve(M.T, np.array([0, 0, 1])))
n = np.sqrt((76/11)**2 + (35/22)**2 + 1)
n = 76/11 + 35/22 + 1
print((76/11)/n)
print((35/22)/n)
print((1)/n)