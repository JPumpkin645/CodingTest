import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

limit = 100001
visited = [False] * limit
queue = deque([(n, 0)])

while queue:
    current, count = queue.popleft()
    if current == k:
        print(count)
        break
    if -1 < 2 * current < limit and not visited[2 * current]:
        queue.appendleft((2 * current, count))
        visited[2 * current] = True
    if -1 < current - 1 < limit and not visited[current - 1]:
        queue.append((current - 1, count + 1))
        visited[current - 1] = True
    if -1 < current + 1 < limit and not visited[current + 1]:
        queue.append((current + 1, count + 1))
        visited[current + 1] = True
