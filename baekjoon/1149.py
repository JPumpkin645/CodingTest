import sys

input = sys.stdin.readline

n = int(input())
red, green, blue = [0], [0], [0]
for _ in range(n):
    r, g, b = map(int, input().split())
    red.append(r)
    green.append(g)
    blue.append(b)

values = [[] for _ in range(n + 1)]
values[1] = [red[1], green[1], blue[1]]

for i in range(2, n + 1):
    # r_min = red[i] + min(green[i - 1], blue[i - 1])
    # g_min = green[i] + min(red[i - 1], blue[i - 1])
    # b_min = blue[i] + min(red[i - 1], green[i - 1])
    r_min = red[i] + min(values[i - 1][1], values[i - 1][2])
    g_min = green[i] + min(values[i - 1][0], values[i - 1][2])
    b_min = blue[i] + min(values[i - 1][0], values[i - 1][1])
    values[i] = [r_min, g_min, b_min]

print(min(values[n]))
