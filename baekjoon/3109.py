import sys

input = sys.stdin.readline

r, c = map(int, input().split())

grid = [list(input().rstrip()) for _ in range(r)]

dx, dy = [1, 1, 1], [-1, 0, 1]

count = 0

for i in range(r):
    stack = [(0, i)]
    grid[i][0] = "x"

    while stack:
        cx, cy = stack.pop()
        grid[cy][cx] = "x"

        if cx == c - 1:
            count += 1
            break

        for j in range(2, -1, -1):
            nx, ny = cx + dx[j], cy + dy[j]
            if 0 <= ny < r and grid[ny][nx] == ".":
                stack.append((nx, ny))

print(count)
