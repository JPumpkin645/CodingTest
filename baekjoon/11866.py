from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n + 1))
stack = []

while queue:
    queue.rotate(-(k - 1))
    stack.append(queue.popleft())

print(f"<{', '.join(map(str, stack))}>")
