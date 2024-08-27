import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]


def count_iceberg_parts():
    visited = [[False] * m for _ in range(n)]
    part_count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                part_count += 1
                queue = deque([(i, j)])
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] > 0:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
    return part_count


def melt_icebergs():
    to_melt = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                water_count = 0
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 0:
                        water_count += 1
                if water_count > 0:
                    to_melt.append((i, j, water_count))

    for x, y, water_count in to_melt:
        graph[x][y] -= water_count
        if graph[x][y] < 0:
            graph[x][y] = 0


years = 0
while True:
    parts = count_iceberg_parts()
    if parts >= 2:
        print(years)
        break
    if parts == 0:
        print(0)
        break
    melt_icebergs()
    years += 1
