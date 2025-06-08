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

scheduler = TaskScheduler()
scheduler.add_task("Clean", 3)
scheduler.add_task("Eat", 1)
scheduler.add_task("Study", 2)

print(scheduler.get_next_task())  # Eat(1)
print(scheduler.get_next_task())  # Study(2)

# -------------------------------------------------------
# ! (1.7) Deque（雙向佇列）+ Undo / Redo 模擬
# -------------------------------------------------------
# from collections import deque
class TextEditor:
    def __init__(self):
        self.undo_stack = deque()
        self.redo_stack = deque()

    def type(self, text):
        self.undo_stack.append(text)
        # self.redo_stack.clear() # 新增就把存放的redo砍了？ 超怪

    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.redo_stack.appendleft(action)
            return f"Undo: {action}"
        return "Nothing to undo."

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.popleft()
            self.undo_stack.append(action)
            return f"Redo: {action}"
        return "Nothing to redo."

    def current_state(self):
        return list(self.undo_stack)

editor = TextEditor()
editor.type("A")
editor.type("B")
print(editor.undo())         # Undo: B
print(editor.redo())         # Redo: B
print(editor.current_state())  # ['A', 'B']
# 這邊使用雙端的deque世因為即便LIFO的stack狀態，也可以做到 undo/ redo
# 但是會沒辦法紀錄事件先後順序
# 例如 A, B, C 加入，這時候我undo，
# 我會希望暫存的redo_stack 按照順序存放由最早開始存放到最新