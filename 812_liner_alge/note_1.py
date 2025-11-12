import numpy as np

A = np.array([[2,1,-1],
              [-3,-1,2],
              [-2,1,2]], float)
b = np.array([8, -11, -3], float)

# 解 Ax = b
x = np.linalg.solve(A, b)
# print(x)

# -----------------------------------------------------------------------------v
import sympy as sp

A = sp.Matrix([[2,1,-1,8],
               [-3,-1,2,-11],
               [-2,1,2,-3]])

# 化成 RREF
rref_matrix, pivots = A.rref()
print(rref_matrix) 
# Matrix([[1, 0, 0, 2], 
#         [0, 1, 0, 3], 
#         [0, 0, 1, -1]])
print(pivots)  # (0, 1, 2) ## 這邊列出你的左側位置，唯一有的那一欄位
