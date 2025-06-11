# 5.1 透過 recursion 的 fib 練習DP
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
# print(fib(100))

def fib_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n+1) # 要先建立好，不然下面無法修改數值
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
# print(fib_dp(100))

# 這方式超級快，recursion ver. 會卡住，這邊順解

# ------------------------------------
# 5.2 0/1 Knapsack Problem
def knapsack(values, weights, W):
    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    print(dp)
    for i in range(1, n+1):
        for w in range(W + 1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]  # 不能裝
            else:
                dp[i][w] = max(
                    dp[i-1][w],  # 不裝
                    dp[i-1][w - weights[i-1]] + values[i-1]  # 裝入第 i-1 個物品
                )

    return dp[n][W]

weights = [2, 1, 3]
values  = [4, 2, 3]
W = 4
# print(knapsack(values, weights, W))


# ------------------------------------
# 5.3 LCS：Longest Common Subsequence
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    return dp[m][n]
print(lcs("ABCBDAB", "BDCAB"))

# ------------------------------------
# 5.4 Edit Distance / Levenshtein Distance
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # 刪除
                    dp[i][j-1],    # 插入
                    dp[i-1][j-1]   # 替換
                )

    return dp[m][n]
