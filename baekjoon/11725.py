import sys
from collections import deque
from typing import List

input = sys.stdin.readline

n = int(input())

nodes: List[List[int]] = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

parent = [0 for _ in range(n + 1)]
parent[1] = 1

queue = deque([1])

while queue:
    p_node: int = queue.pop()
    for node in nodes[p_node]:
        if node != parent[p_node]:
            parent[node] = p_node
            queue.append(node)

for i in range(2, n + 1):
    print(parent[i])
