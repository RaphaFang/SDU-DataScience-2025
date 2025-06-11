# permutations
def permute(nums):
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])  # 加入 path 的拷貝（不能是 path 本身）
            return
        for i in range(len(nums)):
            if used[i]:   # 會在這邊檢查下面的 [False, False, False]
                continue  # 跳過已使用的元素
            path.append(nums[i])
            used[i] = True
            backtrack(path, used)
            path.pop()
            used[i] = False

    backtrack([], [False]*len(nums))
    return result
# print(permute([1, 2, 3]))

# 這思考很複雜
# 直接把他想像成有三層 for
    # [T,T,T] ->  [F,T,T], index -> 0 
    #     [F,T,T] -> [F,F,T], index -> 1 (重要：這loop從 index 2 接續，所以會向下塞 [1,3]，下面的for 會變成[1,3,2])
    #         [F,F,T] -> [F,F,F], index -> 2 (這loop結束)
    #             這邊會pop index 2, 改成 [F,F,T]
    #         這邊會pop index 1, 改成 [F,T,T]


# ------------------------------------------------------------------------
# iteration 的方式
def permute_iter(nums):
    result = [[]]
    for num in nums:
        new_result = []
        for perm in result:
            for i in range(len(perm) + 1):
                # 在 perm 的每個位置插入 num
                new_perm = perm[:i] + [num] + perm[i:]
                new_result.append(new_perm)
        result = new_result
    return result
# print(permute_iter([1, 2, 3]))


# ------------------------------------------------------------------------
# | 寫法 | 複雜度 | 可擴展性（剪枝、限制條件） | 可讀性 |
# | ------------ | ------------ | ----------- | --------------- |
# | Backtracking | O(n × n!) | ✅ 很容易剪枝或加限制 | ✅ |
# | Iterative（插入） | O(n × n!) | ❌ 難剪枝、不靈活 | ❌ |
# | `itertools.permutations` | O(n!) | ❌ 黑箱，不可修改 | ✅（快速原型） |

# ------------------------------------------------------------------------
from itertools import permutations

for p in permutations([1, 2, 2, 3]):
    print(p)
# 這問題是他沒辦法排除重複
# (1, 2, 2, 3) same
# (1, 2, 3, 2)
# (1, 2, 2, 3) same
# (1, 2, 3, 2)
# (1, 3, 2, 2) 
# (1, 3, 2, 2)
