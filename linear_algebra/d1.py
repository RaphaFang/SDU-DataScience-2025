import numpy as np

# A = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])

# B = np.array([[9, 8, 7],
#               [6, 5, 4],
#               [3, 2, 1]])

# # 加法
# print("A + B =\n", A + B)

# # 減法
# print("A - B =\n", A - B)

# # 矩陣乘法（dot product）
# print("A @ B =\n", A @ B)

# ------------------------------------
# ! column vector
# T = np.array([[3, 0],
#               [0, 2]])

# v1 = np.array([1, 2]) # hidden 
# v2 = np.array([[1], [2]]) # clearly display

# print(T @ v1) # → [3 4]      
# print(T @ v2) # → [[3], [4]] 

# ------------------------------------
# RREF（Reduced Row Echelon Form）

# got no clue...
def rref(matrix):
    A = matrix.astype(float)
    rows, cols = A.shape
    lead = 0

    for r in range(rows):
        if lead >= cols:
            break
        i = r
        while A[i, lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if cols == lead: # 原先是用break，但是只有跳出while，當一欄位是[0,0,0,0]會報錯
                    return A
        A[[r, i]] = A[[i, r]]
        A[r] = A[r] / A[r, lead]
        for i in range(rows):
            if i != r:
                A[i] = A[i] - A[i, lead] * A[r]
        lead += 1
    return A

# A = np.array([
#     [1, 1, 1, 6],
#     [2, 3, 1, 13],
#     [0, 0, 0, 0]
# ], dtype=float)

# print(rref(A))
# ------------------------------------
# !! keypoint
# 我在重新整理這部份討論的思路
# 1. 在n*n的arr裡，跑RREF前與後，如果arr出現一個list包含n+1個全為0的list（也就是包含最尾巴的所以加1）
# 並且當總共有 n 未知數，卻只有n-1條方程式，則一定是無線
# 每出現一條，他會說明我至少有一個值無法得到定義，也就是說，我會缺少一個pivot。
# 我缺少一個pivot，會說明這arr必然會是一個無限多解。

# 2. 我下面這函數是不是也可以調整，因為我無法完全判斷跑完上方RREF函數得到的東西到底是不是RREF，有可能得到如這邊的結果
# [[ 1.  0.  2.  5.]
#  [ 0.  1. -1.  1.]
#  [ 0.  0.  0.  0.]]
# 所以我的analyze_rref()函數應該可以調整成，先判斷有沒有[0,0,0,1]接著判斷有沒有[0,0,0,0]
# 這分別可以作為no resolution 跟 ifinity的判斷對吧？


# ------------------------------------
def analyze_rref(rref_matrix):
    rows, cols = rref_matrix.shape
    num_vars = cols - 1
    pivot_cols = []

    for row in rref_matrix:
        if np.all(row[:-1] == 0) and row[-1] != 0: # 這邊是整列都是0，但是最後答案不是0
            return "No Solution"
        if np.all(row == 0): # 如果需要快速識別無線多解，也可以挑出來作
            continue
        leading_idx = np.argmax(row[:-1] != 0) # 這是找第一個「不是 0」的index
        if row[leading_idx] != 0:
            pivot_cols.append(int(leading_idx))

    if len(pivot_cols) == num_vars:
        return f"Unique Solution, {pivot_cols}"
    else:
        # free_vars = num_vars - len(pivot_cols)
        free_vars = [i for i in range(num_vars) if i not in pivot_cols]
        return f"Infinitely, miss a pivot at index: {free_vars}"

# A = np.array([
#     [1, 1, 1, 6],
#     [2, 3, 1, 13],
#     [0, 0, 0, 0],
# ], dtype=float)
# print(rref(A))
# print(analyze_rref(rref(A)))

# 但如果要透過RREF這方式，來算出有幾個nullity，要先算出全部有幾個pivot
# 所以也沒有錯，他原本的方式算出來的就以找出每一個pivot為目標

# ------------------------------------

# A = np.array([
#     [1, 2, 3],
#     [0, 1, 4],
#     [0, 0, 2]
# ])

# print(np.linalg.det(A))

# ------------------------------------
# rank & nullity
# ! 在 RREF 中，pivot 必須是 1，且它的上方與下方都為 0。

aa = np.array([
    [1, 3, -1, 2,5],
    [2, 6, -2,5, 12],
    [-1, -3, 1, -1, -4],
    [0, 0, 0, 0, 0]
])
print(rref(aa))


# ------------------------------------
# vector
# parametric solution