from collections import deque

n, k = map(int, input().split())


def bfs(n: int, k: int):
    max_num = 100000
    visited = [False] * (max_num + 1)
    visit_count = [0] * (max_num + 1)

    queue = deque([n])
    visited[n] = True

    while queue:
        current = queue.popleft()
        if current == k:
            return visit_count[current]
        for i in [current * 2, current + 1, current - 1]:
            if 0 <= i <= max(k + 1, n) and not visited[i]:
                visited[i] = True
                queue.appendleft(i) if i == current * 2 else queue.append(i)
                visit_count[i] = visit_count[current] + 1


print(bfs(n, k))
