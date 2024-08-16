import heapq
import sys

input = sys.stdin.readline
n = int(input())
left_heap = []
right_heap = []

for i in range(1, n + 1):
    input_value = int(input())
    odd = True if i % 2 == 1 else False
    if odd:
        heapq.heappush(left_heap, -input_value)
    else:
        heapq.heappush(right_heap, input_value)

    if right_heap and right_heap[0] < -left_heap[0]:
        left_max = -heapq.heappop(left_heap)
        right_min = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -right_min)
        heapq.heappush(right_heap, left_max)

    print(-left_heap[0])
