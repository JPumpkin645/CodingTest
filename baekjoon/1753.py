import heapq
import sys

input = sys.stdin.readline


INF = 987654321
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)
for _ in range(e):
    fm, to, value = map(int, input().split())
    graph[fm].append((to, value))

queue = []
heapq.heappush(queue, (0, start))
distance[start] = 0
while queue:
    dist, now = heapq.heappop(queue)
    if distance[now] < dist:
        continue
    for to, value in graph[now]:
        cost = dist + value
        if cost < distance[to]:
            distance[to] = cost
            heapq.heappush(queue, (cost, to))

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
