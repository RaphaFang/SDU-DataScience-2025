def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# print(fib_recursive(6))  # 8


def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# print(fib_iterative(6))  # 8

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
# Recursion + Memoization（用空間換時間）
# print(fib_memo(6))  # 8

# ------------------------------------------------------------------------
# stack overflow
import sys
print(sys.getrecursionlimit())  # 預設是 1000

# ------------------------------------------------------------------------
# 使用 recursion 的時間複雜度會是 O(2 square)

# ------------------------------------------------------------------------
# | 問題類型                    | 推薦用法                               |
# | ----------------------- | ---------------------------------- |
# | Fibonacci               | ✅ iteration（迴圈效率高）                 |
# | Tree DFS / Backtracking | ✅ recursion（自然且可讀）                 |
# | 排序（如 Merge Sort）        | ✅ recursion 或 iterative with stack |
# | 線性統計、計數、走訪              | ✅ iteration 最快最穩定                  |
