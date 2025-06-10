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
    return counter

# -------------------------------------------------------
# Huffman Encoding
uncode_str = 'Huffman Encoding is brilliant!'
# def huffman_encoding_manual(uncode_str):
#     counter_dict = {}
#     for n in list(uncode_str):
#         counter_dict[n] = counter_dict.get(n, 0) + 1
    
#     temp = list(counter_dict.items())
#     temp.sort(key= lambda x: x[1])

from collections import Counter
def huffman_encoding_counter(uncode_str):
    counter_dict = Counter(uncode_str)

    temp = (list(counter_dict.items()))
    temp.sort(key= lambda x: x[1])

# -------------------------------------------------------
import heapq
from collections import Counter
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
        # 這邊是設定透過 freq 來比較順序
        # 但如果直接是 int ，不用設定
        # 如果是turple 且第一個是 int 也不用設定

class HuffmanEncoder:
    def __init__(self, text):
        self.text = text
        self.freq_map = Counter(text)
        self.root = None
        self.codes = {}

    def build_tree(self):
        heap = []
        for char, freq in self.freq_map.items():
            heapq.heappush(heap, HuffmanNode(char, freq))

        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            merged = HuffmanNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(heap, merged)
            # 這邊看似又推回同一heap，但是我每推一次就 -2 同時+1
            # 也要將新建立的物件同時比較大小，把樹完成

        self.root = heap[0]

    def generate_codes(self):
        def dfs(node, current_code):
            if node is None:
                return
            if node.char is not None:
                self.codes[node.char] = current_code
                return
            dfs(node.left, current_code + "0")
            dfs(node.right, current_code + "1")

        dfs(self.root, "")

    def encode(self):
        self.build_tree()
        self.generate_codes()
        return "".join(self.codes[c] for c in self.text)

    def get_codes(self):
        if not self.codes:
            self.build_tree()
            self.generate_codes()
        return self.codes

what = HuffmanEncoder('Huffman Encoding is brilliant!')
print(what.encode())

# {'E': '0000', 'H': '00010', 'g': '00011', ' ': '001', 's': '01000', 'b': '01001', 'a': '0101',
#  'l': '0110', 'm': '01110', 'c': '01111', 'i': '100', 'n': '101', 'u': '11000', 'o': '11001',
#  'd': '11010', 'r': '11011', 'f': '1110', '!': '11110', 't': '11111'}