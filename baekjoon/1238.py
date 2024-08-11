import heapq
import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
inverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, dist = map(int, input().split())
    graph[start].append((end, dist))
    inverse_graph[end].append((start, dist))


def d_func(graph: list, node: int, start: int) -> list:
    INF = 987654321
    distance = [INF] * (node + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (distance[start], start))

    while queue:
        c_dist, current = heapq.heappop(queue)

        for next, n_dist in graph[current]:
            if c_dist + n_dist < distance[next]:
                distance[next] = c_dist + n_dist
                heapq.heappush(queue, (distance[next], next))

    return distance[1:]


forward = d_func(graph, n, x)
backward = d_func(inverse_graph, n, x)
result = [f + b for f, b in zip(forward, backward)]


print(max(result))
