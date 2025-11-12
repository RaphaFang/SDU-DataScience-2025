import numpy as np


# 1. Identity Matrix
I = np.eye(3)
A = np.random.randn(3,3)
print(A @ I)
print(I @ A)

# --------------------------------------------------------------------------------------------------------------
# 2. inverse matrix
# not all the matrix has the inverse, if u got a zero-matrix, whatever you dot, zero-matrix is the only output
# A A^{-1} = A^{-1} A = I

# --------------------------------------------------------------------------------------------------------------
# 3. inverse matrix by ->> determinant, adjugate
# the inverse matrix of B, will be generate by this formula, B-1 = (1/det(B)) * adj(B)
B = np.array([[1, 2],
              [3, 4]])
det_B = np.linalg.det(B)

if det_B != 0:
    inv_B = np.linalg.inv(B)
    result = np.allclose(B @ inv_B, np.eye(2))
    print(result)
else:
    print("nana, the det_B is 0")
    
# --------------------------------------------------------------------------------------------------------------
# 4. inverse matrix by, ->> Gauss-Jordan
# if u got [0,0,0]|[-1,-1,1], the matrix is not ganna have the inverse

# --------------------------------------------------------------------------------------------------------------
# 5. we can take A-1 as a way to eliminate the A

# --------------------------------------------------------------------------------------------------------------
# 6. be aware, AB = I, is not guarantee that B will be the A-1
# have to make sure the both side work, AB = BA = I
# otherwise it will only be the "right inverse" or "left inverse"