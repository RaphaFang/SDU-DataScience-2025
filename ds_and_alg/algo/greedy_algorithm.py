activities = [(1, 3), (2, 5), (4, 7), (1, 8), (5, 9), (8, 10)]
activities.sort(key=lambda x: x[1])

selected = []
end_time = 0

for start, end in activities:
    if start >= end_time:
        selected.append((start, end))
        end_time = end

# print("選擇的活動：", selected)

# -------------------------------------------------------
# Fractional Knapsack Problem
items = [(60, 10),(100, 20),(120, 30)]
capacity = 50
def fractional_knapsack(items, capacity):
    items.sort(key= lambda x: x[0]/x[1])
    items.reverse()

    result = 0
    for p, w in items:
        if capacity >0:
            if capacity/w >= 1:
                result+= p
                capacity-= w
            else:
                r = capacity/w
                result+= p*r
                capacity-= w*r
    return result


# -------------------------------------------------------
# Interval Partitioning
scenes = [(0, 6), (1, 4), (2, 8),(5, 7), (6, 10), (9, 12)]
def min_actors(scenes):
    scenes.sort(key=lambda x: x[1])
    result = []
    counter, end_time = 0, 0
    for start, end in scenes:
        if start >= end_time:
            result.append((start, end))
            end_time = end
            counter+=1
    print(counter)

# -------------------------------------------------------
# Huffman Encoding
def huffman_encoding(freq_dict):
    pass