import numpy as np

def process_matrix(A, B):
    """
    傳入兩個矩陣 A, B，返回以下內容：
    1. 若 A 和 B 可以加法 → 傳回 A + B
    2. 若不能加法但可以 broadcasting → 傳回 A + B 的結果
    3. 若加法不可能 → 傳回錯誤 "Cannot broadcast or add"
    4. 將加總後矩陣 flatten 成一維、過濾 > 50 的值、轉置成 row 向量形式
    5. 最後回傳這個處理過的 array
    """
    try:
        r = A + B
        r = r.flatten()
        r = r[r>50]
        r = r.reshape(1, -1)
        return r # 這邊 -1 是自動推倒，自己算出要是多少
    
    except ValueError:
        raise ValueError("Cannot broadcast or add")

if __name__ == "__main__":
    A = np.array([[10, 20], [30, 40]])
    B = np.array([[1, 2], [3, 4]])
    C = np.array([1, 2])    # 可被 broadcast
    D = np.array([9, 9, 9]) # 無法配合 A

    print(process_matrix(A, B))
    print(process_matrix(A, C))
    print(process_matrix(A, D))

# -----------------------------------------------------------------
# flatten() -> 得到的會是 「一維 arr （單純只是舉證）」 -> shape 為 (n,)
# reshape() -> 可以得到的會是 「一維的 row 或 column 向量」 -> shape 為 (n,1) or (1, n)


# -----------------------------------------------------------------
# | 語法               | 意思                         |
# | ---------------- | ----------------------------- |
# | `reshape(1, -1)` | 轉成 1 row（row vector）       |
# | `reshape(-1, 1)` | 轉成 1 column（column vector） |
# | `reshape(-1, 3)` | NumPy 自動決定幾列，每列 3 欄    |


# -----------------------------------------------------------------
# # if __name__ == "__main__":
# 保護檔案中沒有要調用的測試，因為當調用檔案中的函數，其他內容也會被執行