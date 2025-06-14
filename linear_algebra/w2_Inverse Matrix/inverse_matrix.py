import numpy as np
# ------------------------------------
# | 函數       | 支援維度 | 行為說明            | 高維支援？           | 建議用途         |
# | --------- | ------- | ----------------   | -------------------| -------------- |
# | A @ B     | ≥2D     | 矩陣乘法（語法糖）    | ✅（等同 matmul）    | ✅ 推薦，最語意清楚 |
# | np.matmul | ≥2D     | 矩陣乘法 + batch      | ✅（batch matrix） | 適合大型高維矩陣   |
# | np.dot    | ≥1D     | 最後一軸與倒數第二軸內積 | ⚠️ 會混淆          | 不建議用在線性代數  |

# ------------------------------------
# 1.1 Identity Matrix (單位矩陣)
A = np.array([[2, 1], 
              [5, 3]])
I = np.array([[1, 0],
              [0, 1]])
# I = np.array([[0, 1],
#               [1, 0]])
identity_test = np.dot(I, A)  # np.dot(A, I) 要雙邊都跑，滿足定義
# print(identity_test)
# [[1 2]
#  [3 5]]

# ------------------------------------
# ! 1.2 四個等價條件，並且可以用這條件檢查是否可能有反舉證
# det(A) ≠ 0
    # 若 det(A) ≠ 0，則表示 A 的行或列沒有線性相關性
    # 代表行向量張成一個平面/體積，有唯一的方向 → 解可以被還原（即可逆）
    # 他的作法會是右斜線 - 左斜線
    # np.linalg.det(A_det)

# A 的列（或行）向量線性獨立
    # 也就是每一行不會是另一行的 n 倍
    # 如果沒有線性獨立，算 det 會得到0

# A 的簡化形式 rref(A) 是單位矩陣

# Ax = b 對任意 b ∈ ℝⁿ 都有唯一解


# ------------------------------------
# 1.3 Inverse matrix
A = np.array([[2, 1], 
              [5, 3]])

A_inv = np.linalg.inv(A)
# print(A_inv)
# [[ 3. -1.]
#  [-5.  2.]]
# 如果你丟一個沒有向量線性獨立的進去 .inv() 會報下面的錯
    # ! numpy.linalg.LinAlgError: Singular matrix
    # Singular matrix (奇異矩陣)，不可逆（non-invertible）矩陣
    # A = np.array([[2, 1], 
                #   [4, 2]])

# print(np.dot(A, A_inv))
# print(np.round(np.dot(A, A_inv),5))

# ------------------------------------
# 1.4 Gauss–Jordan elimination
# 簡單來說透過削減，把 A I ，轉變成 I A
# 
# [2 1] [1 0]     [1 0] [3 -1]
# [5 3] [0 1]  -> [0 1] [-5 2]

# ------------------------------------
# ------------------------------------
# 2.1 Block Matrix
A11 = np.array([[1, 2], [5, 6]])
A12 = np.array([[3, 4], [7, 8]])
A21 = np.array([[9, 10], [13, 14]])
A22 = np.array([[11, 12], [15, 16]])

A = np.block([[A11, A12],
              [A21, A22]])
# print(A)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]

# ------------------------------------
# 2.2 block-wise matrix multiplication
A11 = np.array([[1, 2],
                [3, 4]])
A12 = np.array([[5, 6],
                [7, 8]])
A21 = np.array([[0, 1],
                [1, 0]])
A22 = np.array([[2, 3],
                [4, 5]])

B11 = np.array([[1, 0],
                [0, 1]])
B12 = np.array([[9, 9],
                [9, 9]])
B21 = np.array([[1, 1],
                [1, 1]])
B22 = np.array([[2, 2],
                [2, 2]])

C11 = A11 @ B11 + A12 @ B21
C12 = A11 @ B12 + A12 @ B22
C21 = A21 @ B11 + A22 @ B21
C22 = A21 @ B12 + A22 @ B22

A_block = np.array([[1, 2, 5, 6],
                    [3, 4, 7, 8],
                    [0,1,2,3],
                    [1,0,4,5]])
B_block = np.array([[1,0,9,9],
                    [0,1,9,9],
                    [1,1,2,2],
                    [1,1,2,2]])

C_by_small_block = np.block([[C11, C12],
              [C21, C22]])
C_by_whole_block = np.dot(A_block,B_block)
# print(C_by_small_block,C_by_whole_block)


