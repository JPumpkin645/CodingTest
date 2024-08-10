from collections import deque

a, b = map(int, input().split())

queue = deque([(a, 0)])
is_find = False
while queue:
    n, count = queue.popleft()

    if n == b:
        is_find = True
        print(count + 1)
        break

    if 10 * n + 1 <= b:
        queue.appendleft((10 * n + 1, count + 1))
    if 2 * n <= b:
        queue.append((2 * n, count + 1))

if not is_find:
    print(-1)
