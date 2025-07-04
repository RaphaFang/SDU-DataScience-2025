# contradiction
# 367. Valid Perfect Square
def isPerfectSquare(num: int) -> bool:
    log = int(num**0.5)
    # print(log)
    return log*log == num
# isPerfectSquare(num = 14)
print(isPerfectSquare(num = 10000000000000000000000000000000000000000000000))
# ! edge case, 當數太大，計算會錯誤
# log = 99999999999999991611392
# False
# 
# ---------------------------------------------------------------
def two_pointer_isPerfectSquare(num: int) -> bool:
    low, high = 1, num

    while low<= high:
        mid = (low + high) // 2
        sq  = mid * mid
        if sq == num:
            return True
        elif sq < num:
            low = mid + 1
        else:
            high = mid - 1
    return False

# two_pointer_isPerfectSquare(num = 14)


# 反證填空
# 補全下列論述，使其成為嚴謹反證：
# 假設迴圈某步選擇 sq < num，但真實平方根 r ≤ mid…（填反證衝突）

# 邊界案例分析
# 解釋演算法對 num = 1 和 num = 2³¹ – 1 為何仍然正確且不溢位。
    #! 他要證明的是為什麼不會超 python 的位元上限？  不會，因為 Python int 無上界（自動大整數）
    # 你是說在最邊界的情況是嗎？因為最極端情況是兩個都是最邊界（最大最小），
    # 這時候得到的mid還是會在範圍中間，而可以證明，mid square 必定比最右邊的指針大
    # 一數的square，必定大於一數的*2

# 改寫牛頓迭代
# 寫出 isPerfectSquare_Newton(num)，並用逆否或反證思路說明收斂必定落在 floor(√num) 或 ceil(√num)。
# ! 真的完全看不懂...
def isPerfectSquare(num: int) -> bool:
    log = int(num**0.5)
    return log*log == num

# ---------------------------------------------------------------
# | 方法    | 時間             | 核心不變量                                    | 證明套路                                     |
# | ----- | ----------------- | ------------------------------------------- | ------------------------------------------- |
# | 二分搜尋  | **O(log num)** | 區間 `[low, high]` 必含答案（若存在）           | 反證：假設 mid² ≠ num，但仍把錯方向的一半留區間內 ⇒ 與不變量衝突 |
# | 牛頓迭代  | O(log num)     | `xᵢ ≥ √num` & 單調下降                       | 強歸納 + 取極限                                |
# | 逐次減奇數 | O(√num)       | `num = n² ⇒ num – 1 – 3 – 5 … – (2n–1) = 0` | 直接證：∑ₖ₌₀ⁿ₋₁ (2k+1)=n²                      |
