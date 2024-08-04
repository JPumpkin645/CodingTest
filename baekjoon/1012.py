# def dfs(cor_list: list, visited_list: list, x: int, y: int) -> bool:
#     m = len(cor_list[0])
#     n = len(cor_list)
#     stack = [(x, y)]

#     if cor_list[y][x] == 1 and not visited_list[y][x]:
#         visited_list[y][x] = True
#     else:
#         return False

#     while stack:
#         cx, cy = stack.pop()
#         for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
#             if 0 <= nx < m and 0 <= ny < n and cor_list[ny][nx] == 1 and not visited_list[ny][nx]:
#                 visited_list[ny][nx] = True
#                 stack.append((nx, ny))

#     return True


# t = int(input())

# for _ in range(t):
#     m, n, k = map(int, input().split())
#     cor_list = [[0] * m for _ in range(n)]
#     visited_list = [[False] * m for _ in range(n)]
#     for _ in range(k):
#         x, y = map(int, input().split())
#         cor_list[y][x] = 1
#     count = 0
#     for i in range(m):
#         for j in range(n):
#             if dfs(cor_list=cor_list, visited_list=visited_list, x=i, y=j):
#                 count += 1
#     print(count)


def dfs(cor_list: list, x: int, y: int) -> bool:
    m = len(cor_list[0])
    n = len(cor_list)
    stack = [(x, y)]

    if cor_list[y][x] == 1:
        cor_list[y][x] = 0
    else:
        return False

    while stack:
        cx, cy = stack.pop()
        for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
            if 0 <= nx < m and 0 <= ny < n and cor_list[ny][nx] == 1:
                cor_list[ny][nx] = 0
                stack.append((nx, ny))

    return True


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    cor_list = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        cor_list[y][x] = 1
    count = 0
    for i in range(m):
        for j in range(n):
            if dfs(cor_list=cor_list, x=i, y=j):
                count += 1
    print(count)
