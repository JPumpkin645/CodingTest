import sys
from collections import deque

input = sys.stdin.readline

w, h = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(h)]
points = []
for i in range(w):
    for j in range(h):
        if graph[j][i] == "C":
            points.append((i, j))
start, end = points[0], points[1]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


visited = [[[-1] * 4 for _ in range(w)] for _ in range(h)]

queue = deque()

for direction in range(4):
    queue.append((start[0], start[1], 0, direction))
    visited[start[1]][start[0]][direction] = 0

while queue:
    cx, cy, count, direction = queue.popleft()

    if (cx, cy) == end:
        print(count)
        break

    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] != "*":
            new_count = count if direction == i else count + 1
            if visited[ny][nx][i] == -1 or new_count < visited[ny][nx][i]:
                visited[ny][nx][i] = new_count
                if direction == i:
                    queue.appendleft((nx, ny, new_count, i))
                else:
                    queue.append((nx, ny, new_count, i))
