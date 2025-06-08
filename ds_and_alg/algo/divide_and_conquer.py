# 1 Divide and Conquer（分治法）
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])       # Divide
    right = merge_sort(arr[mid:])
    return merge(left, right)          # Combine

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):  # Conquer
        if left[i] < right[j]:  # 這邊是設定，如果出現小，先加入大還是小？ 反過來就會是大到小
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([50, 2, 60, 4, 6, 7, 1, 3]))


# 並且，如果左邊完全比右邊小，就會一直把左邊加完
# 接著跳出while，再加上右邊全部

# print("Recursion Iteration".lower().replace(" ", "_"))