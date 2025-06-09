activities = [(1, 3), (2, 5), (4, 7), (1, 8), (5, 9), (8, 10)]
activities.sort(key=lambda x: x[1])

selected = []
end_time = 0

for start, end in activities:
    if start >= end_time:
        selected.append((start, end))
        end_time = end

print("選擇的活動：", selected)

# -------------------------------------------------------