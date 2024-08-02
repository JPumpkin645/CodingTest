import sys
from collections import deque

n = int(input())
qs = list(map(int, sys.stdin.readline().rstrip().split()))
qs_value = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
input_list = list(map(int, sys.stdin.readline().rstrip().split()))

deq = deque(qs_value[i] for i in range(n) if qs[i] == 0)

result = []

for i in input_list:
    deq.appendleft(i)
    result.append(deq.pop())

print(*result)
