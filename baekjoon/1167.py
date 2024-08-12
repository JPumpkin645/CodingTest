import sys

input = sys.stdin.readline

v = int(input())

root_node = 0
graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)
for _ in range(v):
    input_list = list(map(int, input().split()))
    node = input_list.pop(0)
    while input_list:
        c_node = input_list.pop(0)
        if c_node == -1:
            break
        dist = input_list.pop(0)
        graph[node].append((c_node, dist))

for i in range(1, v + 1):
    if len(graph[i]) == 1:
        root_node = i
        break


def dfs(graph, visited, root_node):
    stack = [(root_node, 0)]
    visited[root_node] = True
    # distaces = []
    max_node = 0
    max_dist = 0
    while stack:
        c_node, c_dist = stack.pop()
        # distaces.append((c_node, c_dist))
        if max_dist < c_dist:
            max_dist = c_dist
            max_node = c_node
        for n_node, n_dist in graph[c_node]:
            if not visited[n_node]:
                visited[n_node] = True
                stack.append((n_node, c_dist + n_dist))
    # return max(distaces, key=lambda x: x[1])
    return (max_node, max_dist)


node, dist = dfs(graph, visited[:], root_node)
final_node, final_dist = dfs(graph, visited[:], node)

print(final_dist)
