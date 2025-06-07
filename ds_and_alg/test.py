import heapq

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority  # 小的先出隊

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
