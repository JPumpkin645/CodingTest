import sys


def dfs(x: int, y: int) -> bool:
    stack = [(x, y)]
    if graph[y][x] == 1:
        graph[y][x] = 0
    else:
        return False

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                stack.append((nx, ny))

    return True


input = sys.stdin.readline
t = int(input())


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    count = 0
    for i in range(m):
        for j in range(n):
            if dfs(x=i, y=j):
                count += 1
    print(count)
