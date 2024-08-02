import sys
from collections import deque


def command(s: str, deque: deque):
    if s.startswith("1"):
        _, n = s.split()
        deque.appendleft(int(n))
    elif s.startswith("2"):
        _, n = s.split()
        deque.append(int(n))
    elif s.startswith("3"):
        print(deque.popleft() if deque else -1)
    elif s.startswith("4"):
        print(deque.pop() if deque else -1)
    elif s.startswith("5"):
        print(len(deque))
    elif s.startswith("6"):
        print(0 if deque else 1)
    elif s.startswith("7"):
        print(deque[0] if deque else -1)
    elif s.startswith("8"):
        print(deque[-1] if deque else -1)


n = int(input())
d = deque()
for _ in range(n):
    command(sys.stdin.readline().rstrip(), d)
