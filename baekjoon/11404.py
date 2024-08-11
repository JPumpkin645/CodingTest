import sys

input = sys.stdin.readline

INF = 987654321

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    start, end, dist = map(int, input().split())
    graph[start][end] = min(dist, graph[start][end])

for start in range(1, n + 1):
    for end in range(1, n + 1):
        if start == end:
            graph[start][end] = 0
for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

for start in range(1, n + 1):
    for end in range(1, n + 1):
        if graph[start][end] == INF:
            graph[start][end] = 0
    print(*graph[start][1:])
