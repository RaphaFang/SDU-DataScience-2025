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

from collections import deque
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
# Queue vs Deque