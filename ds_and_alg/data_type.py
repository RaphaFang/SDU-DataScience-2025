from collections import deque
# primitive / structured / abstracted

# java 的reference 會是 structured 或是 abstracted
# 都有可能

# -------------------------------------------------------
# ! (1.1) Stack, LIFO
# -------------------------------------------------------
# 他的優勢是雙邊的速度都會是O(1)
# popleft()

def stack(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(stack("()"))        # True
print(stack("())("))      # False

def stack_by_deque(s):
    stack = deque()
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(stack_by_deque("((()))"))  # True
print(stack_by_deque("())"))     # False

# -------------------------------------------------------
# ! (1.3) Queue(舊方法) vs Deque, FIFO
# -------------------------------------------------------
class CallQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, name):
        self.queue.append(name)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def peek(self):
        if self.queue:
            return self.queue[0]
        return None

    def is_empty(self):
        return not self.queue

cq = CallQueue()
cq.enqueue("Alice")
cq.enqueue("Bob")
print(cq.peek())        # Alice 這時候會是 [Alice, Bob]
print(cq.dequeue())     # Alice 這時候會是 [Bob]
print(cq.dequeue())     # Bob   這時候會是 []
print(cq.is_empty())    # True


# -------------------------------------------------------
# ! (1.5) Priority Queue
# -------------------------------------------------------
import heapq

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority  # 小的先出隊
        # return self.priority > other.priority  # 大的先出來（Max Heap）


    def __repr__(self):
        return f"{self.name}({self.priority})"

class TaskScheduler:
    def __init__(self):
        self.pq = []

    def add_task(self, name, priority):
        heapq.heappush(self.pq, Task(name, priority))

    def get_next_task(self):
        if self.pq:
            return heapq.heappop(self.pq)
        return None

# 測試
scheduler = TaskScheduler()
scheduler.add_task("Clean", 3)
scheduler.add_task("Eat", 1)
scheduler.add_task("Study", 2)

print(scheduler.get_next_task())  # Eat(1)
print(scheduler.get_next_task())  # Study(2)

# -------------------------------------------------------
# ! (1.7) Deque（雙向佇列）+ Undo / Redo 模擬
# -------------------------------------------------------