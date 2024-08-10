import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    p, c, d = map(int, input().split())
    graph[p].append((c, d))
    graph[c].append((p, d))


def dfs(node_num: int, start: int, graph: list) -> list:
    visited = [False] * (node_num + 1)
    distance = [0] * (node_num + 1)
    stack = [(start, distance[start])]
    visited[start] = True
    while stack:
        current, dist = stack.pop()

        for next, next_dist in graph[current]:
            if not visited[next]:
                visited[next] = True
                distance[next] = dist + next_dist
                stack.append((next, distance[next]))

    index, max_dist = max(enumerate(distance), key=lambda x: x[1])
    return [index, max_dist]


start_values = dfs(n, 1, graph)
final_values = dfs(n, start_values[0], graph)
print(final_values[1])
