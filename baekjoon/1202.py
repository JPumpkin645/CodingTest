import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

n_list = list(tuple(map(int, input().split())) for _ in range(n))
k_list = sorted([int(input()) for _ in range(k)])
bag = []
gem_wait_list = []
heapq.heapify(n_list)

for max_w in k_list:
    while n_list and n_list[0][0] <= max_w:
        w, p = heapq.heappop(n_list)
        heapq.heappush(gem_wait_list, -p)
    if gem_wait_list:
        bag.append(-heapq.heappop(gem_wait_list))

print(sum(bag))
