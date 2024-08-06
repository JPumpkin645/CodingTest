import sys

m, n = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
checked = [[False for _ in range(m)] for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# checked로 구분하고 다 이루어진 다음에 graph에 0이 남아 있으면 -1 리턴

stack_unit = []
for i in range(m):
    for j in range(n):
        if graph[j][i] == 1:
            stack_unit.append((i, j))
            checked[j][i] = True
count = 0
stack = [stack_unit]
while stack:
    unit_list: list = stack.pop()
    next_unit_list = []
    for cx, cy in unit_list:
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if graph[cy][cx] == 1:
                if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0 and not checked[ny][nx]:
                    checked[ny][nx] = True
                    graph[ny][nx] = 1
                    next_unit_list.append((nx, ny))
    if next_unit_list:
        stack.append(next_unit_list)
        count += 1

is_finish = True
for i in range(m):
    for j in range(n):
        if graph[j][i] == 0:
            is_finish = False

print(count if is_finish else -1)
