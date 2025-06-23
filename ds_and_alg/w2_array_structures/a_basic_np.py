import numpy as np

a_list = [1, 2, 3] # <class 'list'>
a_array = np.array([1, 2, 3]) # <class 'numpy.ndarray'>

# -----------------------------------------------------------------
a = np.array([[1, 2, 2], [3, 4, 5]]) # , dtype=object
print("陣列:\n", a)
print("形狀 (shape):", a.shape)  # (2, 3)
print("維度數 (ndim):", a.ndim)  # 2
print("資料類型 (dtype):", a.dtype)  # int64

# 不規則的（ragged） arr 會報錯，如果加上 dtype=object 就不會報錯
# 建立一個一維陣列，裡面每個元素是 Python 的 list。你就失去了 NumPy 的向量加速效果

print("np.zeros:\n", np.zeros((2, 3)))     # 建立 2x3 全為 0
print("np.ones:\n", np.ones((3, 1)))      # 建立 3x1 全為 1
print("np.full:\n", np.full((3, 1), 7))      # 建立 3x3 全為 7


print("np.eye:\n", np.eye(3))            # 單位矩陣
print("np.arange:\n", np.arange(0, 10, 2))  # 類似 range()  ->  [0 2 4 6 8]
print("np.linspace:\n", np.linspace(0, 1, 5)) # 等間距 5 個點  ->  [0.   0.25 0.5  0.75 1.  ]

# -----------------------------------------------------------------
a = np.array([[1, 2], [3, 4]])
b = np.array([10, 20])

# b 會自動「擴張」成 2x2 來配合 a
# print(a + b)

# -----------------------------------------------------------------
# practice
# 1. 建立一個 3x3 的全 7 矩陣
a1 = np.full((3, 3), 7)     # 建立 3x3 全為 7

# 2. 建立一個包含 10 個值的 1D 陣列，從 5 等距到 15
a2 = np.linspace(5, 15, 10)      # 建立 3x3 全為 7

# 3. 檢查它們的 shape、ndim、dtype
print(a1.shape, a1.ndim, a1.dtype)
print(a2.shape, a2.ndim, a2.dtype)
