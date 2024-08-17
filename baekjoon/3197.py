from collections import deque


def get_next_swan_position(swan_queue: deque, swan_visited: list):
    next_swan_position = deque()
    while swan_queue:
        cx, cy = swan_queue.popleft()
        if cx == ex and cy == ey:
            return (True, deque())
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < c and 0 <= ny < r and not swan_visited[ny][nx]:
                swan_visited[ny][nx] = True
                if grid[ny][nx] == "X":
                    next_swan_position.append((nx, ny))
                else:
                    swan_queue.append((nx, ny))
    return (False, next_swan_position)


def get_next_ice_position(water_queue: deque, water_visited: list):
    new_water = deque()
    while water_queue:
        cx, cy = water_queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < c and 0 <= ny < r and not water_visited[ny][nx]:
                water_visited[ny][nx] = True
                if grid[ny][nx] == "X":
                    grid[ny][nx] = "."
                    new_water.append((nx, ny))
                else:
                    water_queue.append((nx, ny))
    return new_water


r, c = map(int, input().split())
grid = []
swan_position = []

swan_queue = deque()
water_queue = deque()
swan_visited = [[False] * c for _ in range(r)]
water_visited = [[False] * c for _ in range(r)]

for i in range(r):
    row = list(input().strip())
    grid.append(row)
    for j in range(len(row)):
        if row[j] == "L" or row[j] == ".":
            water_queue.append((j, i))
            water_visited[i][j] = True
            if row[j] == "L":
                row[j] = "."
                swan_position.append((j, i))


dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
sx, sy = swan_position[0]
ex, ey = swan_position[1]

swan_queue.append((sx, sy))
swan_visited[sy][sx] = True

count = 0

while True:
    find, swan_queue = get_next_swan_position(swan_queue, swan_visited)
    if find:
        print(count)
        break
    water_queue = get_next_ice_position(water_queue, water_visited)
    count += 1
