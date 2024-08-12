import sys

input = sys.stdin.readline


def f_func(graph: list, n: int):
    for mid in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])
                if start == end and graph[start][end] < 0:
                    return True
    return False


t = int(input())

for _ in range(t):
    n, m, w = map(int, input().split())
    INF = 987654321
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        start, end, time = map(int, input().split())
        graph[start][end] = min(time, graph[start][end])
        graph[end][start] = min(time, graph[end][start])

    for _ in range(w):
        start, end, time = map(int, input().split())
        graph[start][end] = min(-time, graph[start][end])

    for i in range(1, n + 1):
        graph[i][i] = min(0, graph[i][i])

    if f_func(graph, n):
        print("YES")
    else:
        print("NO")
