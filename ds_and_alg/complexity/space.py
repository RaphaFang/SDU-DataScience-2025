# 當要計算recursion，要看他實際層數
# 深度是 n，每層都會暫時「卡住等待」結果回傳，所以記憶體會保留 n 層的資訊（像變數、執行點等）
# 所以會是O(n)

# 例如下方，要看visited，因為visited是結束的判斷，他有n 層，會是O(n)
# def dfs_recursive(graph, node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     for neighbor in graph[node]:
#         dfs_recursive(graph, neighbor, visited)

# dp 有可能會是
# time complexity: O(n*m)
# space complexity: O(n*m)