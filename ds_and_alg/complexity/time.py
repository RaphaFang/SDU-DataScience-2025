# | 複雜度        | 說明      | 範例演算法               |
# | ---------- | ------- | -------------------------- |
# | O(1)       | 常數時間    | 直接回傳、dict 查找        |
# | O(log n)   | 對半縮小    | Binary Search            |
# | O(n)       | 線性掃描    | for-loop                 |
# | O(n log n) | 分治演算法常見 | MergeSort, QuickSort   |
# | O(n²)      | 雙層迴圈    | Brute Force Two Sum      |
# | O(2ⁿ)      | 指數級（很慢） | Naive Fibonacci, Backtrack |
# | O(n!)      | 全排列     | Permutations              |

# ---------------------------------------------------------
# Big-O(O), Upper Bound
    # 最差情況
# Big-Ω(Ω), Lower Bound
    # 最好情況
# Big-Θ(Θ), Tight Bound
    # 平均情況

# ---------------------------------------------------------
# ---------------------------------------------------------
# ! 雙層迴圈：O(n × n) = O(n²)
# for i in range(n):       # O(n)
#     for j in range(n):   # O(n)
#         print(i, j)

# ! O(n × 100) → 還是 O(n)（丟常數）
# for i in range(n):
#     for j in range(100):  # 固定 100 次
#         print(i, j)

# ! 連續 → O(n + n) = O(n)
# for i in range(n):        # O(n)
#     print(i)
# for j in range(n):        # O(n)
#     print(j)

# ! O(n * log n)
# for i in range(n):         # 外層 n 次
#     temp = i
#     while temp < n:        # 內層 log n 次（視 i 而定）
#         temp *= 2

# ! binary -> O(log n)
# ! mergesort, heapsort -> O(n log n)
# ! recursion, subset -> O(2ⁿ)
# ! permutation -> O(n!)

# ! dp 廣泛來說會是 n*n
# | 類型           | 狀態維度             | 複雜度範例                       | 是不是 O(n²)       |
# | ------------ | ---------------- | --------------------------- | --------------- |
# | **一維狀態**     | `dp[i]`          | Fib(n), Climb Stairs → O(n) | ❌ 常為 O(n)       |
# | **二維狀態**     | `dp[i][j]`       | LCS, Edit Distance → O(n²)  | ✅ 常為 O(n²)      |
# | **重量/目標類問題** | `dp[i][w]`       | 0/1 Knapsack, Subset Sum    | ✅ 多為 O(nW)      |
# | **三維以上狀態**   | `dp[i][j][k]...` | Sequence Alignment, Game DP | ❗可能是 O(n³) 甚至更高 |


# ! O((log n) × (log n)) = O(log² n)
# i = 1
# while i < n:
#     j = 1
#     while j < n:
#         j *= 2
#     i *= 2

# ! O(n²), Insertion Sort
# 要考慮到最糟的情況，會是n2 square
# for i in range(1, n):
#     while j > 0 and arr[j] < arr[j-1]:
#         ...
