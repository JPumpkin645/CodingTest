import heapq
import math
import sys

input = sys.stdin.readline

N, L = map(int, input().split())
h_list = []
for _ in range(N):
    start, end = map(int, input().split())
    heapq.heappush(h_list, (start, end))

start_point = h_list[0][0]
count = 0
while h_list:
    start, end = heapq.heappop(h_list)
    if start < start_point:
        start = start_point
    if end < start_point:
        continue
    need = math.ceil((end - start) / L)
    start_point = start + need * L
    count += need

print(count)
