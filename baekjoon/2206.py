import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))


def b_func(graph: list, n: int, m: int) -> int:
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    # position/count/item_use = 0 if use => 1
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True
    queue = deque([((0, 0), 1, 0)])

    while queue:
        position, count, item_use = queue.popleft()
        cx, cy = position[0], position[1]
        if cx == m - 1 and cy == n - 1:
            return count

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 1 and item_use == 0 and not visited[ny][nx][1]:
                    visited[ny][nx][1] = True
                    queue.append(((nx, ny), count + 1, 1))
                if graph[ny][nx] == 0 and not visited[ny][nx][item_use]:
                    visited[ny][nx][item_use] = True
                    queue.append(((nx, ny), count + 1, item_use))

    return -1


print(b_func(graph, n, m))
