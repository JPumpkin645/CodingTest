import sys


def dfs(graph: list, visit_list: list, start: int) -> bool:
    if visit_list[start]:
        return False
    stack = [start]
    while stack:
        current = stack.pop()
        if not visit_list[current]:
            visit_list[current] = True
            for i in graph[current]:
                if not visit_list[i]:
                    stack.append(i)
    return True


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit_list = [False for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    graph[s].append(e)
    graph[e].append(s)
result = 0
for i in range(1, n + 1):
    if dfs(graph, visit_list, i):
        result += 1
print(result)
