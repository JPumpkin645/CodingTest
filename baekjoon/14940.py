import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]


def bfs(graph: list, x: int, y: int, m: int, n: int):
    checked = [[False for _ in range(m)] for _ in range(n)]
    result = [[-1 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        for j in range(n):
            if graph[j][i] == 0:
                result[j][i] = 0

    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    checked[y][x] = True
    result[y][x] = 0

    queue = deque([(x, y)])

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not checked[ny][nx]:
                if graph[ny][nx] == 0:
                    checked[ny][nx] = True
                    result[ny][nx] = 0
                elif graph[ny][nx] == 1:
                    checked[ny][nx] = True
                    result[ny][nx] = result[cy][cx] + 1
                    queue.append((nx, ny))

    return result


def get_start_point(graph: list, m: int, n: int):
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 2:
                return (i, j)


x, y = get_start_point(graph, m, n)
result = bfs(graph, x, y, m, n)
for i in result:
    print(*i)