# ------------------------------------
# ------------------------------------
# 3.1 LU decomposition
from scipy.linalg import lu

A = np.array([[2, 3],
              [4, 7]])

P, L, U = lu(A)

# print("P =\n", P)
# print("L =\n", L)
# print("U =\n", U)
# print(L @ U)
# print(np.allclose(P @ A, L @ U))

A_1 = np.array([[1, 0],
              [3, 1]])
A_2 = np.array([[1, 2],
              [0, 2]])
# print(A_1@A_2)
# 我不懂為什麼但是一定要先 L ，才可以乘上 U
# 並且一方一定要是紀錄另一方成上多少倍，建立出對角線 1 1，中間加上倍數

# ! 矩陣乘法沒有交換律：A @ B ≠ B @ A 所以順序一定要 L @ U，而不是 U @ L。

# ------------------------------------
# 3.2 LU 解 Ax = b
# Ly = b
# Ux = y
def forward_substitution(L, b):
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])
    return y

def backward_substitution(U, y):
    n = len(y)
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

# ------------------------------------
# 3.3 解 Ax = b ，得x
from scipy.linalg import lu, solve_triangular

A = np.array([[2, 3],
              [4, 7]])
b = np.array([8, 20]) 

# ! 這邊的 LU 分解，是有包含pivot。所以實際做的是 PA = LU
#     Ax =     b
#     LU = P * b  （這邊的LU 有包含 P，所以b 也要 *P）
# L * y = P * b
# U * x = y

P, L, U = lu(A)
# Ly = b（forward）
y = solve_triangular(L, P @ b, lower=True)  # 這邊不能只寫 b
# Ux = y（backward）
x = solve_triangular(U, y, lower=False)

# print(x)

# ------------------------------------
# ------------------------------------
# 4.1 condition number
# 但如果 A 是一個「接近不可逆」的矩陣，即使 det(A) ≠ 0，解出來的 x 也可能會「極度不穩」或「數值誤差被放大」
# 這時候，我們就需要條件數（condition number）來衡量矩陣的「數值穩定性」

import numpy as np
A = np.array([[1, 2],
              [2.0001, 4]])
kappa = np.linalg.cond(A)
# print(kappa)
# 你原本的 b 有一點小誤差 δb，那解出來的 x 的誤差 δx 會被放大大約 κ 倍：
# κ 大 ⇒ 解 x 很容易不準（浮點誤差放大）
# κ 小 ⇒ 解 x 很穩（誤差不會亂跳）

# ------------------------------------
# ------------------------------------
import numpy as np
from scipy.linalg import lu, solve_triangular

A = np.array([[1, 2],
              [3, 8]])
b = np.array([5, 17])

# 解法1：np.linalg.solve
x_np = np.linalg.solve(A, b)

# 解法2：LU
P, L, U = lu(A)
y = solve_triangular(L, P @ b, lower=True)
x_lu = solve_triangular(U, y, lower=False)

# 解法3：A⁻¹ @ b
A_inv = np.linalg.inv(A)
x_inv = A_inv @ b

# print("x by np.linalg.solve =", x_np)
# print("x by LU decomposition =", x_lu)
# print("x by inverse matrix  =", x_inv)
# print("誤差：LU - np =", np.linalg.norm(x_lu - x_np))
# print("誤差：inv - np =", np.linalg.norm(x_inv - x_np))

# x by np.linalg.solve = [3. 1.]
# x by LU decomposition = [3. 1.]
# x by inverse matrix  = [3. 1.]
# 誤差：LU - np = 0.0
# 誤差：inv - np = 1.047382306668854e-15

# ------------------------------------
A_bad = np.array([[1, 2],
                  [2.00001, 4]])
b_bad = np.array([3, 6.00001])

kappa = np.linalg.cond(A_bad)
x_np = np.linalg.solve(A_bad, b_bad)
x_inv = np.linalg.inv(A_bad) @ b_bad

print("κ(A_bad) =", kappa)
print("x by np =", x_np)
print("x by inv =", x_inv)
print("誤差（inv - np）=", np.linalg.norm(x_inv - x_np))


# 求 A⁻¹ 通常比 LU 分解或直接解 Ax = b 成本更高
# 數值誤差更大
# Python、C++、Fortran 都推薦「不要用 inverse 解聯立方程式」
# 你應該把 np.linalg.inv(A) 看作是「數學理解工具」，不是「實作手段」。