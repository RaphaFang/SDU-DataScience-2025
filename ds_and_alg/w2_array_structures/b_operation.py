import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[10, 20], [30, 40]])
C = A + B
# print(C)

# -----------------------------------------------------------------
C = A @ B.T  # B.T 是轉置，確保 shape 符合
C2 = np.dot(A, B.T)

# print(C)
# print(C2)
# ! 有趣的是，T 可以改變 arr 方向，但是不改變數值
# ! 要確保兩者 @ 時的「形狀」。 例如要是 3*7 @ 7*3

# -----------------------------------------------------------------
A = np.array([[1, 2, 3], [4, 5, 6]])

print("原始陣列:\n", A)
print("轉置:\n", A.T)

# Reshape：調整為 3x2
print("reshape(3,2):\n", A.reshape(3,2))

# Flatten：轉為一維
print("flatten:\n", A.flatten())

# | 錯誤類型                                          | 原因與處理               |
# | ------------------------------------------------ | ---------------------- |
# | `ValueError: operands could not be broadcast`    | shape 不一致            |
# | `ValueError: shapes (2,3) and (2,3) not aligned` | 矩陣乘法時內部維度不符     |
# | `.T` 出錯                                         | 轉置只適用於 2D 陣列，1D 不會轉 |

# -----------------------------------------------------------------
# broadcast
# 這邊的廣播跟spark 那種多節點廣播是不同東西，不過後者在實作中兩種類型的廣播都能作
# -----------------------------------------------------------------
# a. 加法函數（要能處理 shape 不一致的錯誤）
def matrix_add(A, B):
    if A.shape != B.shape:
        raise ValueError(f"shape mismatch: {A.shape} vs {B.shape}")
    return A + B

# b. 矩陣乘法函數（@）
def matrix_multiply(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError(f"shape mismatch: {A.shape} @ {B.shape}")
    return A @ B

# c. 傳入任意陣列，回傳轉置與 flatten 的結果
def transpose_and_flatten(A):
    return (A.T, A.flatten())

# ! 注意, reshape() 不是萬能，如果變形的欄位相成不滿足原先員件數，會轉換失敗