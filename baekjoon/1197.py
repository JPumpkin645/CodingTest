import sys

input = sys.stdin.readline

v, e = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(e)]

graph.sort(key=lambda x: x[2])

parent = list(i for i in range(v + 1))


def get_parent(parent, x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union_parent(parent, a, b):
    root_a = get_parent(parent, a)
    root_b = get_parent(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


answer = 0

for start, end, dist in graph:
    if get_parent(parent, start) != get_parent(parent, end):
        union_parent(parent, start, end)
        answer += dist

print(answer)
