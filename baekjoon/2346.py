from collections import deque

n = int(input())
deq = deque(range(1, n + 1))
command_list = list(map(int, input().split()))
result = []

while deq:
    i = deq.popleft()
    result.append(i)
    command = command_list[i - 1]
    if command > 0:
        deq.rotate(-(command - 1))
    else:
        deq.rotate(-command)

print(*result)
