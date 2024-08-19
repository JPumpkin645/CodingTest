import sys

input = sys.stdin.readline

v, e = map(int, input().split())
INF = 987654321
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for _ in range(e):
    start, end, dist = map(int, input().split())
    graph[start][end] = dist

for mid in range(1, v + 1):
    for start in range(1, v + 1):
        for end in range(1, v + 1):
            graph[start][end] = min(graph[start][mid] + graph[mid][end], graph[start][end])

cycle_list = [graph[i][i] for i in range(1, v + 1)]
answer = min(cycle_list)
print(answer if answer != INF else -1)
