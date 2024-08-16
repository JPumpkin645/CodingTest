import heapq
import sys

input = sys.stdin.readline
n, c = map(int, input().split())
m = int(input())
info_list = []
for _ in range(m):
    start, end, amount = map(int, input().split())
    heapq.heappush(info_list, (end, start, amount))

stack = [0] * (n + 1)
result = 0
while info_list:
    end, start, amount = heapq.heappop(info_list)

    max_v = max(stack[start:end])
    available_v = min(amount, c - max_v)
    if available_v > 0:
        for i in range(start, end):
            stack[i] += available_v
        result += available_v

print(result)
