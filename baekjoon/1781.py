import heapq
import sys

input = sys.stdin.readline

n = int(input())
table = list(tuple(map(int, input().split())) for _ in range(n))
stack = []

heapq.heapify(table)

while table:
    deadline, reward = heapq.heappop(table)
    if deadline > len(stack):
        heapq.heappush(stack, reward)
    elif stack[0] < reward:
        heapq.heappushpop(stack, reward)

print(sum(stack))
