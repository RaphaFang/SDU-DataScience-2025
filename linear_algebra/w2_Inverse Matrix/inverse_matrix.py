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
# LU decomposition
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
print(A_1@A_2)
# 我不懂為什麼但是一定要先 L ，才可以乘上 U
# 並且一方一定要是紀錄另一防成上多少倍