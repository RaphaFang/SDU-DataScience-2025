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
def analyze_rref(rref_matrix):
    rows, cols = rref_matrix.shape
    num_vars = cols - 1
    pivot_cols = []

    for row in rref_matrix:
        leading_idx = np.argmax(row[:-1] != 0) # 這是找第一個「不是 0」的index
        if np.all(row[:-1] == 0) and row[-1] != 0: # 這邊是整列都是0，但是最後答案不是0
            return "No Solution"
        elif row[leading_idx] != 0:
            pivot_cols.append(int(leading_idx))

    if len(pivot_cols) == num_vars:
        return f"Unique Solution, {pivot_cols}"
    else:
        # free_vars = num_vars - len(pivot_cols)
        free_vars = [i for i in range(num_vars) if i not in pivot_cols]
        return f" Infinitely, at index: {free_vars}"

A = np.array([
    [1, 1, 1, 6],
    [0, 0, 0, 0],
    [2, 3, 1, 13],
], dtype=float)
print(rref(A))
print(analyze_rref(rref(A)))