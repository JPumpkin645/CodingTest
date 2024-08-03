from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph: list, start: int, visited: list):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(graph=graph, start=1, visited=visited)
count = 0
for i in visited:
    if i:
        count += 1

print(count - 1)
